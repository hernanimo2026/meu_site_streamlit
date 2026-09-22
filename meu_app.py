import urllib.parse
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Urna Simulada", page_icon="🗳️", layout="centered")

st.title("🗳️ Simulador de Votação: Espectros Políticos")
st.write(
    "Vote para acompanhar a apuração em tempo real e entender como funcionam os votos válidos!"
)

st.divider()

# --- SISTEMA DE MEMÓRIA DA URNA ---
if "votos_direita" not in st.session_state:
    st.session_state.votos_direita = 0
if "votos_centrao" not in st.session_state:
    st.session_state.votos_centrao = 0
if "votos_esquerda" not in st.session_state:
    st.session_state.votos_esquerda = 0
if "votos_brancos" not in st.session_state:
    st.session_state.votos_brancos = 0
if "votos_nulos" not in st.session_state:
    st.session_state.votos_nulos = 0
if "voto_realizado" not in st.session_state:
    st.session_state.voto_realizado = False

# Mensagem da corrente pronta para o WhatsApp
mensagem_zap = "📩 Voto registrado com sucesso! Mande para 10 amigos agora para ver o resultado da apuração em tempo real e não quebrar a corrente! 👇\nhttps://urna-simulada-2026.streamlit.app"
link_whatsapp = (
    f"https://api.whatsapp.com/send?text={urllib.parse.quote(mensagem_zap)}"
)

# --- TELA DE VOTAÇÃO OU CONFIRMAÇÃO ---
if not st.session_state.voto_realizado:
    st.header("👤 Escolha seu espectro/opção:")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("👉 Direita"):
            st.session_state.votos_direita += 1
            st.session_state.voto_realizado = True
            st.rerun()

    with col2:
        if st.button("⚖️ Centrão"):
            st.session_state.votos_centrao += 1
            st.session_state.voto_realizado = True
            st.rerun()

    with col3:
        if st.button("👈 Esquerda"):
            st.session_state.votos_esquerda += 1
            st.session_state.voto_realizado = True
            st.rerun()

    with col4:
        if st.button("⚪ BRANCO"):
            st.session_state.votos_brancos += 1
            st.session_state.voto_realizado = True
            st.rerun()

    with col5:
        if st.button("❌ NULO"):
            st.session_state.votos_nulos += 1
            st.session_state.voto_realizado = True
            st.rerun()
else:
    st.success("✅ Seu voto já foi registrado no sistema!")

    # Banner da Corrente (Opção 2)
    st.info(
        "📩 **Mande para 10 amigos agora para ver o resultado da apuração em tempo real e não quebrar a corrente!**"
    )

    # Botão Direto para o WhatsApp
    st.link_button("📲 Compartilhar no WhatsApp", link_whatsapp)

st.divider()

# --- CÁLCULO E EXIBIÇÃO DO PROGRESSO DOS VOTOS ---
st.header("📊 Progresso da Apuração em Tempo Real")

v_dir = st.session_state.votos_direita
v_cen = st.session_state.votos_centrao
v_esq = st.session_state.votos_esquerda
brancos = st.session_state.votos_brancos
nulos = st.session_state.votos_nulos

votos_validos = v_dir + v_cen + v_esq
total_geral = votos_validos + brancos + nulos

pct_dir = (v_dir / votos_validos * 100) if votos_validos > 0 else 0.0
pct_cen = (v_cen / votos_validos * 100) if votos_validos > 0 else 0.0
pct_esq = (v_esq / votos_validos * 100) if votos_validos > 0 else 0.0

# Cartões de Métricas
c1, c2, c3 = st.columns(3)
with c1:
    st.metric(
        label="👉 Direita",
        value=f"{v_dir} votos",
        delta=f"{pct_dir:.1f}% dos válidos",
    )
with c2:
    st.metric(
        label="⚖️ Centrão",
        value=f"{v_cen} votos",
        delta=f"{pct_cen:.1f}% dos válidos",
    )
with c3:
    st.metric(
        label="👈 Esquerda",
        value=f"{v_esq} votos",
        delta=f"{pct_esq:.1f}% dos válidos",
    )

st.caption(
    f"Total na Urna: **{total_geral}** votos | Votos Válidos: **{votos_validos}** | Brancos: **{brancos}** | Nulos: **{nulos}**"
)

# Gráfico de Barras
dados_votos = {
    "Opção": ["Direita", "Centrão", "Esquerda", "Brancos", "Nulos"],
    "Total de Votos": [v_dir, v_cen, v_esq, brancos, nulos],
}
df_votos = pd.DataFrame(dados_votos)
st.bar_chart(df_votos.set_index("Opção"))

st.divider()

# Botão de Reset
if st.button("Zerar Urna (Reset de Teste)"):
    st.session_state.votos_direita = 0
    st.session_state.votos_centrao = 0
    st.session_state.votos_esquerda = 0
    st.session_state.votos_brancos = 0
    st.session_state.votos_nulos = 0
    st.session_state.voto_realizado = False
    st.rerun()
