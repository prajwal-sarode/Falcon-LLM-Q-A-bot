import streamlit as st
import os
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from apikey_huggingface import apikey_huggingface

os.environ["HUGGINGFACEHUB_API_TOKEN"] = apikey_huggingface

# setup the language model using huggingface api

repo_id = "tiiuae/falcon-7b-instruct"

llm = HuggingFaceHub(
    repo_id=repo_id,
    model_kwargs={
        "temperature": 0.7,  # Adjusted temperature for more varied output
        "max_new_tokens": 200,
        "stop_sequences": ["\n\n"]  # Stop generation after a paragraph
    }
)

# setup prompt

template = """
You are an artificial intelligence assistant.
You provide helpful advice and tips to user questions.
Question: {question}

Answer:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["question"]
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

# create a simple streamlit app

def main():
    st.title("Falcon LLM Q&A App")

    # getting user input
    question = st.text_input("Enter your Question")

    # Generate the response
    if st.button("Get Answer"):
        with st.spinner("Generating Answer.."):
            response = llm_chain.run(question)
            # Optionally, post-process the response to clean it up
            response = response.split("Answer:")[-1].strip()  # Remove prompt from output
        st.success(response)

if __name__ == "__main__":
    main()
