import streamlit as st
from data_handler import fetch_latest_result, update_history
from analyzer import get_frequency, get_hot_and_cold
from predictor import predict_next

st.set_page_config(page_title="Roulette Predictor", layout="wide")

# Sessão para guardar histórico
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("🎰 XXXtreme Lightning Roulette Predictor")

if st.button("🎲 Atualizar Resultado"):
    latest = fetch_latest_result()
    st.session_state.history = update_history(st.session_state.history, latest)

st.subheader("📊 Últimos 50 Resultados")
st.write([h["number"] for h in st.session_state.history])

freq = get_frequency(st.session_state.history)
hot, cold = get_hot_and_cold(freq)

st.subheader("🔥 Números Quentes")
st.write(hot)

st.subheader("❄️ Números Frios")
st.write(cold)

prediction = predict_next(freq)
st.subheader("🔮 Previsão para Próxima Rodada")
st.write(prediction)