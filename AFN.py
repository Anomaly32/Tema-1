
fin = open("input_AFN.txt", "r")


def verificare(cuv, stare_curenta, index):
    if index == len(cuv):
        if stare_curenta in sf:
            return True
        else:
            return False
    if cuvant[index] not in tranzitii[stare_curenta]:
        return False
    tsc = tranzitii[stare_curenta][cuvant[index]]   # tranzitii stare curenta
    nt = len(tsc)                                   # numar tranzitii
    for i in range(nt):
        if verificare(cuv, tsc[i], index + 1) is True:
            return True


nr_stari = int(fin.readline())                  # numar total stari
nr_tranzitii = int(fin.readline())              # numar total tranzitii
tranzitii = list()                              # tranzitiile dintre stari
for i in range(nr_stari):
    tranzitii.append(dict())
for i in range(nr_tranzitii):
    aux = [x for x in fin.readline().split()]
    if aux[2] not in tranzitii[int(aux[0])]:
        tranzitii[int(aux[0])][aux[2]] = list()
    tranzitii[int(aux[0])][aux[2]].append(int(aux[1]))
si = int(fin.readline())                        # stare initiala
nr_sf = int(fin.readline())                     # numar stari finale
sf = [int(x) for x in fin.readline().split()]   # stari finale

nr_cuv = int(input("cate cuvinte veti introduce?: "))
for i in range(nr_cuv):
    cuvant = input("cuvantul de verificat este: ")
    if verificare(cuvant, si, 0) is True:
        print("cuvant valid")
    else:
        print("cuvant invalid")
