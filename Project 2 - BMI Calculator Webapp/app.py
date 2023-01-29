
'''
    HDLC - Python Internship
    Final - Project
    Name - Mohit Jaiswal
    Problem - Design a webpage which has following controls 
    1. Name (textbox) 
    2. Gender(Radio button) 
    3. Age(number_input) 
    4. Address (textbox) 
    5. Hobbies (checkbox) 
    6. Weight in kg (number_input) 
    7. Height in cms(number_input) 
    Get the details of a person from the above controls and calculate the BMI using the height and weight
'''

import streamlit as st
st.set_page_config(page_title="BMI Calculator by Mohit Jaiswal", page_icon=":tada:", layout="wide")



# -----HEADER SECTION-----
st.title("BMI Calculator")
st.write("By Mohit Jaiswal")
st.write("---")



# -----Taking Input form the User------

st.text_input("Enter Your Name: ")

st.radio(label="Gender: ", options=("Male", "Female"))

st.number_input("Enter Your Age: ", value=False)

st.text_area("Address: ")

st.write("Hobbies:")
st.checkbox("Movies")
st.checkbox("Music")
st.checkbox("Playing")
st.checkbox("Singing")
st.checkbox("Coding")
st.checkbox("Travel")

weight=st.number_input("Enter Your Weight (Kg): ", step=1, value=False)

height=st.number_input("Enter Your Height (cm): ", step=1, value=True)

BMI=weight/(height)**2
BMI=BMI*10000

st.success(f"Your BMI Value is {BMI} kg/m^2")

if BMI>=18.5 and BMI<=24.9:
    st.success(f"You are HEALTHY 🥳")

else:
    st.warning(f"You are UNHEALTHY 🥺")


# -----ABOUT ME------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2);

    with left_column:
        st.header("About Me -")
        st.write(
            """
            I am Mohit Jaiswal, 🙋🏻‍♀️
            Second Year B.Tech Student pursuing Computer Engineering @ MIT Academy of Engineering, Pune.
            Open for Project Collaborations and Internship Oppurtunities. 😇
            """
        )



# ------CONTACT ME-------
with st.container():
    left_column, right_column = st.columns(2);

    with left_column:
        st.header("Connet with Me -")
        st.write("[LinkedIn](https://www.linkedin.com/in/mohitjaiswal28/)")
        st.write("[GitHub](https://github.com/mohitjaiswal28)")
        st.write("[Instagram](https://www.instagram.com/mohitjaiswal.in/)")
        st.write("[Twitter](https://twitter.com/mohitjaiswal28_)")



# ------COPYRIGHT-------
st.write("---")
st.write("Ⓒ 2023. Mohit Jaiswal")