import streamlit as st


###############################################################################
###                                                                         ###
###                     Solution de l'exercice 1 du TD1                     ###
###                                                                         ###
###############################################################################
def solution_exercice1():
    st.markdown("""$\\text{Parmi les propositions, lesquelles sont vraies}$""")
    st.markdown("""1. $15 \equiv 7[8]:$ 
    >
    >   $\\text{On a: } 15  = 8 \\times 1 + 7 \implies 15 \equiv 7[8] \implies \\text{La proposition est vraie}$
    >    
    ---            
                """)
    st.markdown("""2. $99 \equiv -1[2]:$
    >
    >   $\\text{On a: } 99  = 100 - 1 = 2 \\times 50 - 1 \implies 99 \equiv -1[2] \implies \\text{La proposition est vraie}$
    >   
    ---            
                
                """)
    st.markdown("""3. $654 \equiv 0[3]:$ 
    >
    >   $\\text{On a: } 654  = 3 \\times 218 + 0 \implies 654 \equiv 0[3] \implies \\text{La proposition est vraie}$
    >     
    ---            
                        
                """)
    st.markdown("""4. $3 \equiv 3[3]:$
    >
    >   $\\text{On a: } 3  = 3 \\times 0 + 3 \implies 3 \equiv 3[3] \implies 3 \equiv 0[3] \implies \\text{La proposition est vraie}$
    >      
    ---            
                """)
    st.markdown("""5. $873 \equiv 555[5] \implies 318 \equiv 0[5]:$ 
    >
    >   $\\text{On a: } 318  = 5 \\times 63 + 3 \implies 318 \equiv 3[5] \\not\equiv  0[5] \implies \\text{La proposition est fausse}$
    >            
    ---            
                """)
    st.markdown("""6. $8704 \equiv 791[13] \implies 7913 \equiv 0[13]:$
    >
    >   $\\text{On a: } 7913  = 13 \\times 608 + 9 \implies 7913 \equiv 9[13] \\not\equiv  0[13] \implies \\text{La proposition est fausse}$
    >             
    
    ---            
                """)
    st.markdown("""7. $-8 \equiv 1[9]:$
    >
    >   $\\text{On a: } -8  = 9 \\times (-1) + 1 \implies -8 \equiv 1[9] \implies \\text{La proposition est vraie}$
    >  
    ---            
                """)
    st.markdown("""8. $-984 \equiv 17[19] \implies -1001 \equiv 0[19]:$
    >
    >   $\\text{On a: } -1001  = 19 \\times (-53) + 6 \implies -1001 \equiv 6[19] \\not\equiv  0[19] \implies \\text{La proposition est fausse}$
    > 
    ---            
                """)



###############################################################################
###                                                                         ###
###                     Solution de l'exercice 2 du TD1                     ###
###                                                                         ###
###############################################################################
def solution_exercice2():
    st.markdown("""$ \\text{Dans chacun des cas, on déterminons } x \\text{ modulo } n \\text{ (donnons un représentant dans } \Z/n\Z)$""")
    st.markdown("""1. $x = 555,\quad n = 12:$
    >
    > $\\text{On a: } \quad 555 = 12 \\times 46 + 3 \implies 555 \equiv 3[12]$
    >
    ---            
""")
    st.markdown("""2. $x = 983,\quad n = 45:$
    >
    > $\\text{On a: } \quad 983 = 45 \\times 22 - 7 \implies 983 \equiv -7[45] \implies 983 \equiv 38[45]$
    >
    ---            
""")
    st.markdown("""3. $x = 3078,\quad n = 487:$
    >
    > $\\text{On a: } \quad 3078 = 3000 + 78 = 500 \\times 6 + 78 = (487 + 13) \\times 6 + 78 = 487 \\times 6 + 13 \\times 6 + 78 = 487 \\times 6 + 78 + 78 = 487 \\times 6 + 156$
    > 
    > $\implies \quad 3078 \equiv 156[487]$
    >
    ---            
""")
    st.markdown("""4. $x = 573,\quad n = 159:$
    >
    > $\\text{On a: } \quad 573 = 159 \\times 3 + 96 \implies 573 \equiv 96[159] $
    >
    ---            
""")



