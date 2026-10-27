# Fixing Errors

AI-written code often has errors on the first try. That's normal. Professional programmers spend more time fixing code than writing it. This chapter shows you how to fix errors calmly and safely.

## Step 1: Read the error message

When something breaks, you'll see an error message in the terminal or in VS Code. It looks scary, but it's trying to help. Read it slowly. Look for:

- The file name where the problem is
- The line number
- A short description of what went wrong

Example:

```
File "budget.py", line 4, in <module>
    print(total)
NameError: name 'total' is not defined
```

Translation: in `budget.py`, on line 4, the program tried to use `total` but `total` was never created.

## Step 2: Copy the error into the AI chat

Paste the full error message into Kilo Code, along with the code that caused it. Ask:

> "This code gave me this error. Can you fix it and explain what went wrong?"

Include:
- The error message (copy and paste, don't retype)
- The file it happened in
- What you were trying to do

## Step 3: Apply the fix carefully

Kilo Code will suggest a corrected version. Before you replace your code:

1. Read the suggested change.
2. Make sure you understand what it changes and why.
3. If anything looks wrong or dangerous, ask the AI to explain or suggest another fix.

You can copy the fix into your file, or ask Kilo Code to apply it directly (review it first either way).

## Step 4: Test again

Run the program again:

```
python your-file.py
```

or open your HTML file in a browser. Did the error go away?

- **Yes:** Great. Read the fixed code so you understand it now.
- **No, same error:** Paste the new error and try again.
- **No, different error:** Progress! You fixed one thing and found the next. Repeat.

## Step 5: Don't guess — verify

After the error is gone, test that the program actually does what you want:

- Try different inputs (big numbers, zero, negative numbers, empty text).
- Check that the output matches what you expect.

AI can write code that runs without errors but still does the wrong thing. Testing catches that.

## Common beginner errors

| Error | Likely cause |
|---|---|
| `NameError` / "not defined" | You used a name before creating it, or misspelled it |
| `SyntaxError` | A typo like a missing parenthesis, quote, or colon |
| `FileNotFoundError` | The program looked for a file that isn't there |
| `TypeError` | You tried to do something with the wrong kind of data (e.g., adding text to a number) |

## Keep a safety net

Before you let AI make big changes, save a copy of your file or make a git commit (see the glossary). If the AI's fix makes things worse, you can go back to the version that worked.

## Exercise

1. Intentionally break a working program — delete a line or misspell a word.
2. Run it and read the error.
3. Ask Kilo Code to fix it.
4. Apply the fix and test.

You just debugged like a pro.
