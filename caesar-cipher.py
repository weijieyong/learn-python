# O(N) for both space and time

# %%

def caesarCipherEncryptor(string, key):
    final = ""
    for i in string:
        next = ord(i)+(key%26)
        if  next > 122:
            next -= 26
        final += chr(next)
    return final
#%%
# driver code
string = "abc"
key = 52
ans = caesarCipherEncryptor(string, key)
print(ans)

#%%
# create own list

def caesarCipherEncryptor(string, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final = ""
    for letter in string:
        next = alphabet.index(letter)+(key%26)
        final += alphabet[next%26]
    return final