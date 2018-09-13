#key   = 072719_7_8072_71978_072719780_72719_7807271_
#cipher='IJGJUO{P_LOUV_AIRUS_GYQUTOLTD_SKRFB_TWNKCFT}'
#        ICECTF{I_DONT_SHINK_GRONSFELD_LIKER_MONDAXS}
#        ICECTF{I_DONT_THINK_GRONSFELD_LIKES_MONDAYS}
cipher='IJGJUOPLOUVAIRUSGYQUTOLTDSKRFBTWNKCFT'
key =  '07271978'

# A=65, Z=90
plaintext = []
for i, char in enumerate(cipher):
    if not char.isalpha():
        plaintext.append(char)
        continue
    k=key[i%len(key)] 
    plaintext.append(chr((((ord(char) - ord('A')) - int(k)) % 26) + ord('A')))

plaintext = "".join(plaintext)
print(plaintext)
