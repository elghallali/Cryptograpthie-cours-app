import pandas as pd
import streamlit as st

from models.programs.arithmetique import *


###############################################################################
###                                                                         ###
###              Solution de l'exercice 1 du Arithmétiqyue de Z             ###
###                                                                         ###
###############################################################################
def solution_exercice1():
    st.markdown("""
$\\text{Prouvons que les propriétés} \enspace$ $\\text{suivantes sont correctes:} \quad$ 
$\\forall (a,b) \in \\Z^2 $ $\enspace \\text{et} \enspace c \in \\Z^*$

>
> - $\\text{Si} \enspace c \, | \, a \enspace \\text{et} \enspace c \, | \, b \enspace \\text{ alors,} \enspace \exist (u,v) \in \\Z^2, \enspace c \, | \, au + bv. $
>
> $\qquad \\text{On a:} \enspace c \, | \, a \implies a = c \\times k \quad \\text{ avec } k \in \\Z \quad$ $ \\text{et:} \enspace c \, | \, b \implies b = c \\times k' \quad \\text{ avec } k' \in \\Z$
>
> $\qquad \\text{Donc:} \enspace au + bv = c \\times k \\times u + c \\times k' \\times v = c \\times (k \\times u + k' \\times v)$
>
> $\qquad \implies c \, | \, au + bv$
>
> ---
>
> - $\\text{Si} \enspace a \, | \, b \enspace \\text{et} \enspace b \, | \, a \enspace \\text{alors,} \enspace a=b \enspace \\text{ ou } \enspace a = -b.$
>
> $\qquad \\text{On a:} \enspace a \, | \, b \implies b = a \\times k, \enspace (k \in \\Z) \quad$ $\\text{et:} \enspace b \, | \, a \implies a = b \\times k', \enspace (k' \in \\Z)$
>
> $\qquad \\text{Donc:} \enspace b = (b \\times k') \\times k$ $\implies b = b \\times k' \\times k$ 
$\implies b = b \\times (k' \\times k)$
$\implies 1 = k' \\times k$
>
> $\qquad \implies k = \\cfrac{1}{k'} \in \\Z \implies k' = 1 \enspace \\text{ou} \enspace k' = -1$
>
> $\qquad \implies \\text{si} \enspace k' = 1 \enspace \\text{on a} \enspace a = bk' = b \\times 1 =b \enspace \\text{si} \enspace k' = 1 \enspace \\text{on a} \enspace a = bk' = b \\times (-1) =-b$
>
> $\qquad \\text{alors,} \enspace a=b \enspace \\text{ ou } \enspace a = -b.$
>
> ---
>
> - $\\text{Si} \enspace c \, | \, b \enspace \\text{et} \enspace b \, | \, a \enspace \\text{alors,} \enspace c \, | \, a \enspace$ $\\text{ (On dit que la relation | est transitive). }$
>
> $\qquad \\text{On a:} \enspace c \, | \, b \implies b = c \\times k, \enspace (k \in \\Z) \enspace $
$\\text{et: } \enspace b \, | \, a \implies a = b \\times k', \enspace (k' \in \\Z) \implies a = (c \\times k) \\times k' \implies a = c \\times (k \\times k')$
>
> $\qquad \implies c \, | \, a$
>
> ---
>
> - $a \, | \, a \enspace \\text{(On dit que la relation | est réflexive).}$
>
> $\qquad \\text{On a:} \enspace a = a \\times 1 \enspace \\text{et} \enspace 1 \in \\Z \implies a \, | \, a$
>
>
> ---
>
> - $1 \, | \, a \enspace \\text{(1 divise tout le monde).}$
>
> $\qquad \\text{On a:} \enspace a = 1 \\times a \enspace \\text{et} \enspace a \in \\Z \implies 1 \, | \, a$
>
> ---
>
> - $a \, | \, 0 \enspace \\text{(tout le monde divise 0).}$
>
> $\qquad \\text{On a:} \enspace 0 = a \\times 0 \enspace \\text{et} \enspace 0 \in \\Z \implies a \, | \, 0$
>
""")


