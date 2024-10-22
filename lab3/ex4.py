def song(notes, pos, start):
    song = []
    current = start
    song.append(notes[current])
    for x in pos:
        current = (current + x) % len(notes)
        song.append(notes[current])
    return song


notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start = 2
print(song(notes, moves, start))