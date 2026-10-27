# Free Models, No Account

You do not have to pay for AI, and you do not have to create an account with an AI company, to use AI for coding. This chapter shows you the options that are free and need no signup.

## Option 1: Local models with Ollama (recommended, private, and free)

**Ollama** lets you run AI models on your own computer. Nothing you type is sent to a company's servers. It works offline after you download a model. It is completely free.

1. Go to `ollama.com` and download Ollama for your computer.
2. Install it and open it. It runs quietly in the background.
3. In your terminal, run a model. For example:

   ```
   ollama run codellama
   ```

   The first time, Ollama downloads the model (this can take a few minutes depending on your internet speed). After that, it's on your machine.
4. Type your question and press Enter. Type `/bye` to exit.

To use a local model with Kilo Code in VS Code, look for a "local model" or "Ollama" option in Kilo Code's settings and point it at `http://localhost:11434`.

**Why local-first?** Your code stays on your computer. No account. No API keys. No subscription. This matches Asdale Dynamics' local-first, private approach.

## Option 2: Free web chat with no account

Some AI providers let you chat with a model in your browser without creating an account. Availability changes, so search for "free AI chat no account" and try a few. Look for:

- No "Sign up" wall before you can type
- No request for a phone number or credit card
- A clear privacy statement

You can paste code into these chats and ask the AI to explain it or fix it, then copy the result back into VS Code. Just don't paste secrets (passwords, API keys, personal data) — see the terminal safety chapter for why.

## Option 3: Free tiers with an account (optional)

Many AI tools have a generous free tier, but they ask you to create an account. You don't need these for this guide. If you ever choose to sign up, never add a credit card unless you intend to pay, and check the pricing page so you don't get surprised by a bill.

## What models are good for coding

When you have a choice, pick a model described as good at code — names you may see include Code Llama, DeepSeek Coder, Qwen, or similar. Any of them can help a beginner. The exact model matters less than just getting started.

## A quick no-account test

Try this right now:

1. Open Ollama (or a no-account web chat).
2. Ask: "Write a short Python program that prints the numbers 1 to 5."
3. Copy the code into a file called `test.py` in VS Code.
4. Run it in the terminal:

   ```
   python test.py
   ```

You just coded with AI for free.

## Stay safe

Even free AI can make mistakes. Always read the code before you run it (next chapter), and never run a terminal command you don't understand (terminal safety chapter). Free doesn't mean careless.
