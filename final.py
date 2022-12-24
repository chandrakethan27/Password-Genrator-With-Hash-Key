import random
from tkinter import * 
# pip install pyperclip
root = Tk()
root.geometry("1000x500")
root.configure(bg='#73b9d7')
passwrd = StringVar()
letters_m = IntVar()
encrypt  = StringVar()
text = StringVar()
decrypt  = StringVar()
letters_m.set(0)
text.set("")
decrypt.set("")
letter = []
number = []
capital = []
special = []
password = []
def auto():
    global ans
    ans = ""
    complete_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    random.shuffle(complete_characters)
    for i in range(letters_m.get()):
       ans += random.choice(complete_characters)
    passwrd.set(ans)
    file1 = open('decrypted.txt', 'w')
    s = ans
    file1.write(s)

def myownhash():
    global d
    global k
    k = ''
    res = ''.join(format(i, '08b') for i in bytearray(ans, encoding ='utf-8'))
    res = str(res)
    a = res.replace('0', 'i')
    b = a.replace('1', 'h')
    d = list(b)
    d.append(len(b)*len(b)-69)
    for i in range(len(d)):
        if i%2 == 0:
            d.insert(i, 'o')
    for i in range(len(d)):
        k +=str(d[i])
    file1 = open('encrypted.txt', 'w')
    s = k
    file1.write(s)
    encrypt.set(k)
    
def decrypter():
    global d
    global ascii_text
    ascii_text = ""
    d = list(text.get())
    binary = ""
    d.pop(-1)
    for i in range(len(d)):        
        if d[i]== 'o':
            continue
        else:
            if d[i] == 'h':
                binary+='1'
            elif d[i] == 'i':
                binary+='0'
    binary_int = int(binary, 2)
    # Getting the byte number
    byte_number = (binary_int.bit_length() + 7 )// 8
    # Getting an array of bytes
    binary_array = binary_int.to_bytes(byte_number, "big")
    # Converting the array into ASCII text
    ascii_text = str(binary_array.decode())
    decrypt.set(ascii_text)
    file1 = open('decrypted.txt', 'w')
    s = binary_array.decode()
    file1.write(s)

Label(root, text="Strong Password Generator", font="Helvetica 40 bold", bg='#73b9d7').pack()
Label(root, text="by Chandrakethan", font="Helvetica 20 ",bg='#73b9d7').pack()
Label(root, text="Enter the length to get password",bg='#73b9d7').pack(pady=3)
Entry(root, textvariable=letters_m,).pack(pady=3)
Button(root, text="Tap to get", command=auto).pack(pady=7)
Entry(root, textvariable=passwrd).pack(pady=3)
Button(root, text="Encrypted format",command=myownhash).pack(pady=7)
Entry(root, textvariable=encrypt).pack(pady=3)
Label(root, text="Enter encrypted text",bg='#73b9d7').pack(pady=3)
Entry(root, textvariable=text).pack(pady=3)
Button(root, text="Tap to get", command=decrypter).pack(pady=7)
Entry(root, textvariable=decrypt).pack(pady=3)
root.mainloop()