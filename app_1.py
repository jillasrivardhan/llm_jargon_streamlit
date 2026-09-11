
import streamlit as st

# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="LLM Jargon Explorer",
    page_icon="🧠",
    layout="wide",
)

# ------------------------------------------------------------
# LLM terms based on the provided LLM Jargon Glossary PDF
# ------------------------------------------------------------
TERMS = [
    {
        "term": "Transformer",
        "category": "How We Got Here",
        "icon": "🔄",
        "summary": "A neural-network architecture that uses attention to understand relationships between words.",
        "easy": (
            "Instead of reading a sentence as isolated words, a Transformer can look at "
            "the whole sentence and focus on the words that matter most to each other."
        ),
        "example": "“The dog chased the ball because it was fast.” Attention helps connect “it” with the relevant context.",
        "flow": ["Sentence", "Attention", "Important relationships", "Better understanding"],
    },
    {
        "term": "Large Language Model (LLM)",
        "category": "The Model",
        "icon": "🧠",
        "summary": "A model trained on a huge amount of text that learns to predict the next token.",
        "easy": (
            "An LLM learns patterns from lots of text. When you give it a prompt, "
            "it predicts what text is likely to come next, one token at a time."
        ),
        "example": "A chatbot can answer questions, write stories, summarize text, or generate code.",
        "flow": ["Prompt", "LLM", "Next-token prediction", "Response"],
    },
    {
        "term": "Parameters",
        "category": "The Model",
        "icon": "🎛️",
        "summary": "Learned internal values that the model adjusts during training.",
        "easy": (
            "Think of parameters as millions or billions of tiny internal settings. "
            "Training adjusts these settings so the model becomes better at recognizing patterns."
        ),
        "example": "A model described as having 7B or 70B parameters has billions of learned values.",
        "flow": ["Training data", "Learning", "Parameters change", "Model learns patterns"],
    },
    {
        "term": "Model Size",
        "category": "The Model",
        "icon": "📦",
        "summary": "The size of a model is commonly described by its number of parameters.",
        "easy": (
            "A small model has fewer parameters, while a large model has more. "
            "Larger models can learn more complex patterns, but usually need more compute."
        ),
        "example": "7B means approximately 7 billion parameters.",
        "flow": ["Parameter count", "Small / Medium / Large", "Capability", "Compute cost"],
    },
    {
        "term": "Foundation Model",
        "category": "The Model",
        "icon": "🏗️",
        "summary": "A general-purpose model that can serve as a base for specialized applications.",
        "easy": (
            "A foundation model is like a strong starting point. Developers can build "
            "different applications or specialized models on top of it."
        ),
        "example": "A general language model can become the foundation for a coding assistant or chatbot.",
        "flow": ["Foundation model", "Customize / build", "Application", "User"],
    },
    {
        "term": "Tokens",
        "category": "Text & Context",
        "icon": "🧩",
        "summary": "Small pieces of text that an LLM processes.",
        "easy": (
            "A token is not always a complete word. It can be a whole word, part of a word, "
            "punctuation, or another small piece of text."
        ),
        "example": "The sentence “Hello world!” is broken into smaller pieces before the model processes it.",
        "flow": ["Text", "Tokenization", "Tokens", "Model processing"],
    },
    {
        "term": "Context Window",
        "category": "Text & Context",
        "icon": "🪟",
        "summary": "The amount of text, measured in tokens, that a model can consider at one time.",
        "easy": (
            "Think of it as the model's short-term working memory. If a conversation or document "
            "is longer than the available context, the model cannot consider everything at once."
        ),
        "example": "A 128K context window can consider far more tokens at once than an 8K context window.",
        "flow": ["Conversation / document", "Context window", "Relevant context", "Model response"],
    },
    {
        "term": "Prompt",
        "category": "Text & Context",
        "icon": "💬",
        "summary": "The instruction or message you give to an AI model.",
        "easy": (
            "A prompt tells the model what you want. Clear and specific prompts generally "
            "make it easier for the model to produce a useful response."
        ),
        "example": "“Explain Transformers to a beginner using a simple example.”",
        "flow": ["Your instruction", "Prompt", "LLM", "Output"],
    },
    {
        "term": "Temperature",
        "category": "Controlling Output",
        "icon": "🌡️",
        "summary": "A setting that controls how predictable or varied model output can be.",
        "easy": (
            "Lower temperature usually gives more predictable output. Higher temperature "
            "allows more variation and can make responses feel more creative."
        ),
        "example": "Low temperature can suit factual or structured tasks; higher temperature can suit creative writing.",
        "flow": ["Prompt", "Temperature", "Prediction choices", "Output"],
    },
    {
        "term": "System Prompt",
        "category": "Controlling Output",
        "icon": "⚙️",
        "summary": "A higher-level instruction that helps shape how a model behaves.",
        "easy": (
            "A system prompt can define the assistant's role, behavior, style, or constraints "
            "before the user starts interacting with it."
        ),
        "example": "An assistant can be instructed to act as a helpful tutor and explain concepts simply.",
        "flow": ["System instructions", "Model behavior", "User prompt", "Response"],
    },
    {
        "term": "Inference",
        "category": "Controlling Output",
        "icon": "⚡",
        "summary": "Using a trained model to generate an answer or prediction.",
        "easy": (
            "Training is when the model learns. Inference is when you actually use that trained "
            "model to generate an output."
        ),
        "example": "Every time you send a prompt to a deployed LLM and receive an answer, inference is happening.",
        "flow": ["Trained model", "Input", "Inference", "Output"],
    },
    {
        "term": "Embeddings",
        "category": "Representing Information",
        "icon": "🔢",
        "summary": "Numerical vector representations of text, images, or other information.",
        "easy": (
            "Embeddings turn information into lists of numbers. Items with similar meanings "
            "can have vectors that are close to each other."
        ),
        "example": "“car” and “automobile” can have similar embeddings because their meanings are related.",
        "flow": ["Text / image", "Embedding model", "Vector", "Similarity search"],
    },
    {
        "term": "Training",
        "category": "Training",
        "icon": "🏋️",
        "summary": "The process of teaching a model by repeatedly adjusting its parameters.",
        "easy": (
            "During training, the model makes predictions, checks how wrong they are, "
            "and adjusts its parameters. This process is repeated many times."
        ),
        "example": "The model repeatedly practices predicting text from training data and gradually improves.",
        "flow": ["Training data", "Prediction", "Error", "Parameter update"],
    },
    {
        "term": "Fine-Tuning",
        "category": "Training",
        "icon": "🎯",
        "summary": "Additional focused training that adapts an existing model for a particular task, topic, or style.",
        "easy": (
            "Instead of training a model from scratch, you start with an existing model "
            "and give it additional task-specific training."
        ),
        "example": "A general model can be fine-tuned to behave better for a particular domain or style.",
        "flow": ["Pretrained model", "Focused data", "Fine-tuning", "Specialized behavior"],
    },
    {
        "term": "RLHF",
        "category": "Training",
        "icon": "👥",
        "summary": "Reinforcement Learning from Human Feedback, where human preferences help shape model behavior.",
        "easy": (
            "People can compare or rank model outputs. Those preferences can then be used "
            "to train the model toward responses humans prefer."
        ),
        "example": "Human reviewers may rank several answers, helping the model learn which style of answer is preferred.",
        "flow": ["Model outputs", "Human feedback", "Preference signal", "Improved behavior"],
    },
    {
        "term": "Hallucination",
        "category": "Modern LLM Concepts",
        "icon": "⚠️",
        "summary": "When a model produces a confident-sounding answer that is incorrect or made up.",
        "easy": (
            "An LLM predicts likely text. It does not automatically guarantee that every statement "
            "is factually correct, so it can sometimes generate convincing but wrong information."
        ),
        "example": "A model might invent a citation, person, event, or fact that does not actually exist.",
        "flow": ["Question", "Model prediction", "Confident answer", "Possible factual error"],
    },
    {
        "term": "RAG (Retrieval-Augmented Generation)",
        "category": "Modern LLM Concepts",
        "icon": "📚",
        "summary": "A technique that retrieves relevant information before the model generates an answer.",
        "easy": (
            "RAG gives the model useful external information first. The model can then use "
            "that retrieved context to produce a more grounded answer."
        ),
        "example": "A college FAQ chatbot can retrieve the relevant FAQ text before answering a student's question.",
        "flow": ["User question", "Retrieve relevant info", "LLM + context", "Grounded answer"],
    },
    {
        "term": "Quantization",
        "category": "Modern LLM Concepts",
        "icon": "📉",
        "summary": "Reducing the numerical precision used to represent model values to make models smaller and faster.",
        "easy": (
            "Quantization can convert higher-precision representations such as FP32 into lower-precision "
            "ones such as INT8 or INT4. This can reduce memory and computation requirements."
        ),
        "example": "A model can be quantized so it is easier to run on hardware with limited memory.",
        "flow": ["Full-precision model", "Lower precision", "Smaller model", "Faster / cheaper inference"],
    },
    {
        "term": "LoRA / PEFT",
        "category": "Modern LLM Concepts",
        "icon": "🧪",
        "summary": "Parameter-efficient fine-tuning methods that train a smaller set of additional parameters.",
        "easy": (
            "Instead of changing every parameter in a large model, PEFT methods such as LoRA "
            "train a much smaller set of parameters, making adaptation more efficient."
        ),
        "example": "LoRA can adapt an existing language model to a specialized task without fully retraining the model.",
        "flow": ["Pretrained model", "Small trainable add-on", "LoRA / PEFT", "Adapted model"],
    },
    {
        "term": "Multimodal Models",
        "category": "Modern LLM Concepts",
        "icon": "🖼️",
        "summary": "Models that can work with more than one type of information, such as text, images, audio, or video.",
        "easy": (
            "A multimodal model can combine different kinds of input instead of working with text alone."
        ),
        "example": "A model can receive an image and a text question and produce a text response.",
        "flow": ["Text / image / audio / video", "Multimodal model", "Reasoning / generation", "Output"],
    },
]

