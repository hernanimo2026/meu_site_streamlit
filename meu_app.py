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
    st.write("Mensagem do dia? [Clique aqui](DEUS SEJA LOUVADO)")

with col2_dir:
    st.link_button(
        "⚠️ WhatsApp do pedreiro", 
        "https://wa.me/5591991211780?text=Olá!%20Vim%20pelo%20site%20e%20gostaria%20de%20um%20orçamento."
    )

# =========================================================================
# 🏪 LINHA 3: PREÇOS DO DEPÓSITO E TIPO DA CONSTRUÇÃO
# =========================================================================
col3_esq, col3_dir = st.columns(2)
with col3_esq:
    with st.expander("🏪 Preços dos Materiais no Depósito (Clique para abrir)"):
        st.write("Configure os valores cobrados na sua região:")
        
        # --- 🧱 1. MATERIAIS BÁSICOS E AGREGADOS ---
        st.markdown("**🧱 Alvenaria e Agregados:**")
        preco_tijolo = st.number_input("Preço do Milheiro de Tijolo (R$):", value=1300.0, step=50.0, key="p_tijolo")
        preco_cimento = st.number_input("Preço do Saco de Cimento (R$):", value=50.0, step=1.0, key="p_cimento")
        preco_areia = st.number_input("Preço do Metro de Areia (R$):", value=180.0, step=5.0, key="p_areia")
        preco_pedra = st.number_input("Preço do Metro de Pedra (R$):", value=240.0, step=5.0, key="p_pedra")
        preco_plastificante = st.number_input("Preço do Aditivo Plastificante / Litro (R$):", value=12.0, step=1.0, key="p_plast")
        
        # --- ⛓️ 2. FERRAGENS E AÇO ---
        st.markdown("**⛓️ Ferragens e Estrutura (Varas de 6m):**") 
        preco_ferro_38_7x20 = st.number_input("Coluna/Viga 3/8 7x20 (R$):", value=130.0, step=2.0, key="p_f_38_7x20")
        preco_ferro_38_7x14 = st.number_input("Coluna/Viga 3/8 7x14 (R$):", value=130.0, step=2.0, key="p_f_38_7x14")
        preco_ferro_516_7x14 = st.number_input("Coluna/Viga 5/16 7x14 (R$):", value=65.0, step=2.0, key="p_f_516_7x14")
        preco_viga_516_7x20 = st.number_input("Coluna/Viga 5/16 7x20 (R$):", value=85.0, step=2.0, key="p_v_516_7x20")
        preco_trelica_h8 = st.number_input("Treliça H8 Padrão (R$):", value=32.0, step=1.0, key="p_t_h8")
        preco_trelica_h12 = st.number_input("Treliça H12 Padrão (R$):", value=45.0, step=1.0, key="p_t_h12")
        preco_malha_pop = st.number_input("Malha Pop de Aço 15x15 (R$):", value=110.0, step=5.0, key="p_malha")
        
        # --- 🔩 3. FIXADORES METÁLICOS E BARRAS ROSCADAS ---
        st.markdown("**🔩 Barras Roscadas e Fixação:**")
        preco_barra_rosca_38 = st.number_input("Barra de Rosca Sem Fim 3/8 (Unidade R$):", value=22.0, step=1.0, key="p_br_38")
        preco_barra_rosca_516 = st.number_input("Barra de Rosca Sem Fim 5/16 (Unidade R$):", value=18.0, step=1.0, key="p_br_516")
        preco_conjunto_fix_38 = st.number_input("Conjunto Porca + Arruela 3/8 (Cento R$):", value=35.0, step=2.0, key="p_conj_38")
        preco_conjunto_fix_516 = st.number_input("Conjunto Porca + Arruela 5/16 (Cento R$):", value=28.0, step=2.0, key="p_conj_516")
        preco_parafuso_telha_unidade = st.number_input("Parafuso Autobrocante para Telha (Unidade R$):", value=0.50, step=0.05, key="p_paraf_telha_un")

        # --- 🪵 4. MADEIRAS E FORMAS ---
        st.markdown("**🪵 Madeiras (Caixaria por Peça / Estrutura por Metro):**")
        preco_tabua_30 = st.number_input("Tábua de 30cm com 3m (R$):", value=26.0, step=1.0, key="p_tab_30")
        preco_tabua_25 = st.number_input("Tábua de 25cm com 3m (R$):", value=22.0, step=1.0, key="p_tab_25")
        preco_tabua_20 = st.number_input("Tábua de 20cm com 3m (R$):", value=19.0, step=1.0, key="p_tab_20")
        preco_viga_005x15 = st.number_input("Viga de Madeira 0,05x15 (Preço por Metro) (R$):", value=18.5, step=1.0, key="p_vig_5x15")
        preco_viga_005x12 = st.number_input("Viga de Madeira 0,05x12 (Preço por Metro) (R$):", value=15.0, step=1.0, key="p_vig_5x12")
        preco_caibro_005x005 = st.number_input("Caibro 0,05x0,05 (Preço por Metro) (R$):", value=8.0, step=0.5, key="p_caibro")
        preco_sarrafo_10 = st.number_input("Sarrafo de 10cm com 3m (R$):", value=12.0, step=1.0, key="p_sar_10")
        preco_pontalete = st.number_input("Pontalete/Pernambraco 3x3 com 3m (R$):", value=18.0, step=1.0, key="p_pont")

        # --- 🔧 5. CONSUMÍVEIS DE OBRA ---
        st.markdown("**🔧 Pregos, Arames e Consumíveis:**")
        preco_prego = st.number_input("Preço do kg do Prego 18x27 (R$):", value=22.0, step=1.0, key="p_prego")
        preco_arame = st.number_input("Preço do kg do Arame Recozido (R$):", value=24.0, step=1.0, key="p_arame")
        preco_argamassa_ac1 = st.number_input("Argamassa AC-I 20kg (R$):", value=18.0, step=1.0, key="p_ac1")
        preco_cola_tubo = st.number_input("Adesivo Plástico/Cola p/ Tubo 175g (R$):", value=15.5, step=1.0, key="p_cola")
        preco_lixa_massa = st.number_input("Lixa d'Água / Ferro (Unidade R$):", value=2.5, step=0.5, key="p_lixa")
        
        # --- 💧 6. HIDRÁULICA E ESGOTO ---
        st.markdown("**💧 Hidráulica e Conexões de Água (3/4\" / 25mm e 50mm):**")
        preco_cano_agua_50 = st.number_input("Cano de Água 50mm / Barra 6m (R$):", value=48.0, step=2.0, key="p_c_ag_50")
        preco_cano_agua_25 = st.number_input("Cano de Água 25mm (3/4\") / Barra 6m (R$):", value=19.5, step=1.0, key="p_c_ag_25")
        preco_registro_agua = st.number_input("Registro de Gaveta/Geral 3/4\" (Unidade R$):", value=45.0, step=2.0, key="p_registro")
        preco_registro_chuveiro = st.number_input("Registro de Pressão (Chuveiro) 3/4\" (Unidade R$):", value=55.0, step=2.0, key="p_reg_chuveiro")
        
        preco_joelho_azul_34 = st.number_input("Joelho 90º Ponta Azul 3/4\" (Unidade R$):", value=8.5, step=0.5, key="p_ja_34")
        preco_t_azul_34 = st.number_input("Tê Ponta Azul 3/4\" (Unidade R$):", value=11.0, step=0.5, key="p_ta_34")
        
        preco_luva_34 = st.number_input("Luva Soldável 3/4\" (Unidade R$):", value=1.5, step=0.2, key="p_luv_34")
        preco_joelho_34 = st.number_input("Joelho 90º Soldável 3/4\" (Unidade R$):", value=1.8, step=0.2, key="p_joe_34")
        preco_curva_34 = st.number_input("Curva 90º Soldável 3/4\" (Unidade R$):", value=4.5, step=0.5, key="p_cur_34")
        preco_t_soldavel_34 = st.number_input("Tê Soldável 3/4\" (Unidade R$):", value=2.2, step=0.2, key="p_ts_34")
        preco_joelho_45_34 = st.number_input("Joelho 45º Soldável 3/4\" (Unidade R$):", value=2.5, step=0.2, key="p_j45_34")
        
        st.markdown("**🚽 Esgoto e Drenagem:**")
        preco_cano_esgoto_100 = st.number_input("Cano de Esgoto 100mm / Barra 6m (R$):", value=62.0, step=2.0, key="p_c_esg_100")
        preco_cano_esgoto_50 = st.number_input("Cano de Esgoto 50mm / Barra 6m (R$):", value=32.0, step=1.0, key="p_c_esg_50")
        preco_cano_esgoto_40 = st.number_input("Cano de Esgoto 40mm / Barra 6m (R$):", value=24.0, step=1.0, key="p_c_esg_40")
        preco_conexao_esgoto = st.number_input("Média p/ Conexões de Esgoto (Tê, Curva) (R$):", value=8.0, step=0.5, key="p_con_esg")
        
        # --- ⚡ 7. ELÉTRICA ---
        st.markdown("**⚡ Instalações Elétricas:**")
        preco_conduite_34 = st.number_input("Conduíte Corrugado 3/4 / Rolo 50m (R$):", value=55.0, step=2.0, key="p_cond")
        preco_caixinha_luz = st.number_input("Caixinha de Luz 4x2 (Unidade) (R$):", value=1.8, step=0.2, key="p_cx_luz")
        preco_bocal_lampada = st.number_input("Bocal / Plafon Simples p/ Lâmpada (Unidade R$):", value=6.5, step=0.5, key="p_bocal")
        preco_tomada = st.number_input("Módulo de Tomada Simples 10A/20A (Unidade R$):", value=9.5, step=0.5, key="p_tomada")
        preco_interruptor = st.number_input("Módulo de Interruptor Simples (Unidade R$):", value=9.5, step=0.5, key="p_interr")
        preco_fio_15 = st.number_input("Cabo Elétrico Flexível 1,5mm² / Rolo 100m (R$):", value=120.0, step=5.0, key="p_fio_15")
        preco_fio_25 = st.number_input("Cabo Elétrico Flexível 2,5mm² / Rolo 100m (R$):", value=160.0, step=5.0, key="p_fio_25")
        preco_fio_40 = st.number_input("Cabo Elétrico Flexível 4,0mm² / Rolo 100m (R$):", value=260.0, step=5.0, key="p_fio_40")

        # --- 🏠 8. COBERTURA E TELHAS ---
        st.markdown("**🏠 Cobertura e Telhas:**")
        preco_telha_sanduiche = st.number_input("Telha Sanduíche Termoacústica (m²) (R$):", value=95.0, step=5.0, key="p_telha_sand")
        preco_telha_americana = st.number_input("Preço do Milheiro de Telha Cerâmica (R$):", value=1800.0, step=50.0, key="p_telha_am")
        preco_telha_fibro_244 = st.number_input("Telha Fibrocimento 2,44 x 1,05m (R$):", value=58.0, step=2.0, key="p_telha_fib_244")
        preco_telha_fibro_366 = st.number_input("Telha Fibrocimento 3,66 x 1,05m (R$):", value=89.0, step=2.0, key="p_telha_fib_366")

