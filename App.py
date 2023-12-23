import streamlit as st

st.set_page_config(
    page_title='Introduction á la Cryptographie | Home',
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
<center>
            
# Introduction à la cryptographie: Exercices
### Réalisé par Yassine EL GHALLALI       
</center>

<br><br>
""",unsafe_allow_html=True)

home_cols = st.columns(4)
with home_cols[0]:
    exercice_cours = st.link_button("Allez à les exercices du cours", "/Exercice_du_cours",use_container_width=True)

with home_cols[1]:
    td1 = st.link_button("Allez à les exercices du TD1", "/TD1",use_container_width=True)

with home_cols[2]:
    td2 = st.link_button("Allez à les exercices du TD2", "/TD2",use_container_width=True)

with home_cols[3]:
    td3 = st.link_button("Allez à les exercices du TD3", "/TD3",use_container_width=True)