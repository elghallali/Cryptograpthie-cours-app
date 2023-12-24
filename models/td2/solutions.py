import streamlit as st

def solution_exercice1():
    st.markdown("""$\\text{Pour chacun des entiers } a\\text{, on déterminons } D(a) \\text{ l'ensemble des diviseurs positifs de }a.$""")
    st.markdown("""$1. \quad a = 99$

<div style="display: grid; grid-template-columns: auto auto;">
    <div style="padding-right: 5px; text-align: end;">
        <span>99</span>
        <br>
        <span>33</span>
        <br>
        <span>11</span>
        <br>
        <span>1</span>
        <br>
    </div>
    <div style="border-left: 4px solid red; padding-left: 5px; text-align: start;">
        <span>3</span>
        <br>
        <span>3</span>
        <br>
        <span>11</span>
        <br>
    </div>
</div>
                
$\\text{On a:} \quad 99 = 3^2 \\times 11$
                
$\implies \quad D(99) = \{1,3,9,11,33,99\}$

---             
                """,unsafe_allow_html=True)
    st.markdown("""$2. \quad a = 1069$
>
> $\\text{Dans la pratique, on doit chercher un diviseur de } n \\text{   parmi les nombres premiers successifs (2, 3, 5, 7, 11 …) jusqu'à la valeur } \sqrt{1069}=32.69 $
>                 
> $Si \quad  p | 1069 \implies p \in \{2, 3, 5,7,11,13,17,19,23,29,31\}$
>                
> -  $9 = 2 \\times 4 + 1 =2k +1 \\not = 2k \implies p \\not = 2 $
> - $ 1 + 0 + 6 + 9 = 16 \quad et \quad 1 + 6 = 7 \\not = 3,6 \\text{ ou } 9 \implies p \\not = 3$
> - $9 \\not = 0 \quad et \quad 9 \\not = 5 \implies p \\not = 5$
> - $1069 = 7 \\times 152 + 5 \implies p \\not = 7$
> - $1069 = 11 \\times 97 + 2 \implies p \\not = 11$
> - $1069 = 13 \\times 82 + 3 \implies p \\not = 13$
> - $1069 = 17 \\times 62 + 15 \implies p \\not = 17$
> - $1069 = 19 \\times 56 + 5 \implies p \\not = 19$
> - $1069 = 23 \\times 46 + 11 \implies p \\not = 23$
> - $1069 = 29 \\times 46 + 25 \implies p \\not = 29$
> - $1069 = 31 \\times 34 + 15 \implies p \\not = 31$
> 
> $\\text{Donc: } \quad p \\not \in \{2, 3, 5,7,11,13,17,19,23,29,31\}$
>                 
> $\\text{Alors: 1069 est un nombre premier} \implies D(1069) =\{1,1069 \}$
>                 
---             
                """,unsafe_allow_html=True)
    st.markdown("""$3. \quad a = 3742$
                
<div style="display: grid; grid-template-columns: auto auto;">
    <div style="padding-right: 5px; text-align: end;">
        <span>3742</span>
        <br>
        <span>1871</span>
        <br>
        <span>1</span>
        <br>
    </div>
    <div style="border-left: 4px solid red; padding-left: 5px; text-align: start;">
        <span>2</span>
        <br>
        <span>1871</span>
        <br>
    </div>
</div>

>
> $3742 = 2 \\times 1871$
>
> $\\text{ donc: } \quad D(3742) =\{1,2,1871,3742 \}$
>                
---
""",unsafe_allow_html=True)
    st.markdown("""$4. \quad a = 6725$
                
<div style="display: grid; grid-template-columns: auto auto;">
    <div style="padding-right: 5px; text-align: end;">
        <span>6725</span>
        <br>
        <span>1345</span>
        <br>
        <span>269</span>
        <br>
        <span>1</span>
        <br>
    </div>
    <div style="border-left: 4px solid red; padding-left: 5px; text-align: start;">
        <span>5</span>
        <br>
        <span>5</span>
        <br>
        <span>269</span>
        <br>
    </div>
</div>

>
> $6725 = 5^2 \\times 269 $
>
> $D(6725) = \{ 1, 5, 25, 269, 1345, 6725\}$

---              
                """,unsafe_allow_html=True)

    st.markdown("""$5. \quad a = 684$
                
<div style="display: grid; grid-template-columns: auto auto;">
    <div style="padding-right: 5px; text-align: end;">
        <span>684</span>
        <br>
        <span>342</span>
        <br>
        <span>171</span>
        <br>
        <span>57</span>
        <br>
        <span>19</span>
        <br>
        <span>1</span>
        <br>
    </div>
    <div style="border-left: 4px solid red; padding-left: 5px; text-align: start;">
        <span>2</span>
        <br>
        <span>2</span>
        <br>
        <span>3</span>
        <br>
        <span>3</span>
        <br>
        <span>19</span>
        <br>
    </div>
</div>
                
>
> $684 = 2^2 \\times 3^2 \\times 19$
>
> $D(684) = \{1, 2, 3, 4, 6, 9, 12, 18, 19, 36, 38, 57, 76, 114, 171, 228, 342, 684 \}$
>

""",unsafe_allow_html=True)

    

