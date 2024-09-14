import streamlit as st

# Function to generate cold email based on inputs
def generate_email(name, company, purpose, custom_message, closing):
    email_template = f"""
    Hi {name},
    
    I hope this message finds you well. My name is [Your Name], and I'm reaching out to discuss {purpose}. 
    I’ve been following {company} closely and I believe that there’s a great opportunity for us to collaborate 
    or find ways I can add value to your organization.
    
    {custom_message}
    
    Let me know if you’d be open to having a conversation. Looking forward to hearing your thoughts.

    Best regards,
    [Your Name]
    
    {closing}
    """

    return email_template

# Streamlit UI layout
def main():
    st.title("Cold Email Generator")
    st.write("Generate personalized cold emails quickly and easily!")

    # User input fields
    name = st.text_input("Recipient's Name", value="John Doe")
    company = st.text_input("Company Name", value="Acme Corp")
    purpose = st.text_input("Purpose (e.g., partnership, job inquiry)", value="partnership opportunity")
    custom_message = st.text_area("Custom Message", value="I believe my experience in [your expertise] can contribute significantly to your goals.")
    closing = st.text_input("Closing", value="Looking forward to connecting.")

    if st.button("Generate Email"):
        email = generate_email(name, company, purpose, custom_message, closing)
        st.subheader("Generated Email:")
        st.text_area("Cold Email", value=email, height=300)

if __name__ == '__main__':
    main()
