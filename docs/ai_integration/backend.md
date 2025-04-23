???+ danger "Stateless & Serverless"
    - **Stateless**: Each request is independent and doesn’t rely on any previous request's data stored on the server.
        - Each AI request is independent — the model doesn’t remember past requests unless you include them again in the new request (you must send the full context every time.).
        - Chat-like memory is typically emulated by appending previous messages to the prompt (called [**prompt chaining**]() or [**context windowing**]()).

    - **Serverless**: Doesn't mean "no servers". It means you don’t manage the servers yourself. The cloud provider (like AWS, Google Cloud, or Vercel) handles infrastructure management for you.
        - Serverless AI means you use AI services without running or managing your own model servers. The model is hosted by a provider (e.g., Together.ai), and you interact with it through APIs. You don’t care where or how the model is running. It's abstracted away.