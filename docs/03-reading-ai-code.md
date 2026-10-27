# Reading AI-Written Code

AI can write code fast. That doesn't mean the code is correct, safe, or easy to understand. Your job as the human is to read it before you run it. This chapter shows you how, step by step, even if you've never read code before.

## Rule one: never run AI code you haven't read

An AI might write code that deletes files, sends data somewhere, or simply crashes. Read it first. If anything looks strange, ask the AI to explain it before running anything.

## How to read a piece of code

Read top to bottom, one piece at a time:

1. **Look at the file name.** `budget.html` is probably a webpage. `calculator.py` is probably a Python program. The name tells you what to expect.
2. **Find the starting point.** Code usually runs from the top (or from a function named `main`). Start there.
3. **Read line by line.** Ask of each line: "What is this line doing?"
4. **Look up words you don't know.** Use the glossary at the end of this guide, or ask the AI: "What does this line do?"

## Use the AI to explain its own code

You can paste AI-written code back into Kilo Code and ask:

> "Can you explain this code line by line, like I'm a beginner?"

Or:

> "What does this function do? Is anything here dangerous?"

The AI is often surprisingly good at explaining its own writing. Use it as a tutor, not just as a writer.

## Common things you'll meet

| What you see | What it usually means |
|---|---|
| `function name() { ... }` or `def name():` | A reusable block of code with a name |
| `if ( ... ) { ... }` or `if ...:` | "Only do this if a condition is true" |
| `for ... { ... }` or `for ...:` | "Do this many times, once for each item" |
| `variable = value` | Storing a value under a name so you can reuse it |
| `print(...)` or `console.log(...)` | Showing text in the terminal or browser console |
| `// comment` or `# comment` | A note for humans; the computer ignores it |

## Comments are your friend

Good AI-written code usually has comments explaining what each section does. If the AI didn't add comments, ask it to:

> "Please add comments explaining what each part does."

Then read those comments as you read the code.

## Small programs are easier to read

Ask the AI to write small, single-purpose files rather than one giant file. A 20-line calculator is easier to check than a 500-line "app." You can combine small files later.

## Exercise

Ask Kilo Code to write a tiny program — for example, a program that converts Fahrenheit to Celsius. Then:

1. Read every line.
2. Ask Kilo Code to explain any line you don't understand.
3. Predict what the program will output before you run it.
4. Run it and compare.

If the output doesn't match your prediction, you found something worth learning from. Move on to the next chapter to fix it.
