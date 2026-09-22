import urllib.parse
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Urna Simulada Nacional", page_icon="🗳️", layout="centered"
)

st.title("🗳️ Simulador de Votação Nacional")
st.write(
    "Selecione o seu estado, vote para acompanhar a apuração em tempo real e entenda como funcionam os votos válidos!"
)

st.divider()

# Lista das Unidades da Federação (26 Estados + DF)
ESTADOS_UF = [
    "AC",
    "AL",
    "AP",
    "AM",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MT",
    "MS",
    "MG",
    "PA",
    "PB",
    "PR",
    "PE",
    "PI",
    "RJ",
    "RN",
    "RS",
    "RO",
    "RR",
    "SC",
    "SP",
    "SE",
    "TO",
]

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
if "historico_estados" not in st.session_state:
    st.session_state.historico_estados = {uf: 0 for uf in ESTADOS_UF}

# Mensagem da corrente para o WhatsApp
mensagem_zap = "📩 Voto registrado com sucesso! Mande para 10 amigos agora para ver o resultado da apuração por estado em tempo real e não quebrar a corrente! 👇\nhttps://meusiteapp-pxdyhvldve88xsg3w6hrkq.streamlit.app"
link_whatsapp = (
    f"https://api.whatsapp.com/send?text={urllib.parse.quote(mensagem_zap)}"
)

# --- TELA DE VOTAÇÃO OU CONFIRMAÇÃO ---
if not st.session_state.voto_realizado:
    st.header("1. Selecione o seu Estado (UF):")
    estado_selecionado = st.selectbox(
        "Escolha a sua Unidade da Federação:",
        ["Selecione..."] + ESTADOS_UF,
    )

    st.header("2. Escolha o seu espectro/opção:")

    # Só libera a votação se o estado for selecionado
    pode_votar = estado_selecionado != "Selecione..."

    if not pode_votar:
        st.warning("⚠️ Selecione o seu estado acima para liberar a votação.")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("👉 Direita", disabled=not pode_votar):
            st.session_state.votos_direita += 1
            st.session_state.historico_estados[estado_selecionado] += 1
            st.session_state.voto_realizado = True
            st.rerun()

    with col2:
        if st.button("⚖️ Centrão", disabled=not pode_votar):
            st.session_state.votos_centrao += 1
            st.session_state.historico_estados[estado_selecionado] += 1
            st.session_state.voto_realizado = True
            st.rerun()

    with col3:
        if st.button("👈 Esquerda", disabled=not pode_votar):
            st.session_state.votos_esquerda += 1
            st.session_state.historico_estados[estado_selecionado] += 1
            st.session_state.voto_realizado = True
            st.rerun()

    with col4:
        if st.button("⚪ BRANCO", disabled=not pode_votar):
            st.session_state.votos_brancos += 1
            st.session_state.historico_estados[estado_selecionado] += 1
            st.session_state.voto_realizado = True
            st.rerun()

    with col5:
        if st.button("❌ NULO", disabled=not pode_votar):
            st.session_state.votos_nulos += 1
            st.session_state.historico_estados[estado_selecionado] += 1
            st.session_state.voto_realizado = True
            st.rerun()
else:
    st.success("✅ Seu voto já foi registrado no sistema!")

    st.info(
        "📩 **Mande para 10 amigos do seu estado para ver o resultado da apuração em tempo real e não quebrar a corrente!**"
    )

    st.link_button("📲 Compartilhar no WhatsApp", link_whatsapp)

st.divider()

# --- CÁLCULO E EXIBIÇÃO DO PROGRESSO DOS VOTOS ---
st.header("📊 Progresso da Apuração Geral")

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

# Gráfico de Votos por Espectro
dados_votos = {
    "Opção": ["Direita", "Centrão", "Esquerda", "Brancos", "Nulos"],
    "Total de Votos": [v_dir, v_cen, v_esq, brancos, nulos],
}
df_votos = pd.DataFrame(dados_votos)
st.bar_chart(df_votos.set_index("Opção"))

st.divider()

# --- MAPA/GRÁFICO DE PARTICIPAÇÃO POR ESTADO ---
st.header("🗺️ Participação por Estado (UF)")

df_estados = pd.DataFrame(
    list(st.session_state.historico_estados.items()),
    columns=["Estado", "Total de Votos"],
)
# Exibe apenas os estados com votos registrados
df_estados_com_votos = df_estados[df_estados["Total de Votos"] > 0]

if not df_estados_com_votos.empty:
    st.bar_chart(df_estados_com_votos.set_index("Estado"))
else:
    st.info("Nenhum voto registrado por estado até o momento.")

st.divider()

# Botão de Reset
if st.button("Zerar Urna (Reset de Teste)"):
    st.session_state.votos_direita = 0
    st.session_state.votos_centrao = 0
    st.session_state.votos_esquerda = 0
    st.session_state.votos_brancos = 0
    st.session_state.votos_nulos = 0
    st.session_state.voto_realizado = False
    st.session_state.historico_estados = {uf: 0 for uf in ESTADOS_UF}
    st.rerun()