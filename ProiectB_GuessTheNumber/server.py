import random
import socket
import threading
from threading import Thread

nr = None
scor = []

nr2 = None
scor2 = []
clients = []
lock = threading.Lock()

def gest_client(client, adresa):
    print("----------------------------------------")
    print(f"Client: {adresa}")
    client.send("\033[36m \n                    Meniu\n"
                "                    Alege un mod: singleplayer sau multiplayer: \n"
                "                    **pentru ajutor: cerinta\033[0m".encode())
    rasp = client.recv(1024).decode().strip().lower()

    if rasp == "cerinta" or rasp == "c":
        client.send("\033[36mCerința :)\033[0m".encode())
        print("Cerința")
        cerinta(client, adresa)

    elif rasp == "singleplayer" or rasp == "s":
        client.send("\033[36mAi ales modul singleplayer\n "
                           "                   Serverul va genera un număr și tu o să trebuiască să îl ghicești \n "
                           "                   Numărul este între 0 și 50 inclusiv\033[0m".encode())
        print("Mod selectat: Singleplayer")
        single(client)
    elif rasp == "multiplayer" or rasp == "m":
        client.send("\033[36mAi ales modul multiplayer\033[0m".encode())
        print("Mod selectat: Multiplayer")
        multi(client)
    else:
        client.send("\033[31m Comandă invalidă.\033[0m".encode())
        gest_client(client, adresa)

def cerinta(client, adresa):
    client.send("\033[35m*Ghicește numărul*\n"
                "                   Aplicație de tip server - client.\n"
                "                   Numărul ce trebuie ghicit se află în intervalul [0, 50].\n"
                "                   Există 2 posibilități:\n"
                "                   1=> Singleplayer: numărul este generat de server.\n"
                "                   2=> Multiplayer: numărul este dat de către un client (player1).\n"
                "                   La fiecare încercare de a ghici numărul, clientul va primi unul din\n"
                "                   mesajele : numărul este corect / numărul este mai mic / mai mare decât numărul ales.\n"
                "                   Fiecare rulare a scriptului va reprezenta o sesiune de joc, formată din mai multe\n"
                "                   partide de joc.\n"
                "                   La finalul sesiunii, se va afișa scorul maxim.\033[0m \n".encode())
    gest_client(client, adresa)

def single(client):
    global nr, scor

    while True:
        client.send("\033[35mJocul a început :)\033[0m".encode())
        runda_min = 1
        runda_max = 4
        #scor = []
        for runda in range(runda_min, runda_max):
            nr = random.randint(0, 50)
            print(f"Numărul {runda} este: {nr}")
            count = 0

            client.send(f"\033[36m\n                    Runda {runda} din {runda_max - 1}.\n"
                        "                    Serverul a generat un număr între 0 și 50. Ghicește!\033[0m".encode())

            while True:
                guess = client.recv(1024).decode().strip()
                if guess.isdigit() and 0 <= int(guess) <= 50:
                    guess = int(guess)
                    print("Clientul a introdus un nr din [0, 50]")

                    count += 1
                    
                    if guess == nr:
                        client.send(
                            "\033[32mNumărul este corect.\n"
                            f"                    L-ai ghicit din {count} încercări.\033[0m".encode())
                        break
                    elif guess < nr:
                        client.send("\033[33mNumărul este mai mare.\033[0m\n".encode())
                    else:
                        client.send("\033[33mNumărul este mai mic.\033[0m\n".encode())
                else:
                    client.send("\033[31mTrebuie un număr între 0 și 50.\033[0m\n".encode())
                    print("Clientul NU a introdus un nr din [0, 50] ")


            scor.append(count)
        scor_max = min(scor)
        client.send(f"\033[32mScor maxim: {scor_max}. \033[0m \n"
                    "\033[35m                    Jocul s-a încheiat!\033[0m \n"
                    "\033[36m                    Joc nou? <<da/exit>>:\033[0m".encode())

        rasp3 = client.recv(1024).decode().strip().lower()

        if rasp3 == "exit":
            #client.close()
            print("Jucătorul a încheiat jocul Singleplayer.")
            break
        elif rasp3 == "da":
            print("Continuam Jocul Singleplayer")
            continue

