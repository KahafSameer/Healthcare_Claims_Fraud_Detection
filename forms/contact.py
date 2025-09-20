import streamlit as st

def contact_form():
    st.header("Get in Touch!")
    st.write("Please fill out the form below to send a message.")

    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submit_button = st.form_submit_button(label='Send Message')

        if submit_button:
            if not name or not email or not message:
                st.warning("Please fill out all fields before sending.")
            else:
                st.success(f"Thank you, {name}! Your message has been sent.")
                # In a real application, you would add code here to handle the form submission,
                # such as sending an email or saving the message to a database.