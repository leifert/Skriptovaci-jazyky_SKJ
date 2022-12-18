import os

def get_files(path):
    """
    ziskejte seznam souboru z cesty "path". Tento adresar tento profiltrujte tak, ze ziskate pouze txt soubory (pouzijte list comprehension). vratte serazeny seznam souboru (funkce sort)
    soubory vratte i s adresarem (funkce os.path.join(adresar, soubor))
    """
    path = path+'/'
    ext = '.txt'
    txt_files = [os.path.join(path,f) for f in os.listdir(path) if f.endswith(ext)]
    return txt_files

def parse_match(table, line):
    """
    funkce zpracuje radek (line) ze souboru ve formatu tym1 tym2 goly1:goly2 - pro rozdeleni retezce pouzijte funkci split(oddelovac)
    pro odstraneni prazdnych znaku na konci retezce pouzijte funkci rstrip()
    do funkce je predana tabulka v podobe slovniku tym: pocet_bodu - tuto tabulku aktualizujte
    """
    line = line.rstrip()
    main_parts = line.split(" ")
    score = main_parts[2].split(':')
    score = [int(i) for i in score]
    club_names = [main_parts[0], main_parts[1]]

    for club in club_names:
        if club not in table:
            table.setdefault(club, 0)

    if score[0] == score[1]:
        table[club_names[0]] = table[club_names[0]] + 1
        table[club_names[1]] = table[club_names[1]] + 1
    elif score[0] > score[1]:
        table[club_names[0]] = table[club_names[0]] + 3
    else:
        table[club_names[1]] = table[club_names[1]] + 3


def generate_table(files, **kw):
    """
    funkce vytvori tabulku tymu tak, ze zpracuje vysledky ze souboru
    funkce bude mit i keyword argumenty _from a _to: interval kol, ze kterych se vytvori tabulka (idealne pres slicing files[from:to]; pozor na index vs. cislo kola)
    otevrete jednotlive soubory, v nem budou radky ve formatu, jak ocekava funkce parse_match, takze vyuzijte tuto funkci a vytvorte tabulku (typ dictionary), kterou vratte
    """

    table = {}
    if "_from" in kw and "_to" in kw:
        try:
            for file in files[kw["_from"]:kw["_to"]]:
                with open(file, "rt", encoding="utf8") as input_file:
                    for line in input_file:
                        parse_match(table, line)
        except IOError as e:
            print(e)

    elif "_from" in kw and "_to" not in kw:
        try:
            for file in files[kw["_from"]]:
                with open(file, "rt", encoding="utf8") as input_file:
                    for line in input_file:
                        parse_match(table, line)
        except IOError as e:
            print(e)
    elif "_from" not in kw and "_to" in kw:
        try:
            for file in files[:kw["_to"]]:
                with open(file, "rt", encoding="utf8") as input_file:
                    for line in input_file:
                        parse_match(table, line)
        except IOError as e:
            print(e)
    else:
        try:
            for file in files:
                with open(file, "rt", encoding="utf8") as input_file:
                    for line in input_file:
                        parse_match(table, line)
        except IOError as e:
            print(e)


    return table

def print_table(data):
    print(16*"-")
    for w in sorted(data, key=lambda x : data[x], reverse=True):
        print(w, data[w])


""" test funkce get_files, po dopsani zbytku kodu, muzete smazat """
#files = get_files("data")
#assert files == ['data/01.txt', 'data/02.txt', 'data/03.txt', 'data/04.txt', 'data/05.txt', 'data/06.txt', 'data/07.txt', 'data/08.txt']
#print(get_files("data"))
""" test funkce parse_match, po dopsani zbytku kodu, muzete smazat """
#table = {}
#parse_match(table, "Liberec Plzen 1:2")
#parse_match(table, "Plzen Olomouc 3:3")
#assert table == {'Liberec': 0, 'Plzen': 4, 'Olomouc': 1}

""" zde je test cele aplikace; vypise se tabulka po vsech kolech a po trech kolech """
files = get_files("data")
d = generate_table(files)
assert d['Slavia'] == 22 and d['Ostrava'] == 16 and d['Liberec'] == 5
print_table(d)
d = generate_table(files, _to=3)
assert d['Slavia'] == 9 and d['Ostrava'] == 6 and d['Liberec'] == 1
print_table(d)

