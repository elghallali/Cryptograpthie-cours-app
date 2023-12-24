import streamlit as st


def style():
    st.markdown("""
        <style>
                
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
                border-radius: 5px 5px 5px 5px;
            }
                
            .logos img:nth-child(odd) {
                width:5em;
                height: 90%;
    
            }
    
            .logos img:nth-child(even) {
                width:12em;
                height: 90%;
            }
            
            @media screen and (min-width: 780px) {
                .logos {
                    height: 8em;
                    
                }
                .logos img:nth-child(odd) {
                    width:8em;
                    
        
                }
        
                .logos img:nth-child(even) {
                    width:20em;
                    
                }
            }
        
            @media screen and (min-width: 992px) {
                .logos {
                    
                    height: 10em;
                    
                }
                .logos img:nth-child(odd) {
                    width:10em;
                    
        
                }
        
                .logos img:nth-child(even) {
                    width:25em;
                    
                }
            }
        
            @media screen and (min-width: 1200px) {
                .logos {
                    height: 12em;
                    
                }
                .logos img:nth-child(odd) {
                    width:12em;
                    
        
                }
        
                .logos img:nth-child(even) {
                    width:30em;
                   
                }
            }
            
        </style>
    """,unsafe_allow_html=True)