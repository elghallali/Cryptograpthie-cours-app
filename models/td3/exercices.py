import streamlit as st

###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 1 du TD3                    ###
###                                                                         ###
###############################################################################
def exercice1():
    st.markdown("""
    $\\text{Soit } A= \\begin{pmatrix} 1 & 2 \\\ 0 & -1 \end{pmatrix},$ 
    $B= \\begin{pmatrix} -1 & 1 \\\ 5 & 0 \end{pmatrix} $ $\enspace \\text{et} \enspace$
    $C=\\begin{pmatrix} 6 & 3 \\\ 3 & 1 \end{pmatrix} $
    $\\text{ des matrices de }$ $ \mathcal{M}_2(\Z/26\Z)$.
  
> $1. \\text{ Calculer } A + B, \quad A \\times C \quad \\text{et} \quad B \\times C$
>                
> $2. \\text{ Comparer } (A + B) \\times C \quad \\text{et} \quad A \\times C + B \\times C$ 
>                 
> $3. \\text{ Comparer le résultat précédent avec } C \\times (A + B)$ 
""")
    

###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 2 du TD3                    ###
###                                                                         ###
###############################################################################
def exercice2():
    st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',unsafe_allow_html=True)
    st.markdown("""$\\text{Calculer le déterminant de chacune des }$ $\\text{matrices suivantes. Identifier les matrices }$ $\\text{de } \mathbf{GL_2}(\\Z/26\\Z).$
""")
    exercice2_td3_cols = st.columns(3)
    with exercice2_td3_cols[0]:
        st.latex(r'''
1. \quad A=
    \begin{pmatrix}
   11 & 3 \\
   2 & -5
   \end{pmatrix}
''')
        st.latex(r'''
2. \quad B=
    \begin{pmatrix}
   3 & 1 \\
   4 & 6
   \end{pmatrix}
''')
        st.latex(r'''
3. \quad C=
    \begin{pmatrix}
   1 & -5 \\
   -1 & 8
   \end{pmatrix}
''')
    with exercice2_td3_cols[1]:
        st.latex(r'''
4. \quad D=
    \begin{pmatrix}
   1 & -5 \\
   1 & 8
   \end{pmatrix}
''')
        st.latex(r'''
5. \quad E=
    \begin{pmatrix}
   1 & 2 \\
   3 & 5
   \end{pmatrix}
''')
        st.latex(r'''
6. \quad F=
    \begin{pmatrix}
   12 & 13 \\
   11 & 10
   \end{pmatrix}
''')
    with exercice2_td3_cols[2]:
        st.latex(r'''
7. \quad G=
    \begin{pmatrix}
   1 & -1 \\
   -1 & 1
   \end{pmatrix}
''')
        st.latex(r'''
8. \quad H=
    \begin{pmatrix}
   4 & 3 \\
   2 & 1
   \end{pmatrix}
''')
        st.latex(r'''
9. \quad I=
    \begin{pmatrix}
   0 & -1 \\
   1 & 0
   \end{pmatrix}
''')


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 3 du TD3                    ###
###                                                                         ###
###############################################################################
def exercice3():
    st.markdown("""
$\\text{Pour chacune des matrices de } \mathbf{GL_2}(\\Z/26\\Z) \enspace$ $\\text{de l'exercice 2, donner la matrice inverse }$ $\\text{(modulairement).}$
""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 4 du TD3                    ###
###                                                                         ###
###############################################################################
def exercice4():
    st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',unsafe_allow_html=True)
    st.markdown("""$\\text{Parmis les matrices suivantes, lesquelles }$ $\\text{sont des clefs du cryptosystème de Hill de }$ $\\text{dimension 2 par paquet de } n?$

""")
    exercice4_td3_cols = st.columns(3)
    with exercice4_td3_cols[0]:
        st.latex(r'''
1. \quad n=1 \text{ et } A=
    \begin{pmatrix}
   1 & 1 \\
   1 & 4
   \end{pmatrix}
''')
        st.latex(r'''
2. \quad n=1 \text{ et } B=
    \begin{pmatrix}
   2 & 4 \\
   6 & 8
   \end{pmatrix}
''')
    with exercice4_td3_cols[1]:
        st.latex(r'''
3. \quad n=2 \text{ et } C=
    \begin{pmatrix}
   1 & 1 \\
   1 & 4
   \end{pmatrix}
''')
        st.latex(r'''
4. \quad n=2 \text{ et } D=
    \begin{pmatrix}
   1 & 100 \\
   100 & 1
   \end{pmatrix}
''')
    with exercice4_td3_cols[2]:
        st.latex(r'''
5. \quad n=3 \text{ et } E=
    \begin{pmatrix}
   1 & 13 \\
   2 & 1
   \end{pmatrix}
''')
        


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 5 du TD3                    ###
###                                                                         ###
###############################################################################
def exercice5():
    
    st.markdown('''
$\\text{ En utilisant un chiffrement de Hill de }$ $\\text{dimension 2 par paquet de 1, chiffrer le }$ $\\text{mot MATH avec }$
    $\\begin{pmatrix} 1 & 1 \\\ 2 & 3 \end{pmatrix}$
    $\\text{ comme clef.}$
''')


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 6 du TD3                    ###
###                                                                         ###
###############################################################################
def exercice6():
    st.markdown('''
$\\text{ En utilisant un chiffrement de Hill de }$ $\\text{dimension 2 par paquet de 1, chiffrer le }$ $\\text{mot KAAMELOT avec }$
    $\\begin{pmatrix} 11 & 1 \\\ 0 & 19 \end{pmatrix}$
    $\\text{ comme clef.}$
''')


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 7 du TD3                    ###
###                                                                         ###
###############################################################################
def exercice7():
    st.markdown('''

$\\text{ On a utilisé un chiffrement de Hill de }$ $\\text{dimension 2 par paquet de 1 avec }$
    $\\begin{pmatrix} 2 & 3 \\\ 5 & 7 \end{pmatrix}$
    $\\text{ comme clef pour obtenir }$ $\\text{QMPPEXZVIKUL. }$ $\\text{Quel était le message clair?}$
''')


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 8 du TD3                    ###
###                                                                         ###
###############################################################################
def exercice8():
    st.markdown('''
$\\text{ On a utilisé un chiffrement de Hill de }$ $\\text{dimension 3 par paquet de 1 avec }$
$\\begin{pmatrix} 8 & 3 & 0 \\\ 1 & 1 & 11 \\\ 0 & 8 & 7 \end{pmatrix}$
$\\text{ comme clef pour obtenir }$ $\\text{YHHKJJUPPLQQGEE. }$ $\\text{Quel était le message clair?}$
''')