###############################################################################
###                                                                         ###
###                     Solution de l'exercice 3 du TD1                     ###
###                                                                         ###
###############################################################################
def solution_exercice3():
    st.markdown("""#### $\\text{Simplifions les expressions suivantes:}$""")
    st.markdown("""1. $123^{122} \enspace modulo \enspace 124:$ 
    >
    > $\\text{On a: } \quad 123 = 124 \\times 1 - 1 \implies 123 \equiv -1[124]$
    >
    > $\implies \quad 123^{122} \equiv (-1)^{122}[124]$
    >
    > $\implies \quad 123^{122} \equiv 1[124]$
    >
    ---
                """)
    st.markdown("""2. $2014 \\times 2015\\times2016 \enspace modulo \enspace 2017:$
    >            
    > $\\text{On a:} \quad 2014 = 2017 \\times 1 - 3 \implies 2014 \equiv -3[2017]$            
    >            
    > $\\text{et:} \quad 2015 = 2017 \\times 1 - 2 \implies 2015 \equiv -2[2017]$          
    >            
    > $\\text{et:} \quad 2016 = 2017 \\times 1 - 1 \implies 2016 \equiv -1[2017]$           
    >            
    > $\\text{donc:} \quad 2014 \\times 2015\\times2016  \equiv (-3) \\times (-2) \\times (-1)[2017]$          
    >            
    > $\implies \quad 2014 \\times 2015\\times2016  \equiv -6[2017]$           
    >
    > $\implies \quad 2014 \\times 2015 \\times 2016 = 2017 \\times q -6$ 
    >
    > $\implies \quad 2014  \\times 2015 \\times 2016 = 2017 \\times (q-1) +2017 -6$ 
    >
    > $\implies \quad 2014  \\times 2015 \\times 2016 = 2017 \\times (q-1) +2011 $
    >            
    > $\implies \quad 2014 \\times 2015\\times2016  \equiv 2011[2017]$           
    >      
    ---      
                """)
    st.markdown("""3. $2792^{217} \enspace modulo \enspace 5:$
    > ##### Rappel:          Petit théorème de Fermat  
    > $\\text{Soient } p \\text{ un nombre premier, et } a \in \Z. \\text{ Alors } a^p \equiv a[p]\\text{. De plus, si } PGCD(a,p) = 1, \\text{ alors } a^{p-1} \equiv 1[p]$           
    >            
               
    >            
    >  $\\text{On a:} \quad 2792 = 5 \\times 558 + 2 \implies 2792 \equiv 2[5]$          
    >  $\\text{et:} \quad 5 = 2 \\times 2 +1$          
    >  $\\text{et:} \quad 2 = 1 \\times 2 + 0 \implies PGCD(2792,5) = 1 $
    >
    >  $\\text{D'après le petit téorième de Fermat on a:} \quad 2792^4 \equiv 1[5]$
    >
    >  $ \implies (2792^4)^{54} \equiv 1^{54}[5] \implies 2792^{216} \equiv 1[5]$
    >
    >  $ \implies 2792^{216} \\times 2792 \equiv 1 \\times 2[5] \implies 2792^{217} \equiv 2[5]$
    ---
                """)
    st.markdown("""4. $133^{39} \enspace modulo \enspace 10:$
    > $\\text{On a:} \quad 133 \equiv 3[10] \\text{ et } 133^2 \equiv 3^2[10] \implies 133^2 \equiv 9[10]$
    > 
    > $\\text{et: } \quad 133^3 \equiv 3^3[10] \implies 133^3 \equiv 27[10] \implies 133^3 \equiv 7[10] $
    >
    > $\\text{et: } \quad 133^3 \\times 133 \equiv 7 \\times 3 [10] \implies 133^4  \equiv 21 [10] \implies 133^4 \equiv 1 [10]$
    >
    > $\\text{donc} \quad (133^4)^9 \equiv 1^9 [10] \implies 133^{36} \equiv 1[10]$
    >
    > $\implies \quad 133^{36} \\times 133^3 \equiv 1 \\times 7 [10] \implies 133^{39} \equiv 7[10]$
    ---
                """)
    st.markdown("""5. $99^{100} \enspace modulo \enspace 42:$
    > $\\text{On a:} \quad 99 = 42 \\times 2 + 15 \implies 99 \equiv 15[42]$            
    >            
    > $\\text{et on a:} \quad 99^2 \equiv 15^2[42] \implies 99^2 \equiv 225[42]$           
    >            
    > $\\text{et on a:} \quad 225 = 42 \\times 5 + 15 \implies 225 \equiv 15[42] \implies 99^2 \equiv 15[42]$           
    >            
    > - $\\text{Montrons que } \\forall n \in \\N^* \quad 99^n \equiv 15[42]$:           
    >            
    >   - $\\text{On a }  \quad 99^1 \equiv 15[42]$
    >   - $\\text{Supposons que }  \quad 99^n \equiv 15[42]$        
    >   - $\\text{Montrons que }  \\forall (n+1) \in \\N^* \quad 99^{n+1} \equiv 15[42]$
    >     
    >       $\\text{On a:} \quad 99^n \equiv 15[42] \implies 99^n \\times 99 \equiv 15 \\times 15[42]$     
    >     
    >       $\implies \quad 99^{n+1} \equiv 225[42] \implies 99^{n+1} \equiv 15[42]$     
    >     
    >       $\\text{Donc } \\forall (n+1) \in \\N^*; \quad 99^{n+1} \equiv 15 [42]$ 
    >         
    > $\\text{Alors } \quad \\forall n \in \\N^*; \quad 99^n \equiv 15[42]$    
    >     
    > $\implies 99^{100} \equiv 15[42]$  
    ---  
    """)
    st.markdown("""6. $2^{1147} \enspace modulo \enspace 17:$
    >            
    > $\\text{On a:} \quad 2^4 = 16 \equiv -1[17] \quad \\text{et } \quad 2^3 \equiv 8[17]$            
    >            
    > $\implies \quad (2^4)^{286} \equiv (-1)^{286}[17] \implies \quad 2^{1144} \equiv 1[17]$           
    >            
    > $\implies \quad 2^{1144} \\times 2^3 \equiv 1 \\times 8 [17] \implies 2^{1147} \equiv 8[17]$           
    >
    ---            
                """)



