# Falcon LLM Q&A App

This is a simple Streamlit application that uses the `Falcon-7B` language model from Hugging Face for answering user questions. The app is built using `Streamlit` and `LangChain`.

## Features

- **Interactive Q&A**: Enter any question and get a thoughtful answer powered by the Falcon LLM.
- **Hugging Face Integration**: Leverages the Falcon-7B model hosted on Hugging Face.
- **Secure Deployment**: The app is designed to keep API keys secure using environment variables.

## Access the App

You can access the deployed application at the following link:

[**Falcon LLM Q&A App**](https://falcon-llm-q-a-bot-akfvwfnz7btdthsbtafc8h.streamlit.app/)

*(Replace the link above with your actual deployed app URL)*

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.11
- Pip (Python package installer)

### Installation

1. **Clone the repository**:
    ```bash
    https://github.com/prajwal-sarode/Falcon-LLM-Q-A-bot.git
    cd Falcon-LLM-Q-A-bot
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your Hugging Face API key**:

    - Create a `.env` file in the root directory of the project and add your API key:

      ```env
      HUGGINGFACEHUB_API_TOKEN=your_hugging_face_api_key
      ```

    - Alternatively, you can set the environment variable directly in your terminal:

      ```bash
      export HUGGINGFACEHUB_API_TOKEN='your_hugging_face_api_key'
      ```

### Running the Application

Run the following command to start the Streamlit app:

```bash
streamlit run app.py
