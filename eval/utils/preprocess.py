"""
https://github.com/lupantech/MathVista/blob/9ed0e8b52c0911e31faa75308082af5dcf8e63b2/evaluation/build_query.py
"""


def create_prompt(sample, use_hint=True):
    question = sample['question']
    choices = sample['options']

    # Question
    question_text = f"Question: {question}"
    
    # Choices
    texts = ["Choices:"]
    for i, choice in enumerate(choices):
        texts.append(f"({chr(ord('A')+i)}) {choice}")
    choices_text = "\n".join(texts)

    # Hint
    if use_hint:
        hint_text = f"Hint: Please provide the correct option letter, such as A, B, C, D, directly."
    else:
        hint_text = ""

    # Answer Prefix
    prompt = "Answer:"
    
    # Full Prompt
    elements = [question_text, choices_text, hint_text, prompt]
    query = "\n".join([e for e in elements if e != ""])
    query = query.strip()

    return query