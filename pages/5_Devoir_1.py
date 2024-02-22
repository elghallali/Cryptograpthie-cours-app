import streamlit as st
from models.chiffrementRSA.chiffrementRSA import rechercher_les_clefs
from models.programs.arithmetique import algorithme_euclide_etendu, bezout, decomposition, modular_exponentiation, pgcd
import pandas as pd

from models.td3.exercices import *
from models.td3.solutions import *
from style.style import style

st.set_page_config(
    page_title='Introduction á la Cryptographie | Devoir 1',
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
    <h1 class="main-title">Introduction à la cryptographie: <br>Devoir 1</h1>
""",unsafe_allow_html=True)

st.markdown("""

## Problème :

Bob et Alice échangent leurs clés publiques.

clé publique de Bob : $n_B = 943$ et $e_B = 7$

clé publique d'Alice : $n_A = 1457$ et $e_A = 11$

Bob utilise la clé publique d'Alice, puis signe avec sa clé privée pour
envoyer le message : 615-134-425-551

Trouver le message d'origine.

## Solution :

- $\\text{Cryptage du message } M_1 :$

            """)
st.latex(r"""
   \begin{equation*}
		\begin{CD}
			M_1 @> C(pk_a)>> M_2  @> C(sk_b)>> M_3
		\end{CD}
	\end{equation*}
""")

st.markdown("""

- $\\text{Décryptage du message } M_3 :$
            """)
st.latex(r"""
         \begin{equation*}
		\begin{CD}
			M_3 @> D(pk_b)>> M_2  @>D(sk_b)>> M_1
		\end{CD}
	\end{equation*}
         """)

st.markdown("""

- $\\text{Avec}$:
    -  $pk_a = (n_a,e_a): \\text{ la clé publique de Alice, et } sk_a = d_a: \\text{la clé privée de Alice.}$
    - $pk_b = (n_b,e_b): \\text{ la clé publique de Bob, et } sk_b = d_b: \\text{la clé privée de Bob.}$
    
$\\text{On a les clés publiques, il ne reste que de }$ $\\text{chercher les } p, q \\text{ et } sk$


            """)
e_a = 11
e_b = 7
n_a = 1457
n_b = 943
message ='615-134-425-551'
message_list =message.split('-')
message_list_int = [int(i) for i in message_list]


p_b,q_b = decomposition(n_b)[1][0][0], decomposition(n_b)[1][1][0]  
phi_n_b = (p_b-1)*(q_b-1)
d_b = bezout(phi_n_b ,e_b)[1]%phi_n_b 


p_a,q_a = decomposition(n_a)[1][0][0], decomposition(n_a)[1][1][0]  
phi_n_a = (p_a-1)*(q_a-1)
d_a = bezout(phi_n_a ,e_a)[1]%phi_n_a     
    
rechercher_les_clefs(e_b, n_b,'Bob')

rechercher_les_clefs(e_a, n_a,'Alice')


st.markdown(f"""

### Le message original du 615-134-425-551 : Déchiffrement
""")
st.latex(r"""
         \begin{equation*}
		\begin{CD}
			M_3 @> D(pk_b)>> M_2  @>D(sk_a)>> M_1
		\end{CD}
	\end{equation*}
         """)
d_pk_int = [modular_exponentiation(i, e_b, n_b) for i in message_list_int]
for i in message_list_int:
    text = "D_{pk_b} (" + str(i) + ") = " + str(i) + "^{" + str(e_b) + "}\equiv " + str(modular_exponentiation(i, e_b, n_b)) + "[" + str(n_b) +"]" + ('\quad (= '+(str(modular_exponentiation(i, e_b, n_b)+n_b))+'<' + str(n_a)+')' if ((modular_exponentiation(i, e_b, n_b) +n_b)< n_a) else '')
    st.markdown(f"""${text}$
            """)

st.markdown("""

<br>

            """,unsafe_allow_html=True)    
    
for i in d_pk_int:
    text = "D_{sk_a} (" + str(i) + ") = " + str(i) + "^{" + str(d_a) + "}\equiv " + str(modular_exponentiation(i, d_a, n_a)) + "[" + str(n_a) +"]" + ('\quad ('+(str(i+n_b))+'^{' + str(d_a) + '}\equiv'+str(modular_exponentiation(i+n_b, d_a, n_a)) +' [' + str(n_a)+'])' if ((i+n_b)< n_a) else '')
    st.markdown(f"""${text}$
            """)
    

st.markdown("""

<br>

$\\text{Donc le message } 190-933-081-304 \implies 19-09-33-08-13-04, \\text{ alors } 33 \\text{ ne signifie aucun alphabet,}$

$\\text{donc on doit voir } D_{sk_a}(1142) \implies D_{sk_a}(1142) = 1142^{251} \equiv 6[1457]$

$\\text{Alors le message } 190-006-081-304 \implies 19-00-06-08-13-04 $

$\implies T - A - G - I-N-E \implies \\text{TAGINE}$

$\\text{Alors le message origine de la } 615-134-425-551 \\text{ est TAGINE}$
            """,unsafe_allow_html=True)  