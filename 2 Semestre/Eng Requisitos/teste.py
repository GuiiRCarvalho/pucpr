class Voluntario:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class ONG:
    def __init__(self):
        self.voluntarios = []
    
    def cadastrar_voluntario(self):
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        voluntario = Voluntario(nome, email, telefone)
        self.voluntarios.append(voluntario)
        print("Voluntário cadastrado com sucesso!\n")
    
    def listar_voluntarios(self):
        if not self.voluntarios:
            print("Nenhum voluntário cadastrado.\n")
            return
        print("Lista de Voluntários:")
        for i, voluntario in enumerate(self.voluntarios, 1):
            print(f"{i}. Nome: {voluntario.nome}, Email: {voluntario.email}, Telefone: {voluntario.telefone}")
        print("")
    
    def menu(self):
        while True:
            print("1. Cadastrar Voluntário")
            print("2. Listar Voluntários")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.cadastrar_voluntario()
            elif opcao == "2":
                self.listar_voluntarios()
            elif opcao == "3":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    ong = ONG()
    ong.menu()
