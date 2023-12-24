# zadaca 1
# Da se napise funkcija koja za vnesena lista i vnesen broevi ke gi ispecati
# indeksite na dva broevi taka sto nivniot zbir ke bide ednakov na vneseniot broevi.

def najdi_indeks(broevi, target):
    lista = {}
    for i, num in enumerate(broevi):
        rezultat = target - num
        if rezultat in lista:
            print(f"Indeksi: {lista[rezultat]}, {i}")
            return
        lista[num] = i
    print("Nema indeks na broevi")

generiraj_lista = list(map(int, input("Vnesi lista: ").split()))
target_broj = int(input("Vnesi broevi: "))

najdi_indeks(generiraj_lista, target_broj)

# zadaca 2
# Da se napise funkcija koja za vnesena lista so elementi ke ispecati dali e toa lista so palindromi.

palindrom = input("Vnesi elementi: ")

def proverka(palindrom):
    if palindrom[::-1] == palindrom:
        print("Zborot e palindrom")
        
    else:
        print("Zborot ne e palindrom")
        
proverka(palindrom)

# zadaca 3
# Da se napise funkcija koja za vnesena recenica ke ja isprinta dolzinata na posledniot zbor.

def dolzina_na_recenica(sentence):
    zbor = sentence.split()

    if len(zbor) == 0:
        print("Pogresen vnes.")
        return

    posleden_zbor = zbor[-1]

    print(f"Dolzinata na posledniot zbor iznesuva: {len(posleden_zbor)}")

recenica = input("Vnesi recenica: ")
dolzina_na_recenica(recenica)

# zadaca 4
# Da se napise funkcija koja za vnesen broevi N1 i broevi N2 ke pecati dali e N1 ednakov na N2 na nekoj stepen.

def stepen_od_N2():
    try:
        N1 = int(input("Vnesi go prviot broevi (N1): "))
        N2 = int(input("Vnesi go vtoriot broevi (N2): "))
    except ValueError:
        print("Pogresen vnes.Vnesi broevi")
        return

    stepen = 1
    rezultat = N2 ** stepen

    while rezultat <= N1:
        if rezultat == N1:
            print(f"{N1} e ednakov na {N2} krenat na stepen {stepen}")
            return

        stepen += 1
        rezultat = N2 ** stepen

    print(f"{N1} ne e ednakov na {N2} krenat na stepen")

stepen_od_N2()