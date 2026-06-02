NOME_MISSAO = "Mission Control"
NOME_EQUIPE  = "Júlia Konishi, João Scheren, João Neves"

dados_missao = [
    [22, 95, 91, 30, 92],
    [26, 83, 75, 45, 86],
    [32, 67, 60, 58, 71],
    [37, 44, 35, 72, 52],
    [40, 25, 17, 88, 33],
    [35, 58, 30, 65, 48],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Geração de energia solar",
    "Consumo energético",
    "Eficiência do sistema",
]

def analisar_temperatura(valor):

    if valor < 18:
        return "ATENÇÃO", "Temperatura baixa — risco de redução na eficiência dos painéis", 1
    elif valor <= 30:
        return "NORMAL", "Temperatura estável — painéis operando em faixa ideal", 0
    elif valor <= 35:
        return "ATENÇÃO", "Temperatura elevada — eficiência dos painéis reduzida", 1
    else:
        return "CRÍTICO", "Superaquecimento — painéis solares em risco de dano", 2


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", "Comunicação crítica — controle energético remoto comprometido", 2
    elif valor < 60:
        return "ATENÇÃO", "Comunicação instável — monitoramento energético prejudicado", 1
    else:
        return "NORMAL", "Comunicação estável — telemetria energética operacional", 0


def analisar_energia_solar(valor):
    if valor < 20:
        return "CRÍTICO", "Geração solar crítica — reservas de emergência ativadas", 2
    elif valor < 50:
        return "ATENÇÃO", "Geração solar reduzida — consumo deve ser priorizado", 1
    else:
        return "NORMAL", "Geração solar adequada — energia renovável estável", 0


def analisar_consumo_energia(valor):
    if valor > 80:
        return "CRÍTICO", "Consumo crítico — deficit energético iminente", 2
    elif valor > 55:
        return "ATENÇÃO", "Consumo elevado — acionar modo de economia de energia", 1
    else:
        return "NORMAL", "Consumo dentro do limite sustentável", 0


def analisar_eficiencia(valor):
    if valor < 40:
        return "CRÍTICO", "Eficiência crítica — perdas energéticas severas", 2
    elif valor < 70:
        return "ATENÇÃO", "Eficiência reduzida — otimizar distribuição de energia", 1
    else:
        return "NORMAL", "Eficiência adequada — sistema energético sustentável", 0


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
            return "Manter operação normal — sistema energético sustentável."
        return "Monitorar consumo e geração solar. Avaliar plano de contingência energética."

    recomendacoes_map = {
        "Temperatura interna":      "Acionar resfriamento dos painéis solares imediatamente.",
        "Comunicação com a base":   "Restabelecer comunicação para retomar controle energético remoto.",
        "Geração de energia solar":  "Ativar reservas de emergência e reduzir consumo ao mínimo.",
        "Consumo energético":       "Ativar modo de economia — desligar sistemas não essenciais.",
        "Eficiência do sistema":    "Redistribuir carga entre módulos e verificar perdas energéticas.",
    }

    if len(criticos) >= 3:
        return "EMERGÊNCIA ENERGÉTICA — Ativar protocolo de sobrevivência. Priorizar suporte à vida e comunicação."

    return " | ".join(recomendacoes_map[area] for area in criticos if area in recomendacoes_map)


def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de piora no balanço energético."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de melhora na gestão de energia."
    else:
        return "O balanço energético da missão permaneceu estável."


def identificar_area_mais_afetada(pontuacao_por_area):
    return max(pontuacao_por_area, key=pontuacao_por_area.get)


def analisar_ciclo(ciclo):
    temp, com, solar, consumo, efic = ciclo
    return {
        "Temperatura interna":      analisar_temperatura(temp),
        "Comunicação com a base":   analisar_comunicacao(com),
        "Geração de energia solar":  analisar_energia_solar(solar),
        "Consumo energético":       analisar_consumo_energia(consumo),
        "Eficiência do sistema":    analisar_eficiencia(efic),
    }


def calcular_risco_ciclo(resultados):
    return sum(pontos for _, (_, _, pontos) in resultados.items())

def exibir_cabecalho():
    print("=" * 62)
    print("     MISSION CONTROL AI — ENERGIAS RENOVÁVEIS E SUSTENTÁVEIS")
    print("=" * 62)
    print(f"  Missão  : {NOME_MISSAO}")
    print(f"  Equipe  : {NOME_EQUIPE}")
    print(f"  Ciclos  : {len(dados_missao)}")
    print("=" * 62)


