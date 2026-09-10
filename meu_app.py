import math
import streamlit as st

# 1. Configuração da página
st.set_page_config(
    page_title="Calculadora do Pedreiro",
    page_icon="🧮",
    layout="wide"
)

# 2. Link da foto de prévia do WhatsApp
LINK_DA_SUA_IMAGEM = "https://images.unsplash.com/photo-1541888946425-d0fbb186a5b7?w=600"

# 3. Metatags Open Graph para redes sociais
st.markdown(f"""
    <div style="display: none;">
        <meta property="og:title" content="🧮 Calculadora do Pedreiro | Orçamentos Rápidos" />
        <meta property="og:description" content="Gere orçamentos precisos para casas, muros e contrapisos em poucos segundos!" />
        <meta property="og:image" content="{LINK_DA_SUA_IMAGEM}" />
        <meta property="og:type" content="website" />
    </div>
""", unsafe_allow_html=True)

# 4. Estilização do botão do WhatsApp
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
    st.write("Mensagem do dia: ***Deus seja louvado!***")
    st.write("Anucios em **GERAL**! [Clique aqui]  (https://drive.google.com/file/d/1J_W1uD78018UqgCo1L2aULdPxU_OF4lh/view?usp=sharing)")

with col2_dir:

     st.link_button("⚠️ WhatsApp", "https://wa.me/5591991211780?text=Olá!%20Vim%20pelo%20site%20e%20gostaria%20de%20um%20orçamento."
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
        preco_pedra = st.number_input("Metro de Pedra/Brita (R$):", value=240.0, step=5.0, key="p_pedra")

    with col_dep2:
        st.markdown("**⛓️ Ferragens (Varas de 6m):**") 
        preco_ferro_38 = st.number_input("Coluna/Viga 3/8 (R$):", value=170.0, step=2.0, key="p_f_38")
        preco_ferro_516 = st.number_input("Coluna/Viga 5/16 (R$):", value=100.0, step=2.0, key="p_f_516")
        preco_trelica_h8 = st.number_input("Treliça H8 (R$):", value=35.0, step=1.0, key="p_t_h8")

    with col_dep3:
        st.markdown("**🏠 Cobertura e Madeiramento:**")
        preco_telha_ceramica = st.number_input("Milheiro Telha Cerâmica (R$):", value=1800.0, step=50.0, key="p_t_cer")
        preco_telha_fibro = st.number_input("Telha Fibrocimento 2,44m (R$):", value=58.0, step=2.0, key="p_t_fib")
        preco_telha_sanduiche = st.number_input("Telha Sanduíche / m² (R$):", value=95.0, step=5.0, key="p_t_sand")
        preco_viga_madeira_m = st.number_input("Viga de Madeira (Metro R$):", value=30.0, step=1.0, key="p_vig_m")
        preco_caibro_m = st.number_input("Caibro/Terça (Metro R$):", value=10.0, step=0.5, key="p_caib_m")

st.write("---")

# =========================================================================
# 🗣️ 1. PERGUNTAS SIMPLES AO CLIENTE
# =========================================================================
st.subheader("🗣️ 1. O que o cliente deseja construir?")

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.markdown("**🏠 Estrutura e Piso da Casa:**")
    area_construcao = st.number_input("Área Total da Casa (m²):", value=63.0, step=1.0, key="f_area")
    qtd_comodos = st.number_input("Quantidade de Cômodos:", value=4, step=1, key="f_comodos")
    
    # --- REBOCO OPCIONAL ---
    incluir_reboco = st.checkbox("Incluir Reboco na Casa?", value=True, key="chk_reboco")
    if incluir_reboco:
        opcao_reboco = st.selectbox(
            "🧱 Tipo de Reboco da Casa:",
            [
                "2 Lados (Interno e Externo Completo)",
                "1 Lado (Apenas Interno ou Externo)"
            ],
            key="sel_reboco_simples"
        )
    else:
        opcao_reboco = "Sem Reboco (Tijolo Aparente / Sem Massa)"

    # --- CONTRAPISO OPCIONAL ---
    incluir_contrapiso = st.checkbox("Incluir Contrapiso / Base?", value=True, key="chk_contrapiso")
    if incluir_contrapiso:
        opcao_contrapiso = st.selectbox(
            "📐 Espessura do Contrapiso:",
            [
                "Contrapiso Padrão (5 cm)",
                "Contrapiso Reforçado (7 cm)"
            ],
            index=0,
            key="sel_contrapiso"
        )
    else:
        opcao_contrapiso = "Sem Contrapiso"
with col_f2:
    st.markdown("**💪 Reforço e Telhado:**")
    nivel_reforco = st.selectbox(
        "Qual o tipo/reforço da construção da Casa?",
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
        "Tipo de Telhado:",
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
            "Quantidade de Caídas:",
            ["1 Caída", "2 Caídas", "3 Caídas", "4 Caídas", "5 Caídas", "6 ou mais Caídas"],
            index=1,
            key="sel_caidas"
        )
    else:
        qtd_caidas = "Nenhuma"

with col_f3:
    st.markdown("**🧱 Muro de Fechamento (Opcional):**")
    incluir_muro = st.checkbox("Incluir Muro no Orçamento?", value=True, key="chk_muro")
    if incluir_muro:
        metros_muro = st.number_input("Comprimento do Muro (Metros):", value=30.0, step=1.0, key="m_muro_m")
        altura_muro = st.number_input("Altura do Muro (Metros):", value=2.0, step=0.1, key="m_muro_h")
        
        opcao_reboco_muro = st.selectbox(
            "Reboco do Muro:",
            [
                "Sem Reboco (Tijolo Aparente)",
                "Rebocar 1 Lado",
                "Rebocar 2 Lados"
            ],
            index=1,
            key="sel_reb_muro"
        )
        
        tipo_ferro_muro = st.selectbox(
            "Ferragem Estrutural do Muro:",
            [
                "Treliça H8 (Padrão / Econômico)",
                "Coluna Ferro 5/16\"",
                "Coluna Ferro 3/8\""
            ],
            index=0,
            key="sel_ferro_muro"
        )
    else:
        metros_muro = 0.0
        altura_muro = 0.0
        opcao_reboco_muro = "Sem Reboco"
        tipo_ferro_muro = "Treliça H8"

# ---- CAMPO DE DESCRIÇÃO AUTOMÁTICO E DINÂMICO ----
partes_desc = [f"Orçamento de uma casa de {int(area_construcao)}m² com {qtd_comodos} cômodos"]

if incluir_reboco:
    partes_desc.append("reboco")
if incluir_contrapiso:
    partes_desc.append("contrapiso")

partes_desc.append("área de circulação")

if incluir_muro:
    partes_desc.append("e muro de fechamento")

texto_dinamico = ", ".join(partes_desc)

descricao_cliente = st.text_input(
    "***Descrição simples da obra:***",
    value=texto_dinamico,
    key=f"desc_cliente_{area_construcao}_{qtd_comodos}_{incluir_reboco}_{incluir_contrapiso}_{incluir_muro}"
)
st.write("---")
# =========================================================================
# 💰 2. VALORAÇÃO E MÃO DE OBRA
# =========================================================================
st.subheader("💰 2. Valoração do Serviço e Mão de Obra")

col_v1, col_v2, col_v3 = st.columns(3)

with col_v1:
    valor_m2_mao_obra = st.number_input("Mão de Obra Casa (R$/m²):", value=400.0, step=10.0, key="v_mo_m2")
    valor_m2_contrapiso_mo = st.number_input("Mão de Obra Contrapiso Extra (R$/m² - Zerar se incluso):", value=0.0, step=5.0, key="v_mo_cp")
    valor_metro_muro_mo = st.number_input("Mão de Obra Muro (R$/Metro Linear):", value=100.0, step=10.0, key="v_mo_muro") if incluir_muro else 0.0
    
    valor_mao_obra_casa = (area_construcao * valor_m2_mao_obra) + (area_construcao * valor_m2_contrapiso_mo if "Sem" not in opcao_contrapiso else 0.0)
    valor_mao_obra_muro = metros_muro * valor_metro_muro_mo
    valor_mao_obra_total = valor_mao_obra_casa + valor_mao_obra_muro
    st.caption(f"Mão de obra Casa: **R$ {valor_mao_obra_casa:,.2f}** | Muro: **R$ {valor_mao_obra_muro:,.2f}**")

with col_v2:
    valor_servicos_extras = st.number_input("Serviços Extras / Acabamento (R$):", value=1000.0, step=100.0, key="v_extras_serv")

with col_v3:
    reserva_materiais = st.number_input("Reserva p/ Materiais Extras (R$):", value=100.0, step=50.0, key="v_reserva_mat")
    desconto = st.number_input("Desconto Concedido (R$):", value=0.0, step=50.0, key="v_desconto")

st.write("---")

# =========================================================================
# 🧮 CÁLCULOS TÉCNICOS SEPARADOS (CASA vs MURO)
# =========================================================================

# --- A. FERRAGEM DA CASA ---
if "1." in nivel_reforco:
    fator_consumo_ferro = 1.30
    preco_ferro_casa_usado = preco_ferro_38
    nome_ferro_casa = "Coluna/Viga 3/8\" (Estrutura Pesada)"
elif "2." in nivel_reforco:
    fator_consumo_ferro = 1.00
    preco_ferro_casa_usado = preco_ferro_38
    nome_ferro_casa = "Coluna/Viga 3/8\" (Padrão Comercial)"
elif "3." in nivel_reforco:
    fator_consumo_ferro = 0.85
    preco_ferro_casa_usado = preco_ferro_38
    nome_ferro_casa = "Coluna/Viga 3/8\" (Padrão Residencial)"
elif "4." in nivel_reforco:
    fator_consumo_ferro = 1.00
    preco_ferro_casa_usado = preco_ferro_516
    nome_ferro_casa = "Coluna/Viga 5/16\""
else:
    fator_consumo_ferro = 1.00
    preco_ferro_casa_usado = preco_trelica_h8
    nome_ferro_casa = "Treliça H8"
# --- B. MATERIAIS DA CASA ---
perimetro_casa = (math.sqrt(area_construcao) * 4) + (qtd_comodos * 3.5)
area_paredes_casa = perimetro_casa * 3.0

qtd_tijolos_casa = area_paredes_casa * 26
milheiros_tijolos_casa = qtd_tijolos_casa / 1000.0
custo_tijolos_casa = milheiros_tijolos_casa * preco_tijolo

fator_reb_casa = 2.0 if "2 Lados" in opcao_reboco else (1.0 if "1 Lado" in opcao_reboco else 0.0)
area_reb_casa = area_paredes_casa * fator_reb_casa

# CÁLCULO DO CONTRAPISO
if "5 cm" in opcao_contrapiso:
    espessura_cp = 0.05
    sacos_cimento_cp = math.ceil(area_construcao * 0.35)
elif "7 cm" in opcao_contrapiso:
    espessura_cp = 0.07
    sacos_cimento_cp = math.ceil(area_construcao * 0.50)
else:
    espessura_cp = 0.0
    sacos_cimento_cp = 0

areia_cp = area_construcao * espessura_cp * 0.60
pedra_cp = area_construcao * espessura_cp * 0.60

# Total Alvenaria + Contrapiso Casa
sacos_cimento_casa = math.ceil((area_paredes_casa * 0.20) + (area_reb_casa * 0.15)) + sacos_cimento_cp
custo_cimento_casa = sacos_cimento_casa * preco_cimento

areia_casa = (area_paredes_casa * 0.04) + (area_reb_casa * 0.025) + areia_cp
custo_areia_casa = areia_casa * preco_areia

pedra_casa = (area_construcao * 0.08) + pedra_cp
custo_pedra_casa = pedra_casa * preco_pedra

varas_ferro_casa = math.ceil(((perimetro_casa * 3) / 6.0) * fator_consumo_ferro)
custo_ferro_casa = varas_ferro_casa * preco_ferro_casa_usado

# Cobertura
fator_caida_num = int(qtd_caidas[0]) if qtd_caidas[0].isdigit() else 2

if "Fibrocimento / Sanduíche" in tipo_telhado:
    area_telhado = area_construcao * (1.10 if "Aparente" in tipo_telhado else 1.0)
    lado_telhado = math.sqrt(area_telhado)
    
    num_linhas_vigas = math.ceil(lado_telhado / 2.0) + 1
    metros_vigas_madeira = num_linhas_vigas * lado_telhado * (1.0 + (fator_caida_num * 0.04))
    
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
    
    metros_vigas_madeira = (lado_telhado / 1.5 + 1) * lado_telhado
    metros_caibros_madeira = (lado_telhado / 0.5 + 1) * lado_telhado
else:
    custo_telhas = 0.0
    metros_vigas_madeira = 0.0
    metros_caibros_madeira = 0.0

custo_vigas = metros_vigas_madeira * preco_viga_madeira_m
custo_caibros = metros_caibros_madeira * preco_caibro_m
custo_cobertura_casa = custo_telhas + custo_vigas + custo_caibros

total_materiais_casa = custo_tijolos_casa + custo_cimento_casa + custo_areia_casa + custo_pedra_casa + custo_ferro_casa + custo_cobertura_casa
total_geral_casa = total_materiais_casa + valor_mao_obra_casa

# --- C. MATERIAIS DO MURO (COM BALDRAME, RESPALDO E COLUNAS A CADA 3M) ---
if incluir_muro:
    area_paredes_muro = metros_muro * altura_muro
    qtd_tijolos_muro = area_paredes_muro * 26
    milheiros_tijolos_muro = qtd_tijolos_muro / 1000.0
    custo_tijolos_muro = milheiros_tijolos_muro * preco_tijolo

    fator_reb_muro = 2.0 if "2 Lados" in opcao_reboco_muro else (1.0 if "1 Lado" in opcao_reboco_muro else 0.0)
    area_reb_muro = area_paredes_muro * fator_reb_muro

    sacos_cimento_muro = math.ceil((area_paredes_muro * 0.20) + (area_reb_muro * 0.15))
    custo_cimento_muro = sacos_cimento_muro * preco_cimento

    areia_muro = (area_paredes_muro * 0.04) + (area_reb_muro * 0.025)
    custo_areia_muro = areia_muro * preco_areia

    pedra_muro = metros_muro * 0.04
    custo_pedra_muro = pedra_muro * preco_pedra

    num_colunas_muro = math.ceil(metros_muro / 3.0) + 1
    metros_colunas_muro = num_colunas_muro * (altura_muro + 0.5)
    
    metros_totais_ferro_muro = metros_muro + metros_muro + metros_colunas_muro
    varas_ferro_muro = math.ceil(metros_totais_ferro_muro / 6.0)

    if "Treliça" in tipo_ferro_muro:
        preco_ferro_muro_usado = preco_trelica_h8
        nome_ferro_muro = "Treliça H8"
    elif "5/16" in tipo_ferro_muro:
        preco_ferro_muro_usado = preco_ferro_516
        nome_ferro_muro = "Coluna 5/16\""
    else:
        preco_ferro_muro_usado = preco_ferro_38
        nome_ferro_muro = "Coluna 3/8\""

    custo_ferro_muro = varas_ferro_muro * preco_ferro_muro_usado

    total_materiais_muro = custo_tijolos_muro + custo_cimento_muro + custo_areia_muro + custo_pedra_muro + custo_ferro_muro
    total_geral_muro = total_materiais_muro + valor_mao_obra_muro
else:
    total_materiais_muro = 0.0
    total_geral_muro = 0.0
    qtd_tijolos_muro = 0
    sacos_cimento_muro = 0
    varas_ferro_muro = 0
    nome_ferro_muro = "Nenhum"
    num_colunas_muro = 0

# Totais Combinados
total_materiais_geral = total_materiais_casa + total_materiais_muro + reserva_materiais
subtotal_obra = total_materiais_geral + valor_mao_obra_total + valor_servicos_extras
total_geral_final = subtotal_obra - desconto

# =========================================================================
# 📋 RESUMO DO ORÇAMENTO
# =========================================================================
st.subheader("📋 Resumo do Orçamento Gerado")

st.info(f"**Pedido do Cliente:** {descricao_cliente}")

col_r1, col_r2 = st.columns(2)

with col_r1:
    st.markdown("### 🏠 Materiais da Casa (Inclui Contrapiso):")
    st.write(f"• **Contrapiso Incluso:** {opcao_contrapiso} ({area_construcao:.0f} m²) → **{sacos_cimento_cp} sacos de cimento**")
    st.write(f"• **Tijolos:** {int(qtd_tijolos_casa)} un → **R$ {custo_tijolos_casa:,.2f}**")
    st.write(f"• **Cimento Total (Paredes + Piso):** {sacos_cimento_casa} sacos → **R$ {custo_cimento_casa:,.2f}**")
    st.write(f"• **Areia Total:** {areia_casa:.2f} m³ | **Pedra/Brita:** {pedra_casa:.2f} m³ → **R$ {(custo_areia_casa + custo_pedra_casa):,.2f}**")
    st.write(f"• **Ferragens Casa ({nome_ferro_casa}):** {varas_ferro_casa} varas (6m) → **R$ {custo_ferro_casa:,.2f}**")
    st.write(f"• **Cobertura/Madeiramento:** **R$ {custo_cobertura_casa:,.2f}**")

with col_r2:
    if incluir_muro:
        st.markdown("### 🧱 Materiais do Muro (Com Baldrame + Respaldo):")
        st.write(f"• **Dimensões:** {metros_muro:.1f}m compr. x {altura_muro:.1f}m alt. ({opcao_reboco_muro})")
        st.write(f"• **Estrutura:** Baldrame + Respaldo + {num_colunas_muro} Colunas (a cada ~3m)")
        st.write(f"• **Tijolos:** {int(qtd_tijolos_muro)} un → **R$ {custo_tijolos_muro:,.2f}**")
        st.write(f"• **Cimento Muro:** {sacos_cimento_muro} sacos → **R$ {custo_cimento_muro:,.2f}**")
        st.write(f"• **Areia Muro:** {areia_muro:.2f} m³ | **Pedra/Brita:** {pedra_muro:.2f} m³ → **R$ {(custo_areia_muro + custo_pedra_muro):,.2f}**")
        st.write(f"• **Ferragem Muro ({nome_ferro_muro}):** {varas_ferro_muro} varas (6m) → **R$ {custo_ferro_muro:,.2f}**")
    else:
        st.markdown("### 🧱 Muro de Fechamento:")
        st.write("• Muro não incluso neste orçamento.")

st.write("---")

# =========================================================================
# 💰 DETALHAMENTO FINANCEIRO DIVIDIDO
# =========================================================================
st.subheader("💰 Divisão dos Valores (Casa vs Muro)")

col_sub1, col_sub2, col_sub3 = st.columns(3)

with col_sub1:
    st.markdown("#### 🏠 TOTAL DA CASA")
    st.write(f"• Materiais (Estrutura + Piso): R$ {total_materiais_casa:,.2f}")
    st.write(f"• Mão de Obra: R$ {valor_mao_obra_casa:,.2f}")
    st.markdown(f"**Subtotal Casa: R$ {total_geral_casa:,.2f}**")

with col_sub2:
    if incluir_muro:
        st.markdown("#### 🧱 TOTAL DO MURO")
        st.write(f"• Materiais: R$ {total_materiais_muro:,.2f}")
        st.write(f"• Mão de Obra: R$ {valor_mao_obra_muro:,.2f}")
        st.markdown(f"**Subtotal Muro: R$ {total_geral_muro:,.2f}**")

with col_sub3:
    st.markdown("#### 🛠️ EXTRAS E DESCONTOS")
    st.write(f"• Serviços Extras: R$ {valor_servicos_extras:,.2f}")
    st.write(f"• Reserva Materiais: R$ {reserva_materiais:,.2f}")
    st.write(f"• Desconto: - R$ {desconto:,.2f}")

st.write("---")

st.success(f"✅ **VALOR TOTAL GERAL DA OBRA:** R$ {total_geral_final:,.2f}")