CATEGORIES = ["All"] + list(dict.fromkeys(item["category"] for item in TERMS))

# ------------------------------------------------------------
# Session state
# ------------------------------------------------------------
if "term_index" not in st.session_state:
    st.session_state.term_index = 0

# ------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------
with st.sidebar:
    st.header("🧠 LLM Jargon Explorer")
    st.caption("Learn one LLM term at a time.")

    category = st.selectbox("Filter by category", CATEGORIES)

    filtered_terms = [
        item for item in TERMS
        if category == "All" or item["category"] == category
    ]

    term_names = [item["term"] for item in filtered_terms]

    # Keep the selected index valid when the filter changes.
    current_term = TERMS[st.session_state.term_index]["term"]
    if current_term in term_names:
        selected_position = term_names.index(current_term)
    else:
        selected_position = 0

    selected_term = st.radio(
        "Terms",
        term_names,
        index=selected_position,
    )

    # Find the actual global index.
    st.session_state.term_index = next(
        i for i, item in enumerate(TERMS) if item["term"] == selected_term
    )

    st.divider()
    st.subheader("📚 Learning path")
    st.write("1. Understand the model")
    st.write("2. Learn text & context")
    st.write("3. Understand training")
    st.write("4. Explore modern LLM concepts")

    progress = (st.session_state.term_index + 1) / len(TERMS)
    st.progress(progress)
    st.caption(f"Overall progress: {st.session_state.term_index + 1}/{len(TERMS)}")

