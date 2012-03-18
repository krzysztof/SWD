from math import sqrt

class Zbior:
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
		s = "Liczba zmiennych: "+str(len(self.lista[0]))+"\n"
		s += "Liczba obserwacji: "+str(len(self.lista))+"\n"
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
		
		for i in f[skip+1:]:
			self.lista.append(i.split(separator))
		for i in range(len(self.lista[0])):
			self.typy.append(unicode)
		
		if(not nazwy_kolumn):
			for i in range(len(self.lista[0])):
				self.kolumny.append('kolumna '+str(i))
		return self.lista
		
	def usun_obserwacja(self, ktora):
		self.lista.pop(ktora)
	
	def usun_zmienna(self, ktora):
		for i in range(len(self.lista)):
			self.lista[i].pop(ktora)
		self.typy.pop(ktora)
		self.kolumny.pop(ktora)

	def rzutuj(self, na_co, ktory):
		self.typy[ktory] = na_co
		for i in range(len(self.lista)):
			if(na_co == float):
				self.lista[i][ktory] = na_co(self.lista[i][ktory].replace(',','.'))
			else:
				self.lista[i][ktory] = na_co(self.lista[i][ktory])
	
	def dyskretyzuj(self,ktora, n):
		min = self.lista[0][ktora]
		max = self.lista[0][ktora]
		for i in range(len(self.lista)):
			if(min > self.lista[i][ktora]):
				min = self.lista[i][ktora]
			if(max < self.lista[i][ktora]):
				max = self.lista[i][ktora]
		
		krok = (max-min)/n
		
		for i in range(len(self.lista)):
			if (self.lista[i][ktora] == max):
				self.lista[i].append(n-1)
			else:
				self.lista[i].append(int((self.lista[i][ktora]-min)/n))
		
		self.kolumny.append('Przedzialy dlugosci: ' + self.kolumny[ktora])
		self.typy.append(int)
		
	def dyskretyzuj2(self, ktora, n):
		pom = []
		for i in range(len(self.lista)):
			pom.append(self.lista[i][ktora])
			
		klucze = self.daj_klucze(pom)
		wystapienia = [0] * len(klucze)
		
		for i in range(len(klucze)):
			wystapienia[i] = pom.count(klucze[i])
		klucze =zip(klucze, wystapienia)
		klucze.sort(key = lambda x:x[1], reverse = True)
		for i in range(len(self.lista)):
			self.lista[i].append(min(self.klasa_liczn(self.lista[i][ktora],klucze),n))
		self.kolumny.append('Przedzialy licznosci: ' + self.kolumny[ktora])
		self.typy.append(int)
		print klucze
		
	def klasa_liczn(self,el,klucze):
		new_wart = [i[1] for i in klucze]
		new_wart = self.daj_klucze(new_wart)
		liczn = 0
		for i in klucze:
			if(el == i[0]):
				liczn = i[1]
		for i in range(len(new_wart)):
			if(liczn==new_wart[i]):
				return i

	def daj_klucze(self,seq): 
		checked = []
		for e in seq:
			if e not in checked:
				checked.append(e)                      
		return checked
	
	def standaryzuj(self, ktora):
		suma = 0.00
		for i in range(len(self.lista)):
			suma += self.lista[i][ktora]

		srednia = suma/ len(self.lista)
		wariancja = 0.00
		for i in range(len(self.lista)):
			wariancja += (self.lista[i][ktora] - srednia)**2
		wariancja = wariancja / len(self.lista)
		odchylenie = sqrt(wariancja)
		
		for i in range(len(self.lista)):
			self.lista[i].append(round(float((float(self.lista[i][ktora]-srednia))/float(odchylenie)),2))
		
		self.kolumny.append('Standaryzacja: ' + self.kolumny[ktora])
		self.typy.append(float)
		
	def normalizuj(self, w_min, w_maks, ktora):
		min = self.lista[0][ktora]
		max = self.lista[0][ktora]
		for i in range(len(self.lista)):
			if(min > self.lista[i][ktora]):
				min = self.lista[i][ktora]
			if(max < self.lista[i][ktora]):
				max = self.lista[i][ktora]

		for i in range(len(self.lista)):
			tmp = float((self.lista[i][ktora]-min)*(w_maks-w_min)/(max-min))
			self.lista[i].append(round(tmp + w_min,2))
		
		self.kolumny.append('Normalizacja: ' + self.kolumny[ktora])
		self.typy.append(float)
	
	def odchylenie_trzykrotne(self, ktora):
		suma = 0.00
		for i in range(len(self.lista)):
			suma += self.lista[i][ktora]

		srednia = suma/ len(self.lista)
		wariancja = 0.00
		for i in range(len(self.lista)):
			wariancja += (self.lista[i][ktora] - srednia)**2
		wariancja = wariancja / len(self.lista)
		odchylenie = sqrt(wariancja)
		
		for i in range(len(self.lista)):
			if (abs(self.lista[i][ktora]-srednia) > abs(3 * odchylenie)):
				self.lista[i].append(1)
			else:
				self.lista[i].append(0)
		
		self.kolumny.append('Czy odstaje: ' + self.kolumny[ktora])
		self.typy.append(bool)
		
	def odstajace_procentowo(self, proc_min, proc_maks, ktora):
		min = self.lista[0][ktora]
		max = self.lista[0][ktora]
		for i in range(len(self.lista)):
			if(min > self.lista[i][ktora]):
				min = self.lista[i][ktora]
			if(max < self.lista[i][ktora]):
				max = self.lista[i][ktora]
		for i in range(len(self.lista)):
			tmp = float(self.lista[i][ktora]-min)/ float(max-min)
			if(tmp< proc_min or tmp > proc_maks):
				self.lista[i].append(1)
			else:
				self.lista[i].append(0)
				
		self.kolumny.append('Czy odstaje proc: ' + self.kolumny[ktora])
		self.typy.append(bool)
			
if(__name__ == "__main__"):
	z = Zbior()
	z.wczytaj('dane.txt', '    ', 11, 1)
	z.rzutuj(int, 7)
	z.rzutuj(str, 1)
	z.rzutuj(float, 4)
	#z.usun_zmienna(0)
	#z.dyskretyzuj(7,3)
	#z.dyskretyzuj2(7,3)
	#z.standaryzuj(7)
	#z.normalizuj(10,100,7)
	z.odchylenie_trzykrotne(7)
	z.odstajace_procentowo(0.1, 0.9, 4)
	print z
