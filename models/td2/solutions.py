import streamlit as st

def solution_exercice1():
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
    <div style="border-left: 2px solid black; padding-left: 5px; text-align: start;">
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
> - $ 1 + 0 + 6 + 9 = 16 \quad et \quad 1 + 6 = 7 \\not = 3,6 \\text{ ou } 9 \implies p \\not 3$
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
    <div style="border-left: 2px solid black; padding-left: 5px; text-align: start;">
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
    <div style="border-left: 2px solid black; padding-left: 5px; text-align: start;">
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
    <div style="border-left: 2px solid black; padding-left: 5px; text-align: start;">
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
> $D(684) = \{1, 2, 3, 4, 6, 9, 12, 18, 19, 36, 38, 57, 76, 114, 228, 342, 684 \}$
>

                """,unsafe_allow_html=True)

    

def solution_exercice2():
    st.markdown("""

""",unsafe_allow_html=True)

def solution_exercice3():
    pass

def solution_exercice4():
    pass

def solution_exercice5():
    pass

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