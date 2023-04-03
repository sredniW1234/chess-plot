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
    ra1, rh1 = [11], [81]
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

    # Piece groups
    nights = [nb1, ng1, nb8, ng8]
    rooks = [ra1, rh1, ra8, rh8]
    bishops = [bc1, bf1, bc8, bf8]
    pawns = [pa2, pb2, pc2, pd2, pe2, pf2, pg2, ph2, pa7, pb7, pc7, pd7, pe7, pf7, pg7, ph7]
    all_pieces = [pa2, pb2, pc2, pd2, pe2, pf2, pg2, ph2, ra1, rh1, nb1, ng1, bc1, bf1, qd1, ke1, pa7, pb7, pc7, pd7, pe7, pf7, pg7, ph7, ra8, rh8, nb8, ng8, bc8, bf8, qd8, ke8]

    # Convert notation to numbers
    print(note)
    for i in range(len(note)):
        note[i] = note[i].replace("a", "_1")
        note[i] = note[i].replace("b", "_2")
        note[i] = note[i].replace("c", "_3")
        note[i] = note[i].replace("d", "_4")
        note[i] = note[i].replace("e", "_5")
        note[i] = note[i].replace("f", "_6")
        note[i] = note[i].replace("g", "_7")
        note[i] = note[i].replace("h", "_8")
        note[i] = note[i].lower()

    # Determine black and white pieces
    for i, tempo in enumerate(note):
        if i % 2:
            note[i] = "b-" + note[i]
        else:
            note[i] = "w-" + note[i]
    print(note)

    # update notation for all pieces
    for i, tempo in enumerate(note):
        # Check if its whites tempo
        if "w-" in tempo:
            # Example: 1. e4 c6 2. d4 d5 3. e5 Bf5
            # Example 2: 1. Ndc4 Kg6 2. Nd2 Kh6 3. Nb2c4 Kg6 4. Nb2 Kh6 5. N6c4 Kg6 6. Nb6 Kh6
            # part the w-
            tempo = tempo.split("w-")[1]

            # if taking
            if "x" in tempo:
                # Case #1: nx_34 n n
                if not tempo[1].isnumeric() and not tempo[2].isnumeric():
                    print(tempo, "case1")
                # Case #2: n6x_34 y n
                elif tempo[1].isnumeric() and not tempo[2].isnumeric():
                    print(tempo, "case2")
                # case #3: n_4x_34 n y n
                elif not tempo[1].isnumeric() and tempo[2].isnumeric() and not tempo[3].isnumeric():
                    print(tempo, "case3")
                # case #4: n_22x_34 n y y
                elif not tempo[1].isnumeric and tempo[2].isnumeric() and tempo[3].isnumeric():
                    print(tempo, "case4")
            else:
                try:
                    if tempo[4] != None:
                        fourthI = True
                except IndexError:
                    fourthI = False
                print(fourthI, tempo, not fourthI)
                # Case #1: n_34 n y y e
                if not tempo[1].isnumeric() and tempo[2].isnumeric() and tempo[3].isnumeric() and fourthI != True:
                    print(tempo, "case1")
                # Case #2: n6_34 y n
                elif tempo[1].isnumeric() and not tempo[2].isnumeric():
                    print(tempo, "case2")
                # case #3: n_4_34 n y n
                elif not tempo[1].isnumeric() and tempo[2].isnumeric() and not tempo[3].isnumeric():
                    print(tempo, "case3")
                # case #4: n_22_34 n y y n
                elif not tempo[1].isnumeric and tempo[2].isnumeric() and tempo[3].isnumeric() and not tempo[4].isnumeric:
                    print(tempo, "case4")
