import random
import streamlit as st

st.write("Hello! What is your name?")
name = st.text_input("Enter your name:")

if name:
    num = random.randint(0, 30)
    st.write(f"{name}, I am thinking of a number between 0 and 30. Can you guess it?")
  
    if "guessed" not in st.session_state:
        st.session_state.guessed = False
        st.session_state.num = num
    guess = st.number_input("Enter your guess:", min_value=0, max_value=30, step=1)

if st.button("check"):
    if not st.session_state.guessed:
        if guess < st.session_state.num:
            st.write("Your guess is lower, try again!")
            
        elif guess > st.session_state.num:
            st.write("Your guess is higher, try again!")
        else:
            st.write("Your guess is correct!")
            st.session_state.guessed = True

