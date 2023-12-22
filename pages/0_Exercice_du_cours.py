import streamlit as st

st.set_page_config(
    page_title='Introduction à la Cryptographie | Exercices du cours',
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
    <h1 class="main-title">Introduction à la cryptographie: <br>Exercices du cours</h>
""",unsafe_allow_html=True)