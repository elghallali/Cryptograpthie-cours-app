
import math


def divEc(a,b):
    return a%b, a//b 


def algorithme_euclide_etendu(a,b):
    
    table = []
    while(b != 0):
        r,q = divEc(a,b)
        table.append( (a, b, r, q))
        a = b
        b = r

    table2 = table[::-1]
    if table2[0][1] < 0:
        table2[0] = table2[0] + (0,-1)
    else:
        table2[0] = table2[0] + (0,1)

    for i in range(1,len(table2)):
        table2[i] = table2[i] + (table2[i-1][-1], -table2[i][-1] * table2[i-1][-1] + table2[i-1][-2])
    return table2[::-1]


def pgcd(a,b):
    if len(algorithme_euclide_etendu(a,b)) == 1:
        return abs(algorithme_euclide_etendu(a,b)[0][1])
    
    return abs(algorithme_euclide_etendu(a,b)[-2][2])
    

def bezout(a,b):
    u,v = algorithme_euclide_etendu(a,b)[0][-2:]
    return u, v 

def primeNumber(a):
    sqrt_a = math.sqrt(a)
    for i in range(2,int(sqrt_a+1)):
        if a%i ==0:
            return False
    return True

def primeNumbersLessThan(a):
    a = abs(a)
    prime_numbers = []
    for i in range(2,a+1):
        if primeNumber(i) == True:
            prime_numbers.append(i)
    return prime_numbers

def divisors(a):
    a = abs(a)
    divisors = []
    for i in range(1,a+1):
        if a%i == 0:
            divisors.append(i)
    return divisors


def decomposition(n):
    n = abs(n)
    pn = primeNumbersLessThan(n)
    q = n
    com = {}
    com_list = []
    while(q > 1):
        for i in pn:
            while( q%i == 0):
                com_list.append((q,i))
                if i in com.keys():
                    com[i] += 1
                else:
                    com[i] = 1
                q = q//i
    com_tuple = [(k, v) for k, v in com.items()]
    return com_list,com_tuple


def modular_exponentiation(x, e, n):
    c = 1
    for i in range(e):
        c = (x * c) % n
    return c

def modular_multiplication(liste, n):
    liste_to_int = [int(i) for i in liste]
    c = 1
    for i in liste_to_int:
        c = (i * c) % n
    return c