def multi(client):
    global nr2, scor2, clients

    with lock:  #accesul la lista clients
        if len(clients) >= 2:
            client.send("\033[31mServerul este ocupat. Încearcă mai târziu.\033[0m".encode())
            client.close()
            return
        clients.append(client)

    if len(clients) < 2:
        client.send("\033[36mAșteptăm conectarea unui alt jucător. \033[0m".encode())
        return

    player1, player2 = clients

    while True:
        runda_min = 1
        runda_max = 4

        for runda in range(runda_min, runda_max):
            mess = f"\033[36m\n                    Runda {runda} din {runda_max - 1}.\033[0m"
            try:
                player1.send(mess.encode())
                player2.send(mess.encode())
            except (ConnectionResetError, ConnectionAbortedError):
                print("Playerii au ieșit din joc.")
                player1.close()
                player2.close()
                return

            while True:
                player1.send("\033[35m\n                    Alege un număr între 0 și 50 pentru Player 2 să ghicească:\033[0m".encode())
                player2.send("\033[36m\n                    Așteaptă ca Player1 să aleagă un număr. \033[0m\n".encode())
                nr2 = player1.recv(1024).decode().strip()
                if nr2.isdigit() and 0 <= int(nr2) <= 50:
                    nr2 = int(nr2)
                    print("Player1 a ales un nr bun")
                    break
                else:
                    player1.send("\033[31mTrebuie să introduci un număr între 0 și 50!\033[0m\n".encode())
                    print("Player1 a ales un nr care nu e bun")

            #Player2
            player2.send("\033[36mPlayer 1 a ales un număr. Încearcă să ghicești!\033[0m\n".encode())
            count = 0

            while True:
                print("Player2 ghiceste")
                player2.send("\033[35mIntrodu un număr între 0 și 50:\033[0m\n".encode())
                guess = player2.recv(1024).decode().strip()
                if guess.isdigit() and 0 <= int(guess) <= 50:
                    guess = int(guess)
                    count += 1

                    if guess == nr2:
                        player1.send(
                            "\033[32mNumărul este corect.\n"
                            f"                    Player2 l-a ghicit din {count} încercări.\033[0m".encode())
                        player2.send(
                            "\033[32mNumărul este corect.\n"
                            f"                    L-ai ghicit din {count} încercări.\033[0m".encode())
                        break
                    elif guess < nr2:
                        player1.send("\033[33mNumărul este mai mare.\033[0m\n".encode())
                        player2.send("\033[33mNumărul este mai mare.\033[0m\n".encode())
                    else:
                        player1.send("\033[33mNumărul este mai mic.\033[0m\n".encode())
                        player2.send("\033[33mNumărul este mai mic.\033[0m\n".encode())

                else:
                    player2.send("\033[31mTrebuie să introduci un număr între 0 și 50!\033[0m\n".encode())

            scor2.append(count)
            scor_max2 = min(scor2)

            player1.send(f"\033[32mScorul maxim este: {scor_max2}.\033[0m\n".encode())
            player2.send(f"\033[32mScorul maxim este: {scor_max2}.\033[0m\n".encode())

        player1.send(f"\033[35m\n                    Jocul s-a terminat. Apasă <<exit>>\033[0m\n".encode())
        player2.send(f"\033[35m\n                    Jocul s-a terminat. Apasă <<exit>> \033[0m\n".encode())

        rasp1 = player1.recv(1024).decode().strip().lower()
        rasp2 = player2.recv(1024).decode().strip().lower()

        if rasp1 == "exit" and rasp2 == "exit":
            with lock:
                clients.remove(player1)
                clients.remove(player2)
            print("Jocul s-a terminat.")

def server_main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 2004
    host = "0.0.0.0"
    server.bind((host, port))
    server.listen(2)
    print("------------SERVER----------------------\n PORT: 2004 \n Așteptăm conexiuni :)")

    while True:
        client, adresa = server.accept()
        threading.Thread(target=gest_client, args=(client, adresa)).start()


if __name__ == "__main__":
    server_main()

