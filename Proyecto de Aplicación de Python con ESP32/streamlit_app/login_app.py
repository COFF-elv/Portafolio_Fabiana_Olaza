import streamlit as st
import pandas as pd

# Validación simple de usuario y clave con un archivo csv
def validarUsuario(usuario,clave):     
    dfusuarios = pd.read_csv('usuarios.csv')
    # Si encunetra una coincidencia marcará 1 y sino 0, devolviendo True y False respectivamente
    if len(dfusuarios[(dfusuarios['usuario']==usuario) & (dfusuarios['clave']==clave)])>0:
        return True
    else:
        return False

# Muestra el formulario de Login y redirige automáticamente a las páginas correspondientes
def generarLogin():
    if 'usuario' not in st.session_state:
        st.session_state['usuario'] = None      
    # Mostrar formulario si no hay usuario logueado
    if not st.session_state['usuario']:
        with st.form('frmLogin'):
            in_usuario = st.text_input('Usuario')
            in_password = st.text_input('Password', type='password')
            boton_login = st.form_submit_button('Ingresar', type='primary')

            if boton_login:
                # Validación contra CSV
                if validarUsuario(in_usuario, in_password):
                    # Guardamos el usuario en session_state
                    st.session_state['usuario'] = in_usuario
                    # Redirigir según usuario
                    if in_usuario.lower() == "invitado":
                        st.switch_page("pages/general.py")
                    elif in_usuario.lower() == "control":
                        st.switch_page("pages/control_dashboard.py")
                else:
                    # Si el usuario es invalido, mostramos el mensaje de error
                    st.error("Usuario o clave inválidos",icon=":material/gpp_maybe:") 

