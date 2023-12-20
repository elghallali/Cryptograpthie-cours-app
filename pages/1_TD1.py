import streamlit as st

st.set_page_config(
    page_title='Introduction à la Cryptographie | TD1',
    page_icon=':smile:',
    layout='wide'
)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>', unsafe_allow_html=True)

st.title('Introduction à la cryptographie: TD1')
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


st.divider()
st.header('Cryptographie de César')
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


###############################################################################
###                                                                         ###
###                             Exercice 9                                  ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice9:
    st.subheader('Exercice 9:')
    Exercice9_tab_1, Exercice9_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice9_tab_1:
        st.write('Instruction')
    with Exercice9_tab_2:
        st.write('Solution')


###############################################################################
###                                                                         ###
###                             Exercice 10                                 ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice10:
    st.subheader('Exercice 10:')
    Exercice10_tab_1, Exercice10_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice10_tab_1:
        st.write('Instruction')
    with Exercice10_tab_2:
        st.write('Solution')


###############################################################################
###                                                                         ###
###                             Exercice 11                                 ###
###                                                                         ###
###############################################################################
if st.session_state.Exercice11:
    st.subheader('Exercice 11:')
    Exercice11_tab_1, Exercice11_tab_2 = st.tabs(['Instruction', 'Solution'])
    with Exercice11_tab_1:
        st.write('Instruction')
    with Exercice11_tab_2:
        st.write('Solution')


