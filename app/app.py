import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="AI PDF Summarizer",
    page_icon="📄",
    layout="centered"
)

# Título
st.title("📄 AI PDF Summarizer")
st.write("Sube un archivo PDF y la IA generará un resumen automáticamente.")

# Subir archivo PDF
uploaded_file = st.file_uploader(
    "Sube tu archivo PDF",
    type=["pdf"]
)

# Botón para generar resumen
if uploaded_file is not None:

    st.success("PDF cargado correctamente")

    if st.button("Generar resumen", type="secondary"):

        st.info("Procesando documento...")

        # Aquí se leerá el pdf, entra el modelo y regresa el resumen del pdf 

        resumen = """
        Este es un ejemplo de resumen generado por la IA.
        *Aquí deberá aparecer el pdf resumido luego de que haga el modelo*
        """

        st.subheader("Resumen generado")
        st.write(resumen)