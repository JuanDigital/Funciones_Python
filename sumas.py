# -*- coding: utf-8 -*-
"""
IDE SPYDER
fuciones
"""

def Suma(num1, num2):#parametros o variables
    print ('hola soy una suma ' + str(num1+num2)) #print es una funcion
    #esta imprimiendo los valores aunque no hay for
    
Suma(5,10)#toma el valor segun el orden
Suma(10,20) 
resultado=Suma(20, 30)

print('nueva suma', str(resultado))




def Suma1(num11, num21):#parametros o variables

    return (num11+num21)

    
resultado2=Suma1(20, 30)

print('nueva suma 2=', str(resultado2))

def concatena (num11, num21):#parametros o variables

    return (num11+num21)

    
resultado3=concatena('20---', '···30')

print('nueva suma 3=', str(resultado3))



def resta (x, y):#parametros o variables

    return (x-y)

    
res4=resta(y=8, x=6) # cambio de orden

print('resta =', str(res4))

#parametros por defecto en una funcion

def resta (x=10,y=6):#parametros o variables

    return (x-y)

    
res4=resta() # cambio de orden

print('resta =', str(res4))


#numero de parametros indeterminados

def sumaind (*numeros):#*ahora es una lista
   print(str(numeros))
   result=0
   #recorere como lista 
   for ns in numeros:
       print(ns)
       result+= ns
       
   return result

result=sumaind(1,2,3,4,5,6,7,8,9)
print(str(result))