def exibir_ciclo(numero, ciclo, resultados, pontuacao, classificacao, recomendacao):
    temp, com, solar, consumo, efic = ciclo
    print(f"\nCICLO {numero}")
    print("-" * 62)

    dados_exibicao = [
        ("Temperatura",    f"{temp} °C"),
        ("Comunicação",    f"{com}%"),
        ("Geração Solar",  f"{solar}%"),
        ("Consumo",        f"{consumo}%"),
        ("Eficiência",     f"{efic}%"),
    ]

    for (label, valor), area in zip(dados_exibicao, areas_monitoradas):
        status, mensagem, _ = resultados[area]
        print(f"  {label:14}: {valor:6} | {status:8} | {mensagem}")

    print(f"\n  Pontuação de risco do ciclo : {pontuacao}")
    print(f"  Classificação do ciclo      : {classificacao}")
    print(f"  Recomendação                : {recomendacao}")


def gerar_relatorio_final(riscos, pontuacao_por_area):
    print("\n" + "=" * 62)
    print("          RELATÓRIO FINAL DA MISSÃO")
    print("=" * 62)
    print(f"  Missão : {NOME_MISSAO}")
    print(f"  Equipe : {NOME_EQUIPE}")
    print(f"  Ciclos analisados: {len(dados_missao)}\n")

    labels_medias = ["temperatura", "comunicação", "geração solar", "consumo energético", "eficiência"]
    unidades       = ["°C", "%", "%", "%", "%"]
    for i, (label, unidade) in enumerate(zip(labels_medias, unidades)):
        media = sum(c[i] for c in dados_missao) / len(dados_missao)
        print(f"  Média de {label:20}: {media:.2f}{unidade}")

    ciclo_critico = riscos.index(max(riscos)) + 1
    risco_medio   = sum(riscos) / len(riscos)
    qtd_criticos  = sum(1 for r in riscos if r >= 6)
    tendencia     = analisar_tendencia(riscos)
    area_afetada  = identificar_area_mais_afetada(pontuacao_por_area)
    classif_final = classificar_ciclo(risco_medio)

    media_solar   = sum(c[2] for c in dados_missao) / len(dados_missao)
    media_consumo = sum(c[3] for c in dados_missao) / len(dados_missao)
    balanco       = media_solar - media_consumo

    print(f"\n  Ciclo mais crítico        : Ciclo {ciclo_critico}")
    print(f"  Maior pontuação de risco  : {max(riscos)}")
    print(f"  Risco médio da missão     : {risco_medio:.2f}")
    print(f"  Ciclos críticos           : {qtd_criticos}")
    print(f"\n  Balanço energético médio  : {balanco:.2f}%")
    if balanco >= 0:
        print(f"  Status do balanço         : SUPERÁVIT — missão energeticamente sustentável")
    else:
        print(f"  Status do balanço         : DÉFICIT — missão consumiu mais do que gerou")

    print(f"\n  Tendência da missão:")
    print(f"    {tendencia}")

    print(f"\n  Pontuação acumulada por área:")
    for area, pts in pontuacao_por_area.items():
        print(f"    {area}: {pts} pontos")

    print(f"\n  Área mais afetada:")
    print(f"    {area_afetada}")

    print(f"\n  Classificação final da missão:")
    print(f"    {classif_final}")

    print(f"\n  Conclusão energética:")
    if balanco >= 0 and risco_medio <= 2:
        conclusao = ("A missão manteve um balanço energético positivo ao longo de todos os ciclos. "
                     "Os painéis solares operaram de forma eficiente e sustentável.")
    elif risco_medio <= 5:
        conclusao = ("A missão apresentou instabilidade no balanço energético em alguns ciclos. "
                     "Recomenda-se revisão dos protocolos de consumo e manutenção dos painéis solares "
                     "para garantir a sustentabilidade em missões futuras.")
    else:
        conclusao = ("A missão enfrentou déficit energético crítico. "
                     "É necessária reavaliação completa do sistema de geração solar e dos protocolos "
                     "de economia de energia antes de qualquer nova operação.")
    print(f"    {conclusao}")
    print("\n" + "=" * 62)


def main():
    exibir_cabecalho()

    riscos             = []
    pontuacao_por_area = {area: 0 for area in areas_monitoradas}

    for i, ciclo in enumerate(dados_missao):
        resultados    = analisar_ciclo(ciclo)
        pontuacao     = calcular_risco_ciclo(resultados)
        classificacao = classificar_ciclo(pontuacao)
        recomendacao  = gerar_recomendacao(resultados)

        riscos.append(pontuacao)

        for area in areas_monitoradas:
            pontuacao_por_area[area] += resultados[area][2]

        exibir_ciclo(i + 1, ciclo, resultados, pontuacao, classificacao, recomendacao)

    gerar_relatorio_final(riscos, pontuacao_por_area)


if __name__ == "__main__":
    main()