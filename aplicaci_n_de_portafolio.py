import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Portafolio de Actividades",
    page_icon="📁",
    layout="wide"
)

st.title("📁 Portafolio de Actividades")
st.write("Bienvenido a mi portafolio. Explora las actividades y gestiona sus enlaces de entrega.")

# 1. Lista inicial de actividades guardada en la sesión
if "actividades" not in st.session_state:
    st.session_state.actividades = [
        {
            "id": 1,
            "titulo": "Casos de Prueba (DemoQA)",
            "materia": "Pruebas de Software",
            "descripcion": "Diseño y ejecución de la plantilla de casos de prueba para validación de formularios web.",
            "imagen": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop",
            "enlace": ""
        },
        {
            "id": 2,
            "titulo": "Solución Taller 1 - Unidad 2",
            "materia": "Matemáticas Especiales",
            "descripcion": "Desarrollo de ejercicios prácticos sobre las temáticas de la unidad 2.",
            "imagen": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=600&auto=format&fit=crop",
            "enlace": ""
        },
        {
            "id": 3,
            "titulo": "Proyecto de Aula / PIA (EnContexto)",
            "materia": "Desarrollo de Software",
            "descripcion": "Presentación del pitch y estructura del proyecto para la convocatoria de proyectos destacados.",
            "imagen": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop",
            "enlace": ""
        }
    ]

# 2. Panel lateral para agregar enlaces manualmente
st.sidebar.header("⚙️ Gestionar Enlaces")
st.sidebar.write("Añade o actualiza el enlace de tu actividad aquí:")

nombres_actividades = [act["titulo"] for act in st.session_state.actividades]
actividad_seleccionada = st.sidebar.selectbox("Selecciona una actividad:", nombres_actividades)

# Obtener objeto de la actividad seleccionada
act_obj = next(act for act in st.session_state.actividades if act["titulo"] == actividad_seleccionada)

# Campo para ingresar el link
nuevo_link = st.sidebar.text_input("Enlace / URL de la actividad:", value=act_obj["enlace"])

if st.sidebar.button("💾 Guardar Enlace"):
    act_obj["enlace"] = nuevo_link
    st.sidebar.success(f"¡Enlace actualizado para '{actividad_seleccionada}'!")
    st.rerun()

st.divider()

# 3. Vista principal del Portafolio
st.subheader("📌 Mis Entregables")

for act in st.session_state.actividades:
    with st.container():
        col_img, col_info = st.columns([1, 2])
        
        # Imagen de la actividad
        with col_img:
            st.image(act["imagen"], use_container_width=True, caption=act["titulo"])
            
        # Información relevante y enlace
        with col_info:
            st.markdown(f"### {act['titulo']}")
            st.caption(f"📚 **Materia/Área:** {act['materia']}")
            st.write(f"**Descripción:** {act['descripcion']}")
            
            if act["enlace"]:
                st.markdown(f"🔗 **[Abrir / Ver Entregables del Portafolio]({act['enlace']})**")
            else:
                st.info("⚠️ Aún no has agregado un enlace para esta actividad. Utiliza el panel lateral de la izquierda para incluirlo.")
                
        st.divider()