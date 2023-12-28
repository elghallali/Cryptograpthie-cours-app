import streamlit as st

###############################################################################
###                                                                         ###
###                     Solution de l'exercice 1 du TD3                     ###
###                                                                         ###
###############################################################################
def solution_exercice1():
    st.markdown("""
    $\\text{Soit } A= \\begin{pmatrix} 1 & 2 \\\ 0 & -1 \end{pmatrix},$ 
    $B= \\begin{pmatrix} -1 & 1 \\\ 5 & 0 \end{pmatrix} $ $\enspace \\text{et} \enspace$
    $C=\\begin{pmatrix} 6 & 3 \\\ 3 & 1 \end{pmatrix} $
    $\\text{ des matrices de }$ $ \mathcal{M}_2(\Z/26\Z)$.
  
$1. \\text{ Calculer } A + B, \quad A \\times C \quad \\text{et} \quad B \\times C$
> - $\\text{ On calculons} \enspace A + B:$
> 
> $\qquad \quad A + B \equiv_{26} $
$\\begin{pmatrix} 1 & 2 \\\ 0 & -1 \end{pmatrix} + $ $\\begin{pmatrix} -1 & 1 \\\ 5 & 0 \end{pmatrix}  \equiv_{26} $
$\\begin{pmatrix} 0 & 3 \\\ 5 & -1 \end{pmatrix} \equiv_{26}$
$\\begin{pmatrix} 0 & 3 \\\ 5 & 25 \end{pmatrix}$
> 
> $\!$
>                
> - $\\text{ On calculons} \enspace A \\times C:$
> 
> $\qquad \quad A \\times C \equiv_{26} $
$\\begin{pmatrix} 1 & 2 \\\ 0 & -1 \end{pmatrix} \\times \\begin{pmatrix} 6 & 3 \\\ 3 & 1 \end{pmatrix} \equiv_{26} $ 
$\\begin{pmatrix} 1 \\times 6 + 2 \\times 3 & 1 \\times 3 + 2 \\times 1 \\\ 0 \\times 6 + (-1) \\times 3 & 0 \\times 3 + (-1) \\times 1 \end{pmatrix} \equiv_{26} $
$\\begin{pmatrix} 12 & 5 \\\ -3 & -1 \end{pmatrix}\equiv_{26}$
$\\begin{pmatrix} 12 & 5 \\\ 23 & 25 \end{pmatrix}$
> 
> $\!$
> 
> - $\\text{ On calculons} \enspace B \\times C:$
> 
> $\qquad \quad B \\times C \equiv_{26} $
$\\begin{pmatrix} -1 & 1 \\\ 5 & 0 \end{pmatrix} \\times \\begin{pmatrix} 6 & 3 \\\ 3 & 1 \end{pmatrix} \equiv_{26} $
$\\begin{pmatrix} -1 \\times 6 + 1 \\times 3 & -1 \\times 3 + 1 \\times 1 \\\ 5 \\times 6 + 0 \\times 3 & 5 \\times 3 + 0 \\times 1 \end{pmatrix} \equiv_{26} $
$\\begin{pmatrix} -3 & -2 \\\ 30 & 15 \end{pmatrix} \equiv_{26}$
$\\begin{pmatrix} 23 & 24 \\\ 4 & 15 \end{pmatrix}$
>
> $\!$
> 
                                              
$2. \\text{ On comparons } (A + B) \\times C \quad \\text{et} \quad A \\times C + B \\times C$ 
>                 
> - $\\text{ On calculons} \enspace (A + B) \\times C:$
>                 
> $\qquad \quad (A + B) \\times C \equiv_{26} $
$\\begin{pmatrix} 0 & 3 \\\ 5 & -1 \end{pmatrix} \\times \\begin{pmatrix} 6 & 3 \\\ 3 & 1 \end{pmatrix} \equiv_{26}$
$\\begin{pmatrix} 0 \\times 6 + 3 \\times 3 & 0 \\times 3 + 3 \\times 1 \\\ 5 \\times 6 + (-1) \\times 3 & 5 \\times 3 + (-1) \\times 1 \end{pmatrix} \equiv_{26} $
$\\begin{pmatrix} 9 & 3 \\\ 27 & 14 \end{pmatrix} \equiv_{26}$
$\\begin{pmatrix} 9 & 3 \\\ 1 & 14 \end{pmatrix}$                              
>                 
> $\!$                
>                 
>                 
> - $\\text{ On calculons} \enspace A \\times C + B \\times C:$
>                 
> $\qquad \quad A \\times C + B \\times C \equiv_{26} $
$\\begin{pmatrix} 12 & 5 \\\ -3 & -1 \end{pmatrix} + \\begin{pmatrix} -3 & -2 \\\ 30 & 15 \end{pmatrix} \equiv_{26} $
$\\begin{pmatrix} 9 & 3 \\\ 27 & 14 \end{pmatrix} \equiv_{26}$
$\\begin{pmatrix} 9 & 3 \\\ 1 & 14 \end{pmatrix}$
>  
> $\!$
> 
> - $\\text{La comparaison: }$                            
>                               
>  $\qquad \quad (A + B) \\times C =  A \\times C + B \\times C$                             
>                               
> $\!$
>                               
$3. \\text{ On Comparons le résultat précédent avec } C \\times (A + B)$ 
>                 
> - $\\text{ On calculons} \enspace C \\times (A + B):$
>                 
> $\qquad \quad C \\times (A + B) \equiv_{26} $
$\\begin{pmatrix} 6 & 3 \\\ 3 & 1 \end{pmatrix} \\times \\begin{pmatrix} 0 & 3 \\\ 5 & -1 \end{pmatrix} \equiv_{26}$
$\\begin{pmatrix} 6 \\times 0 + 3 \\times 5 & 6 \\times 3 + 3 \\times (-1) \\\ 3 \\times 0 + 1 \\times 5 & 3 \\times 3 + 1 \\times (-1) \end{pmatrix} \equiv_{26} $
$\\begin{pmatrix} 15 & 15 \\\ 5 & 8 \end{pmatrix}$                               
>                 
> $\!$                
>  
> - $\\text{La comparaison: }$                            
>  
>  $\qquad \quad C \\times (A + B) \\not = (A + B) \\times C$
>  
                               
""")

