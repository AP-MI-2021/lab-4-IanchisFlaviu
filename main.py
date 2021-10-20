def print_menu():
    print("Menu")
    print("0.Exit")
    print("1.Creare lista")
    print("2.Afisarea listei")
    print("3.afisare numere negative")
    print("4.Afisarea celui mai mic numar care are ultima cifra egala cu o cifra data")
    print("5.Afisarea numerelor superprime din lista")


def create_list():
    lst = []
    size = int(input("Dati lungimea sirului: "))
    while size:
        lst.append(int(input()))
        size = size - 1
    return lst


def print_list(lst):
    for number in lst:
        print(number)


def afisare_nr_negative(lst):
    new_list = []
    for i in lst:
        if i < 0:
            new_list.append(i)
    return new_list


def ultimaNrMic(ultCif, lst):
    min = 0
    for i in lst:
        if i % 10 == ultCif:
            min = i
            break

    ok = False
    for i in lst:
        if i < 0:
            i = -i
            ok = True
        if (i % 10 == ultCif):
            if min > i:
                if ok == True:
                    min = -i
                else:
                    min = i

    return min


def prim(i):
    if i % 2 == 0 and i != 2:
        return False
    if i < 2:
        return False
    d = 3
    while d * d < i:
        if i % d == 0:
            return False
        d = d + 2
    return True


def isSuperPrim(i):
    while prim(i):
        i = i // 10
    if i == 0:
        return True
    else:
        return False


def superPrime(lst):
    newList = []
    for i in lst:
        if isSuperPrim(i):
            newList.append(i)
    return newList


def main():
    lst = []
    while True:
        print_menu()
        option = int(input("Alege optiunea: "))
        if option == 0:
            break
        if option == 1:
            lst = create_list()
        if option == 2:
            print_list(lst)
        if option == 3:
            print_list(afisare_nr_negative(lst))
        if option == 4:
            ultCif = int(input("Dati o cifra: "))
            print(ultimaNrMic(ultCif, lst))
        if option == 5:
            newList = superPrime(lst)
            print_list(newList)


def test_nr_negative():
    new_list = afisare_nr_negative([2, -4, 0, -5, -1, -2])
    assert (new_list == [-4, -5, -1, -2])

    new_list = afisare_nr_negative([])
    assert (new_list == [])

    new_list = afisare_nr_negative([1, 2, 3, 4])
    assert (new_list == [])


def test_ultima_cif():
    numar = ultimaNrMic(2, [22, -41, 0, -52, -21, -12])
    assert (numar == -12)

    numar = ultimaNrMic(0, [22, -41, 0, -52, -21, -12])
    assert (numar == 0)

    numar = ultimaNrMic(5, [22, -41, 0, -52, -21, -12])
    assert (numar == 0)


def test_superPrime():
    lst = superPrime([41, 239, 10, 24])
    assert (lst == [239])

    lst = superPrime([41, 239, 29, 24])
    assert (lst == [239, 29])

    lst = superPrime([41, 28, 10, 24])
    assert (lst == [])


def test_prim():
    assert prim(4) == 0
    assert prim(2) == 1
    assert prim(13) == 1
    assert prim(1) == 0


def test():
    test_nr_negative()
    test_ultima_cif()
    test_prim()
    test_superPrime()


test()
main()
