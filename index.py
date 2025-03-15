import streamlit as st
# Set page title and layout
st.set_page_config(page_title="Home | Encryption App", page_icon="🔐", layout="centered")

# Custom CSS for background and styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #DDD8E6;
            text-align: center;
        }
        .main-title {
            font-size: 40px;
            font-weight: bold;
            color: #333;
        }
        .subtext {
            font-size: 18px;
            color: #555;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;  /* Adds spacing between buttons */
            margin-top: 20px;
        }
        .custom-button {
            background-color: #FFFFFF;
            color: black;
            padding: 12px 24px;
            border: 2px solid #333;
            border-radius: 5px;
            font-size: 18px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
        }
        .custom-button:hover {
            background-color: #bbb;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page content
st.markdown('<h1 class="main-title">🔐 Encryption & Decryption App</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtext">Secure your messages with different encryption techniques.</p>', unsafe_allow_html=True)
st.markdown('<h4> Welcome to Cipher Hub!</h4>', unsafe_allow_html=True)
st.markdown('<h6>Explore the power of encryption and the world of secure communication! A cipher is a tool used in cryptography to transform readable data into unreadable data to secure sensitive information. The main reason for using a cipher is to protect data from unauthorized access</h6>', unsafe_allow_html=True)



# Buttons placed side by side using flexbox
st.markdown(
    """
    <div class="button-container">
        <a href="app" class="custom-button">🔒 Start Encrypting</a>
        <a href="rsa" class="custom-button">📖 RSA</a>
    </div>
    """,
    unsafe_allow_html=True
)