def solution_exercice2():
    st.markdown("""$\\text{Dans chacun des cas suivant, On appliquons l'algorithme d'Euclide pour déterminer le PGCD de A et B.}$""")
    st.markdown("""$1. \quad A = 540, \quad B = 256$

>                                
> |$A$|$B$|$r$|$q$||$u$|$v$|
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> |$540$|$256$|$28$|$2$||$-9$|$19$|
> |$256$|$28$|$\colorbox{aqua}{4}$|$9$||$1$|$-9$|
> |$28$|$4$|$0$|$7$||$0$|$1$|
> 
> $\\negthinspace$
> 
> $\\text{Donc le } PGCD(540,256) = 4 $
> 
                
---
""",unsafe_allow_html=True)
    st.markdown("""$2. \quad A = 561, \quad B = 187$

>                                 
> |$A$|$B$|$r$|$q$||$u$|$v$|
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> |$561$|$\colorbox{aqua}{187}$|$0$|$3$||$0$|$1$|
>
> $\\negthinspace$
> 
> $\\text{Donc le } PGCD(561,187) = 187 $
> 
                                
---
""",unsafe_allow_html=True)
    st.markdown("""$3. \quad A = 982, \quad B = 1000$

>                                 
> |$A$|$B$|$r$|$q$||$u$|$v$|
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> |$982$|$1000$|-|-||-|-|
> |$1000$|$982$|$18$|$1$||$-109$|$111$|
> |$982$|$18$|$10$|$54$||$2$|$-109$|
> |$18$|$10$|$8$|$1$||$-1$|$2$|
> |$10$|$8$|$\colorbox{aqua}{2}$|$1$||$1$|$-1$|
> |$8$|$2$|$0$|$4$||$0$|$1$|
> 
> $\\negthinspace$
> 
> $\\text{Donc le } PGCD(982,1000) = 2 $
> 

                
---
""",unsafe_allow_html=True)
    st.markdown("""$4. \quad A = 998, \quad B = 47$

>                                 
> |$A$|$B$|$r$|$q$||$u$|$v$|
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> |$998$|$47$|$11$|$21$||$-17$|$361$|
> |$47$|$11$|$3$|$4$||$4$|$-17$|
> |$11$|$3$|$2$|$3$||$-1$|$4$|
> |$3$|$2$|$\colorbox{aqua}{1}$|$1$||$1$|$-1$|
> |$2$|$1$|$0$|$2$||$0$|$1$|
> 
> $\\negthinspace$
> 
> $\\text{Donc le } PGCD(998,47) = 1 $
> 

---
""",unsafe_allow_html=True)
    st.markdown("""$5. \quad A = 5742, \quad B = 1320$

>                                 
> |$A$|$B$|$r$|$q$||$u$|$v$|
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> |$5742$|$1320$|$462$|$4$||$3$|$13$|
> |$1320$|$462$|$396$|$2$||$-1$|$3$|
> |$462$|$396$|$\colorbox{aqua}{66}$|$1$||$1$|$-1$|
> |$396$|$66$|$0$|$6$||$0$|$1$|
> 
> $\\negthinspace$
> 
> $\\text{Donc le } PGCD(5742,1320) = 66 $
> 
                
---
""",unsafe_allow_html=True)
    st.markdown("""$6. \quad A = 5454, \quad B = 8572$

>                                 
> |$A$|$B$|$r$|$q$||$u$|$v$|
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> |$5454$|$8572$|-|-||-|-|
> |$8572$|$5454$|$3118$|$1$||$-544$|$855$|
> |$5454$|$3118$|$2336$|$1$||$311$|$-544$|
> |$3118$|$2336$|$782$|$1$||$-233$|$311$|
> |$2336$|$782$|$772$|$2$||$78$|$-233$|
> |$782$|$772$|$10$|$1$||$-77$|$78$|
> |$772$|$10$|$\colorbox{aqua}{2}$|$77$||$1$|$77$|
> |$10$|$2$|$0$|$5$||$0$|$1$|
> 
> $\\negthinspace$
> 
> $\\text{Donc le } PGCD(5454,8572) = 2 $
> 
                
---
""",unsafe_allow_html=True)



