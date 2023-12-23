import streamlit as st

from models.td2.exercices import *
from models.td2.solutions import *

st.set_page_config(
    page_title='Introduction á la Cryptographie | TD2',
    page_icon=':student:',
    layout='wide'
)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>', unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("""
            <style>
                .logos {
                    background-color: white;
                    height: 170px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    border-radius: 5px 5px 5px 5px;
                }
                
            </style>
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
    <h1 class="main-title">Introduction à la cryptographie: <br>TD2</h1>
    <br><br>
""",unsafe_allow_html=True)

col_td2_row1 = st.columns(5)
for i in range(5):
    with col_td2_row1[i]:
        st.button(f"Exercice {i+1}",key=f'Exercice{i+1}',use_container_width=True)

col_td2_row2 = st.columns(5)
for i in range(5):
    with col_td2_row2[i]:
        st.button(f"Exercice {i+6}",key=f'Exercice{i+6}',use_container_width=True)



###############################################################################
###                                                                         ###
###                                Exercice 1                               ###
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
###                                Exercice 2                               ###
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
###                                Exercice 3                               ###
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
###                                Exercice 4                               ###
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
###                                Exercice 5                               ###
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
###                                Exercice 6                               ###
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
###                                Exercice 7                               ###
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
###                                Exercice 8                               ###
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
###                                Exercice 9                               ###
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
###                                Exercice 10                              ###
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
###                        Les nombres premier < 100                        ###
###                                                                         ###
###############################################################################
st.markdown("""
---
            
####   La liste des nombres premier de 1 à 1000:
            
<center>
            
|2|3|5|7|11|13|17|19|23|29|31|37|41|43|47|53|59|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|61|67|71|73|79|83|89|97|101|103|107|109|113|127|131|137|139|
|149|151|157|163|167|173|179|181|191|193|197|199|211|223|227|229|233|
|239|241|251|257|263|269|271|277|281|283|293|307|311|313|317|331|337|
|347|349|353|359|367|373|379|383|389|397|401|409|419|421|431|433|439|
|443|449|457|461|463|467|479|487|491|499|503|509|521|523|541|547|557|
|563|569|571|577|587|593|599|601|607|613|617|619|631|641|643|647|653|          
|659|661|673|677|683|691|701|709|719|727|733|739|743|751|757|761|769|          
|773|787|797|809|811|821|823|827|829|839|853|857|859|863|877|881|883|          
|887|907|911|919|929|937|941|947|953|967|971|977|983|991|997|||          
            
</center>
""",unsafe_allow_html=True)