###############################################################################
###                                                                         ###
###                     Solution de l'exercice 4 du TD1                     ###
###                                                                         ###
###############################################################################
def solution_exercice4():
    solution_exercice4_col_1,solution_exercice4_col_2,solution_exercice4_col_3,solution_exercice4_col_4 = st.columns([1,4,4,1])
    with solution_exercice4_col_2:
        st.markdown("""
                    $ \\text{La table d'addition de }\\Z/7\\Z:$

|$+$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|                   
|$\dot{0}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|
|$\dot{1}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{0}$|
|$\dot{2}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{0}$|$\dot{1}$|
|$\dot{3}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|
|$\dot{4}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|
|$\dot{5}$|$\dot{5}$|$\dot{6}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|
|$\dot{6}$|$\dot{6}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|
""")
    with solution_exercice4_col_3:
        st.markdown("""
                    $ \\text{La table de multiplication de }\\Z/7\\Z:$

|$\\times$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|                   
|$\dot{0}$|$\dot{0}$|$\dot{0}$|$\dot{0}$|$\dot{0}$|$\dot{0}$|$\dot{0}$|$\dot{0}$|
|$\dot{1}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|
|$\dot{2}$|$\dot{0}$|$\dot{2}$|$\dot{4}$|$\dot{6}$|$\dot{1}$|$\dot{3}$|$\dot{5}$|
|$\dot{3}$|$\dot{0}$|$\dot{3}$|$\dot{6}$|$\dot{2}$|$\dot{5}$|$\dot{1}$|$\dot{4}$|
|$\dot{4}$|$\dot{0}$|$\dot{4}$|$\dot{1}$|$\dot{5}$|$\dot{2}$|$\dot{6}$|$\dot{3}$|
|$\dot{5}$|$\dot{0}$|$\dot{5}$|$\dot{3}$|$\dot{1}$|$\dot{6}$|$\dot{4}$|$\dot{2}$|
|$\dot{6}$|$\dot{0}$|$\dot{6}$|$\dot{5}$|$\dot{6}$|$\dot{3}$|$\dot{2}$|$\dot{1}$|
""")
        