with col3_dir:
    tipo_obra = st.selectbox(
        "Escolha o tipo de construção:",
        ["🏠 Casas e Barracões", "🧱 Construção de Muros", "🔨 Reformas em Geral"],
        key="seletor_obra"
    )

st.write("---")

# =========================================================================
# 📐 PASSO 3: DIMENSÕES DA OBRA
# =========================================================================
st.subheader("📐 PASSO 3: DIMENSÕES DA OBRA")

col_p3_1, col_p3_2 = st.columns(2)

with col_p3_1:
    comprimento = st.number_input("Digite o comprimento da obra (em metros):", value=9.0, step=0.5, key="p3_comprimento")

with col_p3_2:
    largura = st.number_input("Digite a largura da obra (em metros):", value=7.0, step=0.5, key="p3_largura")

area_total = comprimento * largura
st.info(f"**A área total da sua construção é de:** {area_total:.2f} m²")

st.write("---")

# =========================================================================
# 🧱 PASSO 4: METRAGEM LINEAR DA PAREDE
# =========================================================================
st.subheader("🧱 PASSO 4: METRAGEM LINEAR DA PAREDE")

st.caption("Você pode usar o perímetro automático do cômodo ou adicionar trechos individuais de parede abaixo:")

usar_soma_trechos = st.checkbox("Deseja somar trechos individuais de parede (modo avançado)?", key="chk_trechos")