# ------------------------------------------------------------
# Current term
# ------------------------------------------------------------
term = TERMS[st.session_state.term_index]

# ------------------------------------------------------------
# Header
# ------------------------------------------------------------
st.title("🧠 LLM Jargon Explorer")
st.caption("A beginner-friendly guide to important Large Language Model terms.")

st.info(
    "Use the sidebar to choose a term, or use Previous / Next to move through the guide."
)

# ------------------------------------------------------------
# Stats
# ------------------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Core terms", len(TERMS))

with c2:
    st.metric("Learning sections", len(CATEGORIES) - 1)

with c3:
    st.metric("Current slide", f"{st.session_state.term_index + 1}/{len(TERMS)}")

with c4:
    st.metric("Level", "Beginner")

st.divider()

# ------------------------------------------------------------
# Navigation
# ------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])

with nav1:
    if st.button("⬅️ Previous", use_container_width=True):
        st.session_state.term_index = (st.session_state.term_index - 1) % len(TERMS)
        st.rerun()

with nav2:
    st.markdown(
        f"<div style='text-align:center; padding-top:8px;'>"
        f"<b>{term['icon']} {term['category']}</b>"
        f"</div>",
        unsafe_allow_html=True,
    )

with nav3:
    if st.button("Next ➡️", use_container_width=True):
        st.session_state.term_index = (st.session_state.term_index + 1) % len(TERMS)
        st.rerun()