###############################################################################
###                                                                         ###
###                     Solution de l'exercice 2 du TD3                     ###
###                                                                         ###
###############################################################################
def solution_exercice2():
    st.markdown("""##### $\\text{Calculer le déterminant de chacune des }$ $\\text{matrices suivantes. Identifier les matrices }$ $\\text{de } \mathbf{GL_2}(\\Z/26\\Z).$
> ###### $1. \quad A= \\begin{pmatrix} 11 & 3 \\\ 2 & -5 \end{pmatrix}:$
>                
> $\qquad \quad det(A)= \\begin{vmatrix} 11 & 3 \\\ 2 & -5 \end{vmatrix} =$
$11 \\times (-5) - 3 \\times 2 \enspace \equiv_{26} \enspace -61 \enspace \equiv_{26} \enspace 17$
>
>
>---
>
> ###### $2. \quad B= \\begin{pmatrix} 3 & 1 \\\ 4 & 6 \end{pmatrix}:$
>
> $\qquad \quad det(B)= \\begin{vmatrix} 3 & 1 \\\ 4 & 6 \end{vmatrix} =$
$3 \\times 6 - 4 \\times 1 \enspace \equiv_{26} \enspace 14$
>
>
>---
>
> ###### $3. \quad C=\\begin{pmatrix} 1 & -5 \\\ -1 & 8 \end{pmatrix}:$
>
> $\qquad \quad det(C)= \\begin{vmatrix} 1 & -5 \\\ -1 & 8 \end{vmatrix} =$
$1 \\times 8 - (-5) \\times (-1) \enspace \equiv_{26} \enspace 3$
>
>---
>
> ###### $4. \quad D=\\begin{pmatrix} 1 & -5 \\\ 1 & 8 \end{pmatrix}:$
>
> $\qquad \quad det(D)= \\begin{vmatrix} 1 & -5 \\\ 1 & 8 \end{vmatrix} =$
$1 \\times 8 - (-5) \\times 1 \enspace \equiv_{26} \enspace 13$
>
>
>---
>
> ###### $5. \quad E= \\begin{pmatrix} 1 & 2 \\\ 3 & 5 \end{pmatrix}:$
>
> $\qquad \quad det(E)= \\begin{vmatrix} 1 & 2 \\\ 3 & 5 \end{vmatrix}=$
$1 \\times 5 - 2 \\times 3 \enspace \equiv_{26} \enspace -1 \enspace \equiv_{26} \enspace 25$
>
>
>---
>
> ###### $6. \quad F=\\begin{pmatrix} 12 & 13 \\\ 11 & 10 \end{pmatrix}:$
>
> $\qquad \quad det(F)= \\begin{vmatrix} 12 & 13 \\\ 11 & 10 \end{vmatrix} = $
$12 \\times 10 - 13 \\times 11 \enspace \equiv_{26} \enspace -23 \enspace \equiv_{26} \enspace 3$
>
>
>
>---
>
> ###### $7. \quad G=\\begin{pmatrix} 1 & -1 \\\ -1 & 1 \end{pmatrix}:$
> 
> $\qquad \quad det(G)= \\begin{vmatrix} 1 & -1 \\\ -1 & 1 \end{vmatrix} = $
$1 \\times 1 - (-1) \\times (-1) \enspace \equiv_{26} \enspace 0$
>
>
>---
>
> ###### $8. \quad H=\\begin{pmatrix} 4 & 3 \\\ 2 & 1 \end{pmatrix}:$
> 
> $\qquad \quad det(H)= \\begin{vmatrix} 4 & 3 \\\ 2 & 1 \end{vmatrix} = $
$4 \\times 1 - 3 \\times 2 \enspace \equiv_{26} \enspace -2 \enspace \equiv_{26} \enspace 24$
>
>
>---
>
> ###### $9. \quad I=\\begin{pmatrix} 0 & -1 \\\ 1 & 0 \end{pmatrix}:$
> 
> $\qquad \quad det(I)= \\begin{vmatrix} 0 & -1 \\\ 1 & 0 \end{vmatrix} = $
$0 \\times 0 - (-1) \\times 1 \enspace \equiv_{26} \enspace 1$
> 
>--- 
> 
> 
> ##### $\\text{Les matrices de } \mathbf{GL_2}(\\Z/26\\Z) \enspace \\text{sont }:$ $A, C, E, F, I$
> 
> 
> 
""")

