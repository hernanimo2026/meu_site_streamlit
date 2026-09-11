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
    st.markdown("****🏠 Estrutura da Casa:****")
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
    # --- FERRAGENS OPCIONAIS ---
    incluir_ferragens = st.checkbox("Incluir Ferragens no Orçamento?", value=True, key="chk_ferragens")

    if incluir_ferragens:
        nivel_reforco = st.selectbox(
        "Qual o tipo de ferragem pronta da Casa?",
        [
            "Coluna/Viga 3/8\" Pronta (Padrão Comercial)",
            "Coluna/Viga 5/16\" Pronta (Padrão Econômico)",
            "Treliça H8 / H12 Pronta (Padrão Leve)"
        ],
        index=0,
        key="sel_reforco"
    )
    else:
        nivel_reforco = "Sem Ferragem"
# --- COLUNA 2: FERRAGENS E TELHADO ---
with col_f2:
    # --- FERRAGENS OPCIONAIS ---
    incluir_ferragens = st.checkbox("Incluir Ferragens no Orçamento?", value=True, key="chk_ferragens_casa")
    
    if incluir_ferragens:
        nivel_reforco = st.selectbox(
            "Qual o tipo de ferragem pronta da Casa?",
            [
                "Coluna/Viga 3/8\" Pronta (Padrão Comercial)",
                "Coluna/Viga 5/16\" Pronta (Padrão Econômico)",
                "Treliça H8 / H12 Pronta (Padrão Leve)"
            ],
            index=0,
            key="sel_reforco"
        )
    else:
        nivel_reforco = "Sem Ferragem"

    # --- TELHADO OPCIONAL ---
    incluir_telhado = st.checkbox("Incluir Telhado / Cobertura?", value=True, key="chk_telhado")
    
    if incluir_telhado:
        st.markdown("**🏠 TELHADO:**")
        tipo_telha = st.selectbox(
            "Tipo de Telha:",
            [
                "Fibrocimento (Padrão 6mm)",
                "Isotérmica (Telha Sanduíche)"
            ],
            key="sel_tipo_telha"
        )
        
        estilo_telhado = st.selectbox(
            "Estilo / Estrutura do Telhado:",
            [
                "Telhado Embutido (Com Platibanda)",
                "Telhado Aparente (Com Beiral)"
            ],
            key="sel_estilo_telhado"
        )
        
        qtd_caidas = st.selectbox(
            "Quantidade de Caídas:",
            ["1 Caída", "2 Caídas", "4 Caídas"],
            index=1,
            key="sel_caidas"
        )
        
        opcao_telhado = f"{estilo_telhado} - Telha {tipo_telha}"
    else:
        tipo_telha = "Sem Telha"
        estilo_telhado = "Sem Telhado"
        qtd_caidas = "1 Caída"
        opcao_telhado = "Sem Cobertura / Sem Telhado"

# =========================================================
# LÓGICA DE CÁLCULO (BACKEND)
# =========================================================

# 1. CÁLCULOS BASE (Tem que vir ANTES para não dar erro)
perimetro_casa = (math.sqrt(area_construcao) * 4) + (qtd_comodos * 3.5)
area_paredes_casa = perimetro_casa * 3.0

# ---- A. FERRAGEM DA CASA ----
if incluir_ferragens:
    metros_ferro_casa = perimetro_casa * 1.2
    
    if "3/8" in nivel_reforco:
        fator_consumo_ferro = 1.00
        preco_ferro_casa_usado = preco_ferro_38
        nome_ferro_casa = "Coluna/Viga 3/8\" Pronta"
    elif "5/16" in nivel_reforco:
        fator_consumo_ferro = 1.00
        preco_ferro_casa_usado = preco_ferro_516
        nome_ferro_casa = "Coluna/Viga 5/16\" Pronta"
    else:
        fator_consumo_ferro = 1.00
        preco_ferro_casa_usado = preco_trelica_h8
        nome_ferro_casa = "Treliça Pronta"
        
    varas_ferro_casa = math.ceil(metros_ferro_casa / 6.0)
    custo_ferro_casa = varas_ferro_casa * preco_ferro_casa_usado
else:
    fator_consumo_ferro = 0.0
    preco_ferro_casa_usado = 0.0
    nome_ferro_casa = "Sem Ferragem"
    varas_ferro_casa = 0
    custo_ferro_casa = 0.0


