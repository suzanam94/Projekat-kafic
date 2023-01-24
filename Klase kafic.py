class Proizvodi:
    
    def __init__(self, id_proizvod, pice, cena):
        self.id_proizvod = id_proizvod
        self.pice = pice
        self.cena = cena

    def __str__(self):
        return f"{self.id_proizvod} {self.pice} {self.cena}"

class Proizvod:

    def __init__(self):
        self.lista = []

    def ucitavanje(self):
        l = [line.strip() for line in open("Picovnik.txt")]

        for i in l:
            id_proizvod = i.split("|")[0]
            pice = i.split("|")[1]
            cena = i.split("|")[2]

            p = Proizvodi(id_proizvod, pice, cena)
            self.lista.append(p)

class Kafic:
    def __init__(self,id_stola, narudzbina, racun):
        self.id_stola = id_stola
        self.narudzbina = narudzbina
        self.racun = racun
        

    def __str__(self):
        return f"{self.id_stola} {self.narudzbina} {self.racun}"

class Kafe:

    def __init__(self):
        self.lista_stolova=[]

    def ucitavanje_stola(self):
        stolovi = [linija.strip() for linija in open("Stolovi.txt")]

        for i in stolovi:
            id_stola = i.split(" ")[0]
            narudzbina = []
            racun = []

            s = Kafic(id_stola, narudzbina, racun)
            self.lista_stolova.append(s)

    def dodavanje(self,id_stola,id_proizvod):
        for i in self.lista_stolova:
            if id_stola == i.id_stola:
                for j in p.lista:
                    if id_proizvod == j.id_proizvod:
                        i.narudzbina.append(j.id_proizvod)
                        i.racun.append(j.cena)
                        self.ucitavanje_kafica()
                        return "Proizvod je dodat."
                return "Ne postoji proizvod sa tim ID"
        return "Ne postoji sto sa tim ID"

    def racun(self, id_stola):
        for i in self.lista_stolova:
            if id_stola == i.id_stola:
                r = sum([eval(i) for i in i.racun])
                return r
        return "Ne postoji sto sa tim ID"
        
                
                
                        

    def ucitavanje_kafica(self):
        f = open("Stolovi.txt","w")
        f.close()
        f=open("Stolovi.txt","a")
        for i in K.lista_stolova:
            print(i, file=f)
        f.close()


    

P = Proizvodi("",""," ")
p = Proizvod()
p.ucitavanje()
k = Kafic ("1", "2", "3")
K = Kafe()
K.ucitavanje_stola()
##print(K.dodavanje("1","2"))
##print(K.dodavanje('1', '3'))
##print(K.dodavanje('2', '3'))
##print(K.racun('1'))
##print(K.racun('2'))

##for i in K.lista_stolova:
##    print(i)
##for i in p.lista:
##    print(i)
        
