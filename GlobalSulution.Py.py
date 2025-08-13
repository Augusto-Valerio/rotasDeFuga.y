# Jonas Esteves RM:564143
# Augusto Valério RM:562185

                        # Programa para prevenção, monitoramento e ação durante enchentes

# Lista de rotas onde cada dicionário representa uma rota de evacuação.
# Elementos: nome da rota,onde a rota leva, se é acessível para pessoas com deficiência, se permite animais e distância.
rotas = [
    {"nome": "Rota1", "destino": "Escola Municipal", "acessivel": False, "animais": False, "distancia": 1.0},
    {"nome": "Rota2", "destino": "Abrigo Central", "acessivel": True, "animais": True, "distancia": 1.2},
    {"nome": "Rota3", "destino": "Ginásio Público", "acessivel": True, "animais": False, "distancia": 1.5}
]

# Variável para armazenar o alerta de enchente, aparece para o usuário quando solicitado.
mensagemAlerta = "Alerta de enchente nível moderado. Abrigue-se caso esteja em área de risco!"

# Função para exibir o menu com opções para o usuário escolher.
def exibirMenu():
    print("\n--- Sistema de Rotas Para Evacuação De Enchentes ---")
    print("1. Ver rotas disponíveis")
    print("2. Filtrar rotas para pessoas com qualquer deficiência")
    print("3. Filtrar rotas para animais")
    print("4. Ver alerta de enchente!")
    print("5. Modo Offline")
    print("6. Sair")

# Funcão para mostrar TODAS as rotas cadastradas(sem filtro de "acessível", "animais" e etc).
def exibirRotas():
    print("\nRotas disponíveis e mais perto de você:")
    for rota in rotas:
        print(f'{rota['nome']}: {rota['destino']}, Está a {rota['distancia']}Km de você.')

# Esta função mostra apenas as rotas que também são acessíveis para pessoas com deficiência (acessível == True).
def rotasAcessiveis():
    print("\nRotas acessíveis para pessoas com qualquer deficiência:")
    for rota in rotas:
        if rota["acessivel"] == True:
            print(f"{rota['nome']}: {rota['destino']}, Está a {rota['distancia']}Km de você.")

# Função que filtra as rotas para quem também leva animais (animais == True).
def rotasAnimais():
    print("\nRotas para quem leva animais:")
    for rota in rotas:
        if rota["animais"] == True:
            print(f"{rota['nome']}: {rota['destino']}, Está a {rota['distancia']}Km de você.")

# Função para mostrar a váriavel de alerta de enchente criada anteriormente.
def alertaMensagem():
    print("\n[ALERTA]", mensagemAlerta)

# Funçao para o MODO OFFLINE, caso o usuário não tenha internet, dados e etc.
# Também informa o usuário para usar rádios locais como fonte de informação.
def modoOff():
    print("\n[MODO OFFLINE]")
    print("Utilizando os últimos dados de localização do seu dispositivo e dados previamente salvos")
    for rota in rotas:
        print(f"{rota['nome']}: {rota['destino']} Está a {rota['distancia']}Km de você.")
    print("Fique de olho em telões e sintonize rádios locais para atualizações mais precisas do seu local.")

# Loop principal que mantém o programa rodando até o usuário escolher a opção 6 (sair).
# Caso escolha uma opção inválida, exibe uma mensagem de erro.
while True:
    exibirMenu()
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        exibirRotas()
    elif opcao == "2":
        rotasAcessiveis()
    elif opcao == "3":
        rotasAnimais()
    elif opcao == "4":
        alertaMensagem()
    elif opcao == "5":
        modoOff()
    elif opcao == "6":
        print("Encerrando aplicação. Fique seguro!")
        break
    else:
        print("Opção inválida. Tente novamente.")