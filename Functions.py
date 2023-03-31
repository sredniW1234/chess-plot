import math


def notation_to_data(notation):
    note = notation.split(" ")

    # Removes all the 1. 2. 3
    x = 0
    for i in range(math.floor(len(note) / 3)):
        note.pop(x)
        x += 2

    # White starting position
    pa2, pb2, pc2, pd2, pe2, pf2, pg2, ph2 = [12], [22], [32], [42], [52], [62], [72], [82]
    ra1, rh8 = [11], [81]
    nb1, ng1 = [21], [71]
    bc1, bf1 = [31], [61]
    qd1 = [41]
    ke1 = [51]

    # Black starting position
    pa7, pb7, pc7, pd7, pe7, pf7, pg7, ph7 = [17], [27], [37], [47], [57], [67], [77], [87]
    ra8, rh8 = [18], [88]
    nb8, ng8 = [28], [78]
    bc8, bf8 = [38], [68]
    qd8 = [48]
    ke8 = [58]

    # Convert notation to numbers
    print(note)
    for i in range(len(note)):
        if i % 2:
            note[i] = note[i].replace("a", "-B1")
            note[i] = note[i].replace("b", "-B2")
            note[i] = note[i].replace("c", "-B3")
            note[i] = note[i].replace("d", "-B4")
            note[i] = note[i].replace("e", "-B5")
            note[i] = note[i].replace("f", "-B6")
            note[i] = note[i].replace("g", "-B7")
            note[i] = note[i].replace("h", "-B8")
            note[i] = note[i].lower()
        else:
            note[i] = note[i].replace("a", "-W1")
            note[i] = note[i].replace("b", "-W2")
            note[i] = note[i].replace("c", "-W3")
            note[i] = note[i].replace("d", "-W4")
            note[i] = note[i].replace("e", "-W5")
            note[i] = note[i].replace("f", "-W6")
            note[i] = note[i].replace("g", "-W7")
            note[i] = note[i].replace("h", "-W8")
            note[i] = note[i].lower()
    print(note)

    # update notation for all pieces
    for i in range(len(note)):
        # update horse movement white
        if "n-w" in note[i]:
            note_number = int(note[i].split("-w")[1])
            if note_number + 12 == nb1[-1] or note_number + 21 == nb1[-1] or note_number + 19 == nb1[-1] or note_number\
                    + 8 == nb1[-1] or note_number - 12 == nb1[-1] or note_number - 21 == nb1[-1] or \
                    note_number - 19 == nb1[-1] or note_number - 8 == nb1[-1]:
                nb1.append(note_number)
                print(nb1)
            if note_number + 12 == ng1[-1] or note_number + 21 == ng1[-1] or note_number + 19 == ng1[-1] or note_number\
                    + 8 == ng1[-1] or note_number - 12 == ng1[-1] or note_number - 21 == ng1[-1] or \
                    note_number - 19 == ng1[-1] or note_number - 8 == ng1[-1]:
                ng1.append(note_number)
                print(ng1)

        # update horse movement black
        if "n-b" in note[i]:
            note_number = int(note[i].split("-b")[1])
            if note_number + 12 == nb8[-1] or note_number + 21 == nb8[-1] or note_number + 19 == nb8[-1] or note_number\
                    + 8 == nb8[-1] or note_number - 12 == nb8[-1] or note_number - 21 == nb8[-1] or \
                    note_number - 19 == nb8[-1] or note_number - 8 == nb8[-1]:
                nb8.append(note_number)
                print(nb8)
            if note_number + 12 == ng8[-1] or note_number + 21 == ng8[-1] or note_number + 19 == ng8[-1] or note_number\
                    + 8 == ng8[-1] or note_number - 12 == ng8[-1] or note_number - 21 == ng8[-1] or \
                    note_number - 19 == ng8[-1] or note_number - 8 == ng8[-1]:
                ng8.append(note_number)
                print(ng8)

        if "b-w" in note[i]:
            note_number = note[i].split("-w")[1]
            if int(note_number[0]) % 2 and not int(note_number[1]) % 2:
                bf1.append(note_number)
            elif not int(note_number[0]) % 2 and int(note_number[1]) % 2:
                bf1.append(note_number)
            else:
                bc1.append(note_number)

        if "b-b" in note[i]:
            note_number = note[i].split("-b")[1]
            if int(note_number[0]) % 2 and not int(note_number[1]) % 2:
                bf8.append(note_number)
            elif not int(note_number[0]) % 2 and int(note_number[1]) % 2:
                bf8.append(note_number)
            else:
                bc8.append(note_number)