def solution_exercice3():
    st.markdown("""$\\text{Dans chacun des cas, donnons l'inverse de } a \\text{ modulo } n \\text{ lorsque cela est possible.}$""")
    st.markdown("""$1. \quad a = 13, \quad n = 7$
>
> $\\text{On a: } \quad 13 \equiv 6[7]$
>
> $\\text{et: } \quad 6 \equiv 6[7]$
>
> $\implies \quad 13 \\times 6 \equiv 6^2[7] \implies 13 \\times 6 \equiv 36[7] \implies 13 \\times 6 \equiv 1[7] $
>
> $\\text{Donc l'inverse de 13 modulo 7 est 6 modulo 7.}$
>

---                
                    """)
    st.markdown("""$2. \quad a = 4, \quad n = 17$
>
> $\\text{On a: } \quad 4 \equiv 4[17]$
>
> $\\text{et: } \quad 13 \equiv 13[17]$
>
> $\implies \quad 4 \\times 13 \equiv 4 \\times 13[17] \implies 4 \\times 13 \equiv 52[17] \implies 4 \\times 13 \equiv 1[17] \quad (car \quad 52 = 17 \\times 3 +1)$
>
> $\\text{Donc l'inverse de 4 modulo 17 est 13 modulo 17.}$
>

---                    
                    """)
    
    st.markdown("""$3. \quad a = 2, \quad n = 8$
>
> $\\text{D'après l'exercice 5 du TD1, on a: } \quad \\forall i \in \\Z/8\\Z; \quad 2i \equiv 0[8], \quad 2i \equiv 2[8], \quad 2i \equiv 4[8] \quad  ou \quad 2i \equiv 6[8]$
>
> $\\text{Donc: } \quad \\forall i \in \\Z/8\\Z; \quad 2i \\not \equiv 1[8]$
>
> $\\text{Alors: l'inverse de 2 modulo 8 n'est existé pas.}$
>
                             
---
                    """)
    
    st.markdown("""$4. \quad a = 54, \quad n = 17$
>
> $\\text{On a:} \quad 54 \equiv 3[17]$
>
> $\\text{et:} \quad 6 \equiv 6[17]$
>
> $\implies \quad 54 \\times 6 \equiv 3 \\times 6[17] \implies \quad 54 \\times 6 \equiv 18[17] \implies \quad 54 \\times 6 \equiv 1[17] \quad (car \quad 18 = 17 \\times 1 +1)$
>
> $\\text{Donc l'inverse de 54 modulo 17 est 6 modulo 17.}$
>
                
---
                    """)
    
    st.markdown("""$5. \quad a = 100, \quad n = 101$
>                    
> $\\text{On a:} \quad 100 \equiv -1[101]$                    
>                    
> $\implies \quad 100 \\times 100 \equiv (-1) \\times (-1) [101] \implies \quad 100 \\times 100 \equiv 1[101]$                   
>                    
> $\\text{Donc l'inverse de 100 modulo 101 est 100 modulo 101.}$                   
    
---                    
                """)
    
    st.markdown("""$6. \quad a = 396, \quad n = 111$
>                    
> $\\text{On applique l'algorithme d'Euclide étendu}$                     
>                    
> |$a$|$b$|$r$|$q$||$u$|$v$|                   
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|                   
> |$111$|$63$|$48$|$1$||$4$|$-7$|                   
> |$63$|$48$|$15$|$1$||$-3$|$4$|                   
> |$48$|$15$|$\colorbox{aqua}{3}$|$3$||$1$|$-3$|                   
> |$15$|$3$|$0$|$5$||$0$|$1$|                   
>
> $\\negthinspace$
>
> $\\text{Donc :} \quad PGCD(396,111) = PGCD(63,111) = 3 \\not = 1$                
>                
> $\\text{Alors: l'inverse de 396 modulo 111 n'est existé pas.}$
>               

---
                    """)
    
    st.markdown("""$7. \quad a = 48, \quad n = 619$
>                    
> $\\text{On applique l'algorithme d'Euclide étendu}$ 
>                  
> |$a$|$b$|$r$|$q$||$u$|$v$|                   
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|                   
> |$619$|$48$|$43$|$12$||$19$|$-245$|                   
> |$48$|$43$|$5$|$1$||$-17$|$19$|                   
> |$43$|$5$|$3$|$8$||$2$|$-17$|                   
> |$5$|$3$|$2$|$1$||$-1$|$2$|                   
> |$3$|$2$|$\colorbox{aqua}{1}$|$1$||$1$|$-1$|                   
> |$2$|$1$|$0$|$2$||$0$|$1$|                   
>                    
> $\\negthinspace$                   
>                    
> $\\text{On a d'après le tableau:} \quad 619 \\times 19 + 48 \\times (-245) = 1 \implies 619 \\times 19 + 48 \\times (-245) \equiv 1[619]$                   
>                    
> $\implies 48 \\times (-245) \equiv 1[619] \quad (car \quad 619 \\times 19 = 0[619])$                   
>                    
> $\implies -245 \equiv 374[619]$                   
>                    
> $\implies 48 \\times 374 \equiv 1[619]$                   
>                    
> $\\text{Donc l'inverse de 48 modulo 619 est 374 modulo 619.}$                   
>                    
                    
    
---
                    """)
    
    st.markdown("""$8. \quad a = 987, \quad n = 1069$
>                    
> $\\text{On applique l'algorithme d'Euclide étendu}$                    
>                    
> |$a$|$b$|$r$|$q$||$u$|$v$|                   
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|                   
> |$1069$|$987$|$82$|$1$||$325$|$-352$|                   
> |$987$|$82$|$3$|$12$||$-27$|$325$|                   
> |$82$|$3$|$\colorbox{aqua}{1}$|$27$||$1$|$-27$|                   
> |$3$|$1$|$0$|$3$||$0$|$1$|                  
>
> $\\negthinspace$                   
>                                    
> $\\text{On a d'après le tableau:} \quad 1069 \\times 325 + 987 \\times (-352) = 1 \implies 1069 \\times 325 + 987 \\times (-352) \equiv 1[1069]$                   
>                    
> $\implies 987 \\times (-352) \equiv 1[1069] \quad (car \quad 1069 \\times 325 = 0[1069])$                   
>                    
> $\implies -352 \equiv 717[1069]$                   
>                    
> $\implies 987 \\times 717 \equiv 1[1069]$                   
>                    
> $\\text{Donc l'inverse de 987 modulo 1069 est 717 modulo 1069.}$                   
>                    
>                    
                

                    """)



