import math
import streamlit as st

# Configuração da página para modo amplo
st.set_page_config(
    page_title="Calculadora do Pedreiro",
    page_icon="🧮",
    layout="wide"
)

# Estilização visual para o botão do WhatsApp
st.markdown("""
<style>
    .stLinkButton > button {
        background-color: #25D366 !important;
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
        border: none;
    }
    .stLinkButton > button:hover {
        background-color: #128C7E !important;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================================
# 🧱 LINHA 1: TÍTULO PRINCIPAL E AVISO DISCRETO
# =========================================================================
st.title("🧮 CALCULADORA DO PEDREIRO")
st.caption("⚠️ O programa está em fase de teste e pode conter erros.")

# =========================================================================
# 🧭 LINHA 2: SUBTÍTULO E BOTÃO WHATSAPP
# =========================================================================
col2_esq, col2_dir = st.columns(2)
with col2_esq:
    st.write("Sistemas de Orçamentos Rápidos — Serviços Gerais")
    st.write("Mensagem do dia? **DEUS SEJA LOUVADO**")

with col2_dir:
    st.link_button(
        "⚠️ WhatsApp do pedreiro", 
        "https://wa.me/5591991211780?text=Olá!%20Vim%20pelo%20site%20e%20gostaria%20de%20um%20orçamento."
    )

# =========================================================================
# 🏪 PREÇOS DO DEPÓSITO (EXPANDER OCULTO)
# =========================================================================
with st.expander("🏪 Preços dos Materiais no Depósito (Clique para ajustar os valores da sua região)"):
    st.write("Configure os valores cobrados na sua região:")
    
    col_dep1, col_dep2, col_dep3 = st.columns(3)
    
    with col_dep1:
        st.markdown("**🧱 Alvenaria e Agregados:**")
        preco_tijolo = st.number_input("Milheiro de Tijolo (R$):", value=1300.0, step=50.0, key="p_tijolo")
        preco_cimento = st.number_input("Saco de Cimento 50kg (R$):", value=50.0, step=1.0, key="p_cimento")
        preco_areia = st.number_input("Metro de Areia (R$):", value=180.0, step=5.0, key="p_areia")
        preco_pedra = st.number_input("Metro de Pedra (R$):", value=240.0, step=5.0, key="p_pedra")

    with col_dep2:
        st.markdown("**⛓️ Ferragens (Varas de 6m):**") 
        preco_ferro_38 = st.number_input("Coluna/Viga 3/8 (R$):", value=130.0, step=2.0, key="p_f_38")
        preco_ferro_516 = st.number_input("Coluna/Viga 5/16 (R$):", value=65.0, step=2.0, key="p_f_516")
        preco_trelica_h8 = st.number_input("Treliça H8 (R$):", value=32.0, step=1.0, key="p_t_h8")
        preco_trelica_h12 = st.number_input("Treliça H12 (R$):", value=45.0, step=1.0, key="p_t_h12")

    with col_dep3:
        st.markdown("**🏠 Telhados e Coberturas:**")
        preco_telha_ceramica = st.number_input("Milheiro Telha Cerâmica (R$):", value=1800.0, step=50.0, key="p_t_cer")
        preco_telha_fibro = st.number_input("Telha Fibrocimento 2,44m (R$):", value=58.0, step=2.0, key="p_t_fib")
        preco_telha_sanduiche = st.number_input("Telha Sanduíche / m² (R$):", value=95.0, step=5.0, key="p_t_sand")
        preco_madeira_m2 = st.number_input("Estrutura Madeira / m² (R$):", value=45.0, step=5.0, key="p_mad_m2")

st.write("---")

# =========================================================================
# 💬 PERGUNTA DO CLIENTE (MODO FÁCIL E DIRETO)
# =========================================================================
st.subheader("🗣️ 1. O que o cliente deseja construir?")

descricao_cliente = st.text_input(
    "Descrição simples da obra (exemplo do cliente):",
    value="Orçamento de uma casa de 63m² com 4 cômodos e uma área de circulação",
    key="desc_cliente"
)

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    area_construcao = st.number_input("Área Total da Construção (m²):", value=63.0, step=1.0, key="f_area")
    qtd_comodos = st.number_input("Quantidade de Cômodos/Divisões:", value=4, step=1, key="f_comodos")

with col_f2:
    # Pergunta intuitiva sobre o Nível de Reforço da Estrutura
    nivel_reforco = st.selectbox(
        "💪 Qual o tipo/reforço da construção?",
        [
            "1. Mais Reforçada (Estrutura Pesada / Ferro 3/8)",
            "2. Reforçada (Padrão Comercial / Ferro 3/8)",
            "3. Menos Reforçada (Padrão Residencial)",
            "4. Menos Econômica (Reforço Médio)",
            "5. Econômica (Ferro 5/16 + Treliça)",
            "6. Mais Econômica (Estrutura Enxuta)",
            "7. Menos Leve (Treliça H12)",
            "8. Leve (Treliça H8)",
            "9. Mais Leve (Estrutura Leve / Muro/Anexo)"
        ],
        index=1,
        key="sel_nivel_reforco"
    )

with col_f3:
    tipo_telhado = st.selectbox(
        "🏠 Tipo de Telhado:",
        [
            "Telhado Embutido (Platibanda / Telha Fibrocimento/Sanduíche)",
            "Telhado Tradicional (Amostra / Telha Cerâmica)",
            "Sem Cobertura / Laje Exposta"
        ],
        key="sel_tipo_telhado"
    )
    
    if "Sem Cobertura" not in tipo_telhado:
        qtd_caidas = st.selectbox(
            "📐 Quantidade de Caídas (Quedas d'água):",
            ["1 Caída", "2 Caídas", "3 Caídas", "4 Caídas", "5 Caídas", "6 ou mais Caídas"],
            index=1,
            key="sel_caidas"
        )
    else:
        qtd_caidas = "Nenhuma"

st.write("---")

# =========================================================================
# 💰 2. MÃO DE OBRA E VALORES
# =========================================================================
st.subheader("💰 2. Valoração do Serviço e Mão de Obra")

col_v1, col_v2, col_v3 = st.columns(3)

with col_v1:
    valor_m2_mao_obra = st.number_input("Valor da Mão de Obra por m² (R$):", value=350.0, step=10.0, key="v_mo_m2")
    valor_mao_obra_total = area_construcao * valor_m2_mao_obra
    st.caption(f"Mão de obra calculada: **R$ {valor_mao_obra_total:,.2f}**")

with col_v2:
    valor_servicos_extras = st.number_input("Serviços Extras / Acabamento (R$):", value=1000.0, step=100.0, key="v_extras_serv")

with col_v3:
    reserva_materiais = st.number_input("Reserva p/ Materiais Extras (R$):", value=500.0, step=50.0, key="v_reserva_mat")
    desconto = st.number_input("Desconto Concedido (R$):", value=0.0, step=50.0, key="v_desconto")

st.write("---")

# =========================================================================
# 🧮 CÁLCULOS AUTOMÁTICOS BASEADOS NAS RESPOSTAS SIMPLES
# =========================================================================

# 1. Estimativa de Paredes (Média por m² + cômodos)
# Uma casa típica de 63m² com 4 cômodos possui aproximadamente 45 a 55 metros lineares de parede.
perimetro_estimado = (math.sqrt(area_construcao) * 4) + (qtd_comodos * 3.5)
altura_padrao = 3.0
area_paredes = perimetro_estimado * altura_padrao

# 2. Tijolos, Cimento, Areia e Pedra
qtd_tijolos = area_paredes * 26
milheiros_tijolos = qtd_tijolos / 1000.0
custo_tijolos = milheiros_tijolos * preco_tijolo

sacos_cimento = math.ceil(area_construcao * 1.35)  # Média de cimento por m² construído
custo_cimento = sacos_cimento * preco_cimento

metros_areia = area_construcao * 0.18
custo_areia = metros_areia * preco_areia

metros_pedra = area_construcao * 0.08
custo_pedra = metros_pedra * preco_pedra

# 3. Definição do Tipo de Ferro pelo Nível de Reforço
if any(term in nivel_reforco for term in ["1.", "2.", "3."]):
    preco_ferro_usado = preco_ferro_38
    nome_ferro = "Coluna/Viga 3/8\" (Estrutura Reforçada)"
elif any(term in nivel_reforco for term in ["4.", "5.", "6."]):
    preco_ferro_usado = preco_ferro_516
    nome_ferro = "Coluna/Viga 5/16\" (Estrutura Econômica)"
else:
    preco_ferro_usado = preco_trelica_h8
    nome_ferro = "Treliça H8 / Estrutura Leve"

# Estimativa de Varas de Ferro (Pilares + Baldrame + Respaudo + Vergas)
qtd_varas_ferro = math.ceil((perimetro_estimado * 3) / 6.0)
custo_ferragens = qtd_varas_ferro * preco_ferro_usado

# 4. Cálculo do Telhado baseado na escolha e caídas
custo_telhado = 0.0
detalhe_telhado = "Nenhum"

if "Embutido" in tipo_telhado:
    # Telhado embutido usa menos madeira, mas precisa de calhas/platibanda
    custo_telha = area_construcao * (preco_telha_fibro / 2.5)
    custo_madeira = area_construcao * (preco_madeira_m2 * 0.6)
    fator_caida = 1.0 + (int(qtd_caidas[0]) * 0.05) if qtd_caidas[0].isdigit() else 1.1
    custo_telhado = (custo_telha + custo_madeira) * fator_caida
    detalhe_telhado = f"Telhado Embutido com {qtd_caidas}"

elif "Tradicional" in tipo_telhado:
    # Telhado tradicional cerâmico consome mais madeira e telhas
    milheiros_telha_cer = (area_construcao * 30) / 1000.0  # ~30 telhas/m²
    custo_telha = milheiros_telha_cer * preco_telha_ceramica
    fator_caida = 1.0 + (int(qtd_caidas[0]) * 0.08) if qtd_caidas[0].isdigit() else 1.2
    custo_madeira = (area_construcao * preco_madeira_m2) * fator_caida
    custo_telhado = custo_telha + custo_madeira
    detalhe_telhado = f"Telhado Tradicional Cerâmico ({qtd_caidas})"

# Totais
total_materiais = custo_tijolos + custo_cimento + custo_areia + custo_pedra + custo_ferragens + custo_telhado + reserva_materiais
subtotal = total_materiais + valor_mao_obra_total + valor_servicos_extras
total_geral = subtotal - desconto

# =========================================================================
# 📋 RESUMO DO ORÇAMENTO PRONTO PARA O CLIENTE
# =========================================================================
st.subheader("📋 Resumo do Orçamento Gerado")

st.info(f"**Pedido do Cliente:** {descricao_cliente}")

col_r1, col_r2 = st.columns(2)

with col_r1:
    st.markdown("### 🧱 Materiais Calculados:")
    st.write(f"• **Tijolos:** {int(qtd_tijolos)} un ({milheiros_tijolos:.2f} milheiros) → **R$ {custo_tijolos:,.2f}**")
    st.write(f"• **Cimento:** {sacos_cimento} sacos → **R$ {custo_cimento:,.2f}**")
    st.write(f"• **Areia:** {metros_areia:.2f} m³ → **R$ {custo_areia:,.2f}**")
    st.write(f"• **Pedra:** {metros_pedra:.2f} m³ → **R$ {custo_pedra:,.2f}**")

with col_r2:
    st.markdown("### 🏗️ Estrutura e Cobertura:")
    st.write(f"• **Estrutura Escolhida:** {nivel_reforco.split('(')[0]}")
    st.write(f"• **Ferragens ({nome_ferro}):** {qtd_varas_ferro} varas (6m) → **R$ {custo_ferragens:,.2f}**")
    st.write(f"• **Cobertura:** {detalhe_telhado} → **R$ {custo_telhado:,.2f}**")
    st.write(f"• **Reserva Materiais Extras:** **R$ {reserva_materiais:,.2f}**")

st.write("---")

st.subheader("💰 Resumo Financeiro da Obra")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total de Materiais", f"R$ {total_materiais:,.2f}")
m2.metric("Mão de Obra Total", f"R$ {valor_mao_obra_total:,.2f}")
m3.metric("Serviços Extras", f"R$ {valor_servicos_extras:,.2f}")
m4.metric("TOTAL DA OBRA", f"R$ {total_geral:,.2f}")

st.success(f"✅ **VALOR FINAL ESTIMADO PARA O CLIENTE:** R$ {total_geral:,.2f}")