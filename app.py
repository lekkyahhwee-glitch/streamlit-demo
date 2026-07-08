import streamlit as st
from PIL import Image

# App title
st.title("Kyah Hwee's First App")

# Header and subheader
st.header("Welcome to My App")
st.subheader("An interactive Python web app")

# Display text and markdown
st.text("This is plain text.")
st.markdown("**This is bold markdown text.**")

# Display status messages
st.success("Operation successful!")
st.info("Here is some information.")
st.warning("This is a warning.")
st.error("An error occurred.")

# Image display
img = Image.open("dog.jpg")
st.image(img, width=200)

# Checkbox
if st.checkbox("Show message"):
   st.write("Checkbox is checked!")
   
# Radio button
gender = st.radio("Select Gender:", ['Male', 'Female'])
st.success(f"Selected: {gender}")
if gender == "Male":
    st.write("You have chosen Male")
else:
    st.write("You have chosen Female")

# Selectbox - using a list variable instead of hardcoded values
hobbies = ["Dancing", "Reading", "Sports", "Gaming",
           "Cooking", "Music", "Photography", "Gardening"]

hobby = st.selectbox("Select your main hobby:", hobbies)
st.write("Your main hobby is:", hobby)

# Multiselect - lets the user pick more than one hobby
selected = st.multiselect("Pick all your hobbies:", hobbies)

# Loop through the selected hobbies and display each one
if selected:
    st.write(f"You selected {len(selected)} hobbies:")
    for h in selected:
        st.write(f"  - {h}")
else:
    st.info("No hobbies selected yet.")

# Dictionary mapping each hobby to a fun fact
hobby_facts = {
    "Dancing": "Dancing burns about 300 calories per hour.",
    "Reading": "The average person reads 12 books a year.",
    "Sports": "Regular exercise improves memory by 20%.",
    "Gaming": "The global gaming industry is worth $180 billion.",
    "Cooking": "The world's oldest recipe is over 4,000 years old.",
}

# Get the list of hobbies from the dictionary keys
hobbies = list(hobby_facts.keys())

# Selectbox using the dictionary keys as options
hobby = st.selectbox("Select a Hobby to read up more about it!", hobbies)

# Look up the fun fact from the dictionary
if hobby in hobby_facts:
    st.info(hobby_facts[hobby])
else:
    st.warning("No fun fact available for this hobby yet.")


# Slider
level = st.slider("Choose a level", 1, 5)
st.write(f"Selected level: {level}")

# Text input
name = st.text_input("Enter your name", "Type here...")
if st.button("Submit"):
   st.success(f"Hello, {name.title()}!")
