import streamlit as st
from models.chiffrementRSA.chiffrementRSA import rechercher_les_clefs
from models.programs.arithmetique import *


from style.style import style

st.set_page_config(
    page_title='Introduction á la Cryptographie | Devoir 2',
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
    <h1 class="main-title">Introduction à la cryptographie: <br>Devoir 2</h1>
""",unsafe_allow_html=True)

###############################################################################
###                                                                         ###
###                              Les variables                              ###
###                                                                         ###
###############################################################################
n_A = 1961
e_A = 151
n_B = 1927
e_B = 213
message ='2416-0373-1440-0959-1730-0569-1340-2469-1724-1184'
message_list =message.split('-')
message_list_int = [int(i) for i in message_list]

p_B,q_B = decomposition(n_B)[1][0][0], decomposition(n_B)[1][1][0]  
phi_n_B = (p_B-1)*(q_B-1)
d_b = bezout(phi_n_B ,e_B)[1]%phi_n_B 


p_A,q_A = decomposition(n_A)[1][0][0], decomposition(n_A)[1][1][0]  
phi_n_A = (p_A-1)*(q_A-1)
d_a = bezout(phi_n_A ,e_A)[1]%phi_n_A

st.markdown("""

## Problème :

Alice et Bob s’échangent leurs clés publiques :
$n_A = 1961$, $e_A = 151$
$n_B = 1927$, $e_B = 213$

Bob envoie un message chiffré à Alice en utilisant trois méthodes l’une
à la suite de l’autre.

a) La méthode RSA : il utilise d’abord la clé publique d’Alice ensuite
sa clé privée à lui.

b) La méthode affine par paquets de deux, avec $a=2147$ et $k=1342$

c) La méthode de Hill par paquets de deux, avec la matrice :

A = $\\begin{pmatrix} 1 & 3 \\\ 2 & 11 \end{pmatrix}$

On ne sait pas dans quel ordre il a utilisé les 3 méthodes, on sait
juste qu’il n’a pas commencé par la méthode b) et qu’il n’a pas fini
avec la méthode c).

Le message chiffré reçu est :
2416-0373-1440-0959-1730-0569-1340-2469-1724-1184

Trouver la phrase secrète d’origine.

Il est conseillé d’écrire les codes pythons correspondant aux
différentes méthodes et de les appliquer pour trouver la solution.            
            
## Solution :

### 1. La méthode RSA

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



rechercher_les_clefs(e_B, n_B,'Bob')

rechercher_les_clefs(e_A, n_A,'Alice')