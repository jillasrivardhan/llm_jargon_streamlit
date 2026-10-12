🧠 LLM Jargon Explorer

Live - Demo -Link : https://llm-jargon-introduction.streamlit.app/

A beginner-friendly Streamlit learning application that explains important Large Language Model (LLM) concepts one term at a time.

The project is designed as an interactive revision guide for learners who are getting started with Generative AI, LLMs, RAG, fine-tuning, embeddings, and modern LLM concepts.

📸 Application Screenshots

LLM Jargon Explorer — Main Interface



LLM Jargon Explorer — Learning View



✨ Features

📚 20 core LLM terms explained in beginner-friendly language

🗂️ Category-based filtering for easier navigation

🔘 Term selection through the sidebar

⬅️➡️ Previous / Next navigation to move through concepts like slides

📌 Short summaries for quick revision

💡 Easy explanations without unnecessary technical complexity

🌍 Everyday examples to connect concepts with practical use cases

🔄 Simple concept flows to visually explain how ideas work

🎯 Interview takeaways for quick interview preparation

📝 Quick interview cheat sheet with common LLM terminology

📊 Learning progress indicator

🎓 Beginner-focused learning path

🖥️ Wide-layout Streamlit interface

📖 Concepts Covered

The application currently covers the following concepts:

Model Fundamentals

Transformer

Large Language Model (LLM)

Parameters

Model Size

Foundation Model

Text & Context

Tokens

Context Window

Prompt

Controlling Output

Temperature

System Prompt

Inference

Representing Information

Embeddings

Training

Training

Fine-Tuning

RLHF

Modern LLM Concepts

Hallucination

RAG (Retrieval-Augmented Generation)

Quantization

LoRA / PEFT

Multimodal Models

🧭 How the Application Works

The application presents each LLM concept as an interactive learning "slide."

             ┌──────────────────────┐
             │   Choose a category  │
             │     or LLM term      │
             └──────────┬───────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │   Concept overview   │
             └──────────┬───────────┘
                        │
              ┌─────────┼─────────┐
              ▼         ▼         ▼
         Short       Easy      Everyday
        Summary   Explanation   Example
              │         │         │
              └─────────┼─────────┘
                        ▼
             ┌──────────────────────┐
             │    Simple concept    │
             │        flow          │
             └──────────┬───────────┘
                        ▼
             ┌──────────────────────┐
             │  Interview takeaway  │
             └──────────────────────┘

🛠️ Tech Stack

Python

Streamlit

Markdown

Git / GitHub

The application is intentionally lightweight and does not require an external LLM API. The educational content is stored directly in the application data structure.

📂 Project Structure

llm_jargon_streamlit-main/
│
├── app_1.py
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── Screenshot 2026-09-11 073807.png
    └── Screenshot 2026-09-11 073823.png

Note: The current source file is named app_1.py. If you want to use the conventional Streamlit filename, you can rename it to app.py.

⚙️ Installation

1. Clone the repository

git clone <YOUR-GITHUB-REPOSITORY-URL>
cd llm_jargon_streamlit-main

2. Create a virtual environment

python -m venv .venv

3. Activate the environment

Windows

.venv\Scripts\activate

macOS / Linux

source .venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

▶️ Run the Application

Because the current application file is app_1.py:

streamlit run app_1.py

If you rename the file to app.py:

streamlit run app.py

The application will open in your browser.

🎓 Learning Path

The application follows a simple progression:

1. Understand the Model
          ↓
2. Learn Text & Context
          ↓
3. Understand Training
          ↓
4. Explore Modern LLM Concepts

This makes the project useful as a small LLM revision dashboard rather than just a glossary.

💡 Example Learning Flow

For example, when learning about RAG:

User Question
      ↓
Retrieve Relevant Information
      ↓
LLM + Retrieved Context
      ↓
Grounded Answer

For LLM generation:

Prompt
   ↓
LLM
   ↓
Next-token Prediction
   ↓
Response

These simple flows are intended to help beginners understand the big picture before diving into implementation details.

🎯 Why I Built This

LLM terminology can become confusing very quickly when learning Generative AI.

Terms such as:

Parameters

Tokens

Context Window

Embeddings

Inference

RAG

Fine-Tuning

LoRA

Quantization

RLHF

can sound complicated when encountered for the first time.

This project was created as a visual and interactive revision tool to make these concepts easier to understand and remember.

🚀 Possible Future Improvements

Some ideas for extending the project:

🔎 Add a global search bar

📖 Add detailed examples for every concept

🧪 Add interactive quizzes

🧠 Add flashcards

🤖 Connect the app to an actual LLM

💬 Add an "Ask about this term" chatbot

📚 Add links to official documentation

📈 Track completed concepts

🗃️ Move the terminology data into JSON/YAML

🌐 Deploy the application with Streamlit Community Cloud

🎨 Add optional diagrams and architecture visualizations

🔊 Add text-to-speech explanations

📌 Project Status

Status: Beginner learning / educational project

This project focuses on understanding LLM terminology and building an interactive Streamlit interface. It is not intended to be a production-grade LLM application.

🙌 Learning Goals

This project helped reinforce concepts around:

Streamlit UI development

Session state

Interactive navigation

Filtering data

Organizing educational content

LLM terminology

Generative AI fundamentals

RAG fundamentals

Model training and inference concepts

📄 License

This project is intended for educational and learning purposes. You can adapt and extend it for your own practice.
