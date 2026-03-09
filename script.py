import numpy as np
print("Versao no numpy:", np.__version__)

# exemplos de utilizacao do numpy
a = np.array([1, 2, 3])
print("Array a:", a)        

# operacoes com arrays simples
b = a * 2
print("Array b (a * 2):", b)    

# array bidimensional
c = np.array([[1, 2], [3, 4]])
print("Array c:\n", c)

# somar um numero a cada elemento do array
d = c + 10  
print("Array d (c + 10):\n", d)

# calculando media dos elementos do array a 
media_a = np.mean(a)
print("Media dos elementos do array a:", media_a)
