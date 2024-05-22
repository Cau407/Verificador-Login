emailCadastrado = "zezim@gmail.com"
senhaCadastrada = "12345678"

emailPedido = input("Digite seu email: ")
senhaPedida = input("Digite sua senha: ")

while emailPedido != emailCadastrado or senhaPedida != senhaCadastrada:
    if emailPedido != emailCadastrado:
        print("Email errado!")
        emailPedido = input("Digite seu email novamente: ")
    elif senhaPedida != senhaCadastrada:
        print("Senha errada!")
        senhaPedida = input("Digite sua senha novamente: ")

print("Você entrou em sua conta com sucesso!")