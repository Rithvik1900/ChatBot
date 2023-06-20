import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat
sign = Login('rithvik_vankadari@srmap.edu.in', 'Pranay$00077')
cookies = sign.login()

# Save cookies to usercookies/<email>.json
sign.saveCookies()
st.set_page_config(page_title="Strangify-Chat")

# Sidebar contents
with st.sidebar:
    st.title('🤗💬 Stangify Chat')
    st.markdown('''
    ## About
    Are you Feeling Stressed? Please share with us, we can help you!:
    - [Website](https://www.strangify.com/)
    - [Contact](https://www.strangify.com/contact-us)
    - [About us](https://www.strangify.com/about-us)
    ''')
    add_vertical_space(5)
   

# Generate empty lists for generated and past.
## generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = []

# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chat_history_ids = hugchat.ChatBot(cookies=cookies.get_dict())
    response = chat_history_ids.chat(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))