import streamlit as st


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 1 du TD2                    ###
###                                                                         ###
###############################################################################
def exercice1():
    st.markdown("""$\\text{Pour chacun des entiers } a\\text{, déterminer } D(a) \\text{ l'ensemble des diviseurs positifs de }a.$""")
    col_exercice1 = st.columns(5)
    with col_exercice1[0]:
        st.markdown("""$1. \quad a = 99$""")
    with col_exercice1[1]:
        st.markdown("""$2. \quad a = 1069$""")
    with col_exercice1[2]:
        st.markdown("""$3. \quad a = 3742$""")
    with col_exercice1[3]:
        st.markdown("""$4. \quad a = 6725$""")
    with col_exercice1[4]:
        st.markdown("""$5. \quad a = 684$""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 2 du TD2                    ###
###                                                                         ###
###############################################################################
def exercice2():
    st.markdown("""$\\text{Dans chacun des cas suivant, appliquer l'algorithme d'Euclide pour déterminer le PGCD de A et B.}$""")
    col_exercice2 = st.columns(3)
    with col_exercice2[0]:
        st.markdown("""
$1. \quad A = 540, \quad B = 256$
                    
$2. \quad A = 561, \quad B = 187$
""")
    with col_exercice2[1]:
        st.markdown("""
        $3. \quad A = 982, \quad B = 1000$
                    
        $4. \quad A = 998, \quad B = 47$
                    """)
    with col_exercice2[2]:
        st.markdown("""
        $5. \quad A = 5742, \quad B = 1320$
                    
        $6. \quad A = 5454, \quad B = 8572$
                    """)


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 3 du TD2                    ###
###                                                                         ###
###############################################################################
def exercice3():
    st.markdown("""$\\text{Dans chacun des cas, donner l'inverse de } a \\text{ modulo } n \\text{ lorsque cela est possible.}$""")
    col_exercice3 = st.columns(4)
    with col_exercice3[0]:
        st.markdown("""
    $1. \quad a = 13, \quad n = 7$
                    
    $2. \quad a = 4, \quad n = 17$
                    """)
    with col_exercice3[1]:
        st.markdown("""
    $3. \quad a = 2, \quad n = 8$
                    
    $4. \quad a = 54, \quad n = 17$
                    """)
    with col_exercice3[2]:
        st.markdown("""
    $5. \quad a = 100, \quad n = 101$
                    
    $6. \quad a = 396, \quad n = 111$
                    """)
    with col_exercice3[3]:
        st.markdown("""
    $7. \quad a = 48, \quad n = 619$
                    
    $8. \quad a = 987, \quad n = 1069$
                    """)


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 4 du TD2                    ###
###                                                                         ###
###############################################################################
def exercice4():
    st.markdown("""$\\text{Les couples suivants définissent-ils des clefs de cryptage affine par paquet de N}$
                
$1. \quad \\text{Pour } N = 1 : (3; 2), \, (13; 8), \, (9; 0).$

$2. \quad \\text{Pour } N = 2 : (7; 421), \, (25; 11), \, (421; 801)$

$3. \quad \\text{Pour } N = 3 : (2015; 1998), \, (4567; 9002), \, (4073; 88)$           
                """)


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 5 du TD2                    ###
###                                                                         ###
###############################################################################
def exercice5():
    st.markdown("""$\\text{Pour chacune des clefs valides de l'exercice 4, déterminer la fonction de déchiffrement.}$""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 6 du TD2                    ###
###                                                                         ###
###############################################################################
def exercice6():
    st.markdown("""$\\text{Crypter le message CHOCOBO par la méthode affine par paquet de 1 avec (7; 7) comme clef.}$""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 7 du TD2                    ###
###                                                                         ###
###############################################################################
def exercice7():
    st.markdown("""$\\text{Crypter le message VACANCES par la méthode affine par paquet de 2 avec (1999; 999) comme clef.}$""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 8 du TD2                    ###
###                                                                         ###
###############################################################################
def exercice8():
    st.markdown("""$\\text{On a utilisé le cryptosystème affine par paquet de 1 avec (7; 1) comme clef pour obtenir CBLXD. Retrouver le message original.}$""")


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 9 du TD2                    ###
###                                                                         ###
###############################################################################
def exercice9():
    st.markdown("""$\\text{Décrypter ce message sachant que l'on a utilisé un cryptage affine et que le texte claire commence par TOUT.}$              
$\\text{OLZOJFENAFKNZOWNDEFWLXDLAHZXUFJLZEFUFOFDRFZG UFOFDR-}$               
$\\text{FZGKFSODENJDLZPLANPFOSFPYEFFODFKLXONEFAKFSD}$
                """)


###############################################################################
###                                                                         ###
###                    Instuction de l'exercice 10 du TD2                   ###
###                                                                         ###
###############################################################################
def exercice10():
    st.markdown("""$\\text{On a utilisé le cryptosystème affine pour obtenir 50029-125229-237773-}$ 
                $\\text{194389-55281-50645. Retrouver le message original.}$""")