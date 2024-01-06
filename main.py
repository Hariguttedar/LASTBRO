import uuid

import streamlit as st
import os
import pathlib
import textwrap
from IPython.display import display, Markdown
import PIL.Image as Pil
from langdetect import detect
from googletrans import Translator
import google.generativeai as genai
import pickle
from med_validators import validations
#
# # Used to securely store your API key
#
#
# id = uuid.uuid4()
#
# with open('chat_history2.pkl', 'rb') as file:
#     loaded_history = pickle.load(file)
#
# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=loaded_history)
#
#
# def translate_text(text, target_language='en'):
#     translator = Translator()
#     try:
#         translation = translator.translate(text, dest=target_language)
#         return translation.text
#     except Exception as e:
#         st.error(f"Error translating text: {e}")
#         return None
#
# def image_prompting():
#     img = Pil.open('./cancer.jpeg')
#     vision_model = genai.GenerativeModel('gemini-pro-vision')
#     user_prompt = input('Enter image prompt here: ')
#     print("Generating response for your image prompt........\nThis process may take a while...\n")
#     response = vision_model.generate_content([user_prompt, img],stream=True)
#     response.prompt_feedback
#     response.resolve()
#     try:
#         # print(response.candidates)
#         print(translate_text(response.text, target_language=user_lang))
#     except Exception as e:
#         print(e)
#
#
# # def main():
# #     GOOGLE_API_KEY = 'AIzaSyBcOPhz5bPwQlgoqC3Ad2z0J5CHDD3Pbpw'
# #     genai.configure(api_key=GOOGLE_API_KEY)
# #     st.title("Generative Chat with Streamlit")
# #
# #     user_lang = st.selectbox(
# #         'Select your language preference:',
# #         ['kn', 'en', 'hi', 'ta', 'te']
# #     )
# #
# #     st.write("Enter 'quit' to end the chat.")
# #     text = "you are yunigma a medical chatbot greet user"
# #     text = st.text_input('You:')
# #
# #     response = chat.send_message(text)
# #
# #     for chunk in response:
# #         en_text = chunk.text
# #         translated_input = translate_text(en_text, target_language=user_lang)
# #         st.write('Model:', translated_input)
# def main():
#     st.set_page_config(page_title="YUNIGMA Medical Chatbot")
#
#     GOOGLE_API_KEY = 'AIzaSyBcOPhz5bPwQlgoqC3Ad2z0J5CHDD3Pbpw'
#     genai.configure(api_key=GOOGLE_API_KEY)
#     st.title("Generative Chat with Streamlit")
#
#     with st.sidebar:
#         st.title('YUNIGMA medical chat')
#         st.markdown('''
#         ## About
#        hi w aoihdoihadas  gr
#        gdvfbdf gn j gjiv  gfdhgn nt   hrth
#
#         ''')
#           # Adjust the number of spaces as needed
#         st.write('DISCLAIMER, this CHATBOT is trained on few medical textbooks.  ')
#     option = st.selectbox(
#         'choose your language ',
#         ('en', 'hi', 'kn'))
#
#     st.markdown(
#         """
#         <style>
#             .chat-container {
#                 display: flex;
#                 flex-direction: column;
#                 height: 400px;
#                 overflow-y: auto;
#                 padding: 10px;
#                 color: white; /* Font color */
#             }
#             .user-bubble {
#                 background-color: #007bff; /* Blue color for user */
#                 align-self: flex-end;
#                 border-radius: 10px;
#                 padding: 8px;
#                 margin: 5px;
#                 max-width: 70%;
#                 word-wrap: break-word;
#             }
#             .bot-bubble {
#                 background-color: #363636; /* Slightly lighter background color */
#                 align-self: flex-start;
#                 border-radius: 10px;
#                 padding: 8px;
#                 margin: 5px;
#                 max-width: 70%;
#                 word-wrap: break-word;
#             }
#         </style>
#         """
#         , unsafe_allow_html=True)
#
#     conversation = st.session_state.get("conversation", [])
#
#     def translate_text(text, target_language='en'):
#         translator = Translator()
#         try:
#             translation = translator.translate(text, dest=target_language)
#             return translation.text
#         except Exception as e:
#             print(f"Error translating text: {e}")
#             return None
#
#     query = st.text_input("Ask your question here():", key="user_input")
#     if st.button("Get Answer"):
#         if query:
#             answer = chat.send_message(query)
#             answer = answer.text
#             answer = translate_text(answer, option)
#             conversation.append({"role": "bot", "message": answer})
#             st.session_state.conversation = conversation
#         else:
#             st.warning("Please input a question.")
#
#     chat_container = st.empty()
#     chat_bubbles = ''.join([f'<div class="{c["role"]}-bubble">{c["message"]}</div>' for c in conversation])
#     chat_container.markdown(f'<div class="chat-container">{chat_bubbles}</div>', unsafe_allow_html=True)
#
# if __name__ == '__main__':
#     main()
import streamlit as st
import PIL.Image as Pil
from googletrans import Translator
import google.generativeai as genai
import pickle

