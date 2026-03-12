import ollama 
import re

def summarize_half(chunks):

    summaries = []

    for chunk in chunks:

        prompt = f'''
        Resume el siguiente texto en español en máximo 80 palabras.

        Reglas:
        - Solo escribe el resumen.
        - No escribas introducciones.
        - No escribas frases como "Aquí te presento" o "A continuación".
        - No agregues comentarios.

        Texto:
        {chunk}
        '''

        response = ollama.generate(
            model="llama3",
            prompt=prompt
        )

        summary = response["response"]

        summary = re.sub(r"Aquí te presento.*?:", "", summary)
        summary = re.sub(r"A continuación.*?:", "", summary)

        summaries.append(summary.strip())

    return summaries

def summarize_quarter(chunks):

    summaries = []

    for chunk in chunks:

        prompt = f'''
        Resume el siguiente texto en español en máximo 40 palabras.

        Reglas:
        - Solo escribe el resumen.
        - No escribas introducciones.
        - No escribas frases como "Aquí te presento" o "A continuación".
        - No agregues comentarios.

        Texto:
        {chunk}
        '''

        response = ollama.generate(
            model="llama3",
            prompt=prompt
        )

        summary = response["response"]

        summary = re.sub(r"Aquí te presento.*?:", "", summary)
        summary = re.sub(r"A continuación.*?:", "", summary)

        summaries.append(summary.strip())

    return summaries