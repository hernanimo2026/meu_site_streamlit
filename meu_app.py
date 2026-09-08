import math
import streamlit as st

# Configuração da página
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
# 🧱 LINHA 1: TÍTULO E BOTÃO WHATSAPP
# =========================================================================
st.title("🧮 CALCULADORA DO PEDREIRO")
st.caption("⚠️ O programa está em fase de teste e pode conter erros.")

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
# 🏪 PREÇOS DO DEPÓSITO
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

    with col_dep3:
        st.markdown("**🏠 Cobertura e Madeiramento:**")
        preco_telha_ceramica = st.number_input("Milheiro Telha Cerâmica (R$):", value=1800.0, step=50.0, key="p_t_cer")
        preco_telha_fibro = st.number_input("Telha Fibrocimento 2,44m (R$):", value=58.0, step=2.0, key="p_t_fib")
        preco_telha_sanduiche = st.number_input("Telha Sanduíche / m² (R$):", value=95.0, step=5.0, key="p_t_sand")
        preco_viga_madeira_m = st.number_input("Viga de Madeira (Metro R$):", value=18.5, step=1.0, key="p_vig_m")
        preco_caibro_m = st.number_input("Caibro/Terça (Metro R$):", value=8.0, step=0.5, key="p_caib_m")

st.write("---")

# =========================================================================
# 🗣️ 1. PERGUNTAS SIMPLES AO CLIENTE
# =========================================================================
st.subheader("🗣️ 1. O que o cliente deseja construir?")

descricao_cliente = st.text_input(
    "Descrição simples da obra:",
    value="Orçamento de uma casa de 63m² com 4 cômodos e uma área de circulação",
    key="desc_cliente"
)

col_f1, col_f2 = st.columns(2)

with col_f1:
    area_construcao = st.number_input("Área Total da Construção (m²):", value=63.0, step=1.0, key="f_area")
    qtd_comodos = st.number_input("Quantidade de Cômodos/Divisões:", value=4, step=1, key="f_comodos")
    
    opcao_reboco = st.selectbox(
        "🧱 Acabamento de Reboco/Massa:",
        [
            "2 Lados (Interno e Externo Completo)",
            "1 Lado (Apenas Interno ou Externo)",
            "Sem Reboco (Tijolo Aparente / Sem Massa)"
        ],
        key="sel_reboco_simples"
    )