###############################################################################
###                                                                         ###
###                     Solution de l'exercice 5 du TD1                     ###
###                                                                         ###
###############################################################################
def solution_exercice5():
    solution_exercice5_col_1,solution_exercice5_col_2,solution_exercice5_col_3,solution_exercice5_col_4 = st.columns([1,4,4,1])
    with solution_exercice5_col_2:
        st.markdown("""
                    $ \\text{La table d'addition de }\\Z/8\\Z:$

|$+$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{7}$|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|                 
|$\dot{0}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{7}$|
|$\dot{1}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{7}$|$\dot{0}$|
|$\dot{2}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{7}$|$\dot{0}$|$\dot{1}$|
|$\dot{3}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{7}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|
|$\dot{4}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{7}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|
|$\dot{5}$|$\dot{5}$|$\dot{6}$|$\dot{7}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|
|$\dot{6}$|$\dot{6}$|$\dot{7}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|
|$\dot{7}$|$\dot{7}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|
""")
    with solution_exercice5_col_3:
        st.markdown("""
$ \\text{La table de multiplication de }\\Z/8\\Z:$                    

|$\\times$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{7}$|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|                   
|$\dot{0}$|$\dot{0}$|$\dot{0}$|$\dot{0}$|$\dot{0}$|$\dot{0}$|$\dot{0}$|$\dot{0}$|$\dot{0}$|
|$\dot{1}$|$\dot{0}$|$\dot{1}$|$\dot{2}$|$\dot{3}$|$\dot{4}$|$\dot{5}$|$\dot{6}$|$\dot{7}$|
|$\dot{2}$|$\dot{0}$|$\dot{2}$|$\dot{4}$|$\dot{6}$|$\dot{0}$|$\dot{2}$|$\dot{4}$|$\dot{6}$|
|$\dot{3}$|$\dot{0}$|$\dot{3}$|$\dot{6}$|$\dot{1}$|$\dot{4}$|$\dot{7}$|$\dot{2}$|$\dot{5}$|
|$\dot{4}$|$\dot{0}$|$\dot{4}$|$\dot{0}$|$\dot{4}$|$\dot{0}$|$\dot{4}$|$\dot{0}$|$\dot{4}$|
|$\dot{5}$|$\dot{0}$|$\dot{5}$|$\dot{2}$|$\dot{7}$|$\dot{4}$|$\dot{1}$|$\dot{6}$|$\dot{3}$|
|$\dot{6}$|$\dot{0}$|$\dot{6}$|$\dot{4}$|$\dot{2}$|$\dot{0}$|$\dot{6}$|$\dot{4}$|$\dot{2}$|
|$\dot{7}$|$\dot{0}$|$\dot{7}$|$\dot{6}$|$\dot{5}$|$\dot{4}$|$\dot{3}$|$\dot{2}$|$\dot{1}$|
""")



###############################################################################
###                                                                         ###
###                     Solution de l'exercice 6 du TD1                     ###
###                                                                         ###
###############################################################################
def solution_exercice6():
    st.markdown("""$ \\text{On cryptons le mot MATHEMATIQUES par la méthode de César par paquet de 1 avec 19 comme clef:}$
<center>
                
|$x \longrightarrow$|$M$|$A$|$T$|$H$|$E$|$M$|$A$|$T$|$I$|$Q$|$U$|$E$|$S$|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|$\\Z/26\\Z$|$12$|$0$|$19$|$7$|$4$|$12$|$0$|$19$|$8$|$16$|$20$|$4$|$18$|
|$+19$|$31$|$19$|$38$|$26$|$23$|$31$|$19$|$38$|$27$|$35$|$39$|$23$|$37$|
|$\\Z/26\\Z$|$5$|$19$|$12$|$0$|$23$|$5$|$19$|$12$|$1$|$9$|$13$|$23$|$11$|
|$Cr(x) \longrightarrow$|$F$|$T$|$M$|$A$|$X$|$F$|$T$|$M$|$B$|$J$|$N$|$X$|$L$|

</center>
<br>
                
$\\text{Le message crypté du mot MATHEMATIQUES par la méthode de César par paquet de 1 avec 19 comme clef est: FTMAXFTMBJNXL}$
""",unsafe_allow_html=True)



###############################################################################
###                                                                         ###
###                     Solution de l'exercice 7 du TD1                     ###
###                                                                         ###
###############################################################################
def solution_exercice7():
    st.markdown("""$ \\text{On cryptons le mot ZEBRE par la méthode de César par paquet de 1 avec 25 comme clef.}$
<center>
                
|$x \longrightarrow$|$Z$|$E$|$B$|$R$|$E$|
|:---:|:---:|:---:|:---:|:---:|:---:|
|$\\Z/26\\Z$|$25$|$4$|$1$|$17$|$4$|
|$+25$|$50$|$29$|$26$|$42$|$29$|
|$\\Z/26\\Z$|$24$|$3$|$0$|$16$|$3$|
|$Cr(x) \longrightarrow$|$Y$|$D$|$A$|$Q$|$D$|

</center>
<br>
                
$\\text{Le message crypté du mot ZEBRE par la méthode de César par paquet de 1 avec 25 comme clef est: YDAQD}$
""",unsafe_allow_html=True)


