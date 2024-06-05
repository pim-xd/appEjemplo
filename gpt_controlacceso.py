import streamlit as st
import pandas as pd
import os

# Definir la ruta del archivo de registro de usuarios
registro_usuarios_path = './data/registroUsuarios.csv'

# Crear la carpeta y el archivo si no existen
os.makedirs('./data', exist_ok=True)
if not os.path.exists(registro_usuarios_path):
    df = pd.DataFrame(columns=['dni', 'nombre', 'apellido', 'mail'])
    df.to_csv(registro_usuarios_path, index=False)

# Función para cargar datos de archivos CSV
def load_data(filename):
    return pd.read_csv(filename)

# Función para guardar datos en archivos CSV
def save_to_csv(data, filename):
    if os.path.exists(filename):
        data.to_csv(filename, mode='a', header=False, index=False)
    else:
        data.to_csv(filename, index=False)

# Página de inicio
def inicio_page():
    st.title("Bienvenido")
    email = st.text_input("Ingrese su email")
    if st.button("Acceder"):
        df_usuarios = load_data(registro_usuarios_path)
        if email in df_usuarios['mail'].values:
            st.session_state.page = "menu_opciones"
        else:
            st.session_state.page = "registro_usuario"

# Página de registro de usuarios
def registro_page():
    st.title("Registro de Usuario")
    dni = st.text_input("DNI")
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")
    email = st.text_input("Email")
    if st.button("Registrar"):
        nuevo_usuario = pd.DataFrame({'dni': [dni], 'nombre': [nombre], 'apellido': [apellido], 'mail': [email]})
        save_to_csv(nuevo_usuario, registro_usuarios_path)
        st.success("Usuario registrado con éxito")
        st.session_state.page = "menu_opciones"
    if st.button("Volver a inicio"):
        st.session_state.page = "inicio"

# Página de menú de opciones
def menu_opciones_page():
    st.title("Menu Opciones")
    st.write("Bienvenido al menú de opciones.")
    if st.button("Volver a inicio"):
        st.session_state.page = "inicio"

# Inicialización de la sesión
if 'page' not in st.session_state:
    st.session_state.page = "inicio"

# Navegación entre páginas
if st.session_state.page == "inicio":
    inicio_page()
elif st.session_state.page == "registro_usuario":
    registro_page()
elif st.session_state.page == "menu_opciones":
    menu_opciones_page()
