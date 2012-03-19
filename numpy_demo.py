from pylab import *
def daj_klucze(seq): 
	checked = []
	for e in seq:
		if e not in checked:
			checked.append(e)                      
	return checked
def get_sets(zbior,kol_dist):
	zbior

def wykres(t,s,kolor,x_str,y_str):
	kolory = ['b','g','r','c','m','y','k','w'] + [(r,g,b) for r in arange(0.5,1.,0.1) for g in arange(0.0,0.5,0.1) for b in arange(0.3,0.5,0.1)]
	distinct = daj_klucze(kolor)
	kol_dist = zip(kolory,distinct)
	zbior = zip(t,s,kolor)
	sety = []
	for i in range(len(kol_dist)):
		sety.append([z for z in zbior if z[2]==kol_dist[i][1]])
	for i in sety:
		t = [z[0] for z in i]
		s = [z[1] for z in i]
		for j in kol_dist:
			if(z[2]==j[1]):
				kol = j[0]
				break;
		plot(t, s, color=kol,marker='o',linestyle='None')	
	xlabel(x_str)
	ylabel(y_str)
	title('SWD')
	grid(True)
	show()
