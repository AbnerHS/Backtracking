m = []
a = []
b = []
n = 6
import time
def criarMatriz():
	for i in range(n):
		l = []
		for j in range(n):
			l.append(0)
		m.append(l)

def mostrar():
	for linha in m:
		for val in linha:
			print ('{:5}'.format(val),end=""),
		print ('')
def preencher():
	a.append(2),b.append(1)
	a.append(1),b.append(2)
	a.append(-1),b.append(2)
	a.append(-2),b.append(1)
	a.append(-2),b.append(-1)
	a.append(-1),b.append(-2)
	a.append(1),b.append(-2)
	a.append(2),b.append(-1)

def mover(mov, x, y):
	if(mov == n*n+1):
		return 1
	for j in range(8):
		xp = x + a[j]
		yp = y + b[j]
		if((xp >= 0 and xp < n) and (yp >= 0 and yp < n)):
			if(m[xp][yp] == 0):
				m[xp][yp] = mov
				if(not mover(mov+1, xp, yp)):
					m[xp][yp] = 0
				else:
					return 1
	return 0
	
criarMatriz()
preencher()
m[0][0] = 1
inicio = time.time()
mover(2,0,0)
fim = time.time()
mostrar()
print("\ntime:",(fim - inicio),end="s\n")
