import streamlit as st
import random
import pandas as pd

# Read the DataFrame outside of the Streamlit app
df = pd.read_csv('WORDS.csv')

# print(df)

# Function to generate a set of numbers within a given range
def generate_list(start, stop):
    number_set = {num for num in range(start, stop + 1)}
    return number_set

# Initialize session states for org_list, number_to_be_removed, and generate_random
if 'org_list' not in st.session_state:
    # Generate the initial org_list based on the entire DataFrame length
    st.session_state.org_list = generate_list(0, len(df) - 1)

if 'number_to_be_removed' not in st.session_state:
    st.session_state.number_to_be_removed = None

if 'generate_random' not in st.session_state:
    st.session_state.generate_random = False

# Slider widget to select a range of values
values = st.slider(
    'Select a range of values',
    1, len(df), (1, 3))
st.write('Values:', values)

# Button to reset the session state
reset = st.button("Reset", type="primary")
if reset:
    st.session_state.org_list = generate_list(values[0], values[1])

# Button to generate a random number
if st.button("Generate Random Number"):
    st.session_state.number_to_be_removed = random.choice(list(st.session_state.org_list))
    st.session_state.generate_random = True

SEE_MEANING = st.button("SEE MEANING")

# Logic to handle user responses (YES or NO)
if st.session_state.generate_random:
    # st.subheader(f"Word: {df[st.session_state.generate_random]}")

    st.title(df['words'][st.session_state.number_to_be_removed - 1])

    if SEE_MEANING and len(st.session_state.org_list) - 1 != 0:
        st.header(df['meaning'][st.session_state.number_to_be_removed - 1])

        # Image Path
        image_path = f'images/{st.session_state.number_to_be_removed}.png'
        # print(image_path)
        st.image(image_path, caption='Local PNG Image', use_column_width=True)
        st.write(df['sentence'][st.session_state.number_to_be_removed - 1])


    YES = st.button("YES")
    if YES and len(st.session_state.org_list) - 1 != 0:
        st.session_state.org_list.remove(st.session_state.number_to_be_removed)
        st.session_state.generate_random = False
    

# Display the generated number if it exists
if st.session_state.number_to_be_removed is not None:
    st.write("Number generated: " + str(st.session_state.number_to_be_removed))

# Display the current state of the org_list
st.write(st.session_state.org_list)
