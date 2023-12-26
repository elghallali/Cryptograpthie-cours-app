import streamlit as st

################################################################
###                                                          ###
###                 Exercices Instructuions                  ###
###                                                          ###
################################################################
from models.cours.arithmetiqueModulaire.exercices import *
from models.cours.arithmetiqueZ.exercices import *
from models.cours.chiffrementAffine.exercices import *
from models.cours.chiffrementPuissance.exercices import *
from models.cours.cryptographieSymetrique.exercices import *
from models.cours.exercices import *

################################################################
###                                                          ###
###                    Exercices Solutions                   ###
###                                                          ###
################################################################
from models.cours.arithmetiqueModulaire.solutions import *
from models.cours.arithmetiqueZ.solutions import *
from models.cours.chiffrementAffine.solutions import *
from models.cours.chiffrementPuissance.solutions import *
from models.cours.cryptographieSymetrique.solutions import *
from models.cours.solutions import *


from style.style import style



st.set_page_config(
    page_title='Introduction à la Cryptographie | Exercices du cours',
    page_icon=':student:',
    layout='wide'
)

style()
st.markdown("""
            
            <div class="logos">
              <img src="https://raw.githubusercontent.com/elghallali/my-images/master/Faculty%20Official/fsjest.jpg" title="fsjest" alt="fsjest" width="150" height="150" />
              <img src="https://raw.githubusercontent.com/elghallali/my-images/master/Faculty%20Official/logo.png" title="DSDS" alt="DSDS" width="400" height="150"/>
              <img src="https://raw.githubusercontent.com/elghallali/my-images/master/Faculty%20Official/uae.png" title="UAE" **alt="UAE" width="150" height="150" /> 
            </div>
    """,unsafe_allow_html=True)
st.markdown("""
    <h1 class="main-title">Introduction à la cryptographie: <br>Exercices du cours</h1>
    <br><br>
""",unsafe_allow_html=True)


###############################################################################
###                                                                         ###
###                             Arithmétique de Z                           ###
###                                                                         ###
###############################################################################

st.header('Arithmétique de $\\Z$:')
for j in range(4):
    col_arithmetique = st.columns(5)
    for i in range(5):
        with col_arithmetique[i]:
            st.button(f"Exercice {i+j*5+1}",key=f'Exercice{j*5+i+1}',use_container_width=True)

###############################################################################
###                                                                         ###
###                             Exercice 1                                  ###
###                                                                         ###
###############################################################################

if st.session_state.Exercice1:
    st.subheader('Exercice 1:')
    Exercice1_tab_1, Exercice1_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice1_tab_1:
        exercice1()
    with Exercice1_tab_2:
        solution_exercice1()

###############################################################################
###                                                                         ###
###                             Exercice 2                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice2:
    st.subheader('Exercice 2:')
    Exercice2_tab_1, Exercice2_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice2_tab_1:
        exercice2()
    with Exercice2_tab_2:
        solution_exercice2()


###############################################################################
###                                                                         ###
###                             Exercice 3                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice3:
    st.subheader('Exercice 3:')
    Exercice3_tab_1, Exercice3_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice3_tab_1:
        exercice3()
    with Exercice3_tab_2:
        solution_exercice3()


###############################################################################
###                                                                         ###
###                             Exercice 4                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice4:
    st.subheader('Exercice 4:')
    Exercice4_tab_1, Exercice4_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice4_tab_1:
       exercice4()
    with Exercice4_tab_2:
        solution_exercice4()


###############################################################################
###                                                                         ###
###                             Exercice 5                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice5:
    st.subheader('Exercice 5:')
    Exercice5_tab_1, Exercice5_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice5_tab_1:
        exercice5()
    with Exercice5_tab_2:
        solution_exercice5()


###############################################################################
###                                                                         ###
###                             Exercice 6                                  ###
###                                                                         ###
###############################################################################

if st.session_state.Exercice6:
    st.subheader('Exercice 6:')
    Exercice6_tab_1, Exercice6_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice6_tab_1:
        exercice6()
    with Exercice6_tab_2:
        solution_exercice6()

###############################################################################
###                                                                         ###
###                             Exercice 7                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice7:
    st.subheader('Exercice 7:')
    Exercice7_tab_1, Exercice7_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice7_tab_1:
        exercice7()
    with Exercice7_tab_2:
        solution_exercice7()


###############################################################################
###                                                                         ###
###                             Exercice 8                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice8:
    st.subheader('Exercice 8:')
    Exercice8_tab_1, Exercice8_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice8_tab_1:
        exercice8()
    with Exercice8_tab_2:
        solution_exercice8()


