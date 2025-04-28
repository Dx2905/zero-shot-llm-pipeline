# src/prompt_builder.py

def build_prompt(task: str, input_text: str) -> str:
    """Dynamically build prompts based on the selected task."""
    if task == "Summarization":
        return f"Summarize the following text:\n\n{input_text}"
    elif task == "Translation":
        return f"Translate this English text into French:\n\n{input_text}"
    elif task == "Question Generation":
        return f"Generate two questions from the following text:\n\n{input_text}"
    elif task == "Sentiment Analysis":
        return f"Analyze the sentiment (Positive, Negative, Neutral) of this text:\n\n{input_text}"
    else:
        return f"Perform the task '{task}' on this text:\n\n{input_text}"