# Used to securely store your API key
# ...

id = uuid.uuid4()

loaded_history = []

# File paths for the two history files
file_paths = ['chat_history1.pkl', 'chat_history2.pkl']

# Loop through the file paths and load each history file
for file_path in file_paths:
    with open(file_path, 'rb') as file:
        # Load the history from the current file and extend the loaded_history list
        loaded_history.extend(pickle.load(file))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=loaded_history)

def translate_text(text, target_language='en'):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        st.error(f"Error translating text: {e}")
        return None

def validate_queries(user_message):
    splitted_user_message = user_message.split()
    for word in splitted_user_message:
        if word in validations:
            return False
    return True

def main():
    st.set_page_config(page_title="YUNIGMA Medical Chatbot")

    GOOGLE_API_KEY = 'AIzaSyBcOPhz5bPwQlgoqC3Ad2z0J5CHDD3Pbpw'
    genai.configure(api_key=GOOGLE_API_KEY)
    st.title("Yunigma Medical Chatbot")

    with st.sidebar:
        st.title('YUNIGMA medical chat')
        st.markdown('''
        ## About
        Hi i am Yunigma Medical Chat Bot
        ''')
        # Adjust the number of spaces as needed
        st.write('DISCLAIMER, this CHATBOT is trained on few medical textbooks.  ')

    option = st.selectbox(
        'choose your language ',
        ('en', 'hi', 'kn', 'ta', 'te'))

    st.markdown("""
        <style>
            #file-upload {
                display: block;
                margin: 10px 0;
            }
            .chat-container {
                display: flex;
                flex-direction: column;
                height: 400px;
                overflow-y: auto;
                padding: 10px;
                color: white; /* Font color */
            }
            .user-bubble {
                background-color: #007bff; /* Blue color for user */
                align-self: flex-end;
                border-radius: 10px;
                padding: 8px;
                margin: 5px;
                max-width: 70%;
                word-wrap: break-word;
            }
            .bot-bubble {
                background-color: #363636; /* Slightly lighter background color */
                align-self: flex-start;
                border-radius: 10px;
                padding: 8px;
                margin: 5px;
                max-width: 70%;
                word-wrap: break-word;
            }
        </style>
        """, unsafe_allow_html=True)

    conversation = st.session_state.get("conversation", [])

    # File upload for the image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Text input for user's prompt
    #user_promptt = st.text_input("Enter your text prompt here:")
    

    user_prompt = st.text_input("Enter your prompt here:")

    if st.button("Generate Response"):
        if uploaded_file and user_prompt:
            # Open and display the uploaded image
            image = Pil.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Process the image and prompt
            vision_model = genai.GenerativeModel('gemini-pro-vision')
            st.write("Generating response for your image prompt...\nThis process may take a while...\n")
            response = vision_model.generate_content([user_prompt, image])
            #response.prompt_feedback
            response.resolve()

            # Translate and display the response
            try:
                translated_response = translate_text(response.text, target_language=option)
                conversation=[]
                conversation.append({"role": "bot", "message": translated_response})
                st.session_state.conversation = conversation
                st.write('Model Response:', translated_response)
            except Exception as e:
                st.error(f"Error translating text: {e}")

        elif user_prompt: 
            response = chat.send_message(user_prompt)
            if validate_queries(user_prompt):
                try:
                    translated_response = translate_text(response.text, target_language=option)
                    conversation=[]
                    conversation.append({"role": "bot", "message": translated_response})
                    st.session_state.conversation = conversation
                    st.write('Model Response:', translated_response)
                except Exception as e:
                    st.error(f"Error translating text: {e}")
            else:
                st.write(translate_text("I am sorry! I am a medical chatbot. Try asking questions relevent to medical field.",
                                         target_language=option))
        else:
            st.warning("Please give any prompt.")
    #
    # chat_container = st.empty()
    # chat_bubbles = ''.join([f'<div class="{c["role"]}-bubble">{c["message"]}</div>' for c in conversation])
    # chat_container.markdown(f'<div class="chat-container">{chat_bubbles}</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
