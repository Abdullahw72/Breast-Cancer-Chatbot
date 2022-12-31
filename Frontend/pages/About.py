import streamlit as st
from streamlit_chat import message
import requests
import json

BACKGROUND_COLOR = 'white'
COLOR = 'black'


def Intro():
    st.image('images/Logo.jpg', width=675)
    st.header("Welcome to our Chatbot Program")
    st.subheader("Data Source")
    st.write("Medscape, LLC, is accredited by the Accreditation Council for Continuing Medical Education (ACCME) as a provider of certified physician education, by the American Nurses Credentialing Center (ANCC) as a provider of continuing nursing education, and by the Accreditation Council for Pharmacy Education (ACPE) as a provider of continuing pharmacy education.")


def Progress():
    st.subheader("Progress")
    col1, col2, col3  = st.columns(3)
    with col1:
        st.image('images/Week2.jpg', width=200, caption="Week 1 & Week 2")
        st.write('https://drive.google.com/drive/folders/1BsQOgBxbPbty47_ysfW8U4cumNjA9gRO')
    with col2:
        st.image('images/Week4.jpg', width=200, caption="Week 3 & Week 4")
        st.write('https://drive.google.com/drive/folders/1BsQOgBxbPbty47_ysfW8U4cumNjA9gRO')
    with col3:
        st.image('images/Week5.jpg', width=200, caption="Week 5")
        st.write('https://drive.google.com/drive/folders/1BsQOgBxbPbty47_ysfW8U4cumNjA9gRO')
    st.subheader("Source Preview")
    st.image('images/Questions.JPG', width=675, caption = 'Source Questions')
    st.subheader("Dataset Preview")
    st.image('images/Dataset.JPG', width=675, caption = 'Dataset')


def Developers():
    st.subheader("Developed By")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image('images/Abdullah.jpg', width=150, caption="Abdullah Abdul Wahid")
    with col2:
        st.image('images/Neeraj.jpg', width=150, caption="Neeraj Prakash")
    with col3:
        st.image('images/Ahmed.jpg', width=150, caption="Ahmed Ashraf")
    with col4:
        st.image('images/Hasnain.jpg', width=150, caption="Hasnain Ali")

Intro()
Progress()
Developers()