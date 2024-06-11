import streamlit as st
import os
import pdfplumber
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

def main():
    # Set the OpenAI API Key
    #os.environ["OPENAI_API_KEY"] = "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"

    # Title and instructions
    st.title("Report ChatBot")

    # Define the options and corresponding PDF files
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

   
    # Dropdown menu to select a PDF file
    selected_option = st.sidebar.selectbox("Select Date", list(options_pdf.keys()))

    if selected_option:
        selected_pdf = options_pdf[selected_option]
        pdf_path = os.path.join("reports", selected_pdf)
        
        # Extract text from the selected PDF
        with pdfplumber.open(pdf_path) as pdf:
            page = pdf.pages[0]
            raw_text = page.extract_text()

        # Split the text into manageable chunks using a custom text splitter
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=800,
            chunk_overlap=200,
            length_function=len,
        )
        texts = text_splitter.split_text(raw_text)

        # Load embeddings and initialize document search
        embeddings = OpenAIEmbeddings()
        document_search = FAISS.from_texts(texts, embeddings)

        # Create a QA chain
        chain = load_qa_chain(OpenAI(), chain_type="stuff")

        # Initialize history for chat-like display
        if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = []

        # User query input
        query = st.text_input("Enter your query:")

        # Perform a search query when query is submitted
        if st.button("Search"):
            if query:
                # Perform a search query with user input
                docs = document_search.similarity_search(query)
                result = chain.run(input_documents=docs, question=query)

                # Append query and result to chat history
                st.session_state['chat_history'].append((query, result))

        # Display chat history
        for chat_entry in st.session_state['chat_history']:
            st.write("User: ", chat_entry[0])
            st.write("ChatBot: ", chat_entry[1])

if __name__ == "__main__":
    main()
