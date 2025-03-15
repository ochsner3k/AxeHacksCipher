import streamlit as st
from io import StringIO
import pandas as pd


def custom_warning(message):
    st.markdown(
        f"""
        <div style="
            display: flex;
            align-items: center;
            padding: 10px;
            border-radius: 5px;
            background-color: #B3005E;  
            color: white;
            font-weight: bold;
            margin-bottom: 15px;
            ">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="white" style="margin-right: 10px;">
                <path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/>
            </svg>
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <style>
        .stApp {
            background-color: #DDD8E6;
            base="light"
            primaryColor="#B3005E"

        }
    </style>
    """,
    unsafe_allow_html=True
)
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

#### Brute Force Caesar Algo
def caesarBrute(userInput):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    userInput = ''.join(c.lower() for c in userInput if c.isalpha())
    output = []
    for shift in range(1, 26):  
        decrypted_text = ''
        for c in userInput:
            if c in alpha:
                decrypted_text += alpha[(alpha.index(c) - shift) % len(alpha)]
        output.append(decrypted_text)
    
    df = pd.DataFrame(output, index=[ i for i in range(0, 25)]) 
    return df


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

if st.button("Submit"):
    if text.strip():  
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
    else:
         custom_warning("Please enter text to decrypt.")

if cipher_choice == "Caesar Cipher":
    col1, col2, col3 = st.columns([1, 2, 1]) 

    if "show_brute_popup" not in st.session_state:
        st.session_state.show_brute_popup = False 

    with col2:
        if st.button("*No shift value? Try our brute force algorithm!*", key="brute_force_button"):
            st.session_state.show_brute_popup = True 

    if st.session_state.show_brute_popup:
        st.markdown("### Brute Force Caesar Cipher")
        user_text = st.text_area("Enter the text to decrypt:", key="brute_text_input")
        
        if st.button("Submit", key="brute_submit"):
            if user_text.strip():  
                result_df = caesarBrute(user_text).T  
                
                st.text(result_df.to_string(index=False, header=True)) 
            else:
                custom_warning("Please enter text to decrypt.")
        if st.button("Close", key="close_popup"):
            st.session_state.show_brute_popup = False 
