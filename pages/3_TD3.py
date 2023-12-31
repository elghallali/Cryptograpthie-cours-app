import streamlit as st

from models.td3.exercices import *
from models.td3.solutions import *
from style.style import style

st.set_page_config(
    page_title='Introduction á la Cryptographie | TD3',
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
    <h1 class="main-title">Introduction à la cryptographie: <br>TD3</h1>
""",unsafe_allow_html=True)
st.header('Matrices:')

col_matrices = st.columns(3)
for i in range(3):
    with col_matrices[i]:
        st.button(f"Exercice {i+1}",key=f'Exercice{i+1}',use_container_width=True)
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
st.divider()
st.header('Hill:')
col_hill = st.columns(5)
for i in range(5):
    with col_hill[i]:
        st.button(f"Exercice {i+4}",key=f'Exercice{i+4}',use_container_width=True)
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


