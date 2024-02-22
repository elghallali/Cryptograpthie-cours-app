import streamlit as st
import pandas as pd
from models.programs.arithmetique import *


def rechercher_les_clefs(e_b, n_b,nom):
    if nom == 'Bob':
        var_nom = 'b'
    else:
        var_nom = 'a'
    on_cherchons = "\\text{On cherchons }"
    sub_header = "\\text{Décomposition }"
    st.markdown(f"""
                
#### Pour {nom}:

- ${sub_header} n_{var_nom} = {n_b}:$                
                """)
    com_list,com_tuple = decomposition(n_b)

    html_content = ''
    html_content2 = ''
    for i in com_list:
        html_content += '<span>' + str(i[0]) + '</span><br>'
        html_content2 += '<span>' + str(i[1]) + '</span><br>'
    html_content += '<span>1</span><br>'
    text = f""
    if n_b < 0:
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

    ########################################
    ###                                  ###
    ###            p_b et q_b            ###
    ###                                  ###
    ########################################
    if com_tuple[0][1] == 1:
        p_b = com_tuple[0][0]

    if com_tuple[1][1] == 1:
        q_b = com_tuple[1][0]

    phi_n_b = (p_b - 1) * (q_b - 1)

    donc = "\\text{Donc}:\quad " + str(n_b) + "= " + text

    proposons = "\\text{Proposons que} :\quad p_"+ var_nom + "="+str(p_b)+ "\, \\text{ et }\, q_"+ var_nom + " =" + str(q_b)
    st.markdown(f""" 

<div style="display: grid; grid-template-columns: auto auto;">            
<div style="padding-right: 5px; text-align: end;">
{html_content}
</div>
<div style="border-left: 4px solid #E694FF; padding-left: 5px; text-align: start;">
{html_content2}
</div>
</div>    

<br>

${donc}$

${proposons}$ 

<br>


""",unsafe_allow_html=True)

    st.markdown(f"""

- ${on_cherchons} \\varphi(n_{var_nom}):$            
            """)

    st.markdown(f"""

<center>

$\\varphi(n_{var_nom}) = \\varphi(p_{var_nom}) \\times \\varphi(q_{var_nom}) = (p_{var_nom} - 1) \\times (q_{var_nom} -1) = {p_b - 1} \\times {q_b - 1} = {phi_n_b}$

</center>
<br>        
            """,unsafe_allow_html=True)

    st.markdown(f"""
- ${on_cherchons} sk_{var_nom}:$
            """, unsafe_allow_html=True)

    st.markdown("""
<style>
      tr th:first-child {
                display: none;
                visibility:hidden;
            }          
</style>
""",unsafe_allow_html=True)
    df = pd.DataFrame(algorithme_euclide_etendu(phi_n_b,e_b), columns=["a","b","r","q","u","v"])
    algo_cols = st.columns([1,4,1])
    with algo_cols[1]:
        st.table(df)
    
    conclus_b = "\\text{D'après l'algorithme d'Euclide Étendu on a:}" 
    implies_b = "\\text{le pgcd(}" + str(phi_n_b) + "," + str(e_b) + ") = " + str(abs(pgcd(phi_n_b,e_b))) + "\implies " + str(phi_n_b) + "\\text{ et } e_"+ var_nom + "=" + str(e_b) + "\\text{ sont premier entre eux.}"
    exist_d_b = "\\text{donc } \exist \, d_"+ var_nom + "  \in \\Z \quad \\text{tel que } \enspace e_"+ var_nom + ".d_"+ var_nom + " \equiv 1[" + str(phi_n_b) + "]"

    bezout_b = "\\text{D'après la théorème de Bézout on a:}"

    inverse_b = "\\text{Donc l'inverse de }" + str(e_b) + "\\text{ modulo }" + str(phi_n_b) + "\\text{ est }" + (str(bezout(phi_n_b,e_b)[1]) + '['+ str(phi_n_b) + ']' if bezout(phi_n_b,e_b)[1] >= 0 else str(bezout(phi_n_b,e_b)[1]) + ' \equiv ' + str(phi_n_b) + str(bezout(phi_n_b,e_b)[1]) +'\equiv' + str(phi_n_b + bezout(phi_n_b,e_b)[1]) + '['+ str(phi_n_b) + ']')
    alors_b = "\\text{Alors } d_"+ var_nom + " = " + str(bezout(phi_n_b,e_b)[1]%phi_n_b) + "\\text{ modulo }" + str(phi_n_b)
    st.markdown(f"""
    
${conclus_b}$

${implies_b}$

${exist_d_b}$

${bezout_b}$

${phi_n_b} \\times u {' + '+ str(e_b) if e_b >= 0 else e_b} \\times v ={phi_n_b} \\times {bezout(phi_n_b,e_b)[0] if bezout(phi_n_b,e_b)[0] >= 0 else '('+str(bezout(phi_n_b,e_b)[0])+')'} {' + '+ str(e_b) if e_b >= 0 else e_b} \\times {bezout(phi_n_b,e_b)[1] if bezout(phi_n_b,e_b)[1] >= 0 else '('+str(bezout(phi_n_b,e_b)[1])+')'} = {str(abs(pgcd(phi_n_b,e_b)))}$

$\implies {phi_n_b} \\times {bezout(phi_n_b,e_b)[0] if bezout(phi_n_b,e_b)[0] >= 0 else '('+str(bezout(phi_n_b,e_b)[0])+')'} {' + '+ str(e_b) if e_b >= 0 else e_b} \\times {bezout(phi_n_b,e_b)[1] if bezout(phi_n_b,e_b)[1] >= 0 else '('+str(bezout(phi_n_b,e_b)[1])+')'} \equiv {str(abs(pgcd(phi_n_b,e_b)))} [{phi_n_b}] \implies {str(e_b) if e_b >= 0 else e_b} \\times {bezout(phi_n_b,e_b)[1] if bezout(phi_n_b,e_b)[1] >= 0 else '('+str(bezout(phi_n_b,e_b)[1])+')'} \equiv {str(abs(pgcd(phi_n_b,e_b)))} [{phi_n_b}]$

${inverse_b}$

${alors_b}$
""")