import streamlit as st
import pandas as pd
from models.chiffrementHill.chiffrementHill import hill, hill_matrice_inv
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
base = 2526
a_affine = 2147
a_affine_inv = bezout(base,a_affine)[1]%base
k_affine = 1342

hill_m =[[1,3],[2,11]]
hill_m_det = hill_m[0][0]*hill_m[1][1] - hill_m[0][1] * hill_m[1][0]
hill_m_det_inv = bezout(base,hill_m_det)[1]%base
hill_m_inv = [[hill_m_det_inv * hill_m[1][1],hill_m_det_inv * (-hill_m[0][1])],[hill_m_det_inv * (-hill_m[1][0]),hill_m_det_inv * hill_m[0][0]]]
hill_m_inv_modulo = [[(j%base) for j in i] for i in hill_m_inv]
dim = 2
message ='2416-0373-1440-0959-1730-0569-1340-2469-1724-1184'
message_list =message.split('-')
message_list_int = [int(i) for i in message_list]

p_B,q_B = decomposition(n_B)[1][0][0], decomposition(n_B)[1][1][0]  
phi_n_B = (p_B-1)*(q_B-1)
d_b = bezout(phi_n_B ,e_B)[1]%phi_n_B 


p_A,q_A = decomposition(n_A)[1][0][0], decomposition(n_A)[1][1][0]  
phi_n_A = (p_A-1)*(q_A-1)
d_a = bezout(phi_n_A ,e_A)[1]%phi_n_A

###############################################################################
###                                                                         ###
###                            Affine décryptage                            ###
###                                                                         ###
###############################################################################

def affine(x,a,k):
    return a*(x-k)%2526

