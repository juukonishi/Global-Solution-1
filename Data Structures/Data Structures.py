missao = "Simulador de Missão"
equipe = "Júlia Konishi, João Scheren, João Neves"

historico = []

def verificar_temperatura(temp):
    if temp > 80:
        return "CRITICO", "ALERTA: Superaquecimento detectado!"
    elif temp > 60:
        return "ATENCAO", "Temperatura elevada, fique de olho."
    else:
        return "NORMAL", "Temperatura estavel."

def verificar_energia(energia):
    if energia < 20:
        return "CRITICO", "ALERTA: Ativar modo de economia de energia!"
    elif energia < 40:
        return "ATENCAO", "Energia abaixo do recomendado."
    else:
        return "NORMAL", "Energia estavel."

def verificar_comunicacao(comunicacao):
    if comunicacao == 0:
        return "CRITICO", "ALERTA: Falha de comunicacao detectada!"
    elif comunicacao < 30:
        return "ATENCAO", "Comunicacao instavel."
    else:
        return "NORMAL", "Comunicacao estavel."

def analisar_leitura(leitura):
    temp_status, temp_alerta = verificar_temperatura(leitura["temperatura"])
    ener_status, ener_alerta = verificar_energia(leitura["energia"])
    comu_status, comu_alerta = verificar_comunicacao(leitura["comunicacao"])

    return {
        "temperatura": (leitura["temperatura"], temp_status, temp_alerta),
        "energia":     (leitura["energia"],     ener_status, ener_alerta),
        "comunicacao": (leitura["comunicacao"], comu_status, comu_alerta),
    }

def classificar_missao(resultados):
    statuses = [v[1] for v in resultados.values()]
    if "CRITICO" in statuses:
        return "MISSAO CRITICA"
    elif "ATENCAO" in statuses:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO ESTAVEL"

def inserir_dados():
    print("\n--- INSERIR DADOS ---")
    try:
        temp        = float(input("  Temperatura (graus C): "))
        energia     = float(input("  Nivel de energia (%): "))
        comunicacao = float(input("  Comunicacao (%): "))

        leitura = {
            "temperatura": temp,
            "energia":     energia,
            "comunicacao": comunicacao,
            "numero":      len(historico) + 1,
        }
        historico.append(leitura)
        print("\n  Dados registrados com sucesso!")

    except ValueError:
        print("\n  Entrada invalida. Digite apenas numeros.")

def visualizar_status():
    if not historico:
        print("\n  Nenhuma leitura ainda. Insira os dados primeiro.")
        return

    leitura       = historico[-1]
    resultados    = analisar_leitura(leitura)
    status_missao = classificar_missao(resultados)

    print("\n--- STATUS ATUAL ---")
    print(f"  Missao  : {missao}")
    print(f"  Equipe  : {equipe}")
    print(f"  Leitura : #{leitura['numero']}")
    print("-" * 40)
    print(f"  Temperatura : {leitura['temperatura']} graus | {resultados['temperatura'][1]}")
    print(f"  {resultados['temperatura'][2]}")
    print(f"\n  Energia     : {leitura['energia']}% | {resultados['energia'][1]}")
    print(f"  {resultados['energia'][2]}")
    print(f"\n  Comunicacao : {leitura['comunicacao']}% | {resultados['comunicacao'][1]}")
    print(f"  {resultados['comunicacao'][2]}")
    print("-" * 40)
    print(f"  Status geral: {status_missao}")

def executar_analise():
    if not historico:
        print("\n  Nenhuma leitura ainda. Insira os dados primeiro.")
        return

    print("\n--- ANALISE COMPLETA ---")

    criticos = 0
    atencoes = 0

    for leitura in historico:
        resultados    = analisar_leitura(leitura)
        status_missao = classificar_missao(resultados)
        if "CRITICA" in status_missao:
            criticos += 1
        elif "ATENCAO" in status_missao:
            atencoes += 1

    media_temp  = sum(l["temperatura"]  for l in historico) / len(historico)
    media_ener  = sum(l["energia"]      for l in historico) / len(historico)
    media_comu  = sum(l["comunicacao"]  for l in historico) / len(historico)

    print(f"  Total de leituras   : {len(historico)}")
    print(f"  Leituras criticas   : {criticos}")
    print(f"  Leituras em atencao : {atencoes}")
    print(f"  Leituras estaveis   : {len(historico) - criticos - atencoes}")
    print(f"\n  Media de temperatura : {media_temp:.1f} graus")
    print(f"  Media de energia     : {media_ener:.1f}%")
    print(f"  Media de comunicacao : {media_comu:.1f}%")

    if criticos > len(historico) / 2:
        print("\n  CONCLUSAO: Missao em estado critico na maior parte do tempo.")
    elif atencoes > len(historico) / 2:
        print("\n  CONCLUSAO: Missao requer atencao continua.")
    else:
        print("\n  CONCLUSAO: Missao operando de forma estavel.")

def visualizar_historico():
    if not historico:
        print("\n  Nenhuma leitura ainda. Insira os dados primeiro.")
        return

    print("\n--- HISTORICO DE LEITURAS ---")
    print(f"  {'#':<5} {'Temp':<10} {'Energia':<12} {'Comunicacao':<14} {'Status'}")
    print("  " + "-" * 55)

    for leitura in historico:
        resultados    = analisar_leitura(leitura)
        status_missao = classificar_missao(resultados)
        print(f"  {leitura['numero']:<5} {leitura['temperatura']:<10} {leitura['energia']:<12} {leitura['comunicacao']:<14} {status_missao}")

def exibir_menu():
    print("\n" + "=" * 40)
    print("       MISSION CONTROL AI")
    print("=" * 40)
    print("  1. Inserir dados")
    print("  2. Visualizar status atual")
    print("  3. Executar analise")
    print("  4. Historico das leituras")
    print("  5. Encerrar sistema")
    print("=" * 40)

def main():
    print(f"\n  Iniciando Mission Control AI...")
    print(f"  Missao : {missao}")
    print(f"  Equipe : {equipe}")

    while True:
        exibir_menu()
        opcao = input("  Escolha uma opcao: ").strip()

        if opcao == "1":
            inserir_dados()
        elif opcao == "2":
            visualizar_status()
        elif opcao == "3":
            executar_analise()
        elif opcao == "4":
            visualizar_historico()
        elif opcao == "5":
            print("\n  Encerrando sistema. Ate a proxima missao!")
            break
        else:
            print("\n  Opcao invalida. Digite um numero de 1 a 5.")

main()