###############################################################################
###                                                                         ###
###                             Exercice 9                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice9:
    st.subheader('Exercice 9:')
    Exercice9_tab_1, Exercice9_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice9_tab_1:
       exercice9()
    with Exercice9_tab_2:
        solution_exercice9()


###############################################################################
###                                                                         ###
###                             Exercice 10                                 ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice10:
    st.subheader('Exercice 10:')
    Exercice10_tab_1, Exercice10_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice10_tab_1:
        exercice10()
    with Exercice10_tab_2:
        solution_exercice10()

###############################################################################
###                                                                         ###
###                             Exercice 11                                 ###
###                                                                         ###
###############################################################################

if st.session_state.Exercice11:
    st.subheader('Exercice 11:')
    Exercice11_tab_1, Exercice11_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice11_tab_1:
        exercice11()
    with Exercice11_tab_2:
        solution_exercice11()

###############################################################################
###                                                                         ###
###                             Exercice 12                                 ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice12:
    st.subheader('Exercice 12:')
    Exercice12_tab_1, Exercice12_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice12_tab_1:
        exercice12()
    with Exercice12_tab_2:
        solution_exercice12()


###############################################################################
###                                                                         ###
###                             Exercice 13                                 ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice13:
    st.subheader('Exercice 13:')
    Exercice13_tab_1, Exercice13_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice13_tab_1:
        exercice13()
    with Exercice13_tab_2:
        solution_exercice13()


###############################################################################
###                                                                         ###
###                             Exercice 14                                 ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice14:
    st.subheader('Exercice 14:')
    Exercice14_tab_1, Exercice14_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice14_tab_1:
       exercice14()
    with Exercice14_tab_2:
        solution_exercice14()


###############################################################################
###                                                                         ###
###                             Exercice 15                                 ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice15:
    st.subheader('Exercice 15:')
    Exercice15_tab_1, Exercice15_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice15_tab_1:
        exercice15()
    with Exercice15_tab_2:
        solution_exercice15()


###############################################################################
###                                                                         ###
###                             Exercice 16                                 ###
###                                                                         ###
###############################################################################

if st.session_state.Exercice16:
    st.subheader('Exercice 16:')
    Exercice16_tab_1, Exercice16_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice16_tab_1:
        exercice16()
    with Exercice16_tab_2:
        solution_exercice16()

###############################################################################
###                                                                         ###
###                             Exercice 17                                 ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice17:
    st.subheader('Exercice 17:')
    Exercice17_tab_1, Exercice17_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice17_tab_1:
        exercice17()
    with Exercice17_tab_2:
        solution_exercice17()


###############################################################################
###                                                                         ###
###                             Exercice 18                                 ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice18:
    st.subheader('Exercice 18:')
    Exercice18_tab_1, Exercice18_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice18_tab_1:
        exercice18()
    with Exercice18_tab_2:
        solution_exercice18()


###############################################################################
###                                                                         ###
###                             Exercice 19                                 ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice19:
    st.subheader('Exercice 19:')
    Exercice19_tab_1, Exercice19_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice19_tab_1:
       exercice19()
    with Exercice19_tab_2:
        solution_exercice19()


###############################################################################
###                                                                         ###
###                            Exercice 20                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice20:
    st.subheader('Exercice 20:')
    Exercice20_tab_1, Exercice20_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice20_tab_1:
        exercice20()
    with Exercice20_tab_2:
        solution_exercice20()



###############################################################################
###                                                                         ###
###                          Arithmétique modulaire                         ###
###                                                                         ###
###############################################################################

st.divider()
st.header('Arithmétique modulaire:')
col_arithmetique_modulaire = st.columns(5)
for i in range(5):
        with col_arithmetique_modulaire[i]:
            st.button(f"Exercice {i+1}",key=f'Exercice_modulaire{i+1}',use_container_width=True)

###############################################################################
###                                                                         ###
###                             Exercice 1                                  ###
###                                                                         ###
###############################################################################

if st.session_state.Exercice_modulaire1:
    st.subheader('Exercice 1:')
    Exercice1_tab_1, Exercice1_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice1_tab_1:
        modulaire_exercice1()
    with Exercice1_tab_2:
        st.text('solution')

###############################################################################
###                                                                         ###
###                             Exercice 2                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice_modulaire2:
    st.subheader('Exercice 2:')
    Exercice2_tab_1, Exercice2_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice2_tab_1:
        modulaire_exercice2()
    with Exercice2_tab_2:
        st.text('solution')


###############################################################################
###                                                                         ###
###                             Exercice 3                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice_modulaire3:
    st.subheader('Exercice 3:')
    Exercice3_tab_1, Exercice3_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice3_tab_1:
        modulaire_exercice3()
    with Exercice3_tab_2:
        st.text('solution')


