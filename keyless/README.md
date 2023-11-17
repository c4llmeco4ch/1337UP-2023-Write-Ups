# Keyless

## Category

Crypto

## Tools Used

Python 3

## Key Takeaways

- Undoing simple cryptographic function is simply a matter of reversing the process of encryption

## Question

My friend made a new encryption algorithm. Apparently it's so advanced, you don't even need a key!

_keyless.zip_ is provided

## Process

Unzipping the provided file, we are presented with an encrypted file and a python script, encrypt.py. Taking a quick glance at the file, we can understand the basics of what is happening here:

1. Acquire the passphrase
2. Encrypt it
3. Save it to the file

As such, the process we must undertake is the exact opposite:

1. Read the encrypted message from the file
2. Decrypt it
3. Spit out the decrypted flag

To do this, we need to better understand what is happening in the function, encrypt:

```py3
def encrypt(message):
    encrypted_message = ""
    for char in message:
        a = (ord(char) * 2) + 10
        b = (a ^ 42) + 5
        c = (b * 3) - 7
        encrypted_char = c ^ 23
        encrypted_message += chr(encrypted_char)
    return encrypted_message
```

Essentially, we are taking each character from the message (`for char in message:`), turning it into a number representing the ASCII character (`ord(char)`), and messing with it before reverting it back into a character and adding it to the new, jumbled message (`encrypted_message += chr(encrypted_char)`).

Thus, to reverse this process, we are going to flip the function vertically before reversing the order of operations on each line to unscramble our flag.

```py3
def decrypt(message):
    decrypted_message = ""
    for char in message:
        c = ord(char) ^ 23 # reverse c ^ 23
        b = (c + 7) // 3  # reverse (b * 3) - 7
        a = (b - 5) ^ 42  # reverse (a ^ 42) + 5
        val = (a - 10) // 2 # reverse (ord(char) * 2) + 10
        decrypted_message += chr(val)
    return decrypted_message
```

With our reversing function complete, all we need to do is add some code to extract our encrypted message from the provided file and print out the result of our decryption.

```py3
with open("flag.txt.enc") as file:
    decrypted_flag = decrypt(file.read())
    print(decrypted_flag)
```

With these lines of code saved, we can run our creation in the same directory as the encrypted text to receive our flag: `INTIGRITI{m4yb3_4_k3y_w0uld_b3_b3773r_4f73r_4ll}`!