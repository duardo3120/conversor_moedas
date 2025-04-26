import requests
import os

def conversor_moedas():
    nome_usuario = input("Bem-vindo ao conversor de moedas! Para iniciar, qual é o seu nome? ").strip()
    moeda_origem = input(f"Olá {nome_usuario}, qual a moeda de origem que você gostaria de converter? ").strip().upper()
    moeda_destino = input("Qual a moeda de destino para a conversão? ").strip().upper()
    
    # Tentativa de receber o valor corretamente
    try:
        valor = float(input(f"{nome_usuario}, qual valor você deseja converter de {moeda_origem} para {moeda_destino}? "))
    except ValueError:
        print("Valor inválido! Por favor, digite um número válido.")
        return

    url = f"https://hexarate.paikama.co/api/rates/latest/{moeda_origem}?target={moeda_destino}"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança exceção para códigos de erro HTTP
        dados = resposta.json()
        
        taxa_conversao = dados['data']['mid']
        valor_convertido = taxa_conversao * valor
        
        print(f"\n{valor} {moeda_origem} equivale a {valor_convertido:.2f} {moeda_destino}.\n")

    except requests.exceptions.RequestException as erro:
        print("\nErro ao acessar a API:", erro)
    except (KeyError, TypeError):
        print("\nErro: Não foi possível encontrar a taxa de conversão. Verifique se as moedas estão corretas.")

def lista_moedas():
    print("\nAlgumas moedas disponíveis:")
    print("USD - Dólar Americano")
    print("EUR - Euro")
    print("BRL - Real Brasileiro")
    print("JPY - Iene Japonês")
    print("GBP - Libra Esterlina")
    print("AUD - Dólar Australiano")
    print("CAD - Dólar Canadense")
    print("CHF - Franco Suíço")
    print("CNY - Yuan Chinês\n")

def menu():
    print("=== Conversor de Moedas ===")
    print("1. Converter Moedas")
    print("2. Lista de moedas disponíveis")
    print("3. Sair")
    opcao = input("Escolha uma opção: ").strip()
    return opcao

# Loop principal
while True:
    opcao = menu()
    if opcao == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        conversor_moedas()
    elif opcao == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        lista_moedas()
    elif opcao == "3":
        print("\nSaindo do programa... Até a próxima!\n")
        break
    else:
        print("\nOpção inválida. Tente novamente.\n")
