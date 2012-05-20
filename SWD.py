#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import *

TypToS = {str(int):"int",str(float):"float",str(bool):"bool",str(unicode):"str",str(str):"str"}
SToTyp = {"int":int,"float":float,"bool":bool,"unicode":str,"str":str}

class Zbior:
	def __init__(self):
		self.lista = [] # wektory wartosci
		self.kolumny = [] # nazwy kolumn
		self.typy = [] # typy zmiennych
		pass
	def dodaj_liste(self,lista):
		self.lista += list(lista)
	def dodaj_typy(self,typy):
		self.typy += list(typy)
	def dodaj_kolumny(self,kolumny):
		self.kolumny += list(kolumny)
	def rzutuj_dane(self):
		for i in range(len(self.typy)):
			self.rzutuj(self.typy[i],i)
	def __repr__(self):
		s = "Liczba zmiennych: "+str(len(self.lista[0]))+"\n"
		s += "Liczba obserwacji: "+str(len(self.lista))+"\n"
		s += str(self.kolumny)+"\n"
		s += str(self.typy)+"\n"
		for i in self.lista:
			s+= str(i)+"\n"
		return s
	
	def zapisz(self,fname, separ, kol,typy):
		pl = open(fname,"w");
		#f = list(f)
		separ = str(separ)
		fname = str(fname)
		out = []
		if(kol):
			names = separ.join([str(x) for x in self.kolumny])
			out+= [names]
		if(typy):
			typy = separ.join([TypToS[str(x)] for x in self.typy])
			out+= [typy]
		items = []
		for i in range(len(self.lista)):
			items.append(separ.join([str(x) for x in self.lista[i]]))
		out += items
		pl.write('\n'.join(out))
		#write to file
		pl.close()
	def wczytaj(self,plik,separator,skip,nazwy_kolumn,nazwy_typow):
		pl = open(plik,"r");
		#f = list(f)
		f = pl.read().split('\n')
		pl.close()
		start = skip
		
		if (nazwy_kolumn):
			self.kolumny = f[start].split(separator)
			start += 1
		if (nazwy_typow):
			self.typy = [SToTyp[x] for x in f[start].split(separator)]
			start += 1
		
		for i in f[start:]:
			self.lista.append(i.split(separator))
		if (not nazwy_typow):
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
			if(na_co == float and type(self.lista[i][ktory]) in [str,unicode]):
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
		
	def klasyfikuj(self, obiekt, indeksy, klasa_decyzyjna, metryka, k):
		# obiekt - wiersz z wartoscia do klasyfikacji
		# indeksy - indeksy kolumn, na podstawie ktorych odbywac sie bedzie klasyfikacja
		# klasa_decyzyjna - indeks kolumny, ktora mamy ustawic
		# metryka - rodzaj metryki uzytej przy klasyfikacji
		# k- liczba najblizszych sasiadow
		zbior =[]
		wzor = []
		
		#ustalenie zbioru wektorow do klasyfikacji - na koncu kazdego wektora klasa decyzyjna
		for i in self.lista:
			tmp = []
			for j in range(len(indeksy)):
				tmp.append(i[indeksy[j]])
			tmp.append(i[klasa_decyzyjna])
			zbior.append(tmp)
			
		#ustalenie wektora wzorcowego 
		for i in range(len(indeksy)):
			wzor.append(obiekt[indeksy[i]])
		
		#na koncu kazdego wektora dodaje odleglosc od klasyfikowanego obiektu
		for i in range(len(zbior)):
			zbior[i].append(metryka(wzor, zbior[i][:-1]))
		
		#sortuje ten zbior wedlug odleglosci
		zbior.sort(key = lambda x: x[-1])
		
		#wybieram tylko k najblizszych sasiadow
		zbior = zbior[:k]
		
		lista = []
		
		for i in range(len(zbior)):
			lista.append(zbior[i][-2])

		return self.najczesciejWyst(lista)
		
		
	def najczesciejWyst(self, lista):
		return max(set(lista), key=lista.count)
		
		
	def metrykaEuklidesowa(self, A, B):
		suma = 0
		for i in range(len(A)):
			suma += pow(A[i] - B[i],2)
		suma = sqrt(suma)
		return suma
		
	def metrykaMiejska(self, A, B):
		suma = 0
		for i in range(len(A)):
			suma += fabs(A[i] - B[i])
		return suma
	
	def metrykaMahalanobisa(self, A, B):
		from numpy import cov
		from matrix import matrix
		cov_matrix=[]
		for i in cov(A,B):
			tmp = []
			for j in i:
				tmp.append(j)
			cov_matrix.append(tmp)
		cov_matrix = matrix(cov_matrix)
		print cov_matrix
		pass #usun to jak cos tu wstawisz
	
	def ocenaKlasyfikacji(self, k, metryka, klasa_decyzyjna, indeksy):
		for i in range(len(self.lista)):
			self.lista[i].append(self.klasyfikuj(self.lista[i], indeksy, klasa_decyzyjna, metryka, k))
		
		ile = 0
		for i in range(len(self.lista)):
			if (self.lista[i][klasa_decyzyjna] == self.lista[i][-1]):
				ile += 1

		return [ile,len(self.lista)]

	def _srednia(self, obiekty):
		sr = [0]*len(obiekty[0])
		for zm in range(len(obiekty[0])):
			suma = 0
			for i in obiekty:
				suma += i[zm]
			sr[zm] = float(suma)/len(obiekty)
		return sr


	def licz_k_srednich(self, k, metryka, klasa_decyzyjna, indeksy, N=None, dopasuj=True):
		"""
		Funkcja klasyfikujaca metoda k-srednich

		metryka - metryka odleglosci
		k - k klas
		klasa_decyzyjna - indeks kolumny klasy decyzyjnej
		indeksy - indeksy kolumn wartosci
		N - ile razy iterowac jesli podane N,
		jesli nie podane, iterowac az nie ma zmian pomiedzy klasami (max 500 iteracji)
		"""
		wartosci = []
		klasy_prawdziwe = []
		for wektor in self.lista:
			wartosci.append([wektor[i] for i in indeksy])
			klasy_prawdziwe.append(wektor[klasa_decyzyjna])
		from random import sample
		srednie = sample(wartosci,k)
		klasy_tmp = [-1]*len(wartosci)

		def iteruj(klasy_tmp, srednie):
			for w in range(len(wartosci)):
				min = [0,metryka(wartosci[w],srednie[0])]
				for s_idx in range(len(srednie)):
					dystans = metryka(srednie[s_idx],wartosci[w])
					if dystans < min[1]:
						min = [s_idx, dystans]
				klasy_tmp[w] = min[0]
			for i in range(k):
				obiekty = [wartosci[w] for w in range(len(wartosci)) if klasy_tmp[w]==i]
				srednie[i] = self._srednia(obiekty)

			return [klasy_tmp, srednie]

		if N:
			for i in range(N):
				klasy_tmp, srednie = iteruj(list(klasy_tmp), list(srednie))
		else:
			for i in range(500):
				klasy_tmp_prev, srednie_prev = list(klasy_tmp), list(srednie)
				klasy_tmp, srednie = iteruj(list(klasy_tmp), list(srednie))

				if klasy_tmp == klasy_tmp_prev:
					break

		def poprawnie_sklasyfikowanych(mapping):
			correct = 0.
			for i in range(len(klasy_prawdziwe)):
				if klasy_tmp[i] == mapping[klasy_prawdziwe[i]]:
					correct+=1
			return correct/len(klasy_prawdziwe)

		if not dopasuj: #jesli nie dopasowujemy klas poczatkowych, zwracamy jedynie wynik i srednie
			return [klasy_tmp, srednie]
		else:
			from itertools import permutations
			klasy_prawdziwe_typy = list(set(klasy_prawdziwe))
			if k == len(klasy_prawdziwe_typy):
				best_klas = [-1.,range(k)]
				for perm in permutations(range(k)):
					mapping = dict((klasy_prawdziwe_typy[i], perm[i]) for i in range(k))
					popr_val = poprawnie_sklasyfikowanych(mapping)
					if popr_val > best_klas[0]:
						best_klas = [popr_val, perm]

				mapping = dict((klasy_prawdziwe_typy[i], best_klas[1][i]) for i in range(k))
				mapping2 = dict((v,k) for k,v in mapping.items())
				for w in range(len(self.lista)):
					self.lista[w].append(mapping2[klasy_tmp[w]])
				self.kolumny.append('Metoda %d-srednich'%(k))
				self.typy.append(str)
				return {'result':'OK', 'val':best_klas[0], 'perm': best_klas[1]}
			else:
				for w in range(len(self.lista)):
					self.lista[w].append(klasy_tmp[w])
				self.kolumny.append('Metoda %d-srednich'%(k))
				self.typy.append(int)
				return {'result':'NIE'}



