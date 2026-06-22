# Rule-Based AI Chatbot — DecodeLabs Project 1

A rule-based chatbot built using Python as part of the DecodeLabs 
AI Industrial Training (Batch 2026).

## Features
- Continuous input loop using `while True`
- Input sanitization (lowercase + strip whitespace)
- Dictionary-based O(1) intent matching
- Fallback response for unknown inputs
- Clean exit command

## How to Run

```
python chatbot.py
```

## Supported Commands
| Input | Response |
|-------|----------|
| hello / hi | Greeting |
| how are you | Status check |
| what is ai | AI definition |
| what can you do | Bot capabilities |
| who made you | Origin info |
| help | Help message |
| bye / exit / quit | End session |

## Tech
Python 3 — no external libraries required