###############################################################################
###                                                                         ###
###              Solution de l'exercice 2 du Arithmétiqyue de Z             ###
###                                                                         ###
###############################################################################
def solution_exercice2():
    st.markdown("""
$\\text{Donnons la liste des nombres premiers }$ $\\text{plus petits que 30}$
                
>
> $\\text{On dit qu'un entier naturel} \enspace$ $n \geqslant 2 \enspace$ $\\text{est premier s'il n'est divisible} \enspace$ $\\text{que par 1 et lui-même.}$
>
> - $2= 1 \\times 2 \implies 2 \enspace \\text{est premier}$
>
> - $3= 1 \\times 3 \implies 3 \enspace \\text{est premier}$
>
> - $4= 1 \\times 2^2 \implies 4 \enspace \\text{n'est pas premier}$
>
> - $5= 1 \\times 5 \implies 5 \enspace \\text{est premier}$
>
> - $6= 1 \\times 2 \\times 3 \implies 6 \enspace \\text{n'est pas premier}$
>
> - $7= 1 \\times 7  \implies 7 \enspace \\text{est premier}$
>
> - $8= 1 \\times 2^3 \implies 8 \enspace \\text{n'est pas premier}$
>
> - $9= 1 \\times 3^2 \implies 9 \enspace \\text{n'est pas premier}$
>
> - $10= 1 \\times 2 \\times 5 \implies 10 \enspace \\text{n'est pas premier}$
>
> - $11= 1 \\times 11 \implies 11 \enspace \\text{est premier}$
>
> - $12= 1 \\times 2^2 \\times 3 \implies 12 \enspace \\text{n'est pas premier}$
>
> - $13= 1 \\times 13 \implies 13 \enspace \\text{est premier}$
>
> - $14= 1 \\times 2 \\times 7 \implies 14 \enspace \\text{n'est pas premier}$
>
> - $15= 1 \\times 3 \\times 5 \implies 15 \enspace \\text{n'est pas premier}$
>
> - $16= 1 \\times 2^4  \implies 16 \enspace \\text{n'est pas premier}$
>
> - $17= 1 \\times 17 \implies 17 \enspace \\text{est premier}$
>
> - $18= 1 \\times 2 \\times 3^2 \implies 18 \enspace \\text{n'est pas premier}$
>
> - $19= 1 \\times 19  \implies 19 \enspace \\text{est premier}$
>
> - $20= 1 \\times 2^2 \\times 5 \implies 20 \enspace \\text{n'est pas premier}$
>
> - $21= 1 \\times 3 \\times 7 \implies 21 \enspace \\text{n'est pas premier}$
>
> - $22= 1 \\times 2 \\times 11 \implies 22 \enspace \\text{n'est pas premier}$
>
> - $23= 1 \\times 23 \implies 23 \enspace \\text{est premier}$
>
> - $24= 1 \\times 2^3 \\times 3 \implies 24 \enspace \\text{n'est pas premier}$
>
> - $25= 1 \\times 5^2  \implies 25 \enspace \\text{n'est pas premier}$
>
> - $26= 1 \\times 2 \\times 13 \implies 26 \enspace \\text{n'est pas premier}$
>
> - $27= 1 \\times 3^3 \implies 27 \enspace \\text{n'est pas premier}$
>
> - $28= 1 \\times 2^2 \\times 7 \implies 28 \enspace \\text{n'est pas premier}$
>
> - $29= 1 \\times 29  \implies 29 \enspace \\text{est premier}$
>
> $\qquad \\text{La liste des nombres premiers }$
$\\text{plus petits que 30 est:}$ $\{2,3,5,7,11,13,17,19,23,29\}$
>

""")

###############################################################################
###                                                                         ###
###              Solution de l'exercice 3 du Arithmétiqyue de Z             ###
###                                                                         ###
###############################################################################
def solution_exercice3():
    st.markdown("""
$\\text{Écrivons la DFP (Décomposition en }$ $\\text{facteur premier) de 121, 101, 33, 392.}$
""")
    for number in [121, 101, 33, 392]:
        com_list,com_tuple = decomposition(number)
        html_content = ''
        html_content2 = ''
        for i in com_list:
            html_content += '<span>' + str(i[0]) + '</span><br>'
            html_content2 += '<span>' + str(i[1]) + '</span><br>'
        html_content += '<span>1</span><br>'
    
        text = f""
        if number < 0:
            text += '-'
        if len(com_tuple) > 1:
            for i in range(len(com_tuple)-1):
                if com_tuple[i][1] != 1:
                    text += str(com_tuple[i][0])+"^{" + str(com_tuple[i][1]) +"} \\times"
                else:
                    text += str(com_tuple[i][0])+ "\\times"
    
        if com_tuple[-1][1] != 1:
            text += str(com_tuple[-1][0])+"^{" + str(com_tuple[-1][1])+"}"
        else:
            text += str(com_tuple[-1][0])
        st.markdown(f"""
    
> - ##### La décomposion de {number} en facteur premier est: 
>
><div style="display: grid; grid-template-columns: auto auto;">            
><div style="padding-right: 5px; text-align: end;">
>{html_content}
></div>
><div style="border-left: 4px solid #E694FF; padding-left: 5px; text-align: start;">
>{html_content2}
></div>
></div>    
>
> <br>
>
>$Donc:\quad {number} = {text}$
>
><br>
""",unsafe_allow_html=True)