if usar_soma_trechos:
    num_trechos = st.number_input("Quantos trechos de parede deseja somar?", min_value=1, max_value=20, value=7, step=1, key="num_trechos")
    
    parede_linear = 0.0
    cols_trechos = st.columns(min(int(num_trechos), 7))
    
    for i in range(int(num_trechos)):
        col_idx = i % 4
        with cols_trechos[col_idx]:
            trecho = st.number_input(f"Trecho {i+1} (m):", value=7.0 if i%2==0 else 8.0, step=0.5, key=f"trecho_{i}")
            parede_linear += trecho
else:
    parede_linear = (comprimento + largura) * 2

st.success(f"**Total acumulado de paredes:** {parede_linear:.2f} metros lineares.")

st.write("---")

# =========================================================================
# 📏 PASSO 5: ALTURA PERSONALIZADA (OPCIONAL)
# =========================================================================
st.subheader("📏 PASSO 5: ALTURA PERSONALIZADA (OPCIONAL)")

if "Muros" in tipo_obra:
    sugestao = 2.00
    st.write("Para **Muro**, a altura sugerida é de **2.00m**.")
else:
    sugestao = 3.30
    st.write("Para **Casa/Barracão**, a altura sugerida é de **3.00m** (considere platibandas/oitões).")

usar_sugerida = st.radio(
    "Como deseja definir a altura da parede?",
    ["Usar altura sugerida", "Digitar altura personalizada"],
    key="rad_altura"
)

