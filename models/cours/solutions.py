import streamlit as st

from models.programs.arithmetique import pgcd

def solution_ordina_exercice1():
    code = """
def divEc(a,b):
    return a%b, a//b
"""
    st.code(code, language="python")
    
def solution_ordina_exercice2():
    code = """

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
"""
    st.code(code, language="python")


def solution_ordina_exercice3():
    code = """
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


def bezout(a,b):
    u,v = algorithme_euclide_etendu(a,b)[0][-2:]
    return u, v
"""

    st.code(code, language="python")


