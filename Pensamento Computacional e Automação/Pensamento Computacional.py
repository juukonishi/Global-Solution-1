NOME_MISSAO = "Jupiter"
NOME_EQUIPE  = "Jojo"

dados_missao = [
    [22, 95, 91, 98, 92],
    [26, 83, 75, 95, 86],
    [32, 67, 60, 92, 71],
    [37, 44, 35, 88, 52],
    [40, 25, 17, 76, 33],
    [35, 58, 30, 83, 48],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]

# FUNÇÕES DE ANÁLISE

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", "Temperatura baixa", 1
    elif valor <= 30:
        return "NORMAL", "Temperatura estável", 0
    elif valor <= 35:
        return "ATENÇÃO", "Temperatura elevada", 1
    else:
        return "CRÍTICO", "Risco de superaquecimento", 2


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", "Comunicação com a base em nível crítico", 2
    elif valor < 60:
        return "ATENÇÃO", "Comunicação instável", 1
    else:
        return "NORMAL", "Comunicação estável", 0


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", "Bateria em nível crítico", 2
    elif valor < 50:
        return "ATENÇÃO", "Bateria abaixo do recomendado", 1
    else:
        return "NORMAL", "Energia estável", 0


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", "Oxigênio em nível crítico", 2
    elif valor < 90:
        return "ATENÇÃO", "Oxigênio abaixo do ideal", 1
    else:
        return "NORMAL", "Oxigênio adequado", 0


def analisar_estabilidade(valor):
    """Classifica a estabilidade e retorna (status, mensagem, pontos)."""
    if valor < 40:
        return "CRÍTICO", "Estabilidade operacional crítica", 2
    elif valor < 70:
        return "ATENÇÃO", "Estabilidade operacional reduzida", 1
    else:
        return "NORMAL", "Estabilidade operacional adequada", 0


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(resultados):
    criticos = [area for area, (status, _, _) in resultados.items() if status == "CRÍTICO"]

    if not criticos:
        atencoes = [area for area, (status, _, _) in resultados.items() if status == "ATENÇÃO"]
        if not atencoes:
            return "Manter operação normal e continuar monitoramento."
        return "Monitorar sistemas em atenção e preparar plano de contingência."

    recomendacoes_map = {
        "Temperatura interna":      "Verificar controle térmico da missão.",
        "Comunicação com a base":   "Tentar restabelecer contato com a base.",
        "Sistema de energia":       "Ativar modo de economia de energia.",
        "Suporte de oxigênio":      "Acionar protocolo de suporte à vida.",
        "Estabilidade operacional": "Reduzir operações não essenciais.",
    }

    if len(criticos) >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

    return " | ".join(recomendacoes_map[area] for area in criticos if area in recomendacoes_map)


def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de piora."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontuacao_por_area):
    return max(pontuacao_por_area, key=pontuacao_por_area.get)


def analisar_ciclo(ciclo):
    temp, com, bat, oxi, est = ciclo
    return {
        "Temperatura interna":      analisar_temperatura(temp),
        "Comunicação com a base":   analisar_comunicacao(com),
        "Sistema de energia":       analisar_bateria(bat),
        "Suporte de oxigênio":      analisar_oxigenio(oxi),
        "Estabilidade operacional": analisar_estabilidade(est),
    }


def calcular_risco_ciclo(resultados):
    return sum(pontos for _, (_, _, pontos) in resultados.items())

# EXIBIÇÃO

def exibir_cabecalho():
    print("=" * 60)
    print("          MISSION CONTROL AI")
    print("=" * 60)
    print(f"  Missão  : {NOME_MISSAO}")
    print(f"  Equipe  : {NOME_EQUIPE}")
    print(f"  Ciclos  : {len(dados_missao)}")
    print("=" * 60)


