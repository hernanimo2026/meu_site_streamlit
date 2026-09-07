import math
import streamlit as st

# Configuração da página para o modo amplo (melhora o visual no computador e celular)
st.set_page_config(layout="wide")

# ========================================================================= #
# 🧱 LINHA 1: TÍTULO PRINCIPAL E AVISO DISCRETO
# ========================================================================= #
st.title("🧮 CALCULADORA DO PEDREIRO")
st.caption("⚠️ O programa está em fase de teste e pode conter erros.")

# ========================================================================= #
# 🧭 LINHA 2: SUBTÍTULO (Esquerda) E BOTÃO WHATSAPP (Direita)
# ========================================================================= #
col2_esq, col2_dir = st.columns(2)
with col2_esq:
    st.write("Sistemas de Orçamentos Rápidos — Serviços Gerais")
    st.write("Mensagem do dia? [Clique aqui](https://vt.tiktok.com/ZSqM1je11/)")

with col2_dir:
    st.link_button(
        "⚠️ WhatsApp do pedreiro", 
        "https://wa.me/5591991211780?text=Olá!%20Vim%20pelo%20site%20e%20gostaria%20de%20um%20orçamento."
    )

# ========================================================================= #
# 🏪 LINHA 3: PREÇOS DO DEPÓSITO (Esquerda) E TIPO DA CONSTRUÇÃO (Direita)
# ========================================================================= #
col3_esq, col3_dir = st.columns(2)
with col3_esq:
    with st.expander("🏪 Preços dos Materiais no Depósito (Clique para abrir)"):
        st.write("Configure os valores cobrados na sua região:")
        
        # Materiais Básicos
        preco_tijolo = st.number_input("Preço do Milheiro de Tijolo (R$):", value=1300.0)
        preco_cimento = st.number_input("Preço do Saco de Cimento (R$):", value=50.0)
        preco_areia = st.number_input("Preço do Metro de Areia (R$):", value=180.0)
        preco_pedra = st.number_input("Preço do Metro de Pedra (R$):", value=240.0)
        
        st.write("---")
        st.write("⛓️ Valores das Ferragens e Colunas:")
        
        # Colunas e Vigas Armadas
        preco_viga_38_7x20 = st.number_input("Coluna/Viga 3/8 7x20 com 6m (R$):", value=150.0)
        preco_viga_38_7x27 = st.number_input("Coluna/Viga 3/8 7x27 com 6m (R$):", value=180.0)
        preco_ferro_516_7x14 = st.number_input("Coluna/Viga 5/16 7x14 com 6m (R$):", value=100.0)
        preco_viga_516_7x20 = st.number_input("Coluna/Viga 5/16 7x20 com 6m (R$):", value=120.0)
        
        # Treliças
        preco_trelica_h8 = st.number_input("Treliça (H8 padrão de 6m) (R$):", value=35.0)
        preco_trelica_h12 = st.number_input("Treliça (H12 padrão de 6m) (R$):", value=45.0)
        preco_trelica_h16 = st.number_input("Treliça (H16 padrão de 6m) (R$):", value=65.0)
        
        st.write("---")
        st.write("🪵 Madeiras e Fixadores:")
        
        # Tábuas e Fixadores
        preco_tabua_20 = st.number_input("Tábua de 20cm com 3m (Unidade R$):", value=20.0)
        preco_tabua_25 = st.number_input("Tábua de 25cm com 3m (Unidade R$):", value=25.0)
        preco_prego = st.number_input("Kg do Prego (R$):", value=25.0)
        preco_arame = st.number_input("Kg do Arame Cozido (R$):", value=30.0)
        
        # Vigas de Madeira e Caibros
        preco_viga_madeira_15 = st.number_input("Preço do metro da Viga 0,05x0,15 (R$):", value=35.0)
        preco_viga_madeira_12 = st.number_input("Preço do metro da Viga 0,05x0,12 (R$):", value=30.0)
        preco_caibro = st.number_input("Preço do metro do Caibro 0,05x0,05 (R$):", value=15.0)

with col3_dir:
    tipo_obra = st.selectbox(
        "Escolha o tipo de construção:",
        ["🏠 Casas e Barracões", "🧱 Construção de Muros", "🔨 Reformas em Geral"],
        label_visibility="collapsed",
        key="seletor_obra"
    )

st.write("---")