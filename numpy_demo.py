from pylab import *
kolory = ['b','g','r','c','m','y','k','w'] + [(r,g,b) for r in arange(0.5,1.,0.1) for g in arange(0.0,0.5,0.1) for b in arange(0.3,0.5,0.1)]
def wykres3D(x,y,z,kolor,labels):
	#print x
	#print y
	#print z
	import numpy as np
	from mpl_toolkits.mplot3d import Axes3D
	import matplotlib.pyplot as plt

	#def randrange(n, vmin, vmax):
	#	return (vmax-vmin)*np.random.rand(n) + vmin

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	distinct = daj_klucze(kolor)
	kol_dist = zip(kolory,distinct)
	kol_dict = {}
	for i in range(len(distinct)):
		kol_dict[distinct[i]]=kolory[i]
	zbior = zip(x,y,z,kolor)
	
	sety = []
	for i in range(len(kol_dist)):
		sety.append([z for z in zbior if z[3]==kol_dist[i][1]])
	for i in sety:
		x = [z[0] for z in i]
		y = [z[1] for z in i]
		z = [z[2] for z in i]
		k1 = kol_dict[i[0][3]]
		#for j in kol_dist:
		#	if(z[3]==j[1]):
		#		kol = j[0]
		#		break;
		ax.scatter(x,y,z,c=k1,marker='o')
		#plot(t, s, color=kol,marker='o',linestyle='None')
	## OLD
	#n = 100
	#for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
	#	xs = randrange(n, 23, 32)
	#	ys = randrange(n, 0, 100)
	#	zs = randrange(n, zl, zh)
	#	ax.scatter(xs, ys, zs, c=c, marker=m)
	## OLD
	ax.set_xlabel(labels[0])
	ax.set_ylabel(labels[1])
	ax.set_zlabel(labels[2])

	plt.show()
def daj_klucze(seq): 
	checked = []
	for e in seq:
		if e not in checked:
			checked.append(e)                      
	return checked
def get_sets(zbior,kol_dist):
	zbior

def wykres(t,s,kolor,x_str,y_str):
	
	distinct = daj_klucze(kolor)
	kol_dist = zip(kolory,distinct)
	zbior = zip(t,s,kolor)
	sety = []
	kol_dict = {}
	for i in range(len(distinct)):
		kol_dict[distinct[i]]=kolory[i]
	for i in range(len(kol_dist)):
		sety.append([z for z in zbior if z[2]==kol_dist[i][1]])
	#print sety
	for i in sety:
		t = [z[0] for z in i]
		s = [z[1] for z in i]
		k1 = kol_dict[i[0][2]]
		#for j in kol_dist:
		#	if(z[2]==j[1]):
		#		kol = j[0]
		#		break;
		plot(t, s, color=k1,marker='o',linestyle='None')	
	xlabel(x_str)
	ylabel(y_str)
	title('SWD')
	grid(True)
	show()
def debug2d():
	x = range(5)
	y = range(5)
	cols = [1,5,2,0,0]
	labels = ["x","y"]
	wykres(x,y,cols,labels[0],labels[1])
def debug3d():
	x = range(5)
	y = range(5)
	z = range(5)
	cols = [1,1,1,0,0]
	labels = ["x","y","z"]
	wykres3D(x,y,z,cols,labels)
if(__name__=="__main__"):
	debug3d()