import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


def app():
    col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
    with col1:
        st.image('./assets/fraud-alert.png', width=230)
    with col2:
        st.title('Atif Raja')
        st.write(
            'Healthcare Data Analyst, health information manager and coding instructor for kids'
        )
        st.markdown(
            """
            <style>
            .mail-button {
                background-color: ##4FA552;
                border: none;
                color: #000;
                padding: 0.375rem 0.75rem;
                font-size: 1rem;
                border-radius: 0.25rem;
                cursor: pointer;
                text-align: center;
                text-decoration: none;
                display: inline-block;
            }
            .mail-button:hover {
                background-color: #e0e3e8;
            }
            </style>
            <a href="mailto:atif738738@gmail.com" class="mail-button">✉️ Contact Me</a>
            """,
            unsafe_allow_html=True,
        )

    # --- Experience and Qualification
    st.write('\n')
    st.subheader('Experience & Qualifications', anchor=False)
    st.write(
    '''
     - 5 Years experience extracting actional business insights from data
     - Strong hands-on experience and knowledge in Python, SQL, Tableau, SPSS, and Spreadsheets
     - Strong background in Biostatistical principles and their applications
     - Ability to take initiatives and strong communication skills
    '''
    )

    # --- SKILLS -- 
    st.write('\n')
    st.subheader('Hard Skills', anchor=False)
    st.write(
    '''
     - Programming: Python (Scikit-learn, Pandas, Seaborn), SQL, SPSS
     - Data Visualization: Tableau, Seaborn, and Excel
     - Modeling: Logistic Regression, Linear Regression, SGBoosting
     - Database: SQL Server, MySQL
    '''
    )

    st.write('\n')
    st.subheader('Soft Skills', anchor=False)
    st.write(
    '''
     - Problem-solving
     - Initiative
     - Communication
     - Leadership
     - Teamwork
    '''
    )

    