with col_f2:
    nivel_reforco = st.selectbox(
        "💪 Qual o tipo/reforço da construção?",
        [
            "1. Mais Reforçada (Estrutura Pesada / Ferro 3/8)",
            "2. Reforçada (Padrão Comercial / Ferro 3/8)",
            "3. Menos Reforçada (Padrão Residencial)",
            "4. Economica (Ferro 5/16 + Treliça)",
            "5. Leve (Treliça H8)"
        ],
        index=1,
        key="sel_nivel_reforco"
    )

    tipo_telhado = st.selectbox(
        "🏠 Tipo de Telhado:",
        [
            "Telhado Embutido com Platibanda (Fibrocimento / Sanduíche)",
            "Telhado Aparente com Beiral (Fibrocimento / Sanduíche)",
            "Telhado Tradicional Aparente (Telha Cerâmica)",
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
# 💰 2. VALORAÇÃO E MÃO DE OBRA
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
# 🧮 CÁLCULOS TÉCNICOS AUTOMÁTICOS
# =========================================================================

# Geometria estimada
perimetro_estimado = (math.sqrt(area_construcao) * 4) + (qtd_comodos * 3.5)
altura_padrao = 3.0
area_paredes = perimetro_estimado * altura_padrao

# Alvenaria
qtd_tijolos = area_paredes * 26
milheiros_tijolos = qtd_tijolos / 1000.0
custo_tijolos = milheiros_tijolos * preco_tijolo

# Reboco e Cimento
fator_reboco = 2.0 if "2 Lados" in opcao_reboco else (1.0 if "1 Lado" in opcao_reboco else 0.0)
area_reboco_total = area_paredes * fator_reboco

sacos_cimento_assentamento = math.ceil(area_paredes * 0.20)
sacos_cimento_reboco = math.ceil(area_reboco_total * 0.15)
sacos_cimento_total = sacos_cimento_assentamento + sacos_cimento_reboco
custo_cimento = sacos_cimento_total * preco_cimento

metros_areia = (area_paredes * 0.04) + (area_reboco_total * 0.025)
custo_areia = metros_areia * preco_areia

metros_pedra = area_construcao * 0.08
custo_pedra = metros_pedra * preco_pedra

# Ferragens
if "1." in nivel_reforco or "2." in nivel_reforco or "3." in nivel_reforco:
    preco_ferro_usado = preco_ferro_38
    nome_ferro = "Coluna/Viga 3/8\""
elif "4." in nivel_reforco:
    preco_ferro_usado = preco_ferro_516
    nome_ferro = "Coluna/Viga 5/16\""
else:
    preco_ferro_usado = preco_trelica_h8
    nome_ferro = "Treliça H8"

qtd_varas_ferro = math.ceil((perimetro_estimado * 3) / 6.0)
custo_ferragens = qtd_varas_ferro * preco_ferro_usado

# =========================================================================
# 🪵 REGRA ESPECÍFICA DO MADEIRAMENTO (VIGAS 2m / CAIBROS 1m)
# =========================================================================
lado_estimado = math.sqrt(area_construcao)  # Ex: 63m² ≈ 7.94m x 7.94m
fator_caida_num = int(qtd_caidas[0]) if qtd_caidas[0].isdigit() else 2

if "Fibrocimento / Sanduíche" in tipo_telhado:
    area_telhado = area_construcao * (1.10 if "Aparente" in tipo_telhado else 1.0)
    lado_telhado = math.sqrt(area_telhado)
    
    # Vigas a cada 2.0 metros no sentido da água
    num_linhas_vigas = math.ceil(lado_telhado / 2.0) + 1
    metros_vigas_madeira = num_linhas_vigas * lado_telhado * (1.0 + (fator_caida_num * 0.04))
    
    # Caibros/Terças a cada 1.0 metro no sentido cruzado
    num_linhas_caibros = math.ceil(lado_telhado / 1.0) + 1
    metros_caibros_madeira = num_linhas_caibros * lado_telhado * (1.0 + (fator_caida_num * 0.04))
    
    if "Embutido" in tipo_telhado:
        custo_telhas = area_telhado * preco_telha_sanduiche
    else:
        qtd_placas_fibro = math.ceil(area_telhado / 2.3)
        custo_telhas = qtd_placas_fibro * preco_telha_fibro

elif "Tradicional Aparente" in tipo_telhado:
    area_telhado = area_construcao * 1.20
    lado_telhado = math.sqrt(area_telhado)
    milheiros_telha_cer = (area_telhado * 30) / 1000.0
    custo_telhas = milheiros_telha_cer * preco_telha_ceramica
    
    # Telhado cerâmico tradicional usa ripas/caibros bem mais próximos (0.5m)
    metros_vigas_madeira = (lado_telhado / 1.5 + 1) * lado_telhado
    metros_caibros_madeira = (lado_telhado / 0.5 + 1) * lado_telhado
else:
    custo_telhas = 0.0
    metros_vigas_madeira = 0.0
    metros_caibros_madeira = 0.0

custo_vigas = metros_vigas_madeira * preco_viga_madeira_m
custo_caibros = metros_caibros_madeira * preco_caibro_m
custo_madeira_total = custo_vigas + custo_caibros
custo_cobertura_total = custo_telhas + custo_madeira_total

# Totais
total_materiais = custo_tijolos + custo_cimento + custo_areia + custo_pedra + custo_ferragens + custo_cobertura_total + reserva_materiais
subtotal = total_materiais + valor_mao_obra_total + valor_servicos_extras
total_geral = subtotal - desconto

# =========================================================================
# 📋 RESUMO DO ORÇAMENTO
# =========================================================================
st.subheader("📋 Resumo do Orçamento Gerado")

st.info(f"**Pedido do Cliente:** {descricao_cliente}")

col_r1, col_r2 = st.columns(2)

with col_r1:
    st.markdown("### 🧱 Alvenaria e Acabamento:")
    st.write(f"• **Tijolos:** {int(qtd_tijolos)} un ({milheiros_tijolos:.2f} milheiros) → **R$ {custo_tijolos:,.2f}**")
    st.write(f"• **Opção de Reboco:** {opcao_reboco}")
    st.write(f"• **Cimento Total:** {sacos_cimento_total} sacos → **R$ {custo_cimento:,.2f}**")
    st.write(f"• **Areia:** {metros_areia:.2f} m³ → **R$ {custo_areia:,.2f}**")
    st.write(f"• **Pedra:** {metros_pedra:.2f} m³ → **R$ {custo_pedra:,.2f}**")

with col_r2:
    st.markdown("### 🪵 Estrutura e Madeiramento do Telhado:")
    st.write(f"• **Ferragens ({nome_ferro}):** {qtd_varas_ferro} varas (6m) → **R$ {custo_ferragens:,.2f}**")
    st.write(f"• **Telhas / Cobertura:** R$ {custo_telhas:,.2f}")
    st.write(f"• **Vigas (Espaçamento de 2,0m no caimento):** {metros_vigas_madeira:.1f} m → **R$ {custo_vigas:,.2f}**")
    st.write(f"• **Caibros/Terças (Espaçamento de 1,0m cruzado):** {metros_caibros_madeira:.1f} m → **R$ {custo_caibros:,.2f}**")
    st.write(f"• **Reserva Materiais Extras:** **R$ {reserva_materiais:,.2f}**")

st.write("---")

st.subheader("💰 Resumo Financeiro da Obra")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total de Materiais", f"R$ {total_materiais:,.2f}")
m2.metric("Mão de Obra Total", f"R$ {valor_mao_obra_total:,.2f}")
m3.metric("Serviços Extras", f"R$ {valor_servicos_extras:,.2f}")
m4.metric("TOTAL DA OBRA", f"R$ {total_geral:,.2f}")

st.success(f"✅ **VALOR FINAL ESTIMADO PARA O CLIENTE:** R$ {total_geral:,.2f}")