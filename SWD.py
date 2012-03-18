class Zbior:
	def __init__(self):
		self.lista = []
		self.kolumny = []
		self.typy = []
		self.liczba_zm = 0
		self.liczba_obs = 0
		pass
	def dodaj_liste(self,lista):
		self.lista += list(lista)
	def dodaj_typy(self,typy):
		self.typy += list(typy)
	def dodaj_kolumny(self,kolumny):
		self.kolumny += list(kolumny)
	def __repr__(self):
		s = "Liczba zmiennych: "+str(self.liczba_zm)+"\n"
		s += "Liczba obserwacji: "+str(self.liczba_obs)+"\n"
		s += str(self.kolumny)+"\n"
		s += str(self.typy)+"\n"
		for i in self.lista:
			s+= str(i)+"\n"
		return s
	
	def wczytaj(self,plik,separator,skip,nazwy_kolumn):
		pl = open(plik,"r");
		#f = list(f)
		f = pl.read().split('\n')
		pl.close()
		
		if (nazwy_kolumn):
			self.kolumny = f[skip].split(separator)
		else: 
			skip -=1
		
		self.liczba_zm = len(self.kolumny)
		
		for i in range(self.liczba_zm):
			self.typy.append(unicode)
		
		for i in f[skip+1:]:
			self.lista.append(i.split(separator))
			
		self.liczba_obs= len(self.lista)
		return self.lista
		
	def usun_obserwacja(self, ktora):
		self.lista.pop(ktora)
		self.liczba_zm -= 1 
	
	def usun_zmienna(self, ktora):
		for i in range(len(self.lista)):
			self.lista[i].pop(ktora)
		self.typy.pop(ktora)
		self.kolumny.pop(ktora)
		self.liczba_zm -=1
	
	def rzutuj(self, na_co, ktory):
		self.typy[ktory] = na_co
		for i in range(len(self.lista)):
			self.lista[i][ktory] = na_co(self.lista[i][ktory])

if(__name__ == "__main__"):
	z = Zbior()
	z.wczytaj('dane.txt', '    ', 11, 1)
	z.rzutuj(int, 7)
	z.rzutuj(str, 1)
	z.usun_zmienna(0)
	print z