import streamlit as st

from style.style import style

st.set_page_config(
    page_title='Introduction á la Cryptographie | Home',
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
<div class="main-title">
    <h1>Introduction à la cryptographie:  Exercices</h1>
    <h3>Réalisé par Yassine EL GHALLALI</h3>
</div>
<br><br>
""",unsafe_allow_html=True)

home_cols = st.columns(4)
with home_cols[0]:
    exercice_cours = st.link_button("Exercices du cours", "/Exercice_du_cours",use_container_width=True)

with home_cols[1]:
    td1 = st.link_button("Exercices du TD1", "/TD1",use_container_width=True)

with home_cols[2]:
    td2 = st.link_button("Exercices du TD2", "/TD2",use_container_width=True)

with home_cols[3]:
    td3 = st.link_button("Exercices du TD3", "/TD3",use_container_width=True)

st.markdown("""
### Exercices qui j'ai fait:
            
>   ######  TD1: sauf exercice 11
>            
>   ######  TD2: les exercices de 1 à 8
""",unsafe_allow_html=True)