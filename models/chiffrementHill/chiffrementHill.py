import streamlit as st
import pandas as pd
from models.programs.arithmetique import *


def hill(x,a,dim,paquet):
    if paquet == 1:
        base = 26
    elif paquet == 2:
        base =2526
    elif paquet == 3:
        base = 252526
        
    if dim == 2:
        return [(a[0][0]*x[0] + a[0][1]*x[1])%base,(a[1][0]*x[0] + a[1][1]*x[1])%base]
    else:
        return None


def hill_matrice_inv(hill_m,paquet, dim):
    if paquet == 1:
        base = 26
    elif paquet == 2:
        base = 2526
    elif paquet== 3:
        base = 252526
    begin_matrice = "\\begin{pmatrix}"
    end_matrice = "\end{pmatrix}"

    begin_matrice_det = "\\begin{vmatrix}"
    end_matrice_det = "\end{vmatrix}"
    on_a = "\\text{On a }"
    a_inv_text = "A^{-1}"
    a_det_inv_text ="det(A)^{-1}"
    on_cherchons_inv = "\\text{On cherchons l'inverse de }"
    on_calculons_det ="\\text{On calculons le déterminant de }"
    modulo_text = "\\text{ modulo }"
    tel_que = "\\text{ tel que }"
    avec = "\\text{avec }"
    dimension_text = "\\text{ est un vecteur de dimension }"
    est_inverse = "\\text{ est l'inverse de la matrice }"
    hill_m_det = hill_m[0][0]*hill_m[1][1] - hill_m[0][1] * hill_m[1][0]
    hill_m_det_inv = bezout(base,hill_m_det)[1]%base
    hill_m_inv = [[hill_m_det_inv * hill_m[1][1],hill_m_det_inv * (-hill_m[0][1])],[hill_m_det_inv * (-hill_m[1][0]),hill_m_det_inv * hill_m[0][0]]]
    hill_m_inv_modulo = [[(j%base) for j in i] for i in hill_m_inv]
    
    
    st.markdown("""

    - $\\text{Cryptage du message } M_1 :$



                """)
    st.latex(r"""
             \begin{equation*}
    		\begin{CD}
    			M_1 @> C(M_1)>> M_2  
    		\end{CD}
    	\end{equation*}
             """)
    st.markdown(f"""

    ${avec} Cr(M1) = A \cdot X_i {tel_que} A = {begin_matrice} {hill_m[0][0]} & {hill_m[0][1]} \\\ {hill_m[1][0]} & {hill_m[1][1]} {end_matrice} , M_1 = X_1X_2...X_n ,\quad X_i {dimension_text} {dim}$

                """)

    st.markdown("""
    - $\\text{Décryptage du message } M_2 :$

                """)
    st.latex(r"""
             \begin{equation*}
    		\begin{CD}
    			M_2 @> D(M_2)>> M_1  
    		\end{CD}
    	\end{equation*}
             """)

    st.markdown(f"""
    ${avec} D(M2) = {a_inv_text} · Y_i \quad {tel_que} {a_inv_text} {est_inverse} A , M_2 = Y_1Y_2...Y_n , \quad Y_i
    {dimension_text} {dim}$

    ##### ${on_cherchons_inv} A = {begin_matrice} {hill_m[0][0]} & {hill_m[0][1]} \\\ {hill_m[1][0]} & {hill_m[1][1]} {end_matrice} {modulo_text} {base}:$

    - ${on_calculons_det} A :$

    <center>

    $det(A) = {begin_matrice_det} {hill_m[0][0]} & {hill_m[0][1]} \\\ {hill_m[1][0]} & {hill_m[1][1]} {end_matrice_det} = {hill_m[0][0]} \\times {hill_m[1][1]} - {hill_m[0][1]} \\times {hill_m[1][0]} = {hill_m[0][0]*hill_m[1][1]-hill_m[0][1]*hill_m[1][0]}$

    </center>

    - ${on_cherchons_inv} det(A) = {hill_m_det} {modulo_text} {base} : $
                """, unsafe_allow_html=True)

    df_hill = pd.DataFrame(algorithme_euclide_etendu(base,hill_m_det), columns=["a","b","r","q","u","v"])
    algo_cols = st.columns([1,4,1])
    with algo_cols[1]:
        st.table(df_hill)


    conclus_b = "\\text{D'après l'algorithme d'Euclide Étendu on a:}" 
    implies_b = "\\text{le pgcd(}" + str(base) + "," + str(hill_m_det) + ") = " + str(abs(pgcd(base,hill_m_det))) + "\implies " + str(base) + "\\text{ et } det(A)=" + str(hill_m_det) + "\\text{ sont premier entre eux.}"
    exist_d_b = "\\text{donc } \exist \, det(A)^{-1}  \in \\Z \quad \\text{tel que } \enspace det(A).det(A)^{-1} \equiv 1[" + str(base) + "]"

    bezout_b = "\\text{D'après la théorème de Bézout on a:}"

    inverse_b = "\\text{Donc l'inverse de }" + str(hill_m_det) + "\\text{ modulo }" + str(base) + "\\text{ est }" + (str(bezout(base,hill_m_det)[1]) + '['+ str(base) + ']' if bezout(base,hill_m_det)[1] >= 0 else str(bezout(base,hill_m_det)[1]) + ' \equiv ' + str(base) + str(bezout(base,hill_m_det)[1]) +'\equiv' + str(base + bezout(base,hill_m_det)[1]) + '['+ str(base) + ']')
    alors_b = "\\text{Alors } det(A)^{-1} = " + str(bezout(base,hill_m_det)[1]%base) + "\\text{ modulo }" + str(base)
    st.markdown(f"""

    ${conclus_b}$

    ${implies_b}$

    ${exist_d_b}$

    ${bezout_b}$

    ${base} \\times u {' + '+ str(hill_m_det) if hill_m_det >= 0 else hill_m_det} \\times v ={base} \\times {bezout(base,hill_m_det)[0] if bezout(base,hill_m_det)[0] >= 0 else '('+str(bezout(base,hill_m_det)[0])+')'} {' + '+ str(hill_m_det) if hill_m_det >= 0 else hill_m_det} \\times {bezout(base,hill_m_det)[1] if bezout(base,hill_m_det)[1] >= 0 else '('+str(bezout(base,hill_m_det)[1])+')'} = {str(abs(pgcd(base,hill_m_det)))}$

    $\implies {base} \\times {bezout(base,hill_m_det)[0] if bezout(base,hill_m_det)[0] >= 0 else '('+str(bezout(base,hill_m_det)[0])+')'} {' + '+ str(hill_m_det) if hill_m_det >= 0 else hill_m_det} \\times {bezout(base,hill_m_det)[1] if bezout(base,hill_m_det)[1] >= 0 else '('+str(bezout(base,hill_m_det)[1])+')'} \equiv {str(abs(pgcd(base,hill_m_det)))} [{base}] \implies {str(hill_m_det) if hill_m_det >= 0 else hill_m_det} \\times {bezout(base,hill_m_det)[1] if bezout(base,hill_m_det)[1] >= 0 else '('+str(bezout(base,hill_m_det)[1])+')'} \equiv {str(abs(pgcd(base,hill_m_det)))} [{base}]$

    ${inverse_b}$

    ${alors_b}$

    - ${on_cherchons_inv} A = {begin_matrice} {hill_m[0][0]} & {hill_m[0][1]} \\\ {hill_m[1][0]} & {hill_m[1][1]} {end_matrice} \, {modulo_text} {base}$


    ${on_a} {a_inv_text} = {a_det_inv_text} \cdot {begin_matrice} {hill_m[1][1]} & {-hill_m[0][1]} \\\ {-hill_m[1][0]} & {hill_m[0][0]} {end_matrice} = {hill_m_det_inv} \cdot {begin_matrice} {hill_m[1][1]} & {-hill_m[0][1]} \\\ {-hill_m[1][0]} & {hill_m[0][0]} {end_matrice}$
    $= {begin_matrice} {hill_m_inv[0][0]} & {hill_m_inv[0][1]} \\\ {hill_m_inv[1][0]} & {hill_m_inv[1][1]} {end_matrice}$
    $= {begin_matrice} {hill_m_inv_modulo[0][0]} & {hill_m_inv_modulo[0][1]} \\\ {hill_m_inv_modulo[1][0]} & {hill_m_inv_modulo[1][1]} {end_matrice}[{base}]$


    $\implies {a_inv_text} = {begin_matrice} {hill_m_inv_modulo[0][0]} & {hill_m_inv_modulo[0][1]} \\\ {hill_m_inv_modulo[1][0]} & {hill_m_inv_modulo[1][1]} {end_matrice}[{base}]$
    """)