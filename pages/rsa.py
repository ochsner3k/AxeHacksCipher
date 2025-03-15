import streamlit as st

st.markdown(
    """
    <style>
        .stApp {
            background-color: #DDD8E6;
        }
    </style>
    """,
    unsafe_allow_html=True
)

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class rsaClass:
    keySize = 1024
    publicExponent = 65537

    privateKey = rsa.generate_private_key(public_exponent = publicExponent, key_size = keySize)
    publicKey = privateKey.public_key()

    pem_privateKey = privateKey.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption())
    pem_privateKey_str = pem_privateKey.decode('utf-8')
    pem_publicKey = publicKey.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
    pem_publicKey_str = pem_publicKey.decode('utf-8')

#Streamlit UI
st.title("RSA Key Generation")
st.write("Generate and save a public-private key pair.")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button("Generate New Keys", on_click=click_button)

if st.session_state.clicked:
    st.write("Public Key: " + rsaClass.pem_publicKey_str)
    st.write("Private Key: " + rsaClass.pem_privateKey_str)