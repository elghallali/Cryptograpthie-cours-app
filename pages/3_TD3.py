import streamlit as st

st.set_page_config(
    page_title='Introduction á la Cryptographie | TD3',
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
    <h1 class="main-title">Introduction à la cryptographie: <br>TD3</h>
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
        st.write('Instruction')
    with Exercice1_tab_2:
        st.write('Solution')

###############################################################################
###                                                                         ###
###                             Exercice 2                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice2:
    st.subheader('Exercice 2:')
    Exercice2_tab_1, Exercice2_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice2_tab_1:
        st.write('Instruction')
    with Exercice2_tab_2:
        st.write('Solution')


###############################################################################
###                                                                         ###
###                             Exercice 3                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice3:
    st.subheader('Exercice 3:')
    Exercice3_tab_1, Exercice3_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice3_tab_1:
        st.write('Instruction')
    with Exercice3_tab_2:
        st.write('Solution')
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
        st.write('Instruction')
    with Exercice4_tab_2:
        st.write('Solution')


###############################################################################
###                                                                         ###
###                             Exercice 5                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice5:
    st.subheader('Exercice 5:')
    Exercice5_tab_1, Exercice5_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice5_tab_1:
        st.write('Instruction')
    with Exercice5_tab_2:
        st.write('Solution')




###############################################################################
###                                                                         ###
###                             Exercice 6                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice6:
    st.subheader('Exercice 6:')
    Exercice6_tab_1, Exercice6_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice6_tab_1:
        st.write('Instruction')
    with Exercice6_tab_2:
        st.write('Solution')



###############################################################################
###                                                                         ###
###                             Exercice 7                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice7:
    st.subheader('Exercice 7:')
    Exercice7_tab_1, Exercice7_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice7_tab_1:
        st.write('Instruction')
    with Exercice7_tab_2:
        st.write('Solution')


###############################################################################
###                                                                         ###
###                             Exercice 8                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice8:
    st.subheader('Exercice 8:')
    Exercice8_tab_1, Exercice8_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice8_tab_1:
        st.write('Instruction')
    with Exercice8_tab_2:
        st.write('Solution')


