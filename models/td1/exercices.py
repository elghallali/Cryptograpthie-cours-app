import streamlit as st


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 1 du TD1                    ###
###                                                                         ###
###############################################################################
def exercice1():
    st.markdown("""$\\text{Parmi les propositions, lesquelles sont vraies.}$""")
    exercice1_col_1,exercice1_col_2,exercice1_col_3,exercice1_col_4 = st.columns(4)
    with exercice1_col_1:
        st.markdown("""
1. $15 \equiv 7[8]$   
1. $99 \equiv -1[2]$
        """)
    with exercice1_col_2:
        st.markdown("""
3. $654 \equiv 0[3]$   
3. $3 \equiv 3[3]$
        """)
    with exercice1_col_3:
        st.markdown("""
5. $873 \equiv 555[5]$   
5. $8704 \equiv 791[13]$
        """)
    with exercice1_col_4:
        st.markdown("""
7. $-8 \equiv 1[9]$   
7. $-984 \equiv 17[19]$
        """)


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 2 du TD1                    ###
###                                                                         ###
###############################################################################
def exercice2():
    st.markdown("""$ \\text{Dans chacun des cas, déterminer } x \\text{ modulo } n \\text{ (donner un représentant dans } \Z/n\Z)$""")
    exercice2_col_1,exercice2_col_2,exercice2_col_3,exercice2_col_4 = st.columns(4)
    with exercice2_col_1:
        st.markdown("""
1. $x = 555,\quad n = 12$ 
        """)
    with exercice2_col_2:
        st.markdown("""
2. $x = 983,\quad n = 45$
        """)
    with exercice2_col_3:
        st.markdown("""
3. $x = 3078,\quad n = 487$
        """)
    with exercice2_col_4:
        st.markdown("""
4. $x = 573,\quad n = 159$
        """)


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 3 du TD1                    ###
###                                                                         ###
###############################################################################
def exercice3():
    st.markdown("""$ \\text{Simplifier les expressions suivantes: }$""")
    exercice3_col_1,exercice3_col_2,exercice3_col_3 = st.columns([3,2,2])
    with exercice3_col_1:
        st.markdown("""
1. $123^{122} \enspace modulo \enspace 124$   
1. $2014 \\times 2015\\times2016 \enspace modulo \enspace 2017$
        """)
    with exercice3_col_2:
        st.markdown("""
3. $2792^{217} \enspace modulo \enspace 5$   
3. $133^{39} \enspace modulo \enspace 10$
        """)
    with exercice3_col_3:
        st.markdown("""
5. $99^{100} \enspace modulo \enspace 42$   
5. $2^{1147} \enspace modulo \enspace 17$
        """)
    

###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 4 du TD1                    ###
###                                                                         ###
###############################################################################
def exercice4():
    st.markdown("""$ \\text{Dessiner les tables d'addition et de }$ $\\text{multiplication de }\\Z/7\\Z$.""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 5 du TD1                    ###
###                                                                         ###
###############################################################################
def exercice5():
    st.markdown("""$ \\text{Dessiner les tables d'addition et de }$ $\\text{multiplication de }\\Z/8\\Z.$""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 6 du TD1                    ###
###                                                                         ###
###############################################################################
def exercice6():
    st.markdown("""$ \\text{Crypter le mot MATHEMATIQUES par }$ $\\text{la méthode de César par paquet de 1 avec 19 }$ $\\text{comme clef.}$""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 7 du TD1                    ###
###                                                                         ###
###############################################################################
def exercice7():
    st.markdown("""$ \\text{Crypter le mot ZEBRE par la méthode de }$ $\\text{César par paquet de 1 avec 25 comme clef.}$""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 8 du TD1                    ###
###                                                                         ###
###############################################################################
def exercice8():
    st.markdown("""$ \\text{Crypter le message VIVELACRYPTO }$ $\\text{par la méthode de César par paquet de 3 }$ $\\text{avec 190091 comme clef.}$""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 9 du TD1                    ###
###                                                                         ###
###############################################################################
def exercice9():
    st.markdown("""$ \\text{On a utilisé la méthode de César par }$ $\\text{paquet de 1 avec 25 comme clef pour obtenir }$ $\\text{BDRSBGZTCBZAQTKD. }$ $\\text{Quel
était le message original ?}$""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 10 du TD1                   ###
###                                                                         ###
###############################################################################
def exercice10():
    st.markdown("""$ \\text{On a utilisé la méthode de César par paquet }$ $\\text{de 3 avec 250025 comme clef pour obtenir }$ $\\text{208907-107501-39318-
48312-77499. }$ $\\text{Quel était le message original ?}$""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 11 du TD1                   ###
###                                                                         ###
###############################################################################
def exercice11():
    st.markdown("""$ \\text{Ce message a été codé par la méthode de César : }$ $2138-523-1651-1650-712-1434-1834-2338-412-721-212-708. $ $\\text{Quel
était le message original ?}$""")