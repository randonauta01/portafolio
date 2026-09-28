import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Portafolio de Actividades",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Portafolio de Actividades")
st.write("Gestiona y visualiza tus entregas, imágenes y enlaces de proyectos.")

# 1. Inicializar la lista de actividades vacía
if "actividades" not in st.session_state:
    st.session_state.actividades = []

# 2. PANEL LATERAL: Agregar Actividad o Editar Enlaces
st.sidebar.header("🛠️ Panel de Control")

opcion = st.sidebar.radio("Selecciona una acción:", ["➕ Nueva Actividad", "🔗 Editar / Agregar Enlace"])

if opcion == "➕ Nueva Actividad":
    st.sidebar.subheader("Agregar Actividad")
    
    nuevo_titulo = st.sidebar.text_input("Título de la actividad:")
    nueva_materia = st.sidebar.text_input("Materia / Curso:")
    nueva_desc = st.sidebar.text_area("Descripción corta:")
    
    # Subir imagen directamente: Permite Arrastrar, Seleccionar o Pegar con Ctrl+V
    imagen_archivo = st.sidebar.file_uploader(
        "📷 Pega la imagen (Ctrl+V) o arrástrala aquí:", 
        type=["png", "jpg", "jpeg"]
    )
    
    nuevo_enlace = st.sidebar.text_input("Enlace del entregable (Drive, GitHub, etc.):")

    if st.sidebar.button("✨ Guardar Actividad", use_container_width=True):
        if nuevo_titulo and nueva_materia:
            # Si sube imagen la guarda, si no deja una por defecto
            if imagen_archivo is not None:
                img_final = Image.open(imagen_archivo)
            else:
                img_final = None
            
            nueva_act = {
                "titulo": nuevo_titulo,
                "materia": nueva_materia,
                "descripcion": nueva_desc,
                "imagen": img_final,
                "enlace": nuevo_enlace
            }
            
            st.session_state.actividades.insert(0, nueva_act)
            st.sidebar.success(f"¡Actividad '{nuevo_titulo}' agregada!")
            st.rerun()
        else:
            st.sidebar.error("Ingresa al menos el título y la materia.")

elif opcion == "🔗 Editar / Agregar Enlace":
    st.sidebar.subheader("Actualizar Enlace")
    
    if st.session_state.actividades:
        titulos = [act["titulo"] for act in st.session_state.actividades]
        act_sel_titulo = st.sidebar.selectbox("Selecciona la actividad:", titulos)
        
        act_obj = next(act for act in st.session_state.actividades if act["titulo"] == act_sel_titulo)
        
        link_actualizado = st.sidebar.text_input("Nuevo enlace URL:", value=act_obj["enlace"])
        
        if st.sidebar.button("💾 Actualizar Enlace", use_container_width=True):
            act_obj["enlace"] = link_actualizado
            st.sidebar.success("¡Enlace actualizado!")
            st.rerun()
    else:
        st.sidebar.info("Aún no tienes actividades registradas.")

st.divider()

# 3. VISTA PRINCIPAL
st.subheader(f"📌 Entregables ({len(st.session_state.actividades)})")

if not st.session_state.actividades:
    st.info("👋 No hay actividades guardadas aún. Usa el panel lateral izquierdo para agregar la primera.")

for act in st.session_state.actividades:
    with st.container():
        col_img, col_info = st.columns([1, 2])
        
        with col_img:
            if act["imagen"] is not None:
                st.image(act["imagen"], use_container_width=True)
            else:
                st.info("Sin imagen de vista previa")
            
        with col_info:
            st.markdown(f"### {act['titulo']}")
            st.caption(f"📚 **Materia:** {act['materia']}")
            
            if act["descripcion"]:
                st.write(act["descripcion"])
            
            st.write("")
            
            if act["enlace"]:
                st.markdown(f"👉 **[Ver proyecto / entregable completo 🔗]({act['enlace']})**")
            else:
                st.warning("⚠️ Sin enlace adjunto. Puedes agregarlo desde el panel lateral.")
                
        st.divider()
