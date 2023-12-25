import streamlit as st


def exercice1():
    st.markdown("""

> ##### Proposition:
>                
> $\qquad \\text{Les propriétés suivantes sont vraies \enspace}$ $\\forall (a,b) \in \\Z^2 \enspace et \enspace c \in \\Z^*:$
>
> - $\\text{Si} \enspace c \, | \, a \enspace \\text{et} \enspace c \, | \, b \enspace \\text{ alors,} \enspace \exist (u,v) \in \\Z^2, \enspace c \, | \, au + bv. $
>
> - $\\text{Si} \enspace a \, | \, b \enspace \\text{et} \enspace b \, | \, a \enspace \\text{alors,} \enspace a=b \enspace \\text{ ou } \enspace a = -b.$
>
> - $\\text{Si} \enspace c \, | \, b \enspace \\text{et} \enspace b \, | \, a \enspace \\text{alors,} \enspace c \, | \, a \enspace$ $\\text{ (On dit que la relation | est transitive). }$
>
> - $a \, | \, a \enspace \\text{(On dit que la relation | est réflexive).}$
>
> - $1 \, | \, a \enspace \\text{(1 divise tout le monde).}$
>
> - $a \, | \, 0 \enspace \\text{(tout le monde divise 0).}$
>

$\\text{Prouvez que les propriétés ci-dessus }$ $\\text{sont correctes.}$

""")


def exercice2():
    st.markdown("""
$\\text{Donnez la liste des nombres premiers }$ $\\text{plus petits que 30}$
""")


def exercice3():
    st.markdown("""
$\\text{Écrire la DFP (Décomposition en }$ $\\text{facteur premier) de 121, 101, 33, 392.}$
""")


def exercice4():
    st.markdown("""
$\\text{Écrire la division Euclidienne de 121 par 7, }$ $\\text{de 17 par 2 et de 33 par 44.}$
""")


def exercice5():
    st.markdown("""
$\\text{Calculez le PGCD de 15 et 35.} $
""")


def exercice6():
    st.markdown("""
$\\text{Montrez que 32 et 7 sont premiers entre eux.}$
""")


def exercice7():
    st.markdown("""
$\\text{Montrez que si PGCD(a,b) = d alors} \enspace \\cfrac{a}{d} \enspace $ $\\text{et} \enspace \\cfrac{b}{d} \enspace \\text{sont entiers et premiers entre eux.}$
""")


def exercice8():
    st.markdown("""
$\\text{Soient} \enspace a = 111 \enspace \\text{et} \enspace b = 27, \enspace \\text{calculez} \enspace d = PGCD(a,b) \enspace \\text{et donnez la forme de }$ $\\text{tous les couples} \enspace (u,v) \enspace \\text{tel que} \enspace au + bv = d.$
""")


def exercice9():
    st.markdown("""
$\\text{Montrez que } \enspace PGCD(ab,ac) = a \\times PGCD(b,c).$
""")


def exercice10():
    st.markdown("""
###### $\\text{Le Lemme de Gauss:}$
                
$\qquad \\text{Montrez que si} \enspace  a \, | \, bc \enspace \\text{et} \enspace PGCD(a,b) = 1, \enspace \\text{alors} \enspace a \, | \, c.$
""")


def exercice11():
    st.markdown("""
$\\text{Calculez les PGCD suivants:}$
""")
    exercice11_cols = st.columns(3)
    with exercice11_cols[0]:
        st.markdown("""
$1. \quad PGCD(46328, 12379)$
                    
$2. \quad PGCD(42098,34345)$
""")
    
    with exercice11_cols[1]:
        st.markdown("""
$3. \quad PGCD(4567, 11111111111111)$
                    
$4. \quad PGCD(34860,4853)$
""")

    with exercice11_cols[2]:
        st.markdown("""
$5. \quad PGCD(30076,12669)$
""")


def exercice12():
    st.markdown("""
$\\text{Montrez qu'il existe une infinité }$ $\\text{de nombres premiers.}$
                
$\\text{Indice:} \quad \\text{Par l'absurde.}$
""")


def exercice13():
    st.markdown("""
$\\text{Dites si les assertions suivantes }$ $\\text{sont vraies ou fausses:}$

>
> $1. \quad 15 \enspace \\text{est divisible par} \enspace 5$
>
> $2. \quad 6 \enspace \\text{divise} \enspace 24$
>
> $3. \quad 12 \enspace \\text{est un multiple de} \enspace 24$
>
> $4. \quad 42 \enspace \\text{est divisible par} \enspace 7$
>
> $5. \quad 18 \enspace \\text{est un multiple de} \enspace 6$
>
""")


def exercice14():
    st.markdown("""
$\\text{(Un partage de bonbon pas très équitable) }$ $\\text{Julien doit partager 73 bonbons}$ 
$\\text{équitablement entre ses 3 trois soeurs }$ $\\text{et ses cousins. Lui ne gardera que le reste}$
$\\text{Il a 5 cousins. combien doit-il appeler de }$ $\\text{cousins pour qu'il lui reste le plus de bonbons?}$
""")


def exercice15():
    st.markdown("""
$\\text{Soit} \enspace n \\text{un entier, montrez que} \enspace 6 \, | \, n(n+1)(n+2).$
""")


def exercice16():
    st.markdown("""
###### $\\text{Résoudre les équations suivantes:}$
""")
    exercice16_cols = st.columns(2)
    with exercice16_cols[0]:
        st.markdown("""
$1. \quad 2x + 5y = 3$
                    
$2. \quad 323x - 391y = 612$
""")
    
    with exercice16_cols[1]:
        st.markdown("""
$3. \quad 162x + 207y = 27$
                    
$4. \quad 221x + 247y = 15$
""")


def exercice17():
    st.markdown("""
$\\text{(Une drole de propriété) }$ $\\text{Démontrer que l'on ne change pas }$ $\\text{le PGCD de deux entiers }$
$\\text{en multipliant l'un d'entre eux par }$ $\\text{un entier premier avec l'autre.}$
""")


def exercice18():
    st.markdown("""
$\\text{(Magicien ou mathématicien?) }$ $\\text{Je vais deviner votre date de naissance. }$
$\\text{Prenez votre jour de naissance. }$ $\\text{Multipliez-le par 31. }$
$\\text{Prenez votre mois de naissance. }$ $\\text{Multipliez-le par 12. }$
$\\text{Combien trouvez-vous? }$ $\\text{811 vous me dites? }$ $\\text{Et bien vous êtes né un 25 mars! }$
$\\text{En plus, c'est vrai. }$ $\\text{Mais comment a-t-il fait?}$
""")


def exercice19():
    st.markdown("""
$\\text{Montrer que l'équation} \enspace x^3 - x^2 + x + 1 = 0 \enspace \\text{n'a pas de solutions rationnelles}$
""")


def exercice20():
    st.markdown("""
$(\sqrt{2} \enspace \\text{ou la hantise de Pythagore}): \enspace \\text{Démontrez que} \enspace \sqrt{2} \enspace \\text{n'est pas un rationnel}$
""")