
from models.programs.arithmetique import bezout, pgcd


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


###############################################################################
###                                                                         ###
###                             Cryptage Affine                             ###
###                                                                         ###
###############################################################################
def affine_crypt(a,k,message,paquet=1):
    if paquet == 1:
        if pgcd(a,26) == 1:
            result = ''
            for char in message:
                i = alphabet.index(char)
                result += alphabet[(a*i+ k)%26]
            return result
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/26\\Z$"
    if paquet == 2:
        if pgcd(a,26) == 1:
            message += "A"*((2 -len(message)%2)%2)
            liste = []
            for i in range(len(message)//2):
                liste.append(message[i*2:i*2+2])
            liste2 = []
            for i in liste:
                res = [char for char in i]
                liste2.append(res)
            ab = [[alphabet.index(k) for k in i] for i in liste2]
            b =[i[0] * 100 + i[1] for i in ab]
            result = [((a*i+k)%2526) for i in b]

            return '-'.join([str(i) for i in result])
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/2526\\Z$"
    if paquet == 3:
        if pgcd(a,26) == 1:
            message += "A"*((3 -len(message)%3)%3)
            liste = []
            for i in range(len(message)//3):
                liste.append(message[i*3:3*(i+1)])
            liste2 = []
            for i in liste:
                res = [char for char in i]
                liste2.append(res)
            ab = [[alphabet.index(k) for k in i] for i in liste2]
            b =[i[0] * 10000 + i[1]*100 + i[2] for i in ab]
            result = [((a*i+k)%252526) for i in b]

            return '-'.join([str(i) for i in result])
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/252526\\Z$"

###############################################################################
###                                                                         ###
###                            Décryptage Affine                            ###
###                                                                         ###
###############################################################################
def affine_decrypt(a,k,message,paquet=1):
    if paquet == 1:
        if pgcd(a,26) == 1:
            inverse_a = bezout(a,26)[0]%26
            result = ''
            for char in message:
                i = alphabet.index(char)
                result += alphabet[(inverse_a*(i- k))%26]
            return result
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/26\\Z$"
    if paquet == 2:
        if pgcd(a,2526) == 1:
            inverse_a = bezout(a,2526)[0]%2526
            message_liste = message.split('-')
            message_liste_to_int = [int(i) for i in message_liste]
            b = [((inverse_a*(i-k))%2526) for i in message_liste_to_int]
            b_index_char = [[i//100,i%100] for i in b]
            char_list = [[alphabet[k] for k in i] for i in  b_index_char]
            return ''.join([''.join(i) for i in char_list])
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/2526\\Z$"
    if paquet == 3:
        if pgcd(a,252526) == 1:
            inverse_a = bezout(a,252526)[0]%252526
            message_liste = message.split('-')
            message_liste_to_int = [int(i) for i in message_liste]
            b = [((inverse_a*(i-k))%252526) for i in message_liste_to_int]
            b_index_char = [[i//10000,(i%10000)//100,(i%10000)%100] for i in b]
            char_list = [[alphabet[k] for k in i] for i in  b_index_char]
            return ''.join([''.join(i) for i in char_list])
        return f"Le nombre {a} n'admit pas un inverse dans $\\Z/252526\\Z$"


###############################################################################
###                                                                         ###
###                           Cryptage Symétrique                           ###
###                                                                         ###
###############################################################################
def symetrique_crypt(k,message,paquet=1):
    if paquet == 1:
        result = ''
        for char in message:
            i = alphabet.index(char)
            result += alphabet[(i+ k)%26]
        return result
    if paquet == 2:
        
        message += "A"*((2 -len(message)%2)%2)
        liste = []
        for i in range(len(message)//2):
            liste.append(message[i*2:i*2+2])
        liste2 = []
        for i in liste:
            res = [char for char in i]
            liste2.append(res)
        a = [[alphabet.index(k) for k in i] for i in liste2]
        b =[i[0] * 100 + i[1] for i in a]
        result = [((i+k)%2526) for i in b]

        return '-'.join([str(i) for i in result])

    if paquet == 3:
        message += "A"*((3 -len(message)%3)%3)
        liste = []
        for i in range(len(message)//3):
            liste.append(message[i*3:3*(i+1)])
        liste2 = []
        for i in liste:
            res = [char for char in i]
            liste2.append(res)
        a = [[alphabet.index(k) for k in i] for i in liste2]
        b =[i[0] * 10000 + i[1]*100 + i[2] for i in a]
        result = [((i+k)%252526) for i in b]

        return '-'.join([str(i) for i in result])


###############################################################################
###                                                                         ###
###                          Décryptage Symétrique                          ###
###                                                                         ###
###############################################################################
def symetrique_decrypt(k,message,paquet):
    if paquet == 1:
        result = ''
        for char in message:
            i = alphabet.index(char)
            result += alphabet[(i-k)%26]
        return result
    if paquet == 2:
        message_liste = message.split('-')
        message_liste_to_int = [int(i) for i in message_liste]
        b = [((i-k)%2526) for i in message_liste_to_int]
        b_index_char = [[i//100,i%100] for i in b]
        char_list = [[alphabet[k] for k in i] for i in  b_index_char]
        return ''.join([''.join(i) for i in char_list])
    
    if paquet == 3:
        message_liste = message.split('-')
        message_liste_to_int = [int(i) for i in message_liste]
        b = [((i-k)%252526) for i in message_liste_to_int]
        b_index_char = [[i//10000,(i%10000)//100,(i%10000)%100] for i in b]
        char_list = [[alphabet[k] for k in i] for i in  b_index_char]
        return ''.join([''.join(i) for i in char_list])


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