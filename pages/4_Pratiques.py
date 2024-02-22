import streamlit as st
import pandas as pd
from models.programs.chiffrement import *
from models.programs.arithmetique import *
from style.style import style



st.set_page_config(
    page_title='Introduction à la Cryptographie | Exercices du cours',
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
    <h1 class="main-title">Introduction à la cryptographie: <br>Pratiques</h1>
    <br><br>
""",unsafe_allow_html=True)

###############################################################################
###                                                                         ###
###                             Pratiques                                   ###
###                                                                         ###
###############################################################################
st.divider()
st.markdown("""
    <div class="main-title">
     
    ## Arithméthique de $\\Z$
    
    </div>
    <br><br>
""",unsafe_allow_html=True)
ordina_exercice_cols = st.columns([1,1,1,2])
with ordina_exercice_cols[0]:
    numberA = st.number_input("**$\\text{Entrer la valeur de a:}$**",step=1)
with ordina_exercice_cols[1]:
    numberB = st.number_input("**$\\text{Entrer la valeur de n ou b:}$**", step=1)
with ordina_exercice_cols[2]:
    numberE = st.number_input("**$\\text{Entrer la valeur de e:}$**", step=1, min_value=1)
with ordina_exercice_cols[3]:
    product_modulo = st.text_input("Entrer des nombres sparé avec (-)",key='product_modulo')


test_cols = st.columns([1,1,2])
with test_cols[0]:
    pgcd_button = st.button("$\\text{PGCD}$", use_container_width=True)
with test_cols[1]:
    bezout_button = st.button("$\\text{Bezout}$",use_container_width=True)
with test_cols[2]:
    algorithme_euclide_etendu_button = st.button("$\\text{Algorithme d'Euclide Étendu}$", use_container_width=True)


test_cols_2 = st.columns([1,1,1,1])
with test_cols_2[0]:
    decomposition_button = st.button("$\\text{Decomposition}$", use_container_width=True)
with test_cols_2[1]:
    nombres_premiers_button = st.button("$\\text{Nombres Premiers}$", use_container_width=True)
with test_cols_2[2]:
    puissance_modulo_button = st.button("$\\text{Puissance modulo}$", use_container_width=True)
with test_cols_2[3]:
    product_modulo_button = st.button("$\\text{Produit modulo}$", use_container_width=True)

if pgcd_button:
    st.markdown("""- $\\text{Le PGCD:}$""")
    st.markdown(f"$\qquad \quad PGCD({numberA},{numberB}) = {pgcd(numberA,numberB)}$")

if bezout_button:
    st.markdown("""- $\\text{L'identité de Bézout:}$""")
    st.write(f"$\qquad \quad u ={bezout(numberA,numberB)[0]}$")
    st.write(f"$\qquad \quad v ={bezout(numberA,numberB)[1]}$")
    st.write(f"$\qquad \quad {numberA} \\times {bezout(numberA,numberB)[0] if bezout(numberA,numberB)[0] >= 0 else '('+str(bezout(numberA,numberB)[0])+')'} {' + '+ str(numberB) if numberB >= 0 else numberB} \\times {bezout(numberA,numberB)[1] if bezout(numberA,numberB)[1] >= 0 else '('+str(bezout(numberA,numberB)[1])+')'} = {str(pgcd(numberA,numberB))}$")

if algorithme_euclide_etendu_button:
    st.markdown("""
<style>
      tr th:first-child {
                display: none;
                visibility:hidden;
            }          
</style>
""",unsafe_allow_html=True)
    st.markdown("""- $\\text{Algorithme d'Euclide Étendu:}$""")
    df = pd.DataFrame(algorithme_euclide_etendu(numberA,numberB), columns=["a","b","r","q","u","v"])
    algo_cols = st.columns([1,4,1])
    with algo_cols[1]:
        st.table(df)
    st.markdown("""- $\\text{L'identité de Bézout:}$""")
    st.write(f"$\qquad \quad {numberA} \\times u {' + '+ str(numberB) if numberB >= 0 else numberB} \\times v ={numberA} \\times {bezout(numberA,numberB)[0] if bezout(numberA,numberB)[0] >= 0 else '('+str(bezout(numberA,numberB)[0])+')'} {' + '+ str(numberB) if numberB >= 0 else numberB} \\times {bezout(numberA,numberB)[1] if bezout(numberA,numberB)[1] >= 0 else '('+str(bezout(numberA,numberB)[1])+')'} = {str(abs(pgcd(numberA,numberB)))}$")
    st.write(f"$\qquad \quad u ={bezout(numberA,numberB)[0]}, \quad v ={bezout(numberA,numberB)[1]}.$")
    st.markdown("""- $\\text{Le PGCD:}$""")
    st.markdown(f"$\qquad \quad Le \, PGCD({numberA},{numberB}) = {abs(pgcd(numberA,numberB))}$")

if decomposition_button:
    com_list,com_tuple = decomposition(numberA)
    html_content = ''
    html_content2 = ''
    for i in com_list:
        html_content += '<span>' + str(i[0]) + '</span><br>'
        html_content2 += '<span>' + str(i[1]) + '</span><br>'
    html_content += '<span>1</span><br>'

    text = f""
    if numberA < 0:
        text += '-'
    if len(com_tuple) > 1:
        for i in range(len(com_tuple)-1):
            if com_tuple[i][1] != 1:
                text += str(com_tuple[i][0])+"^{" + str(com_tuple[i][1]) +"} \\times"
            else:
                text += str(com_tuple[i][0])+ "\\times"

    if com_tuple[-1][1] != 1:
        text += str(com_tuple[-1][0])+"^{" + str(com_tuple[-1][1])+"}"
    else:
        text += str(com_tuple[-1][0])
    st.markdown(f"""

##### La décomposion de {numberA} en facteur premier est: 

<div style="display: grid; grid-template-columns: auto auto;">            
<div style="padding-right: 5px; text-align: end;">
{html_content}
</div>
<div style="border-left: 4px solid #E694FF; padding-left: 5px; text-align: start;">
{html_content2}
</div>
</div>    

$Donc:\quad {numberA} = {text}$

<br>

$\implies D({numberA}) = {divisors(numberA)}$
""",unsafe_allow_html=True)

if nombres_premiers_button:
    st.markdown(f"""

##### Les nombres premiers inférieur a {numberA} sont: 

<div align="center">

###### ${primeNumbersLessThan(numberA)}$

</div>
""",unsafe_allow_html=True)

if puissance_modulo_button:
    puissance_modulo = modular_exponentiation(numberA, numberE, numberB)
    numberE_text = '{' + str(numberE) + '}'
    number = f'{numberA}^{numberE_text}' if numberE != 1 else f'{numberA}'
    st.markdown(f"""
<br>
<center>

${number} \equiv {puissance_modulo} [{numberB}]$ 

</center>                
                """, unsafe_allow_html=True)
    
###############################################################################
###                                                                         ###
###                             Produit Modulo                              ###
###                                                                         ###
############################################################################### 
if product_modulo_button:
    liste_sum = product_modulo.split('+')
    liste_produit = [item.split('x') for item in liste_sum]
    produit_modulo = [modular_multiplication(item, numberB) for item in liste_produit]
    sum_produit_modulo = sum(produit_modulo) % numberB
    total = f''
    if len(liste_sum) == 1:
        produit = f'{liste_produit[0][0]}'
        for i in range(1,len(liste_produit[0])):
            produit += f'\\times {liste_produit[0][i]}'
        total += produit
    else:
        total = f''
        for k in range(len(liste_sum)):
            produit = f''
            for i in range(len(liste_produit)):
                if i != 0:
                    produit += f'\\times {liste_produit[k][i]}'
                else:
                    produit += f'{liste_produit[k][i]}'
            if k < (len(liste_sum)-1):
                total += f'{produit} +'
            else:
                total += f'{produit}'
    
    st.markdown(f"""
<br>
<center>

${total} \equiv {sum_produit_modulo} [{numberB}]$ 

</center>                
                """, unsafe_allow_html=True)
    
###############################################################################
###                                                                         ###
###                             Cryptage César                              ###
###                                                                         ###
###############################################################################    
st.divider()
st.markdown("""
    <h2 class="main-title">Cryptage César</h2>
    <br><br>
""",unsafe_allow_html=True)
cryptage_cesar_cols= st.columns([3,1,1,1])
with cryptage_cesar_cols[0]:
    message_cesar = st.text_input("Message",key='message_cesar').upper()
with cryptage_cesar_cols[1]:
    cesar_paquet = st.number_input("Paquet", key='cesar_paket', step=1, min_value=1, max_value=3)
with cryptage_cesar_cols[2]:
    cesar_key = st.number_input("Key (K)", key='cesar_key', step=1)
with cryptage_cesar_cols[3]:
    cesar_option_selected = st.selectbox("**$\\text{Sélctionné A ou Z}$**",
   ("A", "Z"), key='cesar_option')
cryptage_cesar_buttons_cols= st.columns([1,2,2,1])
with cryptage_cesar_buttons_cols[1]:
    cesar_crypt = st.button("$\\text{Crypter César}$", use_container_width=True)
with cryptage_cesar_buttons_cols[2]:
    cesar_decrypt = st.button("$\\text{Décrypter César}$", use_container_width=True)
if cesar_crypt:
    question = '\\text{Cryptons le message ' + message_cesar +'} $ $\\text{ par la méthode de César par paquet de }' + str(cesar_paquet) +'\\text{ avec }' +str(cesar_key) +'\\text{ comme clef.}'
    st.markdown(f"""
- ${question}$
""")
    st.markdown("""
    <style>
th {
    display: none;
}
tbody tr:nth-child(1) {
    background-color: purple;
    color: white;
}
</style>

""", unsafe_allow_html=True)
    cesar = cesar_cryptage(cesar_key,message_cesar,cesar_option_selected,cesar_paquet)
    if cesar_paquet == 1:
        head= '||'
        head_h = '|:---:|'    
        x = '|$X \longrightarrow$|'
        z26z = '|$\\Z/26\\Z$|'
        plus_k = f'|$+{cesar_key}$|'
        z26z2 = '|$\\Z/26\\Z$|'
        y = '|$Cr(X) \longrightarrow$|'
    elif cesar_paquet == 2:
        head= '||'
        head_h = '|:---:|'    
        x = '|$X \longrightarrow$|'
        z26z = '|$\\Z/2526\\Z$|'
        plus_k = f'|$+{cesar_key}$|'
        z26z2 = '|$\\Z/2526\\Z$|'
        y = '|$Cr(X) \longrightarrow$|'
    elif cesar_paquet == 3:
        head= '||'
        head_h = '|:---:|'    
        x = '|$X \longrightarrow$|'
        z26z = '|$\\Z/252526\\Z$|'
        plus_k = f'|$+{cesar_key}$|'
        z26z2 = '|$\\Z/252526\\Z$|'
        y = '|$Cr(X) \longrightarrow$|'

    for i in cesar:
        head += '|'
        head_h += ':---:|'
        x += f'${str(i[0])}$|'
        z26z += f'${str(i[1])}$|'
        plus_k += f'${str(i[2])}$|'
        z26z2 += f'${str(i[3])}$|'
        y += f'${str(i[4])}$|'

    st.markdown(f"""
<center>
                
{head}
{head_h}
{x}
{z26z}
{plus_k}
{z26z2}
{y}

</center>
<br>
""",unsafe_allow_html=True)
    if cesar_paquet != 1:
        crypted_message = '-'.join([str(i[4])  for i in cesar])
    else:
        crypted_message = ''.join([str(i[4])  for i in cesar])
    result = '\\text{Le message crypté du mot est '+ message_cesar  + ' par la méthode de César par paquet de ' + str(cesar_paquet) +'}$ $ \\text{avec ' +str(cesar_key) +' comme clef, est }' + crypted_message
    st.markdown(f"""
${result}$                  
                    """)

if cesar_decrypt:
    origin = '\\text{On a utilisé la méthode de César par paquet de }' + str(cesar_paquet) + '\\text{ avec }' + str(cesar_key) + '\\text{ comme clef pour obtenir }$ $' + message_cesar + '\\text{. On cherchons le message original}'
    st.markdown(f"""
- ${origin}$""")
    
    st.markdown("""
    <style>
th {
    display: none;
}
tbody tr:nth-child(1) {
    background-color: purple;
    color: white;
}
</style>

""", unsafe_allow_html=True)
    cesar = cesar_decryptage(cesar_key,message_cesar,cesar_paquet)
    head= '||'
    head_h = '|:---:|'    
    col1 = '|$Y \longrightarrow$|'

    if cesar_paquet == 1:
        col2 = '|$\\Z/26\\Z$|'
        col3 = f'|$-{cesar_key}$|'
        col4 = '|$\\Z/26\\Z$|'
        col5 = '|$D(Y) \longrightarrow$|'
        col6 = ''
    elif cesar_paquet == 2:
        col2 = f'|$-{cesar_key}$|'
        col3 = '|$\\Z/2526\\Z$|'
        col4 = '||'
        col5 ='||'
        col6 = '|$D(Y) \longrightarrow$|'
    elif cesar_paquet == 3:
        col2 = f'|$-{cesar_key}$|'
        col3 = '|$\\Z/252526\\Z$|'
        col4 ='||'
        col5 = '||'
        col6 = '|$D(Y) \longrightarrow$|'

    for i in cesar:
        head += '|'
        head_h += ':---:|'
        col1 += f'${str(i[0])}$|'
        col2 += f'${str(i[1])}$|'
        col3 += f'${str(i[2])}$|'
        col4 += f'${str(i[3])}$|'
        col5 += f'${str(i[4])}$|'
        if cesar_paquet != 1:
            col6 += f'${str(i[5])}$|'


    st.markdown(f"""
    <center>

    {head}
    {head_h}
    {col1}
    {col2}
    {col3}
    {col4}
    {col5}
    {col6}

    </center>
    <br>
    """,unsafe_allow_html=True)
    if cesar_paquet != 1:
        original_message = ''.join([str(i[5])  for i in cesar])
    else:
        original_message = ''.join([str(i[4])  for i in cesar])
    result = '\\text{Le message originale est }' + original_message
    st.markdown(f"""
${result}$                  
                    """)
###############################################################################
###                                                                         ###
###                             Cryptage Affine                             ###
###                                                                         ###
###############################################################################
st.divider()
st.markdown("""
    <h2 class="main-title">Cryptage Affine</h2>
    <br><br>
""",unsafe_allow_html=True)
cryptage_affine_cols= st.columns([4,1,1,1,1])
with cryptage_affine_cols[0]:
    message_affine = st.text_input("Message",key='message_affine').upper()
with cryptage_affine_cols[1]:
    affine_paquet = st.number_input("Paquet", key='affine_paket', step=1, min_value=1, max_value=3)
with cryptage_affine_cols[2]:
    affine_a = st.number_input("a", key='affine_a', value=1, step=1)
with cryptage_affine_cols[3]:
    affine_key = st.number_input("Key (K)", key='affine_key', step=1)
with cryptage_affine_cols[4]:
    affine_option_selected = st.selectbox("**$\\text{Sélctionné A ou Z}$**",
   ("A", "Z"), key='affine_option')
    
cryptage_affine_buttons_cols= st.columns([1,2,2,1])
with cryptage_affine_buttons_cols[1]:
    affine_crypt = st.button("$\\text{Crypter Affine}$",key='crypter_affine', use_container_width=True)
with cryptage_affine_buttons_cols[2]:
    affine_decrypt = st.button("$\\text{Décrypter Affine}$", key='decrypter_affine', use_container_width=True)

if affine_crypt:
    question = '\\text{Cryptons le message } \enspace ' + message_affine +'\enspace \\text{ par la méthode de Affine par paquet de }' + str(affine_paquet) +'\\text{ avec (}' +str(affine_a)+';' +str(affine_key) +'\\text{) comme clef.}'
    st.markdown(f"""
- ${question}$""")
    st.markdown("""
<style>
      tr th:first-child {
                display: none;
                visibility:hidden;
            }          
</style>
""",unsafe_allow_html=True)
    st.markdown("""- $\\text{Algorithme d'Euclide Étendu:}$""")
    if affine_paquet == 1:
        base = 26
    elif affine_paquet == 2:
        base = 2526
    elif affine_paquet == 3:
        base = 252526
    df = pd.DataFrame(algorithme_euclide_etendu(affine_a,base), columns=["a","b","r","q","u","v"])
    algo_cols = st.columns([1,4,1])
    with algo_cols[1]:
        st.table(df)
    st.markdown("""- $\\text{L'identité de Bézout:}$""")
    st.write(f"$\qquad \quad {affine_a} \\times u {' + '+ str(base)} \\times v ={affine_a} \\times {bezout(affine_a,base)[0] if bezout(affine_a,base)[0] >= 0 else '('+str(bezout(affine_a,base)[0])+')'} {' + '+ str(base)} \\times {bezout(affine_a,base)[1] if bezout(affine_a,base)[1] >= 0 else '('+str(bezout(affine_a,base)[1])+')'} = {str(abs(pgcd(affine_a,base)))}$")
    st.write(f"$\qquad \quad u ={bezout(affine_a,base)[0]}, \quad v ={bezout(affine_a,base)[1]}.$")
    st.markdown("""- $\\text{Le PGCD:}$""")
    st.markdown(f"$\qquad \quad Le \, PGCD({affine_a},{base}) = {abs(pgcd(affine_a,base))}$")
    st.markdown("""
    <style>
th {
    display: none;
}
tbody tr:nth-child(1) {
    background-color: purple;
    color: white;
}
</style>

""", unsafe_allow_html=True)
    affine = affine_crypto(affine_a,affine_key,message_affine,affine_option_selected,affine_paquet)

    if affine_paquet == 1:
        base = 26
        head= '||'
        head_h = '|:---:|'    
        x = '|$X \longrightarrow$|'
        z26z = '|$\\Z/26\\Z$|'
        plus_k = f'|${affine_a}x+{affine_key}$|'
        z26z2 = '|$\\Z/26\\Z$|'
        y = '|$Cr(X) \longrightarrow$|'
    elif affine_paquet == 2:
        base = 2526
        head= '||'
        head_h = '|:---:|'    
        x = '|$X \longrightarrow$|'
        z26z = '|$\\Z/2526\\Z$|'
        plus_k = f'|${affine_a}x+{affine_key}$|'
        z26z2 = '|$\\Z/2526\\Z$|'
        y = '|$Cr(X) \longrightarrow$|'
    elif affine_paquet == 3:
        base = 252526
        head= '||'
        head_h = '|:---:|'    
        x = '|$X \longrightarrow$|'
        z26z = '|$\\Z/252526\\Z$|'
        plus_k = f'|${affine_a}x+{affine_key}$|'
        z26z2 = '|$\\Z/252526\\Z$|'
        y = '|$Cr(X) \longrightarrow$|'


    if pgcd(affine_a,base) == 1:
        for i in affine:
            head += '|'
            head_h += ':---:|'
            x += f'${str(i[0])}$|'
            z26z += f'${str(i[1])}$|'
            plus_k += f'${str(i[2])}$|'
            z26z2 += f'${str(i[3])}$|'
            y += f'${str(i[4])}$|'
        st.markdown(f"""
    <center>

    {head}
    {head_h}
    {x}
    {z26z}
    {plus_k}
    {z26z2}
    {y}

    </center>
    <br>
    """,unsafe_allow_html=True)
        if affine_paquet != 1:
            crypted_message = '-'.join([str(i[4])  for i in affine])
        else:
            crypted_message = ''.join([str(i[4])  for i in affine])
        result = '\\text{Le message crypté du mot } \enspace ' + message_affine +'\enspace \\text{ par la méthode de Affine par paquet de }' + str(affine_paquet) +'\\text{ avec (}' +str(affine_a)+';' +str(affine_key) +'\\text{) comme clef, est } \enspace'+ crypted_message 
        st.markdown(f"""
${result}$                  
                    """)
    else:
        st.markdown(affine)

if affine_decrypt:
    origin = '\\text{On a utilisé la méthode de Affine par paquet de }' + str(affine_paquet) + '\\text{ avec (}'  + str(affine_a)+';' +str(affine_key)  + '\\text{) comme clef pour obtenir }$ $' + message_affine + '\\text{. On cherchons le message original}'
    st.markdown(f"""
- ${origin}$""")
    st.markdown("""
<style>
      tr th:first-child {
                display: none;
                visibility:hidden;
            }          
</style>
""",unsafe_allow_html=True)
    st.markdown("""- $\\text{Algorithme d'Euclide Étendu:}$""")
    if affine_paquet == 1:
        base = 26
    elif affine_paquet == 2:
        base = 2526
    elif affine_paquet == 3:
        base = 252526
    df = pd.DataFrame(algorithme_euclide_etendu(affine_a,base), columns=["a","b","r","q","u","v"])
    algo_cols = st.columns([1,4,1])
    with algo_cols[1]:
        st.table(df)
    st.markdown(""" - $\\text{L'identité de Bézout:}$""")
    st.write(f"$\qquad \quad {affine_a} \\times u {' + '+ str(base)} \\times v ={affine_a} \\times {bezout(affine_a,base)[0] if bezout(affine_a,base)[0] >= 0 else '('+str(bezout(affine_a,base)[0])+')'} {' + '+ str(base)} \\times {bezout(affine_a,base)[1] if bezout(affine_a,base)[1] >= 0 else '('+str(bezout(affine_a,base)[1])+')'} = {str(abs(pgcd(affine_a,base)))}$")
    st.write(f"$\qquad \quad u ={bezout(affine_a,base)[0]}, \quad v ={bezout(affine_a,base)[1]}.$")
    st.markdown("""- $\\text{Le PGCD:}$""")
    st.markdown(f"$\qquad \quad Le \, PGCD({affine_a},{base}) = {abs(pgcd(affine_a,base))}$")
    
    affine_dec = affine_decryptage(affine_a,affine_key,message_affine,affine_paquet)

    if affine_paquet == 1:
        affine_a_inverse= bezout(affine_a,base)[0]%base
        head= '||'
        head_h = '|:---:|'    
        col1 = '|$Y \longrightarrow$|'
        col2 = '|$\\Z/26\\Z$|'
        col3 = f'|${affine_a_inverse}(y-{affine_key})$|'
        col4 = '|$\\Z/26\\Z$|'
        col5 = '|$D(Y) \longrightarrow$|'
        col6 = ''
    elif affine_paquet == 2:
        affine_a_inverse= bezout(affine_a,base)[0]%base
        head= '||'
        head_h = '|:---:|'    
        col1 = '|$Y \longrightarrow$|'
        col2 = f'|${affine_a_inverse}(y-{affine_key})$|'
        col3 = '|$\\Z/2526\\Z$|'
        col4 = '||'
        col5 = '||'
        col6 = '|$D(Y) \longrightarrow$|' 
    elif affine_paquet == 3:
        affine_a_inverse= bezout(affine_a,base)[0]%base
        head= '||'
        head_h = '|:---:|'    
        col1 = '|$Y \longrightarrow$|'
        col2 = f'|${affine_a_inverse}(y-{affine_key})$|'
        col3 = '|$\\Z/252526\\Z$|'
        col4 = '||'
        col5 = '||'
        col6 = '|$D(Y) \longrightarrow$|' 


    if pgcd(affine_a,base) == 1:
        st.markdown("""
    <style>
.table th {
    display: none;
}
.table tbody tr:nth-child(1) {
    background-color: purple;
    color: white;
}
</style>

""", unsafe_allow_html=True)
        for i in affine_dec:
            head += '|'
            head_h += ':---:|'
            col1 += f'${str(i[0])}$|'
            col2 += f'${str(i[1])}$|'
            col3 += f'${str(i[2])}$|'
            col4 += f'${str(i[3])}$|'
            col5 += f'${str(i[4])}$|'
            if affine_paquet != 1:
                col6 += f'${str(i[5])}$|'
        st.markdown(f"""
    
<center>
<div class='table'>

{head}
{head_h}
{col1}
{col2}
{col3}
{col4}
{col5}
{col6}

</div>
    </center>
<br>
    """,unsafe_allow_html=True)
        if affine_paquet != 1:
            original_message = ''.join([str(i[5])  for i in affine_dec])
        else:
            original_message = ''.join([str(i[4])  for i in affine_dec])
        result = '\\text{Le message originale est }' + original_message
        st.markdown(f"""
${result}$                  
                    """)
        
    else:
        st.markdown(affine_dec)
    
###############################################################################
###                                                                         ###
###                             Cryptage Puissance                          ###
###                                                                         ###
###############################################################################
st.divider()
st.markdown("""
    <h2 class="main-title">Cryptage Puissance</h2>
    <br><br>
""",unsafe_allow_html=True)
cryptage_puissance_cols= st.columns([4,1,1,1,1,1])
with cryptage_puissance_cols[0]:
    message_puissance = st.text_input("Message",key='message_puissance').upper()
with cryptage_puissance_cols[1]:
    puissance_paquet = st.number_input("Paquet", key='puissance_paket', step=1, min_value=1, max_value=3)
with cryptage_puissance_cols[2]:
    puissance_a = st.number_input("a", key='puissance_a', value=1, step=1)
with cryptage_puissance_cols[3]:
    puissance_b = st.number_input("b", key='puissance_b', value=0, step=1)
with cryptage_puissance_cols[4]:
    puissance_c = st.number_input("c", key='puissance_c', value=1, step=1)
with cryptage_puissance_cols[5]:
    puissance_option_selected = st.selectbox("**$\\text{Sélctionné A ou Z}$**",
   ("A", "Z"), key='puissance_option')
    
cryptage_puissance_buttons_cols= st.columns([1,2,2,1])
with cryptage_puissance_buttons_cols[1]:
    puissance_crypt = st.button("$\\text{Crypter Puissance}$",key='crypter_puissance', use_container_width=True)
with cryptage_puissance_buttons_cols[2]:
    puissance_decrypt = st.button("$\\text{Décrypter Puissance}$", key='decrypter_puissance', use_container_width=True)

if puissance_crypt:
    question = '\\text{Cryptons le message } \enspace ' + message_puissance +'\enspace \\text{ par la méthode de Puissance par paquet de }' + str(puissance_paquet) +'\\text{ avec (}' +str(puissance_a)+';' +str(puissance_b) +';' +str(puissance_c) +'\\text{) comme clef.}'
    st.markdown(f"""
- ${question}$""")

if puissance_decrypt:
    origin = '\\text{On a utilisé la méthode de Puissance par paquet de }' + str(puissance_paquet) + '\\text{ avec (}'  + str(puissance_a)+';' +str(puissance_b) +';' +str(puissance_c) + '\\text{) comme clef pour obtenir }$ $' + message_puissance + '\\text{. On cherchons le message original}'
    st.markdown(f"""
- ${origin}$""")
###############################################################################
###                                                                         ###
###                             Cryptage Hill                               ###
###                                                                         ###
###############################################################################
st.divider()
st.markdown("""
    <h2 class="main-title">Cryptage Hill</h2>
    <br><br>
""",unsafe_allow_html=True)
cryptage_hill_cols= st.columns([4,1,1])
with cryptage_hill_cols[0]:
    message_hill = st.text_input("Message",key='message_hill').upper()
with cryptage_hill_cols[1]:
    dimension = st.number_input("Dimension", step=1, min_value=2, max_value=3)
with cryptage_hill_cols[2]:
    hill_option_selected = st.selectbox("**$\\text{Sélctionné A ou Z}$**",
   ("A", "Z"), key='hill_option')
pratiques_cols = st.columns([1,1,1,1,1,3,1])
with pratiques_cols[0]:
    st.markdown("""<br><br><br>""", unsafe_allow_html=True)
    
    st.header("$K=$")
with pratiques_cols[1]:
    a = st.number_input("a",step=1, value=0, label_visibility="hidden")
with pratiques_cols[2]:
    b = st.number_input("b",step=1, value=0, label_visibility="hidden")
with pratiques_cols[3]:
    c = st.number_input("c",step=1, value=0, label_visibility="hidden")
with pratiques_cols[1]:
    d = st.number_input("d",step=1, value=0, label_visibility="hidden")
with pratiques_cols[2]:
    e = st.number_input("e",step=1, value=0, label_visibility="hidden")
with pratiques_cols[3]:
    f = st.number_input("f",step=1, value=0, label_visibility="hidden")
with pratiques_cols[1]:
    g = st.number_input("g",step=1, value=0, label_visibility="hidden")
with pratiques_cols[2]:
    h = st.number_input("h",step=1, value=0, label_visibility="hidden")
with pratiques_cols[3]:
    i = st.number_input("i",step=1, value=0, label_visibility="hidden")
with pratiques_cols[5]:
    st.markdown("""<br><br><br>""", unsafe_allow_html=True)
    hill_crypt_button = st.button("$\\text{Crypter Hill}$", use_container_width=True)
    hill_discrypt_button = st.button("$\\text{Décripter Hill}$", use_container_width=True)

if hill_crypt_button:
    if dimension == 2:
        matrice2 = '\\begin{pmatrix}' + str(a) +'&' + str(b) + '\\\\' + str(d) +'&' + str(e) + '\end{pmatrix}'
        question= '\\text{En utilisant un chiffrement de Hill de }$ $\\text{dimension }'+ str(dimension) +'\\text{ par paquet de 1, chiffrer le }$ $\\text{message ' + message_hill +  ' avec }' + matrice2 + '\\text{ comme clef.}'
        st.markdown(f'${question}$')
    if dimension == 3:
        matrice3 = '\\begin{pmatrix}' + str(a) +'&' + str(b)+'&' + str(c) + '\\\\' + str(d) +'&' + str(e)+'&' + str(f)+ '\\\\' + str(g) +'&' + str(h)+'&' + str(i) + '\end{pmatrix}'
        question= '\\text{En utilisant un chiffrement de Hill de }$ $\\text{dimension }'+ str(dimension) +'\\text{ par paquet de 1, chiffrer le }$ $\\text{message ' + message_hill +  ' avec }' + matrice3 + '\\text{ comme clef.}'
        st.markdown(f'${question}$')

if hill_discrypt_button:
    if dimension == 2:
        matrice2 = '\\begin{pmatrix}' + str(a) +'&' + str(b) + '\\\\' + str(d) +'&' + str(e) + '\end{pmatrix}'
        question= '\\text{On a utilisé un chiffrement de Hill de }$ $\\text{dimension }'+ str(dimension) +'\\text{ par paquet de 1, avec }$ $' + matrice2 + '\\text{ comme clef pour obtenir ' + message_hill + '.} \enspace$ $\\text{On cherchons le message claire:}'
        st.markdown(f'${question}$')
    if dimension == 3:
        matrice3 = '\\begin{pmatrix}' + str(a) +'&' + str(b)+'&' + str(c) + '\\\\' + str(d) +'&' + str(e)+'&' + str(f)+ '\\\\' + str(g) +'&' + str(h)+'&' + str(i) + '\end{pmatrix}'
        question= '\\text{On a utilisé un chiffrement de Hill de }$ $\\text{dimension }'+ str(dimension) +'\\text{ par paquet de 1, avec }$ $' + matrice3 + '\\text{ comme clef pour obtenir ' + message_hill + '. }$  $\\text{On cherchons le message claire:}'
        st.markdown(f'${question}$')



###############################################################################
###                                                                         ###
###                             Cryptage RSA                                ###
###                                                                         ###
###############################################################################
st.divider()
st.markdown("""
    <h2 class="main-title">Cryptage RSA</h2>
    <br><br>
""",unsafe_allow_html=True)