def solution_exercice4():
    st.markdown("""$\\text{Les couples suivants définissent-ils des clefs de cryptage affine par paquet de N}$
""")
    st.markdown("""$1. \quad \\text{Pour } N = 1 :$ 

> $(\\Z/26\\Z)^{\\times} =\{1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25 \}$
>
> $1 \\times 1 \equiv 1[26], \quad 3 \\times 9 \equiv 1[26], \quad 5 \\times 21 \equiv 1[26], \quad 7 \\times 15 \equiv 1[26]$
>
> $11 \\times 19 \equiv 1[26], \quad 17 \\times 23 \equiv 1[26], \quad 25 \\times 25 \equiv 1[26]$
>                                                                
> -   $(3; 2): \quad \\text{on a } 3 \in (\\Z/26\\Z)^{\\times} \quad et \quad 2 \in (\\Z/26\\Z) \implies \quad (3,2) \in (\\Z/26\\Z)^{\\times} \\times (\\Z/26\\Z)$   
> $\quad \implies \quad \\text{le couple (3,2) défini un clef de cryptage affine par paquet de 1}$
>           
> - $(13; 8):\quad \\text{on a } 13 \in (\\Z/26\\Z)^{\\times} \quad et \quad 8 \in (\\Z/26\\Z) \implies \quad (13,8) \in (\\Z/26\\Z)^{\\times} \\times (\\Z/26\\Z)$   
> $\quad \implies \quad \\text{le couple (13,8) défini un clef de cryptage affine par paquet de 1}$         
>                       
> - $(9; 0):\quad \\text{on a } 9 \in (\\Z/26\\Z)^{\\times} \quad et \quad 0 \in (\\Z/26\\Z) \implies \quad (9,0) \in (\\Z/26\\Z)^{\\times} \\times (\\Z/26\\Z)$   
> $\quad \implies \quad \\text{le couple (9,0) défini un clef de cryptage affine par paquet de 1}$           
>            


---            
                """)
    
    st.markdown("""$2. \quad \\text{Pour } N = 2 :$

>            
> - $(7; 421):$           
>            
> $\quad \\text{On applique l'algorithme d'Euclide étendu}$ 
>            
> |$a$|$b$|$r$|$q$|$u$|$v$|           
> |:--:|:--:|:--:|:--:|:--:|:--:|
> |$2526$|$7$|$6$|$360$|$-1$|$361$|            
> |$7$|$6$|$1$|$\colorbox{aqua}{1}$|$1$|$-1$|            
> |$6$|$1$|$0$|$6$|$0$|$1$|            
> 
> $\!$
>           
> $2526 \\times (-1) + 7 \\times 361 = 1 \implies \quad 2526 \\times (-1) + 7 \\times 361 \equiv 1[2526]$
>
> $\implies \quad 7 \\times 361 \equiv 1[2526] \quad ( Car \quad 2526 \\times (-1) \equiv 0[2526])$
>
> $\implies \quad 7 \in (\\Z/2526\\Z)^{\\times} \implies \quad \\text{361 est l'inverse de 7 modulo 2526}$
>
> $\\text{et on a:} \quad 421 \in (\\Z/2526\\Z)$
>
> $\quad \implies \\text{le couple (7,421) défini un clef de cryptage affine par paquet de 2.}$
>
> ---
>
> - $(25; 11):$
>
> $\quad \\text{On applique l'algorithme d'Euclide étendu}$
>
> |$a$|$b$|$r$|$q$|$u$|$v$|           
> |:--:|:--:|:--:|:--:|:--:|:--:|
> |$2526$|$25$|$\colorbox{aqua}{1}$|$101$|$1$|$-101$|
> |$25$|$1$|$0$|$25$|$0$|$1$|
>
> $\!$
>
> $2526 \\times 1 + 25 \\times (-101) = 1 \implies \quad 2526 \\times 1 + 25 \\times (-101) \equiv 1[2526]$
>
> $\implies \quad 25 \\times (-101) \equiv 1[2526] \quad ( Car \quad 2526 \\times (-1) \equiv 0[2526])$
>
> $\\text{On a:} \quad -101 \equiv -101[2526] \implies \quad -101 \equiv 2526 -101[2526] \implies \quad -101 \equiv 2425[2526]$
>
> $\implies \quad 25 \\times 2425 \equiv 1[2526]$
>
> $\implies \quad 25 \in (\\Z/2526\\Z)^{\\times} \implies \quad \\text{2425 est l'inverse de 25 modulo 2526}$
>
> $\\text{et on a:} \quad 11 \in (\\Z/2526\\Z)$
>
> $\quad \implies \\text{le couple (25,11) défini un clef de cryptage affine par paquet de 2.}$
>
> ---
>
> - $(421; 801):$ 
>               
> $\quad \\text{On applique l'algorithme d'Euclide étendu}$              
>               
> |$a$|$b$|$r$|$q$|$u$|$v$|           
> |:--:|:--:|:--:|:--:|:--:|:--:|              
> |$2526$|$\colorbox{aqua}{421}$|$0$|$6$|$0$|$1$|
>              
> $\!$             
>              
> $\\text{On a:} \quad PGCD(2526,421) = 421$             
>              
> $\implies \quad \\text{421 modulo 2526 n'admit pas des inverses dans } \\Z/2526\\Z$                          
>              
> $\implies \\text{le couple (421,801) ne défini pas un clef de cryptage affine par paquet de 2.}$             
>              
                
---            
                """)
    
    st.markdown("""$3. \quad \\text{Pour } N = 3 :$ 

>            
> - $(2015; 1998):$           
>            
> $\quad \\text{On applique l'algorithme d'Euclide étendu}$           
>            
> |$a$|$b$|$r$|$q$|$u$|$v$|           
> |:--:|:--:|:--:|:--:|:--:|:--:|           
> |$252526$|$2015$|$651$|$125$|$31$|$-3885$|           
> |$2015$|$651$|$62|$3$|$-10$|$31$|           
> |$651$|$62$|$\colorbox{aqua}{31}$|$10$|$1$|$-10$|           
> |$62$|$31$|$0$|$2$|$0$|$1$|                    
>           
> $\!$           
>            
> $\implies \quad PGCD(252526,2015) = 31 \\not = 1$  
>         
> $\implies \quad \\text{2015 modulo 252526 n'admit pas des inverses dans } \\Z/252526\\Z$ 
>          
> $\implies \\text{le couple (2015,1998) ne défini pas un clef de cryptage affine par paquet de 3.}$         
>          
> ---           
>            
> - $(4567; 9002):$           
>
> $\quad \\text{On applique l'algorithme d'Euclide étendu}$
>            
> |$a$|$b$|$r$|$q$|$u$|$v$|           
> |:--:|:--:|:--:|:--:|:--:|:--:|           
> |$252526$|$4567$|$1341$|$55$|$-361$|$19961$|           
> |$4567$|$1341$|$544$|$3$|$106$|$-361$|           
> |$1341$|$544$|$253$|$2$|$-43$|$106$|           
> |$544$|$253$|$38$|$2$|$20$|$-43$|           
> |$253$|$38$|$25$|$6$|$-3$|$20$|           
> |$38$|$25$|$13$|$1$|$2$|$-3$|           
> |$25$|$13$|$12$|$1$|$-1$|$2$|           
> |$13$|$12$|$\colorbox{aqua}{1}$|$1$|$1$|$-1$|           
> |$12$|$1$|$0$|$12$|$0$|$1$|           
>            
> $\!$           
>
> $252526 \\times (-361) + 4567 \\times 19961 = 1 \implies \quad 252526 \\times (-361) + 4567 \\times 19961 \equiv 1[252526]$
>
> $\implies \quad 4567 \\times 19961 \equiv 1[252526] \quad ( Car \quad 252526 \\times (-361) \equiv 0[252526])$
>
> $\implies \quad 4567 \in (\\Z/252526\\Z)^{\\times} \implies \quad \\text{19961 est l'inverse de 4567 modulo 252526}$
>
> $\\text{et on a:} \quad 9002 \in (\\Z/252526\\Z)$
>
> $\quad \implies \\text{le couple (4567,9002) défini un clef de cryptage affine par paquet de 3.}$
>
>
> ---
>
> - $(4073; 88):$
>
> $\quad \\text{On applique l'algorithme d'Euclide étendu}$
>
> |$a$|$b$|$r$|$q$|$u$|$v$|           
> |:--:|:--:|:--:|:--:|:--:|:--:|
> |$252526$|$\colorbox{aqua}{4073}$|$0$|$62$|$0$|$1$|           
>            
> $\!$
>            
> $\implies \quad PGCD(252526,4073) = 4973 \\not = 1$  
>         
> $\implies \quad \\text{4073 modulo 252526 n'admit pas des inverses dans } \\Z/252526\\Z$ 
>          
> $\implies \\text{le couple (4073,88) ne défini pas un clef de cryptage affine par paquet de 3.}$           
>            

            
                """)



