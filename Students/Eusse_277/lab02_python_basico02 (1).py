# -*- coding: utf-8 -*-
"""Lab02_python_basico02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ZZ3cefNnlcHYQ-eb7wUMLyWJJwdHZ8K

# Laboratorio 02
### Métodos computacionales para físicos  y astrónomos
### Universidad de Antioquia
### Prof: Hernan D. Salinas Jiménez
"""

!git clone https://github.com/hernansalinas/autogrades.git

# Commented out IPython magic to ensure Python compatibility.
# Ejecutar esta celda antes de cada laboratorio
path="autogrades/Laboratorios_Taller/libs"
pathL="autogrades/Laboratorios_Taller/libs/Lab_02"
# %run -i {path}/libUnitTest.py

"""## Problemas

### Factorial
1. Elaborar un algoritmo e implementar en python, el factorial de un número entero `n` ingresado por el usuario.

1. Si el número es un entero deberá retornal el factorial del número.
2. Si el número es negativo deberá aparecer un mensaje tipo string con el mensaje  "el número no puede ser negativo"

3. Si el número es pertenece a los reales(float) el mensaje será, el número no puede ser real.


     ### Ejemplo de Ejecución
    ```python

    >>> factorial(3)
        6

    >>> factorial(1987123)
        =???
```

"""

def factorial(a):
  if a<0:
    print('El numero no puede ser negativo')
  elif type(a)==float:
    print('El numero no puede ser real')
  else:
    for k in range(1,a):
      a*= k
  return a

factorial(5)

factorial(-5)
factorial(5.0)

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test01.py

"""### Teoria de números

Los enunciados 2 y 3 se refieren a la siguiente información:

Diseñar un programa en el que entrado  un numero `a`  retorne una variable booleana True or false si cumple que es:

2. [Números defectivo](https://es.wikipedia.org/wiki/Número_defectivo) : la suma de los divisores propios es menor que el número. 

  La rutina se deberá llamar números_defectivos



3. [Números abundantes](https://es.wikipedia.org/wiki/Número_abundante): la suma de los divisores es mayor que el número.

  La rutina se deberá llamar números_abundantes



4. [Números semiperfectos](https://es.wikipedia.org/wiki/N%C3%BAmero_semiperfecto) la suma de todos o algunos de los divisores propios es igual al número.

  La rutina se debera llamar numeros_semiperfectos

5. [Números perfectos](https://es.wikipedia.org/wiki/N%C3%BAmero_perfecto) la suma de todos sus divisores propios, excepto el mismo numero, es igual al número.

   La rutina se deberá llamar numeros_perfectos


6. [Números primos](https://es.wikipedia.org/wiki/N%C3%BAmero_primo) el número es divisible unicamente por sí mismo y por 1.
   La rutina se deberá llamar numeros_primos


Problema no obligatorio: 

P1. Retornar los 30 primeros números de cada clase

##### **Divisores** **propios**
"""

def obtenerDivisoresPropios(a):
  #Esta parte es para obtener los divisores propios de un número.
  divis=[]
  for k in range(1,a):
    if  a % k == 0:
      divis.append(k)

  return divis


obtenerDivisoresPropios(70)

"""##### 2. Números defectivos """

def numero_defectivo(a):
  divs = obtenerDivisoresPropios(a)

  suma = sum(divs)

  if (suma<a):
    return True
  else:
    return False

numero_defectivo(8)

"""##### Numeros abundantes"""

def numeros_abundantes(a):
    div= obtenerDivisoresPropios(a)
    suma=sum(div) 
    if suma>a:
      return True
    else:
       return False
numeros_abundantes(12)

"""##### 4. Numeros semiperfectos

"""

from itertools import chain, combinations


def obtieneCombinaciones(lista):
    s = list(lista)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

A = [60, 7, 50]
for x in obtieneCombinaciones(A):
    print(sum(x))

def numero_semiperfecto(a):
  divs = obtenerDivisoresPropios(a)
  sumaCombinaciones = []
    
  for x in obtieneCombinaciones(divs):
     sumaCombinaciones.append(sum(x))

  if a in sumaCombinaciones :
    return True
  else:
    return False

numero_semiperfecto(12)

"""##### Numeros perfectos

"""

def numeros_perfectos(a):
  div= obtenerDivisoresPropios(a)
  suma= sum(div)
  if suma== a:
    return True
  else:
    return False
numeros_perfectos(70)

"""##### 6. Números primos """

def numero_primo(a):
  div=[]
  for divis in range(1,a+1):
    if a % divis==0:
      div.append(divis)
  if len(div)==2:
    return True
  else:
    return False
numero_primo(577)

"""# Problema 1

##### Los 30 primeros números defectivos
"""

