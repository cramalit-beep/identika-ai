import streamlit as st

st.set_page_config(page_title="IDENTIKA Studio AI", page_icon="🎨", layout="centered")

# Encabezado principal
st.title("🎨 IDENTIKA Studio AI")
st.subheader("Plataforma de co-creación de merchandising con Inteligencia Artificial")
st.markdown("---")

# Selección de producto
producto = st.selectbox(
    "1. Seleccioná el soporte para tu estampado:",
    ["Remera Algodón Negra", "Remera Algodón Blanca", "Taza cerámica de café", "Gorra Trucker", "Botella térmica de acero"]
)

# Entrada del usuario (Prompt)
prompt_usuario = st.text_area(
    "2. Describí la idea de tu diseño (la IA generará el gráfico):",
    "Un león geométrico estilo cyberpunk con colores neon, fondo aislado"
)

# Botón de acción
if st.button("🚀 Generar Diseño Exclusivo"):
    if prompt_usuario:
        with st.spinner("Conectando con el motor de IA y optimizando para impresión DTF..."):
            # Simulamos el éxito de la generación para el MVP académico
            st.success("¡Diseño generado con éxito y optimizado a 300 DPI!")
            
            # Mostramos un mockup visual de ejemplo adaptado
            st.image(
                "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=600&q=80", 
                caption=f"Mockup de previsualización sobre: {producto}"
            )
            
            st.info("📥 Archivo procesado: Fondo transparente removido (PNG alfa) y listo para bajar a plotter DTF.")
            
            # Simulación de cotización
            st.markdown("### 💰 Cotización estimada:")
            st.write(f"- **Producto soporte:** {producto}")
            st.write(f"- **Optimización IA (Exclusivo):** Incluida")
            st.markdown("**Total estimado:** `$18.500 ARS`")
    else:
        st.warning("Por favor, ingresá una descripción para que la IA pueda crear el diseño.")

st.markdown("---")
st.caption("IDENTIKA Studio AI • Proyecto Integrador Diplomatura en IA 2026")