def solution_exercice5():
    
    st.markdown("""$\\text{Les clefs valides de l'exercice 4 sont: }$

$1. \quad \\text{Pour } N = 1 : (3; 2),  \, (9; 0).$

$2. \quad \\text{Pour } N = 2 : (7; 421), \, (25; 11)$

$3. \quad \\text{Pour } N = 3 : (4567; 9002)$

#### $\\text{On déterminons la fonction de déchiffrement.}$
""")
    st.markdown("""

$1. \quad \\text{Pour } N = 1 :$
                
> ##### Rappel: $\\text{(Déchiffrement affine)}$
>
> $\quad \quad \\text{Soient } x \in \\Z/26\\Z \quad et \quad (a,b) \in (\\Z/26\\Z)^{\\times} \\times \\Z/26\\Z , \quad x \equiv a^{-1}(y-b)[26]$
>
> ---
>                
> - $(3; 2): \quad 3 \\times 9 \equiv 1[26] $
> 
>   $\quad D_{(3;2)}(y) \equiv 9(y - 2)[26]$
> 
> ---
>                
> - $(9; 0): \quad 9 \\times 3 \equiv 1[26]$
> 
>   $\quad D_{(9;0)}(y) \equiv 3 \\times y[26]$
> 
> ---
                
$2. \quad \\text{Pour } N = 2 :$                

> ##### Rappel: $\\text{(Déchiffrement affine)}$
>
> $\quad \quad \\text{Soient } x \in \\Z/2526\\Z \quad et \quad (a,b) \in (\\Z/2526\\Z)^{\\times} \\times \\Z/2526\\Z , \quad x \equiv a^{-1}(y-b)[2526]$
>
> ---                
>
>                
>  - $(7; 421): \quad 7 \\times 361 \equiv 1[2526]$             
>                
>    $\quad D_{(7;421)}(y) \equiv 361 \\times (y-421)[2526]$              
>                
> ---                
>                
>  - $(25; 11): \quad 25 \\times 2425 \equiv 1[2526]$              
>                
>    $\quad D_{(25;11)}(y) \equiv 2425 \\times (y-11)[2526]$            
> 
> ---

$3. \quad \\text{Pour } N = 3 :$

> ##### Rappel: $\\text{(Déchiffrement affine)}$
>
> $\quad \quad \\text{Soient } x \in \\Z/252526\\Z \quad et \quad (a,b) \in (\\Z/252526\\Z)^{\\times} \\times \\Z/252526\\Z , \quad x \equiv a^{-1}(y-b)[252526]$
>
> --- 
>                
> - $(4567; 9002): \quad 4567 \\times 19961 \equiv 1[252526]$                               
>                                
>   $\quad D_{(4567; 9002)}(y) \equiv 19961 \\times (y-9002)[252526]$                             
>                                
>                                
""")



def solution_exercice6():
    pass

def solution_exercice7():
    pass

def solution_exercice8():
    pass

def solution_exercice9():
    pass

def solution_exercice10():
    pass