###############################################################################
###                                                                         ###
###                     Solution de l'exercice 8 du TD1                     ###
###                                                                         ###
###############################################################################
def solution_exercice8():
    st.markdown("""$ \\text{On cryptons le message VIVELACRYPTO par la méthode de César par paquet de 3 avec 190091 comme clef.}$
<center>
                
|$x \longrightarrow$| $VIV$ | $ELA$ | $CRY$ | $PTO$ |
|:---:|:---:|:---:|:---:|:---:|
|$\\Z/252526\\Z$|$210821$|$041100$|$021724$|$151914$|
|$+190091$|$400912$|$231191$|$211815$|$342005$|
|$\\Z/252526\\Z$|$148386$|$231191$|$211815$|$89479$|
|$Cr(x) \longrightarrow$|$148386$|$231191$|$211815$|$89479$|
</center>
<br>
                
$\\text{Le message crypté du mot VIVELACRYPTO par la méthode de César par paquet de 3 avec 190091 comme clef est: 148386-231191-211815-89479}$
""",unsafe_allow_html=True)


###############################################################################
###                                                                         ###
###                     Solution de l'exercice 9 du TD1                     ###
###                                                                         ###
###############################################################################
def solution_exercice9():
    st.markdown("""$ \\text{On a utilisé la méthode de César par paquet de 1 avec 25 comme clef pour obtenir BDRSBGZTCBZAQTKD. On cherchons le message original ?}$
<center>

|$y \longrightarrow$|$B$|$D$|$R$|$S$|$B$|$G$|$Z$|$T$|$C$|$B$|$Z$|$A$|$Q$|$T$|$K$|$D$|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|$\\Z/26\\Z$|$1$|$3$|$17$|$18$|$1$|$6$|$25$|$19$|$2$|$1$|$25$|$0$|$16$|$19$|$10$|$3$|
|$-25$|$-24$|$-22$|$-8$|$-7$|$-24$|$-19$|$0$|$-6$|$-23$|$-24$|$0$|$-25$|$-9$|$-6$|$-15$|$-22$|
|$\\Z/26\\Z$|$2$|$4$|$18$|$19$|$2$|$7$|$0$|$20$|$3$|$2$|$0$|$1$|$17$|$20$|$11$|$4$|
|$Dc(y) \longrightarrow$|$C$|$E$|$S$|$T$|$C$|$H$|$A$|$U$|$D$|$C$|$A$|$B$|$R$|$U$|$L$|$E$| 

</center>
<br>              

$\\text{Le message original est : C'est chaud ça brule}$
""",unsafe_allow_html=True)



###############################################################################
###                                                                         ###
###                     Solution de l'exercice 10 du TD1                    ###
###                                                                         ###
###############################################################################
def solution_exercice10():
    st.markdown(""" $\\text{On a utilisé la méthode de César par paquet de 3 avec 250025 comme clef pour obtenir 208907-107501-39318-48312-77499. On cherchons le message original ?}$
<center>
                
|$y \longrightarrow$|$208907$|$107501$|$39318$|$48312$|$77499$|
|:---:|:---:|:---:|:---:|:---:|:---:|
|$-250025$|$-41118$|$-142524$|$-210707$|$-211713$|$-172526$|
|$\\Z/252526\\Z$|$211408$|$110002$|$41819$|$50813$|$80000$|
||$21-14-08$|$11-00-02$|$04-18-19$|$05-08-13$|$08-00-00$|
|$Dc(y) \longrightarrow$|$VOI$|$LAC$|$EST$|$FIN$|$IAA$|

</center>
<br>              

$\\text{Le message original est : Voilà c'est fini}$
""",unsafe_allow_html=True)



###############################################################################
###                                                                         ###
###                     Solution de l'exercice 11 du TD1                    ###
###                                                                         ###
###############################################################################
def solution_exercice11():
    pass