import streamlit as st


def style():
    st.markdown("""
        <style> 
            @import url('https://fonts.googleapis.com/css2?family=PT+Serif&display=swap');

            html, body, [class*="css"] {
                font-family: 'PT Serif', serif; 
                font-size: 20px;
                font-weight: 500;
                color: #091747;
            }
            
            h1, h2, h3, h4, h5, h6, button p, a p {
                font-family: 'PT Serif', serif;
            }           
            div.block-container {padding-top: 0.1rem;}
                
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}    

            .main-title {
                    text-align: center
            }
                
            .logos {
                background-color: #fff;
                height: 6em;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
                border-radius: 5px 5px 5px 5px;
                margin-bottom: 30px;
            }
                
            .logos img:nth-child(odd) {
                width:5em;
                height: 90%;
    
            }
    
            .logos img:nth-child(even) {
                width:8em;
                height: 90%;
            }
            
            @media screen and (min-width: 780px) {
                .logos {
                    height: 8em;
                    
                }
                .logos img:nth-child(odd) {
                    width:7em;
                    
        
                }
        
                .logos img:nth-child(even) {
                    width:15em;
                    
                }
            }
        
            @media screen and (min-width: 992px) {
                .logos {
                    
                    height: 10em;
                    
                }
                .logos img:nth-child(odd) {
                    width:9em;
                    
        
                }
        
                .logos img:nth-child(even) {
                    width:22em;
                    
                }
            }
        
            @media screen and (min-width: 1200px) {
                .logos {
                    height: 12em;
                    
                    
                }
                .logos img:nth-child(odd) {
                    width:9em;
                    height: 80%;
                }
        
                .logos img:nth-child(even) {
                    width:20em;
                    height: 70%;
                   
                }
            }
            
        </style>
    """,unsafe_allow_html=True)