st.divider()

# ------------------------------------------------------------
# Slide content
# ------------------------------------------------------------
st.subheader(f"{term['icon']} {term['term']}")
st.caption(f"Category: {term['category']}")

st.markdown(f"### 📌 Short summary")
st.write(term["summary"])

st.markdown("### 💡 Easy explanation")
st.write(term["easy"])

st.markdown("### 🌍 Everyday example")
st.success(term["example"])

# ------------------------------------------------------------
# Visual flow
# ------------------------------------------------------------
st.markdown("### 🔄 Simple flow")

flow_cols = st.columns(len(term["flow"]))

for i, (col, step) in enumerate(zip(flow_cols, term["flow"])):
    with col:
        st.markdown(f"**{step}**")
        if i < len(term["flow"]) - 1:
            st.markdown("↓")

st.divider()

# ------------------------------------------------------------
# Quick takeaway
# ------------------------------------------------------------
st.markdown("### 🎯 Interview takeaway")

takeaways = {
    "Transformer": "Attention is the key idea to remember.",
    "Large Language Model (LLM)": "An LLM predicts the next token based on learned patterns.",
    "Parameters": "Parameters are learned internal values of the model.",
    "Model Size": "Model size is commonly discussed using parameter count.",
    "Foundation Model": "A foundation model is a general base for many applications.",
    "Tokens": "LLMs process text as tokens rather than simply whole words.",
    "Context Window": "It defines how many tokens the model can consider at one time.",
    "Prompt": "A prompt is the instruction or input given to the model.",
    "Temperature": "It controls how predictable or varied the generated output can be.",
    "System Prompt": "It provides higher-level instructions that shape model behavior.",
    "Inference": "Inference means using a trained model to generate an output.",
    "Embeddings": "Embeddings represent information as numerical vectors.",
    "Training": "Training repeatedly adjusts parameters to improve predictions.",
    "Fine-Tuning": "Fine-tuning adapts an existing model to a more specific task or style.",
    "RLHF": "Human preferences can be used to shape model behavior.",
    "Hallucination": "A fluent answer is not automatically a factual answer.",
    "RAG (Retrieval-Augmented Generation)": "RAG retrieves relevant information before generation to ground the answer.",
    "Quantization": "Lower precision can make a model smaller and cheaper to run.",
    "LoRA / PEFT": "LoRA and PEFT adapt models by training fewer parameters.",
    "Multimodal Models": "Multimodal models can work with multiple types of information.",
}

st.write(takeaways[term["term"]])

# ------------------------------------------------------------
# Quick interview cheat sheet
# ------------------------------------------------------------
with st.expander("📝 Quick interview cheat sheet"):
    cheat_sheet = [
        ("70B", "Parameters"),
        ("128K", "Context Window"),
        ("Confident but wrong answer", "Hallucination"),
        ("Ground an LLM with external information", "RAG"),
        ("Make a model smaller", "Quantization"),
        ("Customize an existing model", "Fine-Tuning / LoRA"),
        ("Use a trained model", "Inference"),
        ("Image + text", "Multimodal Model"),
        ("Predict the next token", "LLM"),
        ("Increase creativity / variation", "Temperature"),
    ]

    for phrase, answer in cheat_sheet:
        st.write(f"**{phrase} →** {answer}")

st.divider()
st.caption("Based on the provided “The LLM Jargon Glossary” companion guide. Built as a beginner learning project with Streamlit.")
