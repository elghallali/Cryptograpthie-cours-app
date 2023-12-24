import streamlit as st

from models.td1.exercices import *
from models.td1.solutions import *
from style.style import style

st.set_page_config(
    page_title='Introduction à la Cryptographie | TD1',
    page_icon=':student:',
    layout='wide'
)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
style()
st.markdown("""
            
            <div class="logos">
              <img src="https://raw.githubusercontent.com/elghallali/my-images/master/Faculty%20Official/fsjest.jpg" title="fsjest" alt="fsjest" width="150" height="150" />
              <img src="https://raw.githubusercontent.com/elghallali/my-images/master/Faculty%20Official/logo.png" title="DSDS" alt="DSDS" width="400" height="150"/>
              <img src="https://raw.githubusercontent.com/elghallali/my-images/master/Faculty%20Official/uae.png" title="UAE" **alt="UAE" width="150" height="150" /> 
            </div>
    """,unsafe_allow_html=True)
st.markdown("""
            <style>
                .main-title {
                    text-align: center
                }
            </style>
    <h1 class="main-title">Introduction à la cryptographie: <br>TD1</h1>
""",unsafe_allow_html=True)
st.header('Congruences:')

col_congrue = st.columns(5)
for i in range(5):
    with col_congrue[i]:
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


st.divider()
st.header('Cryptographie de César')
st.markdown("""
<style>
thead {
    background-color: #000;
    color: white;
}
tbody tr:nth-child(even) {
    background-color: #000;
    color: white;
}
tbody tr:nth-child(odd) {
    background-color: #333;
    color: white;
}
</style>
<br>
<center>
            
|$A$|$B$|$C$|$D$|$E$|$F$|$G$|$H$|$I$|$J$|$K$|$L$|$M$|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|$0$|$1$|$2$|$3$|$4$|$5$|$6$|$7$|$8$|$9$|$10$|$11$|$12$|
|$N$|$O$|$P$|$Q$|$R$|$S$|$T$|$U$|$V$|$W$|$X$|$Y$|$Z$|
|$13$|$14$|$15$|$16$|$17$|$18$|$19$|$20$|$21$|$22$|$23$|$24$|$25$|

</center>                        
<br><br>
""",unsafe_allow_html=True)

col_crypto = st.columns(6)
for i in range(6):
    with col_crypto[i]:
        st.button(f"Exercice {i+6}",key=f'Exercice{i+6}',use_container_width=True)
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