if usar_sugerida == "Usar altura sugerida":
    altura = sugestao
else:
    altura = st.number_input("Digite a altura personalizada (em metros):", value=sugestao, step=0.10, key="p5_altura_custom")

area_paredes = parede_linear * altura

st.info(f"**Altura definida:** {altura:.2f} metros.")
st.success(f"**A área total das paredes é de:** {area_paredes:.2f} m²")

st.write("---")

# =========================================================================
# ⚙️ 2. ESCOLHA DE ESTRUTURAS E ACABAMENTOS (COM PILARES INTEGRADOS E VERGAS)
# =========================================================================
st.subheader("⚙️ 2. Escolha de Estruturas e Acabamentos")

opcoes_ferragem = [
    "0. Sem Ferragem",
    "1. Ferragem 3/8\"",
    "2. Ferragem 5/16\"",
    "3. Treliça H8",
    "4. Treliça H12"
]

opcoes_reboco = [
    "0. Sem Reboco",
    "1. Reboco em 1 Lado",
    "2. Reboco em 2 Lados (Interno e Externo)"
]

col_op1, col_op2 = st.columns(2)

with col_op1:
    st.markdown("**🔩 Ferragens da Estrutura:**")
    opt_viga_baldram = st.selectbox("Viga Baldrame:", opcoes_ferragem, index=1, key="sel_viga_baldram")
    opt_viga_respaudo = st.selectbox("Viga de Respaudo:", opcoes_ferragem, index=1, key="sel_viga_resp")
    opt_vergas = st.selectbox("Vergas / Contra-vergas:", opcoes_ferragem, index=2, key="sel_vergas")
    
    if "0. Sem" not in opt_vergas:
        qtd_portas_janelas = st.number_input(
            "Quantidade de aberturas (Portas e Janelas):",
            min_value=1,
            value=3,
            step=1,
            key="inp_qtd_aberturas",
            help="Usado para calcular a quantidade necessária de vergas e contra-vergas."
        )
    else:
        qtd_portas_janelas = 0

    st.markdown("**🏛️ Pilares (Colunas em pé):**")
    opcao_pilar = st.selectbox(
        "Qual tipo de COLUNA PRONTA (6m) usar nos pilares?",
        [
            "1 - Coluna Pronta de Ferro 3/8 (Mais reforçada)",
            "2 - Coluna Pronta de Ferro 5/16 (Mais econômica)",
            "3 - Treliça Pronta H8/H12 (Mais leve)",
            "4 - Não incluir colunas nos pilares (Opcional)"
        ],
        key="sel_opcao_pilar"
    )
    
    if "4 -" not in opcao_pilar:
        qtd_pilares = st.number_input("Quantos pilares a obra vai ter?", min_value=1, value=6, step=1, key="inp_qtd_pilares")
    else:
        qtd_pilares = 0

