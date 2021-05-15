# ask for text
# ask for number

# for letter in text:
#     if is alphabet:
#         convert and add it to final word
#       else:
#         ignore and add it to the final word
# return final word 

def input_string():
    string = input("Enter the text to encrypt: ")
    return string
def input_number():
    try:        
        while True:
            number = input("Enter the encryption key: ")
            if int(number):
                if int(number) > 0 and int(number) < 26:
                    return int(number)
    except:
        print("Try again!")
        return input_number()

string = input_string()
number = input_number()
result = ""

for letter in string:
    z = "z"
    if letter.isalpha():
        if letter.isupper():
            z = "Z"
        ordinal = ord(letter) + number
        z_ord = ord(z)
        if ordinal > z_ord:
            key = ordinal - z_ord
            code = z_ord - 26 + key
            result += chr(code)
        else:
            result += chr(ordinal)

    else:
        result += letter
        
print(result)
