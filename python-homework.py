import re

#ucitava id,name,price
def ucitaj1(nesto):
    recnik1 = dict()
    with open(nesto, "r") as file: #otvara datoteku koja sadrzi podatke id,name,price
        next(file)
        for line in file:
            id, *name, price = line.split(",") #odvaja clanove linije fajla prema zarezu
            ime = "" #u njega upisemo name kao string
            for part in name:
                ime += str(part) + ","

            ime = ime[:-1]
            if (ime.find('"') >= 0): #brise navodnike koji se nalaze ispred imena
                ime = ime[1:-1]

            if (price == "\n"): #ukoliko cena nije uneta, azuriramo vrednost cene na 0
                price = 0.00
            else:
                price = float(price)
            recnik1[id] = [ime, price] #recnik kljuca id, i podatka ime i price
        return recnik1

#ucitava datoteku sa id last_offer user
def ucitaj2(nesto, prva):
    recnik2 = dict() #kljuc recnika id, cuva za taj id najbolju ponudu od svh ponudjenih
    recnik3 = dict() #kljuc recnika id, cuva za taj id ukupan broj validnih ponuda
    a = ucitaj1(prva)
    try: #zbog mogucnosti da iznos nije tipa float
        with open(nesto, "r") as file:
           next(file) #preskace prvu liniju (jer ona sluzi kao objasnjenje)
           for line in file: #prolazi kroz linije fajla
            id, iznos, lic = line.split() #odvaja clanove po razmaku
            if id not in recnik2: #ubacuje id u recnik 2 ukoliko vec nije i ako je validna ponuda
                    if (float(a[id][1]) <= float(iznos)): #proverava da li je iznos veci od procenjene cene
                        recnik2[id] = [iznos, lic]
                        recnik3[id] = 1

            else: # ako je id vec u recniku
                    if (float(iznos) > float(recnik2[id][0])): #proverava da li je dati iznos validna ponuda
                        recnik2[id][0] = iznos
                        recnik2[id][1] = lic
                        recnik3[id] += 1 #povecamo broj validnih licitacija
        return recnik2, recnik3

    except ValueError: #ako je postojao neki iznos koji nije realan broj
        return "GRESKA"


#fja koja ukoliko nema gresaka procesira ulazne fajlove
def process(prva, druga):
    a = ucitaj1(prva)
    b,c = ucitaj2(druga,prva)
    lista = [] #u nju cemo ubacivati podliste gde jedna podlista oznacava red koji treba ispisati u fajlu result.txt
    for key, value in a.items():
        list = [] #podlista koju dodajemo na listu
        list.append(key)
        list.append(value[0])
        list.append(float(value[1]))
        if (key in b):
            if (float(b[key][0]) >= float(value[1])): #provera da li je nasa najveca ponuda koja je validna veca od procenjene cene
                list.append(c[key])
                list.append(float(b[key][0]))
                list.append(b[key][1])
        lista.append(list)
    return lista

def pisi(prva, druga):
    try: #jer postoji mogucnost da imamo DAT_GRESKU
        a=ucitaj1(prva)
        if (ucitaj2(druga, prva) == "GRESKA"):
            with open("result.txt", 'w') as file:
                s = "GRESKA"
                print(s,end="")
        else:
            lista=[]
            lista=process(prva,druga)
            i = 0
            with open("result.txt", 'w') as file:
                #prolazimo kroz listu cije podliste upisujemo u fajl
                while int(i) < len(lista):
            # print(lista[i], file=s)
                    for j in range(len(lista[i])):
                        broj1 = 0
                        #vise slucajeva za ispis postoji u zavisnosti gde treba u odnosu na element da stoji whitespace
                        if type(lista[i][j]) == float:
                           k = float(lista[i][j])
                           if (int(j) < len(lista[i]) - 1):
                              file.write("{:.2f} ".format(k))
                           else:
                              file.write("{:.2f}".format(k))
                        else:
                           if (int(j) < len(lista[i]) - 1):
                              file.write("{} ".format(lista[i][j]))
                           else:
                               file.write("{}".format(lista[i][j]))
                    if (int(i) < len(lista) - 1): #sve do poslednjeg reda prelazimo na kraju reda u novi
                        file.write("\n")
                    i += 1
    except FileNotFoundError:
      with open("result.txt", 'w') as file:
        print("DAT_GRESKA", end="")

#ucitavamo imena datoteka
prva = input()
druga = input()
pisi(prva,druga)