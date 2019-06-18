# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:56:41 2019

@author: USUARIO
"""


#%%       # NUMEROS ABSOLUTOS SEAN DECIMALES O ENTEROS [1] full


x = int and float(input('Escriba un numero cualquiera:'))

if x < 0:
    z=(x*-1)
    print ('Su valor absoluto es:',z)
    
if x > 0:
    print ('Su valor absoluto es:',x)
    
     
#%%           #NUMEROS ENTEROS INVERTIDOS  [2] full

Normal =(input('Escriba un numero entero cualquiera:'))
Imv = []
Neg = []
    

for i in range(len(Normal)):
    if i >= 0:

        Imv.append(Normal[-i-1])

x = (''.join(Imv))
print('Su numero es: ',x)
                
#print ('su numero es:',Imvertido) 
# fue comvertido a lista para manipular elemento por elemento
# el comando [join] se uso para unir la lista por medio del [''] vacio
        


    
#%%           # EXISTENCIA DEL 8 EN UN ENTERO [3] full

x = int(input('escriba un numero entero de tres cifras:'))

d3 = ((((int(x)//10)*10)-int(x))*-1)
d2 = ((int(x)//10)%10)
d1 = (int(x)//100)
L = []
L2 = []
p = 0

for t in range(0,100):
    if x == t:
        print('vuelve a dar el numero pues no es un entero de tres cifras')
for t in range(-99,0):
    if x == t:
        print('vuelve a dar el numero pues no es un entero de tres cifras')          
    
for i in range(0,1000):
   if x == i:
       
       if d1 == 8 or d2 == 8 or d3 == 8:
           L.append(d1)
           L.append(d2)
           L.append(d3)
           for i in L:
               if i == 8:
                   p+= 1
          
if (-999 < x < 0):
    y = x*-1
    d3 = ((((int(y)//10)*10)-int(y))*-1)
    d2 = ((int(y)//10)%10)
    d1 = (int(y)//100)
    if d1 == 8 or d2 == 8 or d3 == 8:
           L.append(d1)
           L.append(d2)
           L.append(d3)
           for i in L:
               if i == 8:
                   p+= 1
        
print('contiene el numero 8:',p,'veces')
 
    
#%%     # NUMEROS PARES ENCONTRADOS SUMADOS [4] full
    
x = input('Escriba un numero entero positivo:')  
z = []
s = 0  

for i in x:
    y = (int(i) % 2) # EL int() para que tome el elemento como un entero
    if y == 0:
        z.append(i)

print ('Los numeros pares son:',z)

for i in list(z):
    
    s = s + int(i)    # uso la variable [s] para definir la suma 
                      # con el primer elemento de la lista
    
print (' y su suma es igual a:',s)  
  
    # Debo buscar como resolver este problema pues la idea seria dar un comando
    # donde sumen los sumeros siguientes indefinidamente 
    

#%%         EXISTENCIA DE NUMEROS 5 EN UN ENTERO [5]


x = input('Ingrese un numero entero cualquiera:')
z = []

for i in x :
    y = int(i) % 5
    if y == 0:
        z.append(i)
        
        
print(z)
print('existen',len(z),'cincos consecutivos')

#%%      NUMERO DE FIBONACCI [6]  full

x = (input(' ingrese un numero cualquiera:'))
a = 1
b = 1
s = 0
r = 0
t = 100
nf = [a,b]

while  r < t:      # notar el ciclo que se da para el ultimo numero de la 
                   # ultima suma y asi sucecivamnte hasta cumplir el [while]
    p = a + b      # se uso para encontrar la serie de fobonacci
    a = b
    b = p
    r += 1
    nf.append(p)
  
#print (nf) 
   
if int(x) < 0:
    
    print ('la suma de los numeros negativos no se encuentran en la \
           ''serie de fibonacci')

    if i != s:
        
     print('la suma no se encuentra la serie de fibonacci' )
 
  
if int(x) > 0:     
   for i in x :          # usaremos este ciclo para sumar los elemntos dentro de 
      s = s + int(i)
                           # la cadena
print('la suma de sus digitos es:',s) 

    
for i in nf:     # sacaremos este [for] para comparar la suma con los numeros 
    if i == s:   # del conjunto [nf]
        print ('¡la suma se encuentra en la serie de fibonacci!')
        break
else:
        print('no existe en la serie de fibonacci')
  
   
     
    
    




#%%           CONTEO DE NUMEROS REPETIDOS EN UN NUMERO DADO [7] full

x = input('Ingrese un numero entero cualquiera:')
z = []
k1,k2,k3,k4,k5,k6,k7,k8,k9 = 0,0,0,0,0,0,0,0,0 # numeros repetidos [contadores]
                                               
for i in x :
    y = int(i) / 1     # los contadores seran diferentes pues se supone que no
    if y == 1:         # hay la misma cantidad de 1 que de 8
        z.append(i)
    y = int(i) / 2
    if y == 1:
        z.append(i)
    y = int(i) / 3
    if y == 1:
        z.append(i)    # relaice esto con el objetivo de poder identificar cada
    y = int(i) / 4     # numero dentro del numero dado
    if y == 1:
        z.append(i)  
    y = int(i) % 5
    if y == 0:
        z.append(i)
    y = int(i) / 6
    if y == 1:
        z.append(i)
    y = int(i) % 7
    if y == 0:
        z.append(i)
    y = int(i) % 8
    if y == 0:
        z.append(i)
    y = int(i) % 9
    if y == 0:
        z.append(i)
                     # debo tener en cuenta que a la hora de realizar un conteo
#print (z)           # necesito precisamente una variable contador que aumente
                     # cada ez que se cumpla la condicion 
for i in z :  
    if int(i) == 1:  
        k1 += 1 
    if int(i) == 2:  
        k2 += 1 
    if int(i) == 3:  
        k3 += 1 
    if int(i) == 4:  
        k4 += 1 
    if int(i) == 5:  
        k5 += 1 
    if int(i) == 6:  
        k6 += 1         
    if int(i) == 7:  
        k7 += 1                  
    if int(i) == 9:   
        k9 += 1       
    if int(i) == 8:  
        k8 += 1     
print('existen',k9,'digitos nueves repetidos en el numero')
print('existen',k8,'digitos ochos repetidos en el numero')
print('existen',k7,'digitos siete repetidos en el numero')
print('existen',k6,'digitos seis repetidos en el numero')
print('existen',k5,'digitos cinco repetidos en el numero')
print('existen',k4,'digitos cuatro repetidos en el numero')
print('existen',k3,'digitos tres repetidos en el numero')
print('existen',k2,'digitos dos repetidos en el numero')
print('existen',k1,'digitos unos repetidos en el numero')



        
    
       
#%%   MULTIPLOS DE 3 Y 4 EN LOS PRIMEROS 100 ENTEROS POSITIVOS [8] full

x=(list(range(1,101)))
cont=1
mult3=[]
mult4=[]

for i in x:
    y = (i % 3)             #Ademas de volver a identificar los multiplos con [%]
    z = (i % 4)             # De nuevo usaremos el contador pues tenemos un 
                            # max en el 15 avo multiplo de 3
    if y==0 and cont<=15:
        mult3.append(i)
        cont+=1
            
    if z == 0 and cont > 15:
        mult4.append (i)
        cont+=1
    
print (mult3) 
print (mult4)

 
#%%       cualquier cadena de texto te la imprime en Mayuscula [10] full


t = str(input('ingrese una cadena de texto:'))

print(' Su texto es:',t.swapcase()) 

# Este metodo nos sirve para comertir las mayusculas en minusculas y viceversa
# En este caso estara de minuscula a mayuscula

#%%  Escribir un programa que reciba una cadena de texto y reporte:[11] full

x = input('escriba una cadena de texto cualquiera:')

vocM =('AEIOU')
CvocM = 0

dig = ('123456789')
Cdig = 0 

esp = (' ')
Cesp = 0

Ltil = ('áéíóúüñÁÉÍÓÚÜÑ')
Ctil = 0

for i in x: 
    if i == ('á'):
        Ctil = Ctil + 1
    if i == ('é'):
        Ctil = Ctil + 1
    if i == ('í'):
        Ctil = Ctil + 1
    if i == ('ó'):
        Ctil = Ctil + 1
    if i == ('ú'):
        Ctil = Ctil + 1
    if i == ('ü'):
        Ctil = Ctil + 1
    if i == ('ñ'):
        Ctil = Ctil + 1
    if i == ('Á'):
        Ctil = Ctil + 1
    if i == ('É'):
        Ctil = Ctil + 1
    if i == ('Í'):
        Ctil = Ctil + 1
    if i == ('Ó'):
        Ctil = Ctil + 1
    if i == ('Ú'):
        Ctil = Ctil + 1
    if i == ('Ü'):
        Ctil = Ctil + 1    
    if i == ('Ñ'):
        Ctil = Ctil + 1    
print ('Existen',Ctil,'letras tildadas en el texto') 
       
for i in x:
    if i == vocM[0]:
        CvocM = CvocM + 1
    if i == vocM[1]:
        CvocM = CvocM + 1
    if i == vocM[2]:
        CvocM = CvocM + 1
    if i == vocM[3]:
        CvocM = CvocM + 1
    if i == vocM[4]:
        CvocM = CvocM + 1        
print ('existen',CvocM,' vocales mayusculas en el texto')   

for i in x:
    if i == (' '):
        Cesp = Cesp +1
print('Existen',Cesp,'espacios en el texto')
        
for i in x:
     if i == ('1'):
       Cdig = Cdig +1
     if i == ('2'):
       Cdig = Cdig +1
     if i == ('3'):
       Cdig = Cdig +1
     if i == ('4'):
       Cdig = Cdig +1
     if i == ('5'):
       Cdig = Cdig +1
     if i == ('6'):
       Cdig = Cdig +1
     if i == ('7'):
       Cdig = Cdig +1
     if i == ('8'):
       Cdig = Cdig +1  
     if i == ('9'):
       Cdig = Cdig +1  
       
print('Existen',Cdig,' digitos en el texto')

#%%      determine cual está primero en el diccionario [12]

p1 = []
p2 = []

for i in range(2):
    p1.append(input('Escriba una palabra'+str(i+1)+':')) 
    p2.append(p1[i].lower()) 
                       
t1 = len(p1[0])
t2 = len(p1[1])  
if (t1 >= t2):
    t = t2
else :
    t = t1 
for i in range(t):
    if(ord(p2[0][i])>ord(p2[1][i])):
        print(p1[1],'se ubica primero en el diccionario')
        break
    elif(ord(p2[0][i])<ord(p2[1][i])):
        print(p1[0],'se ubica primero en el diccionario')
        break
    if (i == t-1) and (t<t2):
        print(p1[0],' se ubica primero en el dicciorario')
    
    

     
#%%     Cadena que imprima como un triangulo  [13] full


x = (input('Escriba un texto:'))

y =x.replace(' ','')
#print (y)

if y[0]:         
   print (y[0].center(100,' ')) 
   if y[1:3]:
      print (y[1:4].center(99,' '))
      if y[4:8]:
         print (y[4:9].center(99,' '))
         if y[9:15]:
            print (y[9:16].center(99,' '))
            if y[16:24]:
               print (y[16:25].center(99,' '))
               if y[25:35]:
                  print (y[25:36].center(99,' '))
                  if y[36:48]:
                     print (y[36:49].center(99,' '))  
                     if y[49:63]:
                        print (y[49:64].center(99,' '))
                        if y[64:80]:
                            print (y[64:81].center(99,' '))
                            if y[81:99]:
                                print (y[81:100].center(99,' '))
                                if y[100:]:
                                    print (y[100:].center(99,' '))
                                    
# se uso en comando .center[para la hubicacion]                                    
# se tendra este ciclo debido a que cada una de las referencias en el texto
# tiene que ver con la posicion del elemento anerior [eso en cuanto al centro]                                    
         
#%%         organizar en forma alfabetica las letras de las cadena [14] full
                                    
x = input('Escriba un texto cualquiera:')

y = list(x.replace(' ',''))   #crearemos la lista pues se debe identificar
                              # elemento por elemento 
y.sort()   # este comando una lista de forma ascendente o decendente segun sea
           # su argumento
           
K = (''.join(y))  # usaremos [join] para volver a la cadena
print('El texto organizado alfabeticamente sera: ',K)    
    
#%%     Leer una lista de números ya ordenados de forma ascendente [16] full         
    

n=int(input("ingresa la lista de manera ordenada ascendente"))
if (n>=0):
    lista=[]#Listas VACIA
    S=[]
    V=[]
    con=0
   #eL ciclo whilE lo usare para pasar mi número a una tipo lista
    while(n>=10):
        resi=n%10
        lista.append(resi)
        n=n//10
        con=con+1
    
    lista.append(n)
        
        #número que sobre del ciclo se guarda en la lista VACIA
k=0
for i in range (0,con+1):
    
    k=lista[i]*10**(con-(con-i))+k
    if (n>0):
        f=(k)
    else:
        f=(-k)
        
        
V=sorted(lista)
print("la lista ingresada ordenada  es:",lista[::-1])
V.reverse()
print("Los números ordenados ascendentes son:")
print(V)

a=int(input("Escriba un número para añadir a la lista:"))
lista.extend([a])
S=sorted(lista)
S.reverse()
print("Luego de agregar el número el orden queda así:")
print(S)    
    