def main():
	z = Zbior()
	z.wczytaj('dane2.txt', '\t', 0, 1,1)
	z.rzutuj(float, 4)
	z.rzutuj(float, 5)
	z.rzutuj(float, 6)
	#z.rzutuj(int, 7)
	#z.rzutuj(str, 1)
	#z.rzutuj(float, 4)
	#z.usun_zmienna(0)
	#z.dyskretyzuj(7,3)
	#z.dyskretyzuj2(7,3)
	#z.standaryzuj(7)
	#z.normalizuj(10,100,7)
	#z.odchylenie_trzykrotne(7)
	#z.odstajace_procentowo(0.1, 0.9, 4)
	obiekt = ["EKSPERM", 0,"PO_1","L", 13.32, 11.0 ,4 ,6]
	#print z.klasyfikuj(obiekt, [4,5,6], 1, z.metrykaMiejska, 5)
	ocena = z.ocenaKlasyfikacji(5, z.metrykaEuklidesowa, 1, [4,5,6])	
	print "%d/%d: %f"%(ocena[0],ocena[1],float(ocena[0])/ocena[1])
	
	#print z
def DBG_Mahalanobis():
	from numpy import cov,matrix,linalg
	#from matrix import matrix
	from math import sqrt
	A = [1,3,4,5]
	B = [3,4,5,6]
	X = matrix([A])
	Y = matrix([B])
	cov_matrix=[]
	for i in range(len(A)):
		tmp = []
		for j in range(len(A)):
			tmp_cov = cov([A[i],B[j]])
			tmp.append(float(tmp_cov))
		cov_matrix.append(tmp)
	cov_matrix = matrix(cov_matrix)
	C = cov_matrix
	print X
	print Y
	print linalg.det(C)
	#return sqrt( (X-Y)*C.I*(X-Y).T )

def DBG_k_srednich():
	z = Zbior()
	z.wczytaj('dane/irisdat2.txt', '\t', 0, 1,1)
	z.rzutuj_dane()
	output = z.licz_k_srednich(3,z.metrykaEuklidesowa,4,[0,1,2,3], None)
	if output['result'] == 'OK':
		print output['val']
if(__name__ == "__main__"):
	DBG_k_srednich()