###############################################################################
###                                                                         ###
###              Solution de l'exercice 4 du Arithmétiqyue de Z             ###
###                                                                         ###
###############################################################################
def solution_exercice4():
    st.markdown("""
$\\text{Écrivons la division Euclidienne de 121 par 7, }$ $\\text{de 17 par 2 et de 33 par 44.}$
""")
    for a,b in [(121 , 7), (17 , 2), (33 , 44)]:
       st.markdown(f"""
> - ##### la division Euclidienne de {a} par {b} est:
>
> ${a} = {b} \\times {divEc(a,b)[1]} + {divEc(a,b)[0]} $
>
""", unsafe_allow_html=True) 



###############################################################################
###                                                                         ###
###              Solution de l'exercice 5 du Arithmétiqyue de Z             ###
###                                                                         ###
###############################################################################
def solution_exercice5():
    st.markdown("""
$\\text{Calculons le PGCD de 15 et 35.} $
""")
    st.markdown("""
<style>
      tr th:first-child {
                display: none;
                visibility:hidden;
            }          
</style>
""",unsafe_allow_html=True)
    st.markdown("""- $\\text{Algorithme d'Euclide Étendu:}$""")
    df = pd.DataFrame(algorithme_euclide_etendu(15,35), columns=["a","b","r","q","u","v"])
    algo_cols = st.columns([1,4,1])
    with algo_cols[1]:
        st.table(df)
    st.markdown("""- $\\text{Le PGCD:}$""")
    st.markdown(f"$\qquad \quad Le \, PGCD(15,35) = {abs(pgcd(15,35))}$")



###############################################################################
###                                                                         ###
###              Solution de l'exercice 6 du Arithmétiqyue de Z             ###
###                                                                         ###
###############################################################################
def solution_exercice6():
    st.markdown("""
$\\text{Montrons que 32 et 7 sont premiers entre eux.}$
""")
    st.markdown("""
<style>
      tr th:first-child {
                display: none;
                visibility:hidden;
            }          
</style>
""",unsafe_allow_html=True)
    st.markdown("""- $\\text{Algorithme d'Euclide Étendu:}$""")
    df = pd.DataFrame(algorithme_euclide_etendu(32,7), columns=["a","b","r","q","u","v"])
    algo_cols = st.columns([1,4,1])
    with algo_cols[1]:
        st.table(df)
    st.markdown("""- $\\text{Le PGCD:}$""")
    st.markdown(f"$\qquad Le \, PGCD(32,7) = {abs(pgcd(32,7))}$")
    st.markdown("$\qquad \implies \\text{32 et 7 sont premiers entre eux.}$")



###############################################################################
###                                                                         ###
###              Solution de l'exercice 7 du Arithmétiqyue de Z             ###
###                                                                         ###
###############################################################################
def solution_exercice7():
    st.markdown("""
$\\text{Montrons que si PGCD(a,b) = d alors} \enspace \\cfrac{a}{d} \enspace $ $\\text{et} \enspace \\cfrac{b}{d} \enspace \\text{sont entiers et premiers entre eux.}$

>
> $\\text{On a PGCD} (a,b) = d \implies a = d \\times k \enspace \\text{donc} \enspace \cfrac{a}{d} = k \enspace \\text{et} \enspace b = d \\times k' \enspace \\text{donc} \enspace \cfrac{b}{d} = k' \enspace \\text{avec} \enspace (k,k') \in \\Z^2$
>
> $\\text{et} \enspace \exist (u,v) \in \\Z^2 \enspace \\text{tel que} \enspace au+bv=d \implies dku+dk'v=d$
>
> $\implies ku+k'v=1 \implies \cfrac{a}{d} \\times u + \cfrac{b}{d} \\times v =1$
>
> $\implies \cfrac{a}{d} \, ,  \, \cfrac{b}{d} \enspace \\text{sont entiers et premiers entre eux.}$
>
""")
    


