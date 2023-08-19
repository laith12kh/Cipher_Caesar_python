logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def cipher_caesar(ci_dirction,ci_text,ci_shift):
    ci_word = ""
    for letter in ci_text:
        index = alphabet.index(letter)
        if ci_dirction == 'encode':
             new_index = index + ci_shift
        elif ci_dirction == 'decode':
            new_index = index - ci_shift
        ci_letter=alphabet[new_index]
        ci_word+=ci_letter
    print(f"the {ci_dirction}d word is {ci_word}")


cipher_caesar(direction,text,shift)


#def encrypt(p_text,num_of_shifts):
#    ci_word=""
#    for letter in p_text:
#        index = alphabet.index(letter)
#        new_index = index + num_of_shifts
#        ci_letter=alphabet[new_index]
#        ci_word+=ci_letter
#    print(f"the encoded word is {ci_word}")

#def decrypt(p_text,num_of_shifts):
#    ci_word=""
#    for letter in p_text:
#        index = alphabet.index(letter)
#        new_index = index - num_of_shifts
#        ci_letter=alphabet[new_index]
#        ci_word+=ci_letter
#    print(f"the encoded word is {ci_word}")



#if direction == 'encode':
#    text = input("Type your message:\n").lower()
#    shift = int(input("Type the shift number:\n"))
#    encrypt(text,shift)
#elif direction == 'decode':
#    text = input("Type your message:\n").lower()
#    shift = int(input("Type the shift number:\n"))  
#    decrypt(text,shift)