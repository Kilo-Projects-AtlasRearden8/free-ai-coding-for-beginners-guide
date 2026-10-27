# Terminal Safety

The terminal (also called the command line, console, or shell) lets you control your computer by typing commands. AI can suggest terminal commands, which is powerful — and potentially dangerous. This chapter keeps you safe.

## The golden rule

Never run a terminal command unless you understand what it does, or you trust the source and have read the chapter on reading AI-written code. If you're not sure, ask the AI to explain the command first, or skip it.

## Commands that are usually safe

These are fine for beginners:

- `pwd` — show where you are
- `ls` (Mac/Linux) or `dir` (Windows) — list files in the current folder
- `cd folder-name` — change into a folder
- `python file.py` — run a Python program
- `ollama run model-name` — run a local AI model
- `mkdir folder-name` — create a new folder

## Commands to be careful with

| Command | Why to be careful |
|---|---|
| `sudo ...` | Runs as administrator. Can change or delete anything. |
| `rm` / `del` | Deletes files. Deleted files usually don't go to a trash bin. |
| `rm -rf` / `del /s /q` | Deletes folders and everything inside, permanently. |
| `chmod` / `chown` | Changes who can read or run files. |
| `curl ... \| bash` | Downloads a script from the internet and runs it immediately. **Never do this.** |

## The one command to never run

```
curl https://example.com/something.sh | bash
```

or any version of "download and run immediately." This hands control of your computer to whoever runs that website. If a tutorial tells you to do this, find a different tutorial. Download the file, read it, then decide whether to run it.

## If Kilo Code suggests a command

Kilo Code may offer to run terminal commands for you. You should:

1. See the command it plans to run.
2. Ask it to explain anything you don't understand.
3. Approve only commands that make sense for what you're doing.
4. Say no to anything involving `sudo`, `rm`, `curl | bash`, or passwords.

You are always allowed to say no and do the step yourself.

## Protect your secrets

Never type or paste these into the terminal or into an AI chat:

- Passwords
- API keys or secret keys
- Credit card numbers
- Personal data (addresses, phone numbers, ID numbers)

If you accidentally paste a secret, treat it as compromised: change the password or revoke the key immediately.

## What to do if you run something bad

1. Don't panic.
2. Press `Ctrl+C` to stop a running command.
3. Close the terminal tab if needed.
4. If you think you deleted something or changed something important, don't keep running commands — ask someone more experienced for help.

## Exercise

1. Open a terminal in VS Code (**Terminal > New Terminal**).
2. Type `pwd` and press Enter. See where you are.
3. Type `ls` and press Enter. See your files.
4. Create a practice folder: `mkdir practice-folder`.
5. Go inside: `cd practice-folder`.
6. Go back: `cd ..`.

You just used the terminal safely.
