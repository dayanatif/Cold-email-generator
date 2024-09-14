import streamlit as st

# Function to generate cold email based on inputs
def generate_email(sender_name, recipient_name, company, purpose, custom_message, closing):
    email_template = f"""
    Hi {recipient_name},
    
    I hope this message finds you well. My name is {sender_name}, and I'm reaching out to discuss {purpose}. 
    I’ve been following {company} closely and believe that there’s a great opportunity for us to collaborate 
    or find ways I can add value to your organization.
    
    {custom_message}
    
    Let me know if you’d be open to having a conversation. Looking forward to hearing your thoughts.

    Best regards,
    {sender_name}
    
    {closing}
    """
    return email_template

# Streamlit UI layout with black background and white text
def main():
    # Adding a logo (You can replace this with a custom image URL)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/1200px-Markdown-mark.svg.png", width=100)

    # Title with white text
    st.markdown("<h1 style='text-align: center; color: white;'>Cold Email Generator</h1>", unsafe_allow_html=True)
    st.write("<p style='color:white;'>Generate personalized cold emails quickly and easily!</p>", unsafe_allow_html=True)

    # Set black background and white text
    st.markdown(
        """
        <style>
        body {
            background-color: black;
        }
        .main {
            background-color: black;
        }
        .stTextInput label, .stTextArea label {
            color: white;
        }
        .stTextInput div, .stTextArea div {
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

    # User input fields
    sender_name = st.text_input("Your Name", value="Jane Smith")
    recipient_name = st.text_input("Recipient's Name", value="John Doe")
    company = st.text_input("Company Name", value="Acme Corp")
    purpose = st.text_input("Purpose (e.g., partnership, job inquiry)", value="partnership opportunity")
    custom_message = st.text_area("Custom Message", value="I believe my experience in [your expertise] can contribute significantly to your goals.")
    closing = st.text_input("Closing", value="Looking forward to connecting.")

    # Button with white text and blue background
    st.markdown(
        """
        <style>
        .stButton > button {
            background-color: #1ABC9C;
            color: white;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
        }
        </style>
        """, unsafe_allow_html=True)

    if st.button("Generate Email"):
        email = generate_email(sender_name, recipient_name, company, purpose, custom_message, closing)
        st.subheader("Generated Email:")
        st.text_area("Cold Email", value=email, height=300)

if __name__ == '__main__':
    main()