###############################################################################
###                                                                         ###
###              Solution de l'exercice 8 du Arithmétiqyue de Z             ###
###                                                                         ###
###############################################################################
def solution_exercice8():
    st.markdown("""
$\\text{Soient} \enspace a = 111 \enspace \\text{et} \enspace b = 27, \enspace \\text{calculons} \enspace d = PGCD(a,b) \enspace \\text{et donnons la forme de }$ $\\text{tous les couples} \enspace (u,v) \enspace \\text{tel que} \enspace au + bv = d.$
""")
    st.markdown("""
<style>
      tr th:first-child {
                display: none;
                visibility:hidden;
            }          
</style>
""",unsafe_allow_html=True)
    st.markdown("""- $\\text{Algorithme d'Euclide Étendu:}$""")
    df = pd.DataFrame(algorithme_euclide_etendu(111,27), columns=["a","b","r","q","u","v"])
    algo_cols = st.columns([1,4,1])
    with algo_cols[1]:
        st.table(df)
    st.markdown("""- $\\text{Le PGCD:}$""")
    st.markdown(f"$\qquad Le \, PGCD(111,27) = {abs(pgcd(111,27))}$")
    st.markdown("""- $\\text{L'identité de Bézout:}$""")
    st.write(f"$\qquad \quad {111} \\times u {' + '+ str(27) if 27 >= 0 else 27} \\times v ={111} \\times {bezout(111,27)[0] if bezout(111,27)[0] >= 0 else '('+str(bezout(111,27)[0])+')'} {' + '+ str(27) if 27 >= 0 else 27} \\times {bezout(111,27)[1] if bezout(111,27)[1] >= 0 else '('+str(bezout(111,27)[1])+')'} = {str(abs(pgcd(111,27)))}$")
    st.write(f"$\qquad \quad u ={bezout(111,27)[0]}, \quad v ={bezout(111,27)[1]}.$")


###############################################################################
###                                                                         ###
###              Solution de l'exercice 9 du Arithmétiqyue de Z             ###
###                                                                         ###
###############################################################################
def solution_exercice9():
    pass




###############################################################################
###                                                                         ###
###              Solution de l'exercice 10 du Arithmétiqyue de Z            ###
###                                                                         ###
###############################################################################
def solution_exercice10():
    pass



###############################################################################
###                                                                         ###
###              Solution de l'exercice 11 du Arithmétiqyue de Z            ###
###                                                                         ###
###############################################################################
def solution_exercice11():
    pass


###############################################################################
###                                                                         ###
###              Solution de l'exercice 12 du Arithmétiqyue de Z            ###
###                                                                         ###
###############################################################################
def solution_exercice12():
    pass



###############################################################################
###                                                                         ###
###              Solution de l'exercice 13 du Arithmétiqyue de Z            ###
###                                                                         ###
###############################################################################
def solution_exercice13():
    pass


###############################################################################
###                                                                         ###
###              Solution de l'exercice 14 du Arithmétiqyue de Z            ###
###                                                                         ###
###############################################################################
def solution_exercice14():
    pass



###############################################################################
###                                                                         ###
###              Solution de l'exercice 15 du Arithmétiqyue de Z            ###
###                                                                         ###
###############################################################################
def solution_exercice15():
    pass



###############################################################################
###                                                                         ###
###              Solution de l'exercice 16 du Arithmétiqyue de Z            ###
###                                                                         ###
###############################################################################
def solution_exercice16():
    pass


###############################################################################
###                                                                         ###
###              Solution de l'exercice 17 du Arithmétiqyue de Z            ###
###                                                                         ###
###############################################################################
def solution_exercice17():
    pass



###############################################################################
###                                                                         ###
###              Solution de l'exercice 18 du Arithmétiqyue de Z            ###
###                                                                         ###
###############################################################################
def solution_exercice18():
    pass


###############################################################################
###                                                                         ###
###              Solution de l'exercice 19 du Arithmétiqyue de Z            ###
###                                                                         ###
###############################################################################
def solution_exercice19():
    pass




###############################################################################
###                                                                         ###
###              Solution de l'exercice 20 du Arithmétiqyue de Z            ###
###                                                                         ###
###############################################################################
def solution_exercice20():
    pass