import streamlit as st
import plotly.graph_objects as go
import base64

# Set page config
st.set_page_config(
    page_title="Dashboard Analisis",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded"
)

def set_background(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    div[data-testid="stMetric"] {{
        text-align: right;
    }}
    </style>
    """, unsafe_allow_html=True)

set_background("assets/fondo.jpg")

st.markdown("""
<h1 style="
    font-size: 100px;
    color: black;
    font-weight: bold;
    text-align: right;
    margin-top: -50px;
    width: 100%;
">
    ALL THE POWER<br>
    IN <span style="color: hotpink;">ONE CLICK</span>
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-size: 18px;
    color: black;
    text-align: right;
    width: 100%;
    font-weight: bold;
">
    We are here to feel, desire and experience.Be the change, you have the last click.
</p>
""", unsafe_allow_html=True)

col1, col2, col3, col4= st.columns([3,1,2,1])
if 'contador' not in st.session_state:
    st.session_state.contador = 0

with col2:
    st.bar_chart([100], width='stretch', height=500)
with col3:
    with st.container():
        st.image("assets/gif1.gif",  width='stretch')

    with st.container():
        def plot_gauge(indicator_number, indicator_color, indicator_suffix, indicator_title, max_bound):
            fig = go.Figure(
                go.Indicator(
                    value=indicator_number,
                    mode="gauge+number",
                    domain={"x": [0, 1], "y": [0, 1]},
                    number={
                        "suffix": indicator_suffix,
                        "font.size": 20,
                    },
                    gauge={
                        "axis": {"range": [0, max_bound], "tickwidth": 1},
                        "bar": {"color": indicator_color},
                    },
                    title={
                        "text": indicator_title,
                        "font": {"size": 20},
                    },
                )
            )
            fig.update_layout(
                height=150,
                margin=dict(l=10, r=10, t=50, b=10, pad=8),
            )
            st.plotly_chart(fig, width='stretch')
        plot_gauge(70, "hotpink", "%", "Estado", 100)

with col4:
    with st.container():
        st.metric("ESTADO", "EUPHORIA")
    with st.container():
        st.metric("ME GUSTA", st.session_state.contador)
        if st.button("❤️"):
            st.session_state.contador += 1
            st.toast("❤️")



