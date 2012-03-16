class Zbior:
	liczba = 12
	def __init__(self):
		self.lista = []
		self.kolumny = []
		self.typy = []
		pass
	def dodaj_liste(self,lista):
		self.lista += list(lista)
	def dodaj_typy(self,typy):
		self.typy += list(typy)
	def dodaj_kolumny(self,kolumny):
		self.kolumny += list(kolumny)
	def __repr__(self):
		s = ""
		s += str(self.kolumny)+"\n"
		s += str(self.typy)+"\n"
		for i in self.lista:
			s+= str(i)+"\n"
		return s
	
	def wczytaj(self,plik,separator,skip,nazwy_kolumn):
		f = open(plik,"r");
		f = list(f)
		if (nazwy_kolumn):
			self.kolumny.append(f[skip].split(separator))
		for i in f[skip+1:]:
			self.lista.append([i.split(separator)])
		return self.lista
#ania to dopisala ¿eby zobaczyc czy dzia³a
# druga zmiana zeby konflikt zobaczyc

if(__name__ == "__main__"):
	z = Zbior()
	z.wczytaj('dane.txt', '	', 11, 'Q')
	#z.dodaj_liste([1,2,"napis",True,1.233])
	#z.dodaj_typy([int,int,str,bool,float])
	print z
	#print z
	#z.dodaj_liste(["ALA","Warszawa"])
	#z.dodaj_typy([str,str])
	#print z
	#x = float
	#liczba = 1
	#print x(liczba) #float(liczba)