###############################################################################
###                                                                         ###
###                     Solution de l'exercice 3 du TD3                     ###
###                                                                         ###
###############################################################################
def solution_exercice3():
    st.markdown("""
$\\text{Pour chacune des matrices de } \mathbf{GL_2}(\\Z/26\\Z) \enspace$
$\\text{de l'exercice 2, On donnons la matrice inverse }$
$\\text{(modulairement).}$
>
> ###### $1. \quad A= \\begin{pmatrix} 11 & 3 \\\ 2 & -5 \end{pmatrix}:$
>
> - $det(A) \equiv_{26} \enspace 17 \implies \quad det(A)^{-1} \equiv_{26} \enspace 23$
>
> - $A^{-1} \enspace \equiv_{26} \enspace det(A)^{-1} \cdot \\begin{pmatrix} -5 & -3 \\\ -2 & 11 \end{pmatrix} \enspace$
$\equiv_{26} \enspace 23 \\times \\begin{pmatrix} -5 & -3 \\\ -2 & 11 \end{pmatrix} \enspace$
$\equiv_{26} \enspace \\begin{pmatrix} 23 \\times (-5) & 23 \\times (-3) \\\ 23 \\times (-2) & 23 \\times 11 \end{pmatrix} \enspace$
$\equiv_{26} \enspace \\begin{pmatrix} -115 & -69 \\\ -46 & 253 \end{pmatrix} \enspace$
>
> $\qquad \quad \\text{Donc} \enspace A^{-1} \enspace \equiv_{26} \enspace \\begin{pmatrix} 15 & 9 \\\ 6 & 7 \end{pmatrix}$
>
>---
>
>
> 
>
> ###### $2. \quad C=\\begin{pmatrix} 1 & -5 \\\ -1 & 8 \end{pmatrix}:$
>
>
> - $det(C) \equiv_{26} \enspace 3 \implies \quad det(C)^{-1} \equiv_{26} \enspace 9$
>
> - $C^{-1} \enspace \equiv_{26} \enspace det(C)^{-1} \cdot \\begin{pmatrix} 8 & 5 \\\ 1 & 1 \end{pmatrix} \enspace$
$\equiv_{26} \enspace 9 \\times \\begin{pmatrix} 8 & 5 \\\ 1 & 1 \end{pmatrix} \enspace$
$\equiv_{26} \enspace \\begin{pmatrix} 9 \\times 8 & 9 \\times 5 \\\ 9 \\times 1 & 9 \\times 1 \end{pmatrix} \enspace$
$\equiv_{26} \enspace \\begin{pmatrix} 72 & 45 \\\ 9 & 9 \end{pmatrix} \enspace$
>
> $\qquad \quad \\text{Donc} \enspace C^{-1} \enspace \equiv_{26} \enspace \\begin{pmatrix} 20 & 19 \\\ 9 & 9 \end{pmatrix}$
>
>
>---
> ###### $3. \quad E= \\begin{pmatrix} 1 & 2 \\\ 3 & 5 \end{pmatrix}:$
>
> - $det(E) \enspace \equiv_{26} \enspace 25 \implies \quad det(E)^{-1} \equiv_{26} \enspace 25$
>
> - $E^{-1} \enspace \equiv_{26} \enspace det(E)^{-1} \cdot \\begin{pmatrix} 5 & -2 \\\ -3 & 1 \end{pmatrix} \enspace$
$\equiv_{26} \enspace 25 \\times \\begin{pmatrix} 5 & -2 \\\ -3 & 1 \end{pmatrix} \enspace$
$\equiv_{26} \enspace \\begin{pmatrix} 25 \\times 5 & 25 \\times (-2) \\\ 25 \\times (-3) & 25 \\times 1 \end{pmatrix} \enspace$
$\equiv_{26} \enspace \\begin{pmatrix} 125 & -50 \\\ -75 & 25 \end{pmatrix} \enspace$
>
> $\qquad \quad \\text{Donc} \enspace E^{-1} \enspace \equiv_{26} \enspace \\begin{pmatrix} 21 & 2 \\\ 3 & 25 \end{pmatrix}$
>
>
>---
> ###### $4. \quad F=\\begin{pmatrix} 12 & 13 \\\ 11 & 10 \end{pmatrix}:$
>
> - $det(F) \enspace \equiv_{26} \enspace 3 \implies \quad det(F)^{-1} \equiv_{26} \enspace 9$
>
> - $F^{-1} \enspace \equiv_{26} \enspace det(F)^{-1} \cdot \\begin{pmatrix} 10 & -13 \\\ -11 & 12 \end{pmatrix}$
$\enspace \equiv_{26} \enspace 9 \\times \\begin{pmatrix} 10 & -13 \\\ -11 & 12 \end{pmatrix}$
$\enspace \equiv_{26} \enspace \\begin{pmatrix} 9 \\times 10 & 9 \\times (-13) \\\ 9 \\times (-11) & 9 \\times 12 \end{pmatrix}$
$\enspace \equiv_{26} \enspace \\begin{pmatrix} 90 & -117 \\\ -99 & 108 \end{pmatrix}$
>
> $\qquad \quad \\text{Donc} \enspace F^{-1} \enspace \equiv_{26} \enspace \\begin{pmatrix} 12 & 13 \\\ 5 & 4 \end{pmatrix}$
>
>
>---
> ###### $5. \quad I=\\begin{pmatrix} 0 & -1 \\\ 1 & 0 \end{pmatrix}:$
>
> - $det(I) \enspace \equiv_{26} \enspace 1 \implies \quad det(I)^{-1} \equiv_{26} \enspace 1$
>
> - $I^{-1} \enspace \equiv_{26} \enspace det(I)^{-1} \cdot \\begin{pmatrix} 0 & 1 \\\ -1 & 0 \end{pmatrix} \enspace$
$\equiv_{26} \enspace 1 \\times \\begin{pmatrix} 0 & 1 \\\ -1 & 0 \end{pmatrix} \enspace$
$\equiv_{26} \enspace \\begin{pmatrix} 0 & 1 \\\ -1 & 0 \end{pmatrix}$
>
> $\qquad \quad \\text{Donc} \enspace I^{-1} \enspace \equiv_{26} \enspace \\begin{pmatrix} 0 & 1 \\\ 25 & 0 \end{pmatrix}$
""")

###############################################################################
###                                                                         ###
###                     Solution de l'exercice 4 du TD3                     ###
###                                                                         ###
###############################################################################
def solution_exercice4():
    pass

###############################################################################
###                                                                         ###
###                     Solution de l'exercice 5 du TD3                     ###
###                                                                         ###
###############################################################################
def solution_exercice5():
    pass

###############################################################################
###                                                                         ###
###                     Solution de l'exercice 6 du TD3                     ###
###                                                                         ###
###############################################################################
def solution_exercice6():
    pass

###############################################################################
###                                                                         ###
###                     Solution de l'exercice 7 du TD3                     ###
###                                                                         ###
###############################################################################
def solution_exercice7():
    pass

###############################################################################
###                                                                         ###
###                     Solution de l'exercice 8 du TD3                     ###
###                                                                         ###
###############################################################################
def solution_exercice8():
    pass