# ---- B. CÁLCULO DA COBERTURA E PLATIBANDA ----
if incluir_telhado:
    if "Platibanda" in estilo_telhado:
        # Telhado Embutido: economiza telha (1.05x), mas exige parede de platibanda (0.80m de altura)
        area_telhado = area_construcao * 1.05
        
        # Platibanda (Alvenaria, Reboco e Respaldo Extra)
        altura_platibanda = 0.80
        area_platibanda = perimetro_casa * altura_platibanda
        
        # Consumos adicionais de material pesado
        tijolos_platibanda = math.ceil(area_platibanda * 26)
        sacos_cimento_platibanda = math.ceil(area_platibanda * 0.25)
        areia_platibanda = area_platibanda * 0.05
        
        # Ferragem de respaldo no topo da platibanda
        varas_ferro_platibanda = math.ceil(perimetro_casa / 6.0)
        custo_ferro_platibanda = varas_ferro_platibanda * (preco_ferro_casa_usado if incluir_ferragens else preco_ferro_38)
        
        # Custo total acumulado da estrutura da platibanda
        custo_platibanda_extra = (
            (tijolos_platibanda / 1000.0 * preco_tijolo) +
            (sacos_cimento_platibanda * preco_cimento) +
            (areia_platibanda * preco_areia) +
            custo_ferro_platibanda
        )
    else:
        # Telhado Aparente: consome 25% a mais de área (beirais), mas não gera alvenaria extra
        area_telhado = area_construcao * 1.25
        custo_platibanda_extra = 0.0

    # Madeiramento e Telhas
    lado_telhado = math.sqrt(area_telhado)
    fator_caida_num = int(qtd_caidas[0]) if (qtd_caidas and qtd_caidas[0].isdigit()) else 2
    
    metros_vigas_madeira = (math.ceil(lado_telhado / 2.0) + 1) * lado_telhado * (1.0 + (fator_caida_num * 0.04))
    
    if "Sanduíche" in tipo_telha:
        custo_telhas = area_telhado * preco_telha_sanduiche
    elif "Fibrocimento" in tipo_telha:
        qtd_placas_fibro = math.ceil(area_telhado / 2.3)
        custo_telhas = qtd_placas_fibro * preco_telha_fibro
    else:
        custo_telhas = 0.0

    # Custo Final da Cobertura (Garante que a Platibanda encareça o Telhado Embutido)
    custo_cobertura_casa = custo_telhas + (metros_vigas_madeira * 12.0) + custo_platibanda_extra
else:
    area_telhado = 0.0
    custo_telhas = 0.0
    metros_vigas_madeira = 0.0
    custo_platibanda_extra = 0.0
    custo_cobertura_casa = 0.0
with col_f3:
    incluir_muro = st.checkbox("Incluir Muro no Orçamento?", value=True, key="chk_muro")
    if incluir_muro:
        st.markdown("**🧱 Muro de Fechamento (Opcional):**")
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

# ---- A. FERRAGEM DA CASA ----
if incluir_ferragens:
    if "3/8" in nivel_reforco:
        fator_consumo_ferro = 1.00
        preco_ferro_casa_usado = preco_ferro_38
        nome_ferro_casa = "Coluna/Viga 3/8\" Pronta"
    elif "5/16" in nivel_reforco:
        fator_consumo_ferro = 1.00
        preco_ferro_casa_usado = preco_ferro_516
        nome_ferro_casa = "Coluna/Viga 5/16\" Pronta"
    else:
        fator_consumo_ferro = 1.00
        preco_ferro_casa_usado = preco_trelica_h8
        nome_ferro_casa = "Treliça Pronta"
else:
    fator_consumo_ferro = 0.0
    preco_ferro_casa_usado = 0.0
    nome_ferro_casa = "Sem Ferragem"    
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
fator_caida_num = int(qtd_caidas[0]) if (qtd_caidas and qtd_caidas[0].isdigit()) else 2

if incluir_telhado:
    # 1. Definição da área do telhado
    area_telhado = area_construcao * (1.10 if "Aparente" in estilo_telhado else 1.0)
    lado_telhado = math.sqrt(area_telhado)
    
    # 2. Cálculos do Madeiramento
    num_linhas_vigas = math.ceil(lado_telhado / 2.0) + 1
    metros_vigas_madeira = num_linhas_vigas * lado_telhado * (1.0 + (fator_caida_num * 0.04))
    
    num_linhas_caibros = math.ceil(lado_telhado / 1.0) + 1
    metros_caibros_madeira = num_linhas_caibros * lado_telhado * (1.0 + (fator_caida_num * 0.04))
    
    # 3. Cálculo Específico por Tipo de Telha
    if "Sanduíche" in tipo_telha:
        custo_telhas = area_telhado * preco_telha_sanduiche
    elif "Fibrocimento" in tipo_telha:
        qtd_placas_fibro = math.ceil(area_telhado / 2.3)
        custo_telhas = qtd_placas_fibro * preco_telha_fibro
    else:
        custo_telhas = 0.0
else:
    # Caso a caixinha do telhado esteja desmarcada
    area_telhado = 0.0
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