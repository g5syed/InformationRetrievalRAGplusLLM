import os
import streamlit as st
import pdfplumber
import requests
from tenacity import retry, wait_random_exponential, stop_after_attempt
import openai
import re
# Set the OpenAI API Key
#api_key = 0 # github not letting me upload code with API key
#openai.api_key = api_key
GPT_MODEL = "gpt-4o"

keywords = [
    "high torque", "vibration", "high vibration", "excessive vibration",
    "failure", "equipment failure", "system failure", "damage ",
    "bit damage", "tool damage", "slow penetration rate", "torque and drag",
    "spike in torque", "stuck pipe", "high pressure", "low pressure",
    "kick", "gas kick", "lost circulation", "borehole instability",
    "mse", "drag", "high rpm", "low rpm", "temperature spike",
    "mud loss", "bop issues", "chatter", "whirl", "stick-slip",
    "washout", "twist off", "pump failure", "severe wear"
]

def highlight_keywords(text, keywords):
    for keyword in keywords:
        text = re.sub(f"(?i)({keyword})", r'<mark>\1</mark>', text)
    return text

def extract_sentences_with_keywords(text, keywords):
    sentences_with_keywords = []
    sentences = re.split(r'(?<=[.!?]) +', text)
    for sentence in sentences:
        for keyword in keywords:
            if re.search(f"(?i){keyword}", sentence):
                sentences_with_keywords.append(sentence)
                break
    return sentences_with_keywords


@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(messages, tools=None, tool_choice=None, model=GPT_MODEL):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + openai.api_key,
    }
    json_data = {"model": model, "messages": messages}
    if tools is not None:
        json_data.update({"tools": tools})
    if tool_choice is not None:
        json_data.update({"tool_choice": tool_choice})
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        return response.json()
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e

def main():
    st.title("DRAKE AI")

    options_pdf = {
        "02July2021": "02July2021.pdf",
        "03July2021": "03July2021.pdf",
        "04July2021": "04July2021.pdf",
        "05July2021": "05July2021.pdf",
        "06July2021": "06July2021.pdf",
        "27June2021": "27June2021.pdf",
        "28June2021": "28June2021.pdf",
        "30June2021": "30June2021.pdf"
    }

    selected_option = st.sidebar.selectbox("Select Date", list(options_pdf.keys()))

    if 'selected_option' not in st.session_state:
        st.session_state['selected_option'] = None

    # Clear chat history when a new file is selected
    if selected_option != st.session_state['selected_option']:
        st.session_state['selected_option'] = selected_option
        st.session_state['chat_history'] = []

    selected_pdf = options_pdf[selected_option]
    pdf_path = os.path.join("reports", selected_pdf)
    
    raw_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            raw_text += page.extract_text() + "\n"

    sentences_with_keywords = extract_sentences_with_keywords(raw_text, keywords)
    if sentences_with_keywords:
        st.write("### DRILLING DYSFUNCTION DETECTED")
        for sentence in sentences_with_keywords:
            st.markdown(f"- {highlight_keywords(sentence, keywords)}", unsafe_allow_html=True)

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    query = st.text_input("Ask ChatBot:")

    if st.button("Send"):
        if query:
            messages = [{"role": "system", "content": raw_text}]
            user_message = query
            messages.append({"role": "user", "content": f"{user_message}, answer concisely"})

            try:
                chat_response = chat_completion_request(messages)
                assistant_message = chat_response["choices"][0]["message"]["content"]
                st.session_state['chat_history'].append((user_message, assistant_message))
            except Exception as e:
                assistant_message = f"Error: {e}"
                st.session_state['chat_history'].append((user_message, assistant_message))

    for chat_entry in st.session_state['chat_history']:
        st.write(f"### {chat_entry[0]}")
        st.markdown(highlight_keywords(chat_entry[1], keywords), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
