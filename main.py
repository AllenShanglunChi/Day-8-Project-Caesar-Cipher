alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

 #encode shift each letter of the 'text' forwards in the alphabet by the shift amount to encrypt text.  
  #e.g. 
  #text = "hello"
  #shift = 5
  #encoded_text = "mjqqt"
#decode shift each letter of the 'text' *backwards* in the alphabet by the shift amount and to decrypt text.  
  #e.g. 
  #encoded_text = "mjqqt"
  #shift = 5
  #decoded_text = "hello"
#Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
# def encrypt(textPara, shiftPara):
#   encoded_text = ""
#   for char in textPara:
#     indexOld = alphabet.index(char)
#     indexNew = indexOld + shiftPara
#     encoded_text += alphabet[indexNew] 
#   print(f"The encoded text is {encoded_text}")
# def decrypt(textPara, shiftPara):
#   decoded_text = ""
#   for char in textPara:
#     indexNew = alphabet.index(char) - shiftPara
#     decoded_text += alphabet[indexNew]
#   print(f"The decoded text is {decoded_text}")

# if direction == "encode":
#   encrypt(textPara=text, shiftPara=shift)
# elif direction == "decode":
#   decrypt(textPara=text, shiftPara=shift)
  
#Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text_para, shift_para, direction_para):
    end_text = ""
    if direction_para == "decode":
      shift_para *= -1
    for char in text_para:
    #keep the number/symbol/space if entered by the user when the text is encoded/decoded
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
        if char in alphabet:        
          index_old = alphabet.index(char)
          index_new = index_old + shift_para     
          end_text += alphabet[index_new]
        else:
          end_text += char
    print(f"The {direction}d text is: {end_text}")
  
#program starts
from art import logo
print(logo)

game_continue = True
while game_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #in case the user enters a shift that is greater than the number of letters in the alphabet
  shift = shift % 26
  #call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
  caesar(text_para=text, shift_para=shift, direction_para=direction)
  #ask the user if they want to restart the cipher program?
  #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
  answer = input("Do you want to restart the cipher program? Type 'yes' or 'no'.\n").lower()
  if answer == "no":
    game_continue = False
    print("Goodbye")