def exibir_ciclo(numero, ciclo, resultados, pontuacao, classificacao, recomendacao):
    temp, com, bat, oxi, est = ciclo
    print(f"\nCICLO {numero}")
    print("-" * 60)

    dados_exibicao = [
        ("Temperatura", f"{temp} °C"),
        ("Comunicação", f"{com}%"),
        ("Bateria",     f"{bat}%"),
        ("Oxigênio",    f"{oxi}%"),
        ("Estabilidade",f"{est}%"),
    ]

    for (label, valor), area in zip(dados_exibicao, areas_monitoradas):
        status, mensagem, _ = resultados[area]
        print(f"  {label:12}: {valor:6} | {status:8} | {mensagem}")

    print(f"\n  Pontuação de risco do ciclo : {pontuacao}")
    print(f"  Classificação do ciclo      : {classificacao}")
    print(f"  Recomendação                : {recomendacao}")


def gerar_relatorio_final(riscos, pontuacao_por_area, todos_resultados):
    print("\n" + "=" * 60)
    print("          RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"  Missão : {NOME_MISSAO}")
    print(f"  Equipe : {NOME_EQUIPE}")
    print(f"  Ciclos analisados: {len(dados_missao)}\n")


    labels_medias = ["temperatura", "comunicação", "bateria", "oxigênio", "estabilidade"]
    unidades       = ["°C", "%", "%", "%", "%"]
    for i, (label, unidade) in enumerate(zip(labels_medias, unidades)):
        media = sum(c[i] for c in dados_missao) / len(dados_missao)
        print(f"  Média de {label:12}: {media:.2f}{unidade}")

    ciclo_critico   = riscos.index(max(riscos)) + 1
    risco_medio     = sum(riscos) / len(riscos)
    qtd_criticos    = sum(1 for r in riscos if r >= 6)
    tendencia       = analisar_tendencia(riscos)
    area_afetada    = identificar_area_mais_afetada(pontuacao_por_area)
    risco_total     = sum(riscos)
    classif_final   = classificar_ciclo(risco_medio)

    print(f"\n  Ciclo mais crítico       : Ciclo {ciclo_critico}")
    print(f"  Maior pontuação de risco : {max(riscos)}")
    print(f"  Risco médio da missão    : {risco_medio:.2f}")
    print(f"  Ciclos críticos          : {qtd_criticos}")
    print(f"\n  Tendência da missão:")
    print(f"    {tendencia}")

    print(f"\n  Pontuação acumulada por área:")
    for area, pts in pontuacao_por_area.items():
        print(f"    {area}: {pts} pontos")

    print(f"\n  Área mais afetada:")
    print(f"    {area_afetada}")

    print(f"\n  Classificação final da missão:")
    print(f"    {classif_final}")

    print(f"\n  Conclusão:")
    if risco_medio <= 2:
        conclusao = "A missão transcorreu de forma estável. Todos os sistemas operaram dentro dos parâmetros normais."
    elif risco_medio <= 5:
        conclusao = ("A missão apresentou instabilidade relevante durante a operação. "
                     "Apesar da tentativa de recuperação, ainda existem sistemas em atenção "
                     "e a equipe deve manter o plano de contingência ativo.")
    else:
        conclusao = ("A missão enfrentou situações críticas severas. "
                     "É necessária revisão completa dos sistemas antes de qualquer nova operação.")
    print(f"    {conclusao}")
    print("\n" + "=" * 60)

# EXECUÇÃO PRINCIPAL

def main():
    exibir_cabecalho()

    riscos             = []
    pontuacao_por_area = {area: 0 for area in areas_monitoradas}
    todos_resultados   = []

    for i, ciclo in enumerate(dados_missao):
        resultados   = analisar_ciclo(ciclo)
        pontuacao    = calcular_risco_ciclo(resultados)
        classificacao = classificar_ciclo(pontuacao)
        recomendacao = gerar_recomendacao(resultados)

        riscos.append(pontuacao)
        todos_resultados.append(resultados)

        for area in areas_monitoradas:
            pontuacao_por_area[area] += resultados[area][2]

        exibir_ciclo(i + 1, ciclo, resultados, pontuacao, classificacao, recomendacao)

    gerar_relatorio_final(riscos, pontuacao_por_area, todos_resultados)


if __name__ == "__main__":
    main()
