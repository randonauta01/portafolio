import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Portafolio de Actividades",
    page_icon="💼",
    layout="wide"
)

# Título Principal
st.title("💼 Portafolio de Actividades")
st.write("Gestiona y visualiza tus entregas, imágenes y enlaces de proyectos en un solo lugar.")

# 1. Inicializar la lista de actividades en el estado de la sesión
if "actividades" not in st.session_state:
    st.session_state.actividades = [
        {
            "titulo": "Casos de Prueba (DemoQA)",
            "materia": "Pruebas de Software",
            "descripcion": "Diseño y ejecución de la plantilla de casos de prueba para validación de formularios web.",
            "imagen": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=600&q=80",
            "enlace": "https://docs.google.com/spreadsheets/d/ejemplo"
        },
        {
            "titulo": "Solución Taller 1 - Unidad 2",
            "materia": "Matemáticas Especiales",
            "descripcion": "Desarrollo de ejercicios prácticos sobre las temáticas de la unidad 2.",
            "imagen": "https://images.unsplash.com/photo-1509228468518-180dd4864904?auto=format&fit=crop&w=600&q=80",
            "enlace": ""
        }
    ]

# 2. PANEL LATERAL: Gestión del Portafolio
st.sidebar.header("🛠️ Panel de Control")

opcion = st.sidebar.radio("Selecciona una acción:", ["➕ Nueva Actividad", "🔗 Editar / Agregar Enlace"])

# Opción A: Añadir una nueva actividad desde cero
if opcion == "➕ Nueva Actividad":
    st.sidebar.subheader("Agregar Actividad")
    
    nuevo_titulo = st.sidebar.text_input("Título de la actividad:")
    nueva_materia = st.sidebar.text_input("Materia / Curso:")
    nueva_desc = st.sidebar.text_area("Descripción corta:")
    nueva_imagen = st.sidebar.text_input(
        "URL de la imagen:", 
        placeholder="https://ejemplo.com/imagen.jpg"
    )
    nuevo_enlace = st.sidebar.text_input(
        "Enlace del proyecto / entregable:", 
        placeholder="https://github.com/... o Google Drive"
    )

    if st.sidebar.button("✨ Guardar Actividad", use_container_width=True):
        if nuevo_titulo and nueva_materia:
            # Usar una imagen por defecto si el usuario no pone una
            img_final = nueva_imagen if nueva_imagen else "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=600&q=80"
            
            nueva_act = {
                "titulo": nuevo_titulo,
                "materia": nueva_materia,
                "descripcion": nueva_desc,
                "imagen": img_final,
                "enlace": nuevo_enlace
            }
            
            # Agregar al inicio de la lista para que aparezca primero
            st.session_state.actividades.insert(0, nueva_act)
            st.sidebar.success(f"¡Actividad '{nuevo_titulo}' agregada exitosamente!")
            st.rerun()
        else:
            st.sidebar.error("Por favor ingresa al menos el título y la materia.")

# Opción B: Actualizar el enlace de una actividad existente
elif opcion == "🔗 Editar / Agregar Enlace":
    st.sidebar.subheader("Actualizar Enlace")
    
    if st.session_state.actividades:
        titulos = [act["titulo"] for act in st.session_state.actividades]
        act_sel_titulo = st.sidebar.selectbox("Selecciona la actividad:", titulos)
        
        # Buscar el objeto de la actividad elegida
        act_obj = next(act for act in st.session_state.actividades if act["titulo"] == act_sel_titulo)
        
        link_actualizado = st.sidebar.text_input("Nuevo enlace URL:", value=act_obj["enlace"])
        
        if st.sidebar.button("💾 Actualizar Enlace", use_container_width=True):
            act_obj["enlace"] = link_actualizado
            st.sidebar.success("¡Enlace actualizado correctamente!")
            st.rerun()
    else:
        st.sidebar.info("No hay actividades registradas aún.")

st.divider()

# 3. VISTA PRINCIPAL: Muestra de tarjetas de actividades
st.subheader(f"📌 Entregables ({len(st.session_state.actividades)})")

if not st.session_state.actividades:
    st.info("No hay actividades guardadas. Utiliza el panel lateral para agregar la primera.")

for act in st.session_state.actividades:
    with st.container():
        col_img, col_info = st.columns([1, 2])
        
        # Columna de la Imagen de la Actividad
        with col_img:
            st.image(act["imagen"], use_container_width=True)
            
        # Columna de la Información y Enlaces
        with col_info:
            st.markdown(f"### {act['titulo']}")
            st.caption(f"📚 **Materia:** {act['materia']}")
            
            if act["descripcion"]:
                st.write(act["descripcion"])
            
            st.write("") # Espacio visual
            
            # Botón / Link para ver la entrega
            if act["enlace"]:
                st.markdown(f"👉 **[Ver proyecto / entregable completo 🔗]({act['enlace']})**")
            else:
                st.warning("⚠️ Sin enlace adjunto. Puedes agregarlo desde el panel lateral.")
                
        st.divider()
