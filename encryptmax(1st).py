pol_letters_dict = { 'ą' : 'a', 'ć' : 'c', 'ę' : 'e', 'ź': 'z', 'ż' : 'z', 'ó' : 'o', 'ł' : 'l', 'ń' : 'n', 'ś' : 's'}

def encrypt(msg : str) -> str: # accepts text in polish without any punctuation marks
    msg = msg.lower()
    for key, val in pol_letters_dict.items():
        msg = msg.replace(key, val)
    

    enc_msg = msg[0]    
    split_msg = msg.split()
    split_msg[0] = split_msg[0][1:]
    prev_l = ord(msg[0])
    for word in split_msg:
        for l in word:
            enc_l = (ord(l) + prev_l)%26 + 97
            enc_msg += chr(enc_l)
            prev_l = enc_l
        enc_msg += ' '
    return enc_msg

def decrypt(enc_msg : str) -> str:
    # chyba by się przydała ta funkcja...
    ...

#testing
enc_msg = 'ztjhgamic qbl hekoke '
dec_msg = decrypt(enc_msg)
print(dec_msg == 'ziemniaki czy kluski') # shoud be True
