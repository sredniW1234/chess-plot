def notation_to_data(notation):
    note = notation.split(" ")

    # Removes all the 1. 2. 3
    x = 0
    for i in range(int(len(note) / 2 - 1)):
        note.pop(x)
        x += 2

    # White starting position
    pa2, pb2, pc2, pd2, pe2, pf2, pg2, ph2 = 12, 22, 32, 42, 52, 62, 72, 82
    ra1, rh8 = 11, 81
    nb1, ng1 = 21, 71
    bc1, bf1 = 31, 61
    qd1 = 41
    ke1 = 51

    # Black starting position
    pa7, pb7, pc7, pd7, pe7, pf7, pg7, ph7 = 17, 27, 37, 47, 57, 67, 77, 87
    ra8, rh8 = 18, 88
    nb8, ng8 = 28, 78
    bc8, bf8 = 38, 68
    qd8 = 48
    ke8 = 58

    # Convert notation to number data for updating position