pri=[]

for num in range(1,100):
  if numero_defectivo(num)==True:
    pri.append(num)
  if len(pri)==30:
    break
#trein=[1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 22, 23, 25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38]    
print(len(pri))
print(pri)

"""##### Los 30 primeros abundantes"""

trein_abun=[]
for num in range(12,138):
    if numeros_abundantes(num)==True:
      trein_abun.append(num)
print(len(trein_abun))
print(trein_abun)

"""##### 30 primeros semiperfetos"""

trein_semi=[]
for num in range (1,200):
  if numero_semiperfecto(num)==True:
    trein_semi.append(num)
  if len(trein_semi)==30:
    break 
print(len(trein_semi)) 
print(trein_semi)

trein_perf=[]
for num in range(1,10000):
  if numeros_perfectos(num)==True:
    trein_perf.append(num)
  if len(trein_perf)==30:
    break

print(len(trein_perf)) 
print(trein_perf)

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test02.py

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test03.py

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test04.py

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test05.py

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test06.py

"""7. Diseñar un programa en el que entrado dos números `a`  y `b` retorne una variable booleana **True** o **false**.

  [Números amigos](https://es.wikipedia.org/wiki/N%C3%BAmeros_amigos) `a` y `b` tales que a es la suma de los divisores propios de `b` y viceversa.
    La rutina se debera llamar numeros_amigos
 



P2. Retornar los 10 primeros pares de numeros perfectos, semiperfectos, amigos

##### Números amigos
"""

def numeros_amigos(a,b):
  dive= obtenerDivisoresPropios(a)
  sumas = sum(dive)
  if sumas == b:
    print(True)
  else:
    print(False)

numeros_amigos(1184,1210)

diez_prim_perfectos = [] #No puedo contar tantos ¿Cómo lo hago para numeros grandes?
for number in range(1,1000):
  if numeros_perfectos(number)== True:
    diez_prim_perfectos.append(number)
print(diez_prim_perfectos)

diez_prim_semip=[]
for number in range(1,300):
  if numero_semiperfecto(number)== True:
    diez_prim_semip.append(number)
  if len(diez_prim_semip)==20:
     break 
print(diez_prim_semip)

def diez_pri_num_ami(n):
  diez_num_ami=[]
  i=1
  while len(diez_num_ami)<n:
    sum_i= sum(obtenerDivisoresPropios(i))
    if sum_i>i:
      sum_sum_i= sum(obtenerDivisoresPropios(sum_i))
      if sum_sum_i == i:
        diez_num_ami.append((i,sum_i))
    i+=1
    if len(diez_num_ami)==n:
      break
  return diez_num_ami   
  

amigos= diez_pri_num_ami(10)
print(amigos)

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test07.py

"""3. Determine si un número `n` entero ingresado por el usuario es un [palíndromo](https://en.wikipedia.org/wiki/Palindromic_number), (Retorne `True` en caso afirmativo y `False` en caso contrario) 

```python


    >>> palindromo(3333333)
        True

    >>> palindromo(2323)
        True
        
    >>> palindromo(1111349111111)
        False
```

##### Palindromos
"""

def palindromo(n):
  digits=[]
  
  while n > 0:
    digit = n % 10
    digits.append(digit)
    n = n // 10
  reverso= digits.copy()
  digits.reverse()
  if reverso==digits:
    return True
  else:
    return False
palindromo(232)

"""8 Construir un programa en el que  entrado un arreglo de números se  ordenen de forma ascendente, Ver algoritmo
[Quicksort](https://es.wikipedia.org/wiki/Quicksort). 


```python


<<< v = [22, 32, 42, 12, 22, 31, 41, 11, 12, 232, 24, 12, 22]
<<< def quicksort(v):

<<<     return v
<<< w = print(quicksort(v))
<<< [11, 12, 12, 12, 22, 22, 22, 24, 31, 32, 41, 42, 232]

```

Sólo para comprobar tu código,  puedes hacer uso del comando sort de python. 
```python
<<< b = [22, 32, 42, 12, 22, 31, 41, 11, 12, 232, 24, 12, 22]

<<< print(b.sort())

<<< [11, 12, 12, 12, 22, 22, 22, 24, 31, 32, 41, 42, 232]
```

##### Quicksorft
"""

def quick_sort(arr):
   
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]# esta parte no la entendi
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
   
    return quick_sort(left) + middle + quick_sort(right)

lista=[3, 6, 1, 8, 4, 2]
lista_ordenada=quick_sort(lista) 
print(lista_ordenada)

b = [22, 32, 42, 12, 22, 31, 41, 11, 12, 232, 24, 12, 22]

lista_ordenada=quick_sort(b)
print(lista_ordenada)
print(b.sort())