## Méthode 1
decryptage_affine = [affine(x,a_affine_inv,k_affine) for x in message_list_int]
list_affine_hill = [decryptage_affine[i*2:i*2+2] for i in range(len(decryptage_affine)//dim)]
decryptage_affine_hill_rsa = [item for sublist in [hill(x,hill_m_inv_modulo,paquet=2,dim=dim) for x in list_affine_hill] for item in sublist]

## Méthode 2
list_affine_rsa_b =[modular_exponentiation(i, e_B, n_B) for i in decryptage_affine]
list_affine_rsa_b_rsa_a =[modular_exponentiation(i, d_a, n_A) for i in list_affine_rsa_b]
list_affine_rsa_b_rsa_a_hill = [list_affine_rsa_b_rsa_a[i*2:i*2+2] for i in range(len(list_affine_rsa_b_rsa_a)//dim)]

## Méthode 3
list_rsa_b = [modular_exponentiation(i, e_B, n_B) for i in message_list_int]
list_rsa_b_rsa_a = [modular_exponentiation(i, d_a, n_A) for i in list_rsa_b]
list_rsa_b_rsa_a_sffine = [affine(x,a_affine_inv,k_affine) for x in list_rsa_b_rsa_a]

###############################################################################
###                                                                         ###
###                              The body page                              ###
###                                                                         ###
###############################################################################

st.markdown("""

## Problème :

Alice et Bob s'échangent leurs clés publiques :
$n_A = 1961$, $e_A = 151$
$n_B = 1927$, $e_B = 213$

Bob envoie un message chiffré à Alice en utilisant trois méthodes l'une
à la suite de l'autre.

a) La méthode RSA : il utilise d'abord la clé publique d'Alice ensuite
sa clé privée à lui.

b) La méthode affine par paquets de deux, avec $a=2147$ et $k=1342$

c) La méthode de Hill par paquets de deux, avec la matrice :

A = $\\begin{pmatrix} 1 & 3 \\\ 2 & 11 \end{pmatrix}$

On ne sait pas dans quel ordre il a utilisé les 3 méthodes, on sait
juste qu'il n'a pas commencé par la méthode b) et qu'il n'a pas fini
avec la méthode c).

Le message chiffré reçu est :
2416-0373-1440-0959-1730-0569-1340-2469-1724-1184

Trouver la phrase secrète d'origine.

Il est conseillé d'écrire les codes pythons correspondant aux
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

st.divider()

st.markdown("""
            
### 2. La méthode Affine: (paquet = 2)
            
- $\\text{Cryptage du message } M_1 :$

            """)
st.latex(r"""
   \begin{equation*}
		\begin{CD}
			M_1 @> Cr(M_1)>> M_2  
		\end{CD}
	\end{equation*}
""")

st.markdown("""
$\\text{avec } Cr(M_1) \equiv a \\times M1 + k[2526] \quad \\text{tel que } a \in (\\Z/2526\\Z)^{\\times}, \, k \in \\Z$

- $\\text{Décryptage du message } M_2 :$
            """)
st.latex(r"""
         \begin{equation*}
		\begin{CD}
			M_2  @>D(M_2)>> M_1
		\end{CD}
	\end{equation*}
         """)

st.markdown("""

$\\text{avec } D(M_2) \equiv a^{-1} \\times (M1 - k)[2526] \quad \\text{tel que } a^{-1} \\text{ l'inverse de } a \\text{ modulo } 2526, \, k \in \\Z$


#### On cherchons l'inverse de $a = 2147$ modulo $2526$

            """)
st.markdown("""
<style>
      tr th:first-child {
                display: none;
                visibility:hidden;
            }          
</style>

- ##### $\\text{Algorithme d'Euclide Étendu:}$
""",unsafe_allow_html=True)
df_affine = pd.DataFrame(algorithme_euclide_etendu(2526,a_affine), columns=["a","b","r","q","u","v"])
algo_cols = st.columns([1,4,1])
with algo_cols[1]:
    st.table(df_affine)

st.markdown("""

$\\text{D'après algorithme d'Euclide Étendu on a :}$

$\\text{le pgcd(}2526,2147\\text{)=} 1 \implies 2526 \\text{ et } 2147 \\text{ sont premiers entre eux.}$

$\\text{donc } \exist \, a^{-1} \in \\Z \quad \\text{tel que } \, a.a^{-1} \equiv 1[2526]$

<br>

- ##### $\\text{L'identité de Bézout:}$
            """, unsafe_allow_html=True)
inverse_text = "\\text{ est l'inverse de }"
modulo_text = "\\text{ modulo }"
a_1 = 'a^{-1}'
st.markdown(f"""
            
${base} \\times u {' + '+ str(a_affine) if a_affine >= 0 else a_affine} \\times v ={base} \\times {bezout(base,a_affine)[0] if bezout(base,a_affine)[0] >= 0 else '('+str(bezout(base,a_affine)[0])+')'} {' + '+ str(a_affine) if a_affine >= 0 else a_affine} \\times {bezout(base,a_affine)[1] if bezout(base,a_affine)[1] >= 0 else '('+str(bezout(base,a_affine)[1])+')'} = {str(abs(pgcd(base,a_affine)))}$

$\implies {base} \\times {bezout(base,a_affine)[0] if bezout(base,a_affine)[0] >= 0 else '('+str(bezout(base,a_affine)[0])+')'} {' + '+ str(a_affine) if a_affine >= 0 else a_affine} \\times {bezout(base,a_affine)[1] if bezout(base,a_affine)[1] >= 0 else '('+str(bezout(base,a_affine)[1])+')'} \equiv {str(abs(pgcd(base,a_affine)))} [{str(base)}]$            
            
$\implies {''+ str(a_affine) if a_affine >= 0 else a_affine} \\times {bezout(base,a_affine)[1] if bezout(base,a_affine)[1] >= 0 else '('+str(bezout(base,a_affine)[1])+')'} \equiv {str(abs(pgcd(base,a_affine)))} [{str(base)}]$ 

$\implies {bezout(base,a_affine)[1] if bezout(base,a_affine)[1] >= 0 else '('+str(bezout(base,a_affine)[1])+')'} {inverse_text} a={a_affine} {modulo_text} {base}$            

$\implies {a_1} = {str(bezout(base,a_affine)[1]%base)}$            
           
            """)
st.divider()

st.markdown(f"""

    ### 3. La méthode Hill: (paquet = 2)

                """)    
hill_matrice_inv(hill_m,2,2)
st.divider()
st.markdown("""

### 4. Le message original

#### 4.1.  (A-C-B)
- $\\text{Cryptage}$
                """)
st.latex(r"""
         \begin{equation*}
		\begin{CD}
			\text{Message original}  @>RSA>> M_1 @>Hill>> M_2 @>affine>> \text{Message crypté}
		\end{CD}
	\end{equation*}
         """)

st.markdown("""
- $\\text{Décryptage}$
                """)   

st.latex(r"""
         \begin{equation*}
		\begin{CD}
              \text{Message crypté} @>affine>> M_2 @>Hill>> M_1 @>RSA>> \text{Message original}
		\end{CD}
	\end{equation*}
         """)
#######################################################################
#####                                                             #####
#####                     1. Affine decryptage                    #####
#####                                                             #####
#######################################################################
d_affine = "D_{affine}"
st.markdown("""
##### 4.1.1 Affine:
                """) 
for i in message_list_int:
    st.markdown(f"""
   
$\qquad {d_affine}({i}) = {a_affine_inv} \\times ({i} - {k_affine}) = {a_affine_inv} \\times {(i - k_affine) if (i - k_affine) >= 0 else '(' + str(i - k_affine)+')'} \equiv {(a_affine_inv* (i - k_affine))%base}[{base}]$                
                """)
    
#######################################################################
#####                                                             #####
#####                   1. Hill decryptage                        #####
#####                                                             #####
#######################################################################
st.markdown("""
            
<br>            
    
##### 4.1.2 Hill:
                """,unsafe_allow_html=True)
d_hill = "D_{Hill}"
a_inv_text = "A^{-1}"
begin_matrice = "\\begin{pmatrix}"
end_matrice = "\end{pmatrix}"
text =''
for i in range(len(list_affine_hill)):
    text += f'Y_{i+1}= {begin_matrice} {list_affine_hill[i][0]} \\\ {list_affine_hill[i][1]} {end_matrice}, \,'
text += f'{a_inv_text}= {begin_matrice} {hill_m_inv_modulo[0][0]} & {hill_m_inv_modulo[0][1]} \\\ {hill_m_inv_modulo[1][0]} & {hill_m_inv_modulo[1][1]} {end_matrice}'
st.markdown(f"""

$\qquad {text}$                
                """)
for i in range(len(list_affine_hill)):
    st.markdown(f"""

$\qquad {d_hill}(Y_{i+1})= {a_inv_text} \cdot Y_{i+1} = {begin_matrice} {hill_m_inv_modulo[0][0]} & {hill_m_inv_modulo[0][1]} \\\ {hill_m_inv_modulo[1][0]} & {hill_m_inv_modulo[1][1]} {end_matrice} \cdot {begin_matrice} {list_affine_hill[i][0]} \\\ {list_affine_hill[i][1]} {end_matrice}$
$= {begin_matrice} {hill_m_inv_modulo[0][0]}\\times {list_affine_hill[i][0]} + {hill_m_inv_modulo[0][1]}\\times {list_affine_hill[i][1]} \\\ {hill_m_inv_modulo[1][0]}\\times {list_affine_hill[i][0]} + {hill_m_inv_modulo[1][1]}\\times {list_affine_hill[i][1]} {end_matrice}$
$=  {begin_matrice}  {(hill_m_inv_modulo[0][0]*list_affine_hill[i][0] + hill_m_inv_modulo[0][1]*list_affine_hill[i][1])%base} \\\ {(hill_m_inv_modulo[1][0]*list_affine_hill[i][0] + hill_m_inv_modulo[1][1]*list_affine_hill[i][1])%base}  {end_matrice}[{base}]$                
                """)
#######################################################################
#####                                                             #####
#####                      1. RSA decryptage                      #####
#####                                                             #####
#######################################################################
st.markdown("""

<br>            
            
##### 4.1.3 RSA:

###### $\qquad \\text{Decryptage RSA}:$
                """, unsafe_allow_html=True)

st.latex(r"""
         \begin{equation*}
		\begin{CD}
			M_1 @> D(pk_b)>> \dot M_1  @>D(sk_a)>> \text{Message orginal}
		\end{CD}
	\end{equation*}
         """)
st.markdown("""

-  $D_{pk_b}(M_1)$ :            
            """)
for i in decryptage_affine_hill_rsa:
    text = "D_{pk_b} (" + str(i) + ") = " + str(i) + "^{" + str(e_B) + "}\equiv " + str(modular_exponentiation(i, e_B, n_B)) + "[" + str(n_B) +"]" + ('\quad (= '+(str(modular_exponentiation(i, e_B, n_B)+n_B))+'<' + str(n_B)+')' if ((modular_exponentiation(i, e_B, n_B) +n_B)< n_B) else '')
    st.markdown(f"""$\qquad {text}$
            """)
st.markdown("""

<br>

            """,unsafe_allow_html=True)
st.markdown("""

-  $D_{sk_a}(\dot M_1)$ :            
            """)
d_pk_int = [modular_exponentiation(i, e_B, n_B) for i in decryptage_affine_hill_rsa]
for i in d_pk_int:
    text = "D_{sk_a} (" + str(i) + ") = " + str(i) + "^{" + str(d_a) + "}\equiv " + str(modular_exponentiation(i, d_a, n_A)) + "[" + str(n_A) +"]" + ('\quad ('+(str(i+n_B))+'^{' + str(d_a) + '}\equiv'+str(modular_exponentiation(i+n_B, d_a, n_A)) +' [' + str(n_A)+'])' if ((i+n_B)< n_A) else '')
    st.markdown(f"""$\qquad {text}$
            """)
st.divider()
st.markdown("""

<br>            
            
#### 4.2.  (C-A-B)
- $\\text{Cryptage}$
                """, unsafe_allow_html=True)
st.latex(r"""
         \begin{equation*}
		\begin{CD}
			\text{Message original}  @>Hill>> M_1 @>RSA>> M_2 @>affine>> \text{Message crypté}
		\end{CD}
	\end{equation*}
         """)

st.markdown("""
- $\\text{Décryptage}$
                """)   

st.latex(r"""
         \begin{equation*}
		\begin{CD}
              \text{Message crypté} @>affine>> M_2 @>RSA>> M_1 @>Hill>> \text{Message original}
		\end{CD}
	\end{equation*}
         """)
#######################################################################
#####                                                             #####
#####                     2. Affine decryptage                    #####
#####                                                             #####
#######################################################################
st.markdown("""
##### 4.2.1 Affine:
                """) 
for i in message_list_int:
    st.markdown(f"""
   
$\qquad {d_affine}({i}) = {a_affine_inv} \\times ({i} - {k_affine}) = {a_affine_inv} \\times {(i - k_affine) if (i - k_affine) >= 0 else '(' + str(i - k_affine)+')'} \equiv {(a_affine_inv* (i - k_affine))%base}[{base}]$                
                """)


#######################################################################
#####                                                             #####
#####                      2. RSA decryptage                      #####
#####                                                             #####
#######################################################################
st.markdown("""

<br>            
            
##### 4.2.2 RSA:

###### $\qquad \\text{Decryptage RSA}:$
                """, unsafe_allow_html=True)

st.latex(r"""
         \begin{equation*}
		\begin{CD}
			M_2 @> D(pk_b)>> \dot M_2  @>D(sk_a)>> M_1
		\end{CD}
	\end{equation*}
         """)
st.markdown("""

-  $D_{pk_b}(M_2)$ :            
            """)
for i in decryptage_affine:
    text = "D_{pk_b} (" + str(i) + ") = " + str(i) + "^{" + str(e_B) + "}\equiv " + str(modular_exponentiation(i, e_B, n_B)) + "[" + str(n_B) +"]" + ('\quad (= '+(str(modular_exponentiation(i, e_B, n_B)+n_B))+'<' + str(n_B)+')' if ((modular_exponentiation(i, e_B, n_B) +n_B)< n_B) else '')
    st.markdown(f"""$\qquad {text}$
            """)
st.markdown("""

<br>

            """,unsafe_allow_html=True)
st.markdown("""

-  $D_{sk_a}(\dot M_2)$ :            
            """)
for i in list_affine_rsa_b:
    text = "D_{sk_a} (" + str(i) + ") = " + str(i) + "^{" + str(d_a) + "}\equiv " + str(modular_exponentiation(i, d_a, n_A)) + "[" + str(n_A) +"]" + ('\quad ('+(str(modular_exponentiation(i, d_a, n_A)))+'+'+ str(n_A) + '='+str(modular_exponentiation(i, d_a, n_A)+n_A) +' <' + str(2526)+')' if ((modular_exponentiation(i, d_a, n_A)+ n_A)< 2526) else '')
    st.markdown(f"""$\qquad {text}$
            """)
#######################################################################
#####                                                             #####
#####                   2. Hill decryptage                        #####
#####                                                             #####
#######################################################################
st.markdown("""

<br>            
            
##### 4.2.3 Hill:
                """, unsafe_allow_html=True)    
text =''
for i in range(len(list_affine_rsa_b_rsa_a_hill)):
    text += f'Y_{i+1}= {begin_matrice} {list_affine_rsa_b_rsa_a_hill[i][0]} \\\ {list_affine_rsa_b_rsa_a_hill[i][1]} {end_matrice}, \,'
text += f'\dot Y_5 ={begin_matrice} {list_affine_rsa_b_rsa_a_hill[4][0]+ n_A} \\\ {list_affine_rsa_b_rsa_a_hill[4][1]} {end_matrice}, \,'
text += f'{a_inv_text}= {begin_matrice} {hill_m_inv_modulo[0][0]} & {hill_m_inv_modulo[0][1]} \\\ {hill_m_inv_modulo[1][0]} & {hill_m_inv_modulo[1][1]} {end_matrice}'
st.markdown(f"""

$\qquad {text}$                
                """)
for i in range(len(list_affine_rsa_b_rsa_a_hill)):
    st.markdown(f"""

$\qquad {d_hill}(Y_{i+1})= {a_inv_text} \cdot Y_{i+1} = {begin_matrice} {hill_m_inv_modulo[0][0]} & {hill_m_inv_modulo[0][1]} \\\ {hill_m_inv_modulo[1][0]} & {hill_m_inv_modulo[1][1]} {end_matrice} \cdot {begin_matrice} {list_affine_rsa_b_rsa_a_hill[i][0]} \\\ {list_affine_rsa_b_rsa_a_hill[i][1]} {end_matrice}$
$= {begin_matrice} {hill_m_inv_modulo[0][0]}\\times {list_affine_rsa_b_rsa_a_hill[i][0]} + {hill_m_inv_modulo[0][1]}\\times {list_affine_rsa_b_rsa_a_hill[i][1]} \\\ {hill_m_inv_modulo[1][0]}\\times {list_affine_rsa_b_rsa_a_hill[i][0]} + {hill_m_inv_modulo[1][1]}\\times {list_affine_rsa_b_rsa_a_hill[i][1]} {end_matrice}$
$=  {begin_matrice}  {(hill_m_inv_modulo[0][0]*list_affine_rsa_b_rsa_a_hill[i][0] + hill_m_inv_modulo[0][1]*list_affine_rsa_b_rsa_a_hill[i][1])%base} \\\ {(hill_m_inv_modulo[1][0]*list_affine_rsa_b_rsa_a_hill[i][0] + hill_m_inv_modulo[1][1]*list_affine_rsa_b_rsa_a_hill[i][1])%base}  {end_matrice}[{base}]$                
                """)
st.markdown(f"""

$\qquad {d_hill}(\dot Y_5)= {a_inv_text} \cdot \dot Y_5 = {begin_matrice} {hill_m_inv_modulo[0][0]} & {hill_m_inv_modulo[0][1]} \\\ {hill_m_inv_modulo[1][0]} & {hill_m_inv_modulo[1][1]} {end_matrice} \cdot {begin_matrice} {list_affine_rsa_b_rsa_a_hill[4][0]+ n_A} \\\ {list_affine_rsa_b_rsa_a_hill[4][1]} {end_matrice}$
$= {begin_matrice} {hill_m_inv_modulo[0][0]}\\times {list_affine_rsa_b_rsa_a_hill[4][0]+ n_A} + {hill_m_inv_modulo[0][1]}\\times {list_affine_rsa_b_rsa_a_hill[4][1]} \\\ {hill_m_inv_modulo[1][0]}\\times {list_affine_rsa_b_rsa_a_hill[4][0]+ n_A} + {hill_m_inv_modulo[1][1]}\\times {list_affine_rsa_b_rsa_a_hill[i][1]} {end_matrice}$
$=  {begin_matrice}  {(hill_m_inv_modulo[0][0]*(list_affine_rsa_b_rsa_a_hill[4][0] + n_A)+ hill_m_inv_modulo[0][1]*list_affine_rsa_b_rsa_a_hill[4][1])%base} \\\ {(hill_m_inv_modulo[1][0]*(list_affine_rsa_b_rsa_a_hill[4][0] + n_A) + hill_m_inv_modulo[1][1]*list_affine_rsa_b_rsa_a_hill[4][1])%base}  {end_matrice}[{base}]$                
                """)
st.divider()
st.markdown("""
#### 4.3.  (C-B-A)
- $\\text{Cryptage}$
                """)
st.latex(r"""
         \begin{equation*}
		\begin{CD}
			\text{Message original}  @>Hill>> M_1 @>Affine>> M_2 @>RSA>> \text{Message crypté}
		\end{CD}
	\end{equation*}
         """)

st.markdown("""
- $\\text{Décryptage}$
                """)   

st.latex(r"""
         \begin{equation*}
		\begin{CD}
              \text{Message crypté} @>RSA>> M_2 @>Affine>> M_1 @>Hill>> \text{Message original}
		\end{CD}
	\end{equation*}
         """)

