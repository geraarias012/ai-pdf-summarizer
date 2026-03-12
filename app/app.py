import streamlit as st
import sys
import os
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.pdf_reader.pdf_reader import extract_text_from_pdf
from src.text_processing.text_chunker import fixed_chunking
from src.summarizer.summarizer import summarize_half, summarize_quarter


st.set_page_config(
    page_title="AI PDF Summarizer",
    page_icon="📄",
    layout="centered"
)


st.title("📄 AI PDF Summarizer")
st.write("Sube un archivo PDF y la IA generará un resumen automáticamente.")

def chunking(uploaded_file):
    text = extract_text_from_pdf(uploaded_file)

    chunks = fixed_chunking(text)

    return chunks


def half_summarizer(chunks):

    st.info("Generando resumen con IA...")

    summaries = summarize_half(chunks)

    return summaries


def quarter_summarizer(chunks):


    st.info("Generando resumen con IA...")

    summaries = summarize_quarter(chunks)

    return summaries

def final_summaries(summaries):

    final_summary = "\n".join(summaries)

    st.subheader("Resumen generado")

    st.write(final_summary)


uploaded_file = st.file_uploader(
    "Sube tu archivo PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("PDF cargado correctamente")

    if st.button("Generar resumen 50%"):
        chunks = chunking(uploaded_file)
        summaries = half_summarizer(chunks)
        final_summaries(summaries)

    if st.button("Generar resumen 25%"):
        chunks = chunking(uploaded_file)
        summaries = quarter_summarizer(chunks)
        final_summaries(summaries)