###############################################################################
###                                                                         ###
###                             Exercice 4                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice_modulaire4:
    st.subheader('Exercice 4:')
    Exercice4_tab_1, Exercice4_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice4_tab_1:
       modulaire_exercice4()
    with Exercice4_tab_2:
        st.text('solution')


###############################################################################
###                                                                         ###
###                             Exercice 5                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice_modulaire5:
    st.subheader('Exercice 5:')
    Exercice5_tab_1, Exercice5_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice5_tab_1:
       modulaire_exercice5()
    with Exercice5_tab_2:
        st.text('solution')           


###############################################################################
###                                                                         ###
###                         Cryptographie symétrique                        ###
###                                                                         ###
###############################################################################
st.divider()
st.header('Cryptographie symétrique:')
col_cryptographie_symetrique = st.columns(5)
for i in range(2):
        with col_cryptographie_symetrique[i]:
            st.button(f"Exercice {i+1}",key=f'Exercice_cryptographie_symetrique{i+1}',use_container_width=True)

###############################################################################
###                                                                         ###
###                             Exercice 1                                  ###
###                                                                         ###
###############################################################################

if st.session_state.Exercice_cryptographie_symetrique1:
    st.subheader('Exercice 1:')
    Exercice1_tab_1, Exercice1_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice1_tab_1:
        symetrique_exercice1()
    with Exercice1_tab_2:
        st.text('solution')

###############################################################################
###                                                                         ###
###                             Exercice 2                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice_cryptographie_symetrique2:
    st.subheader('Exercice 2:')
    Exercice2_tab_1, Exercice2_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice2_tab_1:
        symetrique_exercice2()
    with Exercice2_tab_2:
        st.text('solution')


###############################################################################
###                                                                         ###
###                            Chiffrement affine                           ###
###                                                                         ###
###############################################################################
st.divider()
st.header('Chiffrement affine:')
col_chiffrement_affine = st.columns(5)
for i in range(1):
        with col_chiffrement_affine[i]:
            st.button(f"Exercice {i+1}",key=f'Exercice_chiffrement_affine{i+1}',use_container_width=True)

###############################################################################
###                                                                         ###
###                             Exercice 1                                  ###
###                                                                         ###
###############################################################################

if st.session_state.Exercice_chiffrement_affine1:
    st.subheader('Exercice 1:')
    Exercice1_tab_1, Exercice1_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice1_tab_1:
        affine_exercice1()
    with Exercice1_tab_2:
        st.text('solution')



###############################################################################
###                                                                         ###
###                           Chiffrement puissance                         ###
###                                                                         ###
###############################################################################
st.divider()
st.header('Chiffrement puissance:')
col_chiffrement_puissance = st.columns(5)
for i in range(1):
        with col_chiffrement_puissance[i]:
            st.button(f"Exercice {i+1}",key=f'Exercice_chiffrement_puissance{i+1}',use_container_width=True)

###############################################################################
###                                                                         ###
###                             Exercice 1                                  ###
###                                                                         ###
###############################################################################

if st.session_state.Exercice_chiffrement_puissance1:
    st.subheader('Exercice 1:')
    Exercice1_tab_1, Exercice1_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice1_tab_1:
        puissance_exercice1()
    with Exercice1_tab_2:
        st.text('solution')



###############################################################################
###                                                                         ###
###                          Exercices d'ordinateur                         ###
###                                                                         ###
###############################################################################
st.divider()
st.header("Exercices d'ordinateur:")
col_exercice_ordinateur = st.columns(5)
for i in range(3):
        with col_exercice_ordinateur[i]:
            st.button(f"Exercice {i+1}",key=f'Exercice_ordinateur{i+1}',use_container_width=True)


###############################################################################
###                                                                         ###
###                             Exercice 1                                  ###
###                                                                         ###
###############################################################################

if st.session_state.Exercice_ordinateur1:
    st.subheader('Exercice 1:')
    Exercice1_tab_1, Exercice1_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice1_tab_1:
        ordina_exercice1()
    with Exercice1_tab_2:
        st.text('solution')

###############################################################################
###                                                                         ###
###                             Exercice 2                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice_ordinateur2:
    st.subheader('Exercice 2:')
    Exercice2_tab_1, Exercice2_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice2_tab_1:
        ordina_exercice2()
    with Exercice2_tab_2:
        st.text('solution')


###############################################################################
###                                                                         ###
###                             Exercice 3                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice_ordinateur3:
    st.subheader('Exercice 3:')
    Exercice3_tab_1, Exercice3_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice3_tab_1:
        ordina_exercice3()
    with Exercice3_tab_2:
        st.text('solution')

