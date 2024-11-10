def encrypt(original_text, shift_num):
    generated_text = ""

    for character in original_text:
        index = alphabet.index(character)
        index_with_shift = index + shift_num

        if( index_with_shift >= len(alphabet) - 1):
            difference = index_with_shift - len(alphabet)
            index_with_shift = difference
        
        generated_text += alphabet[index_with_shift]

        
    print(generated_text)
        

def decrypt( original_text, shift_num):
    generated_text = ""

    for character in original_text:
        index = alphabet.index(character)
        index_with_shift = index - shift_num

        if( index_with_shift < 0):
            difference =  len(alphabet) + index_with_shift
            index_with_shift = difference
        
        generated_text += alphabet[index_with_shift]

        
    print(generated_text)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

encrypt("hello", 3)
decrypt("khoor", 3)

