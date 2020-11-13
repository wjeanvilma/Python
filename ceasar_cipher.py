alphabet = 'abcdefghijklmnopqrstuvwxyz'


def start_program():
    task = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    input_text = input("Enter plain text:\n")
    shift_num = int(input("Enter the shift number:\n"))

    # encrypt function
    def encrypt(message, shift_number):
        encrypted_message = ""
        for i in message:
            encrypted_message += alphabet[(alphabet.index(i)+shift_number) % 26]
        print(f"Your encrypted message is: {encrypted_message}")

    # decrypt function
    def decrypt(message, shift_number):
        decrypted_message = ""
        for i in message:
            decrypted_message += alphabet[(alphabet.index(i)-shift_number) % 26]
        print(f"Your decrypted message is: {decrypted_message}")

    if task.lower() == "encode":
        encrypt(input_text, shift_num)
    elif task.lower() == "decode":
        decrypt(input_text, shift_num)
    else:
        print("Not a valid input")

    # restart program if user wants to continue
    continue_program = input("Type 'yes' to continue or 'no' to stop:\n")
    if continue_program == 'yes':
        start_program()
 
        
# starting the program
start_program()
