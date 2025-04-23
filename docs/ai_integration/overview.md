# 🧠 AI Integration

???+ example "Workflow"

    ```text
    Frontend (HTML/JS)
        |
        |---> API Request (user input/prompt)
                |
            Backend & API Interaction (Python/Django)
                |
                LLM (local or platform)
                |
            AI Response
                |
        <--- Response sent to frontend
    ```


We have integrated the [Together API](https://www.together.ai/) into our projects, enabling us to interact with over **200 different large language models (LLMs)** for various purposes. Some of these models are available for free, while others are offered under paid plans.

In this write-up, we'll walk you through the different components we implemented to create an **AI chat system designed to combat imposter syndrome**—step by step.

Before we begin, it’s worth noting that [Together.ai](https://www.together.ai/) is just one of several powerful platforms available for LLM access. Other notable providers include:

- [Hugging Face Inference API](https://huggingface.co/inference-api)
- [Replicate](https://replicate.com/)
- [Groq](https://groq.com/)
- [Fireworks.ai](https://fireworks.ai/) (some offer free-tier usage)
- [OpenAI](https://platform.openai.com/) (especially if you're considering a non-open-source route)

---

### 🔧 Integration

Our AI chat system integration involves the following steps:

1. **Model Selection** – Choosing appropriate LLMs based on response quality, latency, and licensing.
2. **Authentication & API Setup** – Registering API keys and securely managing them within the project.
3. **Backend Integration** – Writing async functions to handle user input, call the API, and return results.
4. **Frontend Chat UI** – Creating a user-friendly interface for smooth interaction with the AI.
5. **Streaming Responses** – Implementing partial rendering as the AI generates responses (for real-time feedback).
6. **Fallback** – Setting up fallback models
7. **Logging** –  Logging for analytics and debugging
