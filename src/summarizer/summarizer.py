import ollama

def summarize_text(chunks):

    summaries = []

    for chunk in chunks:

        prompt = f"""
        Resume el siguiente texto en español en máximo 5 líneas:

        {chunk}
        """

        response = ollama.generate(
            model="llama3",
            prompt=prompt
        )

        summaries.append(response["response"])

    return summaries