with col_op2:
    st.markdown("**🧱 Acabamento de Parede:**")
    opt_reboco = st.selectbox("Opção de Reboco/Massa:", opcoes_reboco, index=2, key="sel_reboco")

st.write("---")

# =========================================================================
# 💰 3. VALORES FINANCEIROS E SERVIÇOS
# =========================================================================
st.subheader("💰 3. Valores Financeiros e Serviços")

col_fin1, col_fin2 = st.columns(2)

with col_fin1:
    valor_mao_obra = st.number_input("Mão de Obra Total (R$):", value=500.0, step=100.0, key="inp_mo")
    valor_servicos_extras = st.number_input("Serviços Extras (R$):", value=500.0, step=50.0, key="inp_extras_serv")

with col_fin2:
    valor_materiais_extras = st.number_input("Reserva p/ Materiais Extras (R$):", value=300.0, step=50.0, key="inp_extras_mat")
    valor_desconto = st.number_input("Desconto Concedido (R$):", value=0.0, step=50.0, key="inp_desconto")

st.write("---")

# =========================================================================
# 🧮 CÁLCULO DETALHADO DE MATERIAIS E VALORES
# =========================================================================

# Tabela de preços de ferragem
mapa_precos_ferro = {
    "0. Sem Ferragem": 0.0,
    "1. Ferragem 3/8\"": preco_ferro_38_7x14,
    "2. Ferragem 5/16\"": preco_ferro_516_7x14,
    "3. Treliça H8": preco_trelica_h8,
    "4. Treliça H12": preco_trelica_h12
}

# 1. Pilares
if "4 -" not in opcao_pilar:
    metros_pilares = qtd_pilares * altura
    pecas_pilar_6m = math.ceil(metros_pilares / 6.0)
else:
    pecas_pilar_6m = 0.0

if "1 -" in opcao_pilar:
    tipo_pilar = "Coluna 3/8"
    preco_pilar_un = preco_ferro_38_7x14
elif "2 -" in opcao_pilar:
    tipo_pilar = "Coluna 5/16"
    preco_pilar_un = preco_ferro_516_7x14
elif "3 -" in opcao_pilar:
    tipo_pilar = "Treliça"
    preco_pilar_un = preco_trelica_h8
else:
    tipo_pilar = "Nenhum"
    preco_pilar_un = 0.0

custo_pilares_total = pecas_pilar_6m * preco_pilar_un

# 2. Tijolos
CONSUMO_TIJOLO_POR_M2 = 26
qtd_tijolos_total = area_paredes * CONSUMO_TIJOLO_POR_M2
milheiros_tijolo = qtd_tijolos_total / 1000.0
custo_tijolo = milheiros_tijolo * preco_tijolo

# 3. Areia, Cimento e Pedra
metros_areia = area_paredes * 0.05
sacos_cimento_alvenaria = math.ceil(area_paredes * 0.20)
metros_pedra = area_paredes * 0.02

custo_areia = metros_areia * preco_areia
custo_pedra = metros_pedra * preco_pedra

# 4. Vigas Baldrame, Respaudo e Vergas/Contravergas
varas_baldrame = math.ceil(parede_linear / 6.0)
custo_baldrame = varas_baldrame * mapa_precos_ferro[opt_viga_baldram]

varas_respaudo = math.ceil(parede_linear / 6.0)
custo_respaudo = varas_respaudo * mapa_precos_ferro[opt_viga_respaudo]

# Estimativa: Cada abertura consome cerca de 1.80m por peça (verga + contraverga = 3.6m por abertura)
metros_vergas_totais = qtd_portas_janelas * 3.6
varas_vergas = math.ceil(metros_vergas_totais / 6.0) if "0. Sem" not in opt_vergas else 0
custo_vergas = varas_vergas * mapa_precos_ferro[opt_vergas]

# 5. Reboco
fator_reboco = 0
if opt_reboco == "1. Reboco em 1 Lado":
    fator_reboco = 1
elif opt_reboco == "2. Reboco em 2 Lados (Interno e Externo)":
    fator_reboco = 2

area_total_reboco = area_paredes * fator_reboco
sacos_cimento_reboco = math.ceil(area_total_reboco * 0.15)

# Consolidação de Cimento e Ferragens
sacos_cimento_total = sacos_cimento_alvenaria + sacos_cimento_reboco
custo_cimento_total = sacos_cimento_total * preco_cimento
custo_ferragens_estrutura = custo_pilares_total + custo_baldrame + custo_respaudo + custo_vergas

# Totais Gerais
custo_materiais_total = (
    custo_tijolo + 
    custo_areia + 
    custo_cimento_total + 
    custo_pedra + 
    custo_ferragens_estrutura + 
    valor_materiais_extras
)

subtotal = custo_materiais_total + valor_mao_obra + valor_servicos_extras
total_geral = subtotal - valor_desconto

# =========================================================================
# 📋 ORÇAMENTO DETALHADO E RESUMO NA TELA
# =========================================================================
st.subheader("📋 Orçamento Detalhado de Materiais")

st.markdown("### 🧱 Quantidade e Valores Individuais:")

col_m1, col_m2 = st.columns(2)

with col_m1:
    st.write(f"• **Tijolos:** {int(qtd_tijolos_total)} un ({milheiros_tijolo:.2f} milheiros) → **R$ {custo_tijolo:,.2f}**")
    st.write(f"• **Cimento Total:** {sacos_cimento_total} sacos → **R$ {custo_cimento_total:,.2f}**")
    st.write(f"• **Areia:** {metros_areia:.2f} m³ → **R$ {custo_areia:,.2f}**")
    st.write(f"• **Vergas / Contra-vergas:** {varas_vergas} varas (6m) → **R$ {custo_vergas:,.2f}**")

with col_m2:
    st.write(f"• **Pedra:** {metros_pedra:.2f} m³ → **R$ {custo_pedra:,.2f}**")
    st.write(f"• **Pilares ({tipo_pilar}):** {int(pecas_pilar_6m)} peças (6m) → **R$ {custo_pilares_total:,.2f}**")
    st.write(f"• **Vigas (Baldrame/Respaudo):** R$ {custo_baldrame + custo_respaudo:,.2f}")
    st.write(f"• **Reserva Materiais Extras:** **R$ {valor_materiais_extras:,.2f}**")

st.write("---")

st.subheader("💰 Resumo Financeiro Final")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Materiais", f"R$ {custo_materiais_total:,.2f}")
m2.metric("Mão de Obra", f"R$ {valor_mao_obra:,.2f}")
m3.metric("Serviços Extras", f"R$ {valor_servicos_extras:,.2f}")
m4.metric("TOTAL GERAL", f"R$ {total_geral:,.2f}")

st.success(f"**Valor Final Estimado da Obra (Com Desconto):** R$ {total_geral:,.2f}")