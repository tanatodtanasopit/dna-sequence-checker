while True:
    seq=input("DNA sequence: ").upper()
    valid = all(base in 'ATCG' for base in seq)
    if valid:
        a, g, c, t = seq.count('A'), seq.count('G'), seq.count('C'), seq.count('T')
        gc = round((g + c) / len(seq) * 100, 1)
        print(f"Valid sequence\nLength: {len(seq)}\nA: {a} G: {g} C: {c} T: {t}\nGC Content: {gc}")
        break
    print('Invalid sequence')