import streamlit as st
from io import StringIO

#### Caesar Cipher Encrypt & Decrypt
class caesarCipher:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # @staticmethod
    def decrypt(userInput, key):
        userInput = ''.join(c.lower() for c in userInput if c.isalpha())
        output = ''
        for c in userInput:
            if c in caesarCipher.alpha:
                output += caesarCipher.alpha[(caesarCipher.alpha.index(c) - key) % len(caesarCipher.alpha)]
        return output   
    # @staticmethod
    def encrypt(userInput, key):
        userInput = ''.join(c.lower() for c in userInput if c.isalpha())
        output = ''
        for c in userInput:
            if c in caesarCipher.alpha:
                output += caesarCipher.alpha[(caesarCipher.alpha.index(c) + key) % len(caesarCipher.alpha)]
        return output   

#### Vigenere Cipher Encrypt & Decrypt
class vigenereCipher:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # @staticmethod
    def decrypt(userInput, key):
        userInput = ''.join(c.lower() for c in userInput if c.isalpha())
        output = ''
        for (i, c) in enumerate(userInput):
            i = i % len(key)
            output += vigenereCipher.alpha[(vigenereCipher.alpha.index(c) - vigenereCipher.alpha.index(key[i % len(key)])) % len(vigenereCipher.alpha)]
        return output
    # @staticmethod
    def encrypt(userInput, key):
        userInput = ''.join(c.lower() for c in userInput if c.isalpha())
        output = ''
        for(i, c) in enumerate(userInput):
            i = i%len(key)
            output += vigenereCipher.alpha[(vigenereCipher.alpha.index(c) + vigenereCipher.alpha.index(key[i % len(key)])) % len(vigenereCipher.alpha)]
        return output

# Streamlit UI
st.title("Encryption & Decryption App")
st.write("Choose a cipher and perform encryption or decryption.")
st.write("Either upload a .txt file or enter your text in the textbox below")

# Input fields
file = st.file_uploader(label="Text File", type="txt", accept_multiple_files=False, label_visibility="visible")
if file is not None:
    file_string = StringIO(file.getvalue().decode('utf-8'))
    text = st.text_area(label="File Contents: ", value=file_string.read())
else:
    text = st.text_area("Enter your text:")
cipher_choice = st.selectbox("Choose a cipher:", ["Caesar Cipher", "Vigenere Cipher"]) 
action = st.radio("Action:", ["Encrypt", "Decrypt"])

if cipher_choice == "Caesar Cipher":
    key = st.number_input("Enter the shift key (integer):", min_value=1, max_value=25, step=1, value=3)
elif cipher_choice == "Vigenere Cipher":
    key = st.text_input("Enter the keyword:", value="key")

# Button to process encryption/decryption
if st.button("Submit"):
    
    if cipher_choice == "Caesar Cipher":
        if action == "Encrypt":
            result = caesarCipher.encrypt(text, key)
        else:
            result = caesarCipher.decrypt(text, key)
    
    elif cipher_choice == "Vigenere Cipher":
        if action == "Encrypt":
            result = vigenereCipher.encrypt(text, key)
        else:
            result = vigenereCipher.decrypt(text, key)
    st.write(f"**Result:** {result}")

