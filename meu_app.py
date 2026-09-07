import streamlit as st
import math

# Configuração da página - Título na aba do navegador e layout wide (amplo)
st.set_page_config(
    page_title="Calculadora do Pedreiro Pro",
    page_icon="👷‍♂️",
    layout="wide", # Essencial para responsividade
    initial_sidebar_state="collapsed" # Recolhe a barra lateral se houver
)

# --- Estilização CSS Personalizada para Melhorar o Visual no Celular ---
# Isso ajuda a ajustar margens e tamanhos de fonte em telas menores.
st.markdown("""
<style>
    /* Ajustes para o título principal no celular */
    @media (max-width: 640px) {
        .stTitle {
            font-size: 24px !important;
            text-align: center;
        }
        .stCaption {
            text-align: center;
            font-size: 12px !important;
        }
    }
    /* Estilização do botão do WhatsApp para destaque */
    .stLinkButton > button {
        background-color: #25D366 !important; /* Cor oficial do WhatsApp */
        color: white !important;
        border-radius: 20px;
        font-weight: bold;
        border: none;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    .stLinkButton > button:hover {
        background-color: #128C7E !important; /* Cor mais escura no hover */
    }
</style>
""", unsafe_allow_html=True)

# ========================================================================= #
# 🧱 LINHA 1: TÍTULO PRINCIPAL E AVISO DISCRETO
# ========================================================================= #
# Usamos Markdown para centralizar o título em telas menores via CSS acima
st.title("🧮 CALCULADORA DO PEDREIRO")
st.caption("⚠️ O programa está em fase de testes e pode conter erros.")

# ========================================================================= #
# 🧭 LINHA 2: SUBTÍTULO E BOTÃO WHATSAPP (Ajustado para Responsividade)
# ========================================================================= #
# Usamos colunas. No desktop ficam lado a lado, no celular empilham automaticamente.
col1, col2 = st.columns([2, 1]) # Proporção 2/3 para texto, 1/3 para botão no desktop

with col1:
    st.markdown("### Sistemas de Orçamentos Rápidos — Serviços Gerais")
    st.write("Mensagem do dia? [Clique aqui](https://vt.tiktok.com/ZSqM1je11/)")

with col2:
    # Espaçamento vertical para centralizar o botão com o texto no desktop
    st.write("##") 
    # Botão do WhatsApp com emoji de alerta e texto claro
    # Link direto validado para abrir a conversa com mensagem pré-definida
    st.link_button(
        "⚠️ Falar no WhatsApp", 
        "https://wa.me/5591991211780?text=Olá!%20Vim%20pelo%20site%20e%20gostaria%20de%20um%20orçamento.",
        help="Clique para abrir conversa direta no WhatsApp"
    )

st.divider() # Linha divisória horizontal

# ========================================================================= #
# 🏗️ ÁREA DE MÓDULOS DE CÁLCULO (Exemplo para demonstração)
# ========================================================================= #
st.header("Módulos de Cálculo")

# Exemplo de como organizar módulos usando cards ou colunas
mod1, mod2, mod3 = st.columns(3)

with mod1:
    with st.container(border=True): # Cria um "card" visual
        st.subheader("🏠 Casas e Barracões")
        st.write("Cálculo completo de materiais e mão de obra.")
        st.button("Abrir Módulo", key="btn_casa")

with mod2:
    with st.container(border=True):
        st.subheader("🧱 Muros")
        st.write("Orçamento rápido para construção de muros.")
        st.button("Abrir Módulo", key="btn_muro")

with mod3:
    with st.container(border=True):
        st.subheader("🔨 Reformas")
        st.write("Cálculos diversos para pequenas reformas.")
        st.button("Abrir Módulo", key="btn_reforma")