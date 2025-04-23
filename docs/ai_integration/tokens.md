## 🔍 What Are Tokens?

???+ danger "Note"

    Tokenization can vary between models. For instance, models like LLaMA or Mistral may use different tokenization schemes compared to OpenAI's GPT models. Therefore, while these tools can provide estimates, they may not always reflect the exact token count used by Together.ai's models.​

A **token** can be a word, part of a word, punctuation mark, or even a space—depending on the model's **tokenization system**. For example:

- `"Hello"` is one token.
- `"ChatGPT is great!"` might be split into: `["Chat", "GPT", "is", "great", "!"]`.

Even **whitespace and punctuation** count as tokens.

Most modern LLMs, like those from [OpenAI](https://platform.openai.com/tokenizer), use **subword tokenization** (often based on **Byte Pair Encoding** or BPE). This means a single word can be broken into smaller token parts. For example:

- `"unhappiness"` might become: `"un"`, `"happi"`, `"ness"`.

---

## 🧠 Why Do Tokens Matter?

Tokens determine **how much text** you can send to or receive from an AI model, and how much it **costs** you.

- **Input tokens (request):** These are the tokens in your prompt (e.g., `"Give me a motivational quote"`).
- **Output tokens (response):** These are the tokens in the model’s reply.

So every message sent and received consumes tokens.

---

## 🧑‍💻 Token Limits

Each LLM has a **maximum token limit** per request. This includes both the **input** (your prompt) and the **output** (the model's reply).

For example:

> 🧠 `Llama-4-Maverick-17B-128E-Instruct-FP8` might have a token limit of **8,000 tokens** (check your model's documentation to confirm).

If your input is **200 tokens**, you can receive up to **7,800 tokens** in response.

---

## ⚖️ Token Pricing & Quotas

For API-based services like:

- [Together.ai](https://www.together.ai/)
- [OpenAI](https://openai.com/pricing)
- [Hugging Face](https://huggingface.co/inference-api)

...you're often billed **per token**.

### Example:

If you send:

- **50 tokens** (prompt)

And the model replies with:

- **150 tokens**

Then you’ve used **200 tokens** in total for that API call.

---

## 📏 How Does This Affect Your App?

- **Short prompts** (like a motivational quote) → minimal token usage.
- **Long prompts** or **story generation** → more tokens, higher costs, or risk of hitting the limit.

---

## 🏷️ How to Handle Tokens in Your App

Here are some tips to manage token usage efficiently:

- **Track tokens:** Use tools or SDK features to count tokens per request.
- **Set limits:** Use the `max_tokens` parameter to control how long responses can be.
- **Restrict input:** For example, cap user input to **150 tokens** to keep usage within budget.

You can use [OpenAI’s tokenizer tool](https://platform.openai.com/tokenizer) to experiment and see how text is split into tokens.