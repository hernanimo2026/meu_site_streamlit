import math
import streamlit as st

# Configuração da página para o modo amplo (melhora o visual no computador)
st.set_page_config(layout="wide")

# ========================================================================= #
# 🧱 LINHA 1: TÍTULO PRINCIPAL (Fixo no topo absoluto)
# ========================================================================= #
st.title("🧮 CALCULADORA DO PEDREIRO")

# ========================================================================= #
# 🧭 LINHA 2: SUBTÍTULO (Esquerda) E CHAT DE NEGOCIAÇÃO (Direita)
# ========================================================================= #
col2_esq, col2_dir = st.columns(2)
with col2_esq:
    st.write("Sistemas de Orçamentos Rápidos — Serviços Gerais")

with col2_dir:
    opcao_chat = st.selectbox(
        "Acessar Mensagens:",
        ["FALE COM O PEDREIRO", "💬 Abrir Chat de Negociação"],
        label_visibility="collapsed",
        key="seletor_chat"
    )

st.write(" ")  # Pequeno espaço entre as linhas

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

# ========================================================================= #
# 🔄 LÓGICA DE EXIBIÇÃO DAS TELAS
# ========================================================================= #
if opcao_chat == "💬 Abrir Chat de Negociação":
    st.markdown("### 💬 Chat de Negociação Direta")
    st.write("Combine detalhes, prazos e valores em tempo real com seu cliente.")
    st.write("---")

    with st.chat_message("user", avatar="👷‍♂️"):
        st.write("**Você (Profissional):** Olá! Acabei de gerar o orçamento aqui no sistema.")

    with st.chat_message("assistant", avatar="👤"):
        st.write("**Cliente:** Opa, amigo! Consegue dar um descontinho se fechar à vista?")

    nova_msg = st.chat_input("Digite sua mensagem para o cliente aqui...")

else:
    # 🏠 1. MÓDULO: CASAS E BARRACÕES
    if tipo_obra == "🏠 Casas e Barracões":
        st.subheader("🏠 Módulo: Casas e Barracões")
        st.write("Área total da construção:")
        area = st.number_input("Metragem quadrada (m²):", value=50.0)
        st.info("Próximo passo: adicionar os cálculos estruturais aqui...")

    # 🧱 2. MÓDULO: CONSTRUÇÃO DE MUROS
    elif tipo_obra == "🧱 Construção de Muros":
        st.subheader("🧱 Módulo: Construção de Muros")
        
        # 1. ENTRADAS DE DIMENSÕES
        st.markdown("### 📌 1. Dimensões do Muro")
        col_muro1, col_muro2 = st.columns(2)
        with col_muro1:
            comprimento = st.number_input("Comprimento do muro (metros):", value=10.0, step=0.5, key="muro_comp")
        with col_muro2:
            altura = st.number_input("Altura do muro (metros):", value=2.0, step=0.1, key="muro_alt")

        area_muro = comprimento * altura
        st.write("---")

        # 2. CONFIGURAÇÕES E PREMISSAS TÉCNICAS
        st.markdown("### ⚙️ 2. Configurações Estruturais")
        
        # Banco de dados centralizado da ferragem (Evita variáveis soltas)
        dados_ferragem = {
            "Coluna/Viga 5/16 7x14 com 6m": {"preco": preco_ferro_516_7x14, "largura_viga": 0.10, "altura_viga": 0.20},
            "Coluna/Viga 5/16 7x20 com 6m": {"preco": preco_viga_516_7x20, "largura_viga": 0.10, "altura_viga": 0.25},
            "Treliça H8 padrão de 6m":       {"preco": preco_trelica_h8,    "largura_viga": 0.08, "altura_viga": 0.12},
            "Treliça H12 padrão de 6m":      {"preco": preco_trelica_h12,   "largura_viga": 0.08, "altura_viga": 0.17},
        }
        opcoes_ferragem = list(dados_ferragem.keys())

        col_viga1, col_viga2, col_viga3 = st.columns(3)
        
        with col_viga1:
            st.markdown("**⛓️ Ferragens Prontas:**")
            tem_baldrame = st.checkbox("Incluir Viga Baldrame (Chão)", value=True, key="chk_bald")
            viga_baldrame = st.selectbox("Ferragem do Baldrame:", opcoes_ferragem, disabled=not tem_baldrame, key="sel_bald")
            
            tem_respaldo = st.checkbox("Incluir Viga de Respaldo (Topo)", value=True, key="chk_resp")
            viga_respaldo = st.selectbox("Ferragem do Respaldo:", opcoes_ferragem, disabled=not tem_respaldo, key="sel_resp")
            
            viga_coluna = st.selectbox("Ferragem das Colunas/Pilares:", opcoes_ferragem, key="sel_col")

        with col_viga2:
            st.markdown("**🪵 Caixaria e Espaçamento:**")
            tipo_tabua = st.selectbox("Tábua para Formas:", ["Tábua de 20cm com 3m", "Tábua de 25cm com 3m"], key="sel_tabua")
            # Amarração direta do preço selecionado
            preco_tabua_atual = preco_tabua_25 if tipo_tabua == "Tábua de 25cm com 3m" else preco_tabua_25
            distancia_pilares = st.number_input("Distância entre Pilares (metros):", value=2.0, step=0.5, key="num_pilares")

        with col_viga3:
            st.markdown("**👷 Mão de Obra e Ajustes:**")
            preco_mao_obra_m2 = st.number_input("Mão de Obra por m² (R$):", value=100.0, step=5.0, key="num_mo")
            custo_material_avulso = st.number_input("Materiais Avulsos (R$):", value=0.0, step=50.0, key="num_avulso")
            custo_servico_extra = st.number_input("Serviços Extras (R$):", value=0.0, step=50.0, key="num_extra")
            valor_desconto = st.number_input("Desconto no Total Geral (R$):", value=0.0, step=10.0, key="num_desc")

        st.write("---")

        # 3. BLOCO ÚNICO DE CÁLCULO (Sem repetições, tudo em cascata)
        
        # A) Ferragens (Unidades e Preços)
        varas_baldrame = math.ceil(comprimento / 6) if tem_baldrame else 0
        varas_respaldo = math.ceil(comprimento / 6) if tem_respaldo else 0
        
        qtd_colunas_verticais = math.ceil(comprimento / distancia_pilares) + 1
        metragem_colunas = qtd_colunas_verticais * altura
        varas_colunas = math.ceil(metragem_colunas / 6)

        custo_ferragem = (
            (varas_baldrame * dados_ferragem[viga_baldrame]["preco"]) +
            (varas_respaldo * dados_ferragem[viga_respaldo]["preco"]) +
            (varas_colunas * dados_ferragem[viga_coluna]["preco"])
        )

        # B) Concreto Dinâmico (Volume baseado estritamente na ferragem escolhida)
        vol_bald = comprimento * (dados_ferragem[viga_baldrame]["largura_viga"] * dados_ferragem[viga_baldrame]["altura_viga"]) if tem_baldrame else 0
        vol_resp = comprimento * (dados_ferragem[viga_respaldo]["largura_viga"] * dados_ferragem[viga_respaldo]["altura_viga"]) if tem_respaldo else 0
        vol_cols = metragem_colunas * (dados_ferragem[viga_coluna]["largura_viga"] * dados_ferragem[viga_coluna]["altura_viga"])
        
        volume_concreto_total = vol_bald + vol_resp + vol_cols

        # C) Insumos Básicos (Cimento, Areia, Pedra, Tijolo)
        qtd_tijolos = math.ceil(area_muro * 30)
        custo_tijolos = (qtd_tijolos / 1000) * preco_tijolo

        cimento_necessario = (volume_concreto_total * 7) + (area_muro * 0.35)
        areia_necessaria = (volume_concreto_total * 0.6) + (area_muro * 0.05)
        pedra_necessaria = volume_concreto_total * 0.8

        qtd_cimento = math.ceil(cimento_necessario * 1.1)
        qtd_areia = round(areia_necessaria * 1.1, 2)
        qtd_pedra = round(pedra_necessaria * 1.1, 2)

        custo_insumos = (qtd_cimento * preco_cimento) + (qtd_areia * preco_areia) + (qtd_pedra * preco_pedra) + (preco_prego * 2) + (preco_arame * 2)

      # D) Caixaria Dinâmica (Considerando Comprimento E Altura da Viga)
        # Identifica a largura real da tábua escolhida pelo usuário (0.30m ou 0.25m)
        largura_tabua_m = 0.30 if tipo_tabua == "Tábua de 30cm com 3m" else 0.25

        # Descobre quantas passadas de tábua verticalmente são necessárias para cobrir a altura de cada viga
        passadas_bald = math.ceil(dados_ferragem[viga_baldrame]["altura_viga"] / largura_tabua_m) if tem_baldrame else 0
        passadas_resp = math.ceil(dados_ferragem[viga_respaldo]["altura_viga"] / largura_tabua_m) if tem_respaldo else 0
        passadas_cols = math.ceil(dados_ferragem[viga_coluna]["largura_viga"] / largura_tabua_m) # coluna usa a largura como face de caixaria

        # Metragem linear total ajustada pela quantidade de passadas de tábua
        formas_bald_total = (comprimento * 2) * passadas_bald
        formas_resp_total = (comprimento * 2) * passadas_resp
        formas_cols_total = (metragem_colunas * 2) * passadas_cols

        # Cenário Tradicional (Soma tudo)
        metragem_linear_formas = formas_bald_total + formas_resp_total + formas_cols_total
        qtd_tabuas_tradicional = math.ceil(metragem_linear_formas / 3)
        custo_tabuas_tradicional = qtd_tabuas_tradicional * preco_tabua_atual

        # Cenário Otimizado (Pega o maior pico de uso simultâneo)
        pico_formas = max(formas_bald_total, formas_resp_total, formas_cols_total)
        qtd_tabuas_otimizada = max(math.ceil(pico_formas / 3), 2)
        custo_tabuas_otimizada = qtd_tabuas_otimizada * preco_tabua_atual

        # E) Fechamento Financeiro
        custo_mao_obra = (area_muro * preco_mao_obra_m2) + custo_servico_extra

        subtotal_tradicional = custo_ferragem + custo_tijolos + custo_insumos + custo_tabuas_tradicional + custo_material_avulso
        total_tradicional = (subtotal_tradicional + custo_mao_obra) - valor_desconto

        subtotal_otimizado = custo_ferragem + custo_tijolos + custo_insumos + custo_tabuas_otimizada + custo_material_avulso
        total_otimizado = (subtotal_otimizado + custo_mao_obra) - valor_desconto

   # 4. INTERFACE DE EXIBIÇÃO DE RESULTADOS
        st.markdown("### 📊 3. Resumo Econômico e Insumos")
        
        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            st.markdown("**📋 Comparativo de Cenários:**")
            dados_comparativos = {
                "Métrica / Item": ["🧱 Madeiras Necessárias", "🪵 Custo Total de Materiais", "👷 Custo de Mão de Obra", "💰 VALOR TOTAL GERAL"],
                "Sem Reaproveitamento": [f"{qtd_tabuas_tradicional} un", f"R$ {subtotal_tradicional:,.2f}", f"R$ {custo_mao_obra:,.2f}", f"R$ {total_tradicional:,.2f}"],
                "Com Otimização": [f"{qtd_tabuas_otimizada} un", f"R$ {subtotal_otimizado:,.2f}", f"R$ {custo_mao_obra:,.2f}", f"R$ {total_otimizado:,.2f}"]
            }
            st.table(dados_comparativos)
            
            economia = total_tradicional - total_otimizado
            if economia > 0:
                st.success(f"🎉 A otimização de caixaria gera **R$ {economia:,.2f}** de economia pura!")
        with col_res2:
            st.markdown("**🧱 Memória de Cálculo / Lista de Materiais (Otimizada):**")
            
            # --- SEÇÃO DE FERRAGENS DETALHADA ---
            st.markdown("**⛓️ Ferragens:**")
            if tem_baldrame:
                custo_b = varas_baldrame * dados_ferragem[viga_baldrame]["preco"]
                st.write(f"• **Viga Baldrame:** {varas_baldrame} varas de 6m ({viga_baldrame}) → **R$ {custo_b:,.2f}**")
            if tem_respaldo:
                custo_r = varas_respaldo * dados_ferragem[viga_respaldo]["preco"]
                st.write(f"• **Viga Respaldo:** {varas_respaldo} varas de 6m ({viga_respaldo}) → **R$ {custo_r:,.2f}**")
            
            custo_c = varas_colunas * dados_ferragem[viga_coluna]["preco"]
            st.write(f"• **Colunas/Pilares:** {varas_colunas} varas de 6m ({viga_coluna}) → **R$ {custo_c:,.2f}**")
            
            # --- SEÇÃO DE MADEIRAS DETALHADA ---
            st.markdown("**🪵 Caixaria:**")
            st.write(f"• **{tipo_tabua}:** {qtd_tabuas_otimizada} unidades → **R$ {custo_tabuas_otimizada:,.2f}**")
            
            # --- SEÇÃO DE INSUMOS BRUTOS E OUTROS ---
            st.markdown("**🧱 Alvenaria e Agregados:**")
            st.write(f"• **Tijolos:** {qtd_tijolos} unidades → **R$ {custo_tijolos:,.2f}**")
            st.write(f"• **Cimento (50kg):** {qtd_cimento} sacos → **R$ {(qtd_cimento * preco_cimento):,.2f}**")
            st.write(f"• **Areia:** {qtd_areia} m³ → **R$ {(qtd_areia * preco_areia):,.2f}**")
            st.write(f"• **Pedra:** {qtd_pedra} m³ → **R$ {(qtd_pedra * preco_pedra):,.2f}**")
            
            st.markdown("**🔧 Fixadores e Diversos:**")
            st.write(f"• **Pregos (Estimado):** 2 kg → **R$ {(preco_prego * 2):,.2f}**")
            st.write(f"• **Arame Recozido (Estimado):** 2 kg → **R$ {(preco_arame * 2):,.2f}**")
            if custo_material_avulso > 0:
                st.write(f"• **Materiais Avulsos:** R$ {custo_material_avulso:,.2f}")
            
            st.caption(f"*(Volume total calculado de concreto para as vigas/pilares: {volume_concreto_total:.2f} m³)*")

        st.write("---")
