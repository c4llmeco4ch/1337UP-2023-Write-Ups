def decrypt(message):
    decrypted_message = ""
    for char in message:
        c = ord(char) ^ 23 # reverse c ^ 23
        b = (c + 7) // 3  # reverse (b * 3) - 7
        a = (b - 5) ^ 42  # reverse (a ^ 42) + 5
        val = (a - 10) // 2 # reverse (ord(char) * 2) + 10
        decrypted_message += chr(val)
    return decrypted_message


with open("flag.txt.enc") as file:
    decrypted_flag = decrypt(file.read())
    print(decrypted_flag)