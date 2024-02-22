
from models.programs.arithmetique import bezout, pgcd
import streamlit as st


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


###############################################################################
###                                                                         ###
###                             Cryptage Affine                             ###
###                                                                         ###
###############################################################################
def affine_crypto(a,k,message,option,paquet=1):
    if paquet == 1:
        if pgcd(a,26) == 1:
            result = []
            for char in message:
                i = alphabet.index(char)
                aik = a*i + k
                aik26 = aik%26
                char_crypt = alphabet[aik26]
                result.append([char, i, aik, aik26, char_crypt])
            return result
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/26\\Z$"
    if paquet == 2:
        if pgcd(a,2526) == 1:
            message += option*((2 -len(message)%2)%2)
            liste = []
            for i in range(len(message)//2):
                liste.append(message[i*2:i*2+2])
            liste2 = []
            for i in liste:
                res = [char for char in i]
                liste2.append(res)
            ab = [[alphabet.index(k) for k in i] for i in liste2]
            b =[i[0] * 100 + i[1] for i in ab]
            aik = [a*i+k for i in b]
            result = [(i%2526) for i in aik]

            return [[char, i, ik_, ik2526, res] for char, i, ik_, ik2526,res in zip(liste, b, aik, result,result)]
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/2526\\Z$"
    if paquet == 3:
        if pgcd(a,252526) == 1:
            message += option*((3 -len(message)%3)%3)
            liste = []
            for i in range(len(message)//3):
                liste.append(message[i*3:3*(i+1)])
            liste2 = []
            for i in liste:
                res = [char for char in i]
                liste2.append(res)
            ab = [[alphabet.index(k) for k in i] for i in liste2]
            b =[i[0] * 10000 + i[1]*100 + i[2] for i in ab]
            aik = [a*i+k for i in b]
            result = [((a*i+k)%252526) for i in b]

            return [[char, i, ik_, ik2526, res] for char, i, ik_, ik2526,res in zip(liste, b, aik, result,result)]
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/252526\\Z$"

##############################################################################
###                                                                         ###
###                            Décryptage Affine                            ###
###                                                                         ###
###############################################################################
def affine_decryptage(a,k,message,paquet=1):
    if paquet == 1:
        if pgcd(a,26) == 1:
            inverse_a = bezout(a,26)[0]%26
            result = []
            for char in message:
                i = alphabet.index(char)
                aik = inverse_a*(i - k)
                aik26 = aik%26
                char_crypt = alphabet[aik26]
                result.append([char, i, aik, aik26, char_crypt])
            return result
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/26\\Z$"
    if paquet == 2:
        if pgcd(a,2526) == 1:
            inverse_a = bezout(a,2526)[0]%2526
            message_liste = message.split('-')
            message_liste_to_int = [int(i) for i in message_liste]
            ik = [inverse_a*(i-k) for i in message_liste_to_int]
            b = [(i%2526) for i in ik]
            b_index_char = [[i//100,i%100] for i in b]
            b_index_char_str = [[str(j) for j in i] for i in b_index_char]
            b_q = ['-'.join(i) for i in b_index_char_str]
            char_list = [[alphabet[k] for k in i] for i in  b_index_char]
            groupBy2 = ['-'.join(i) for i in char_list]
            group =  [''.join(i) for i in char_list] 
            return [[part, i, ik_,b2, gro2, res] for part, i, ik_,b2, gro2,res in zip(message_liste, ik, b, b_q,groupBy2,group)]
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/2526\\Z$"
    if paquet == 3:
        if pgcd(a,252526) == 1:
            inverse_a = bezout(a,252526)[0]%252526
            message_liste = message.split('-')
            message_liste_to_int = [int(i) for i in message_liste]
            ik = [inverse_a*(i-k) for i in message_liste_to_int]
            b = [(i%252526) for i in ik]
            b_index_char = [[i//10000,(i%10000)//100,(i%10000)%100] for i in b]
            b_index_char_str = [[str(j) for j in i] for i in b_index_char]
            b_q = ['-'.join(i) for i in b_index_char_str]
            char_list = [[alphabet[k] for k in i] for i in  b_index_char]
            groupBy3 = ['-'.join(i) for i in char_list]
            group =  [''.join(i) for i in char_list]
            return [[part, i, ik_,b2, gro3, res] for part, i, ik_,b2, gro3,res in zip(message_liste, ik, b, b_q,groupBy3,group)]
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/252526\\Z$"



###############################################################################
###                                                                         ###
###                           Cryptage Puissance                            ###
###                                                                         ###
###############################################################################
def puissance_crypt(a,k,c,message):
    if pgcd(a,26) == 1:
        if pgcd(c,12) == 1:
            result = ''
            for char in message:
                i = alphabet.index(char)
                result += alphabet[((a*(i**c))+k)%26]
            return result
        return f"Le nombre {c} n'admit pas un inverse dans $\\Z/12\\Z$"
    return f"Le nombre {a} n'admit pas un inverse dans $\\Z/26\\Z$"


###############################################################################
###                                                                         ###
###                          Décryptage Puissance                           ###
###                                                                         ###
###############################################################################
def puissance_decrypt(a,k,c,message):
    if pgcd(a,26) == 1:
        if pgcd(c,12) == 1:
            inverse_a = bezout(a,26)[0]%26
            inverse_c = bezout(c,12)[0]%12
            result = ''
            for char in message:
                i = alphabet.index(char)
                result += alphabet[((inverse_a * (i - k))**inverse_c)%26]
            return result
        return f"Le nombre {c} n'admit pas un inverse dans $\\Z/12\\Z$"
    return f"Le nombre {a} n'admit pas un inverse dans $\\Z/26\\Z$"



###############################################################################
###                                                                         ###
###                           Cryptage César                                ###
###                                                                         ###
###############################################################################
def cesar_cryptage(k,message,option,paquet=1):
    if paquet == 1:
        result = []
        for char in message:
            i = alphabet.index(char)
            ik = i + k
            ik26 = ik%26
            char_crypt = alphabet[ik26]
            result.append([char, i, ik, ik26, char_crypt])
        return result
    if paquet == 2:
        message += option*((2 -len(message)%2)%2)
        liste = []
        for i in range(len(message)//2):
            liste.append(message[i*2:i*2+2])
        liste2 = []
        for i in liste:
            res = [char for char in i]
            liste2.append(res)
        a = [[alphabet.index(k) for k in i] for i in liste2]
        b =[i[0] * 100 + i[1] for i in a]
        ik = [i+k for i in b]
        result = [(i%2526) for i in ik]

        return [[char, i, ik_, ik2526, res] for char, i, ik_, ik2526,res in zip(liste, b, ik, result,result)]

    if paquet == 3:
        message += option*((3 -len(message)%3)%3)
        liste = []
        for i in range(len(message)//3):
            liste.append(message[i*3:3*(i+1)])
        liste2 = []
        for i in liste:
            res = [char for char in i]
            liste2.append(res)
        a = [[alphabet.index(k) for k in i] for i in liste2]
        b =[i[0] * 10000 + i[1]*100 + i[2] for i in a]
        ik = [i+k for i in b]
        result = [(i%252526) for i in ik]

        return [[char, i, ik_, ik2526, res] for char, i, ik_, ik2526,res in zip(liste, b, ik, result,result)]
    

###############################################################################
###                                                                         ###
###                          Décryptage César                               ###
###                                                                         ###
###############################################################################
def cesar_decryptage(k,message,paquet):
    if paquet == 1:
        result = []
        for char in message:
            i = alphabet.index(char)
            ik = i-k
            ik26 = ik%26
            char_decrypt = alphabet[ik26]
            result.append([char, i, ik, ik26, char_decrypt])
        return result
    if paquet == 2:
        message_liste = message.split('-')
        message_liste_to_int = [int(i) for i in message_liste]
        ik = [i-k for i in message_liste_to_int]
        b = [(i%2526) for i in ik]
        b_index_char = [[i//100,i%100] for i in b]
        b_index_char_str = [[str(j) for j in i] for i in b_index_char]
        b_q = ['-'.join(i) for i in b_index_char_str]
        char_list = [[alphabet[k] for k in i] for i in  b_index_char]
        groupBy2 = ['-'.join(i) for i in char_list]
        group =  [''.join(i) for i in char_list] 
        return [[part, i, ik_,b2, gro2, res] for part, i, ik_,b2, gro2,res in zip(message_liste, ik, b, b_q,groupBy2,group)]
    
    if paquet == 3:
        message_liste = message.split('-')
        message_liste_to_int = [int(i) for i in message_liste]
        ik = [i-k for i in message_liste_to_int]
        b = [((i-k)%252526) for i in message_liste_to_int]
        b_index_char = [[i//10000,(i%10000)//100,(i%10000)%100] for i in b]
        b_index_char_str = [[str(j) for j in i] for i in b_index_char]
        b_q = ['-'.join(i) for i in b_index_char_str]
        char_list = [[alphabet[k] for k in i] for i in  b_index_char]
        groupBy3 = ['-'.join(i) for i in char_list]
        group =  [''.join(i) for i in char_list]
        return [[part, i, ik_,b2, gro3, res] for part, i, ik_,b2, gro3,res in zip(message_liste, ik, b, b_q,groupBy3,group)]
    