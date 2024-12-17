import socket
import threading
import sys

def gest_mesaje(client):
    while True:
        try:
            data = client.recv(1024).decode()
            sys.stdout.write("\r"
                             + "    " * 20
                             + "\r")
            print(f"\nMesaj de la Server: {data}")
            sys.stdout.write("-------------------> ")
            sys.stdout.flush()
        except ConnectionAbortedError as e:
            print("\033[35mO zi frumoasă!\033[0m")
            break
        except Exception as e:
            print(f"Eroare :( {e}")
            break

def main():
    port = 2004
    ip = "127.0.0.1"
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    print("\033[35m--------------------Ghicește numărul!-------------------\033[0m")

    threading.Thread(target=gest_mesaje, args=(client,)).start()

    while True:
            mesaj = input()
            if mesaj.lower().strip() == "exit":
                print("\033[31mAi ieșit din joc.\033[0m")
                client.send("exit".encode())
                client.close()
                break
            client.send(mesaj.encode())

if __name__ == "__main__":
    main()
