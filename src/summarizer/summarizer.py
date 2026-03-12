import ollama 
import re

def final_summary(chunk_summaries,size):

    combined = "\n".join(chunk_summaries)

    prompt = f"""
    A continuación hay varios resúmenes parciales de un documento.

    Crea un único resumen en español, claro y coherente del documento completo
    en un aproximado de {size*len(chunk_summaries)} palabras.

    Resúmenes:
    {combined}
    """

    response = ollama.generate(
        model="llama3",
        prompt=prompt
    )

    final_response = response["response"]

    final_response = re.sub(r"Aquí te presento.*?:", "", final_response)
    final_response = re.sub(r"A continuación.*?:", "", final_response)

    return final_response

def summarize_half(chunks):

    summaries = []

    for chunk in chunks:

        prompt = f'''
        Resume el siguiente texto en español en un aproximado de 260 palabras.

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
        Resume el siguiente texto en español en un aproximado de 130 palabras.

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
        summary = re.sub(r"Resumen.*?:", "", summary)
        summary = re.sub(r"Resumen:.*?:", "", summary)

        summaries.append(summary.strip())

    return summaries