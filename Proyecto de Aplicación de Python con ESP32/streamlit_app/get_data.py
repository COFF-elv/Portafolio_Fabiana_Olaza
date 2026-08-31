import streamlit as st
import requests

# Obtener lecturas del DB cadda 1 segundo
@st.cache_data(ttl=1)
def obtener_data():
    response = requests.get("http://localhost:8080/estado")
    return response.json()

# Obtener lecturas del DB cadda 1 segundo
@st.cache_data(ttl=1)
def obtener_historial():
    response = requests.get("http://localhost:8080/sensor/historial")
    return response.json()

# Obtener lecturas del DB cadda 1 segundo
@st.cache_data(ttl=1)
def obtener_likes():
    response = requests.get("http://localhost:8080/actual")
    return response.json()