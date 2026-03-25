import time
import sys

# Credenciais de acesso cadastradas no sistema
CORRECT_ID = "admin"
CORRECT_PASSWORD = "123"

def main():
    attempts = 0
    block_time = 300  # Tempo inicial de bloqueio: 5 minutos (300 segundos)
    
    print("=== Sistema de Autenticação ===")
    
    while True:
        try:
            user_id = input("ID: ")
            password = input("Senha: ")
        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada pelo usuário.")
            sys.exit(0)
            
        if user_id == CORRECT_ID and password == CORRECT_PASSWORD:
            print("\nAutenticação realizada com sucesso! Acesso liberado.")
            break
        else:
            attempts += 1
            tentativas_restantes = 3 - attempts
            print("\n[Erro] ID ou senha incorretos.")
            
            if attempts >= 3:
                print("\n[!] Limite de 3 falhas de autenticação atingido.")
                print(f"[!] O sistema está bloqueado por {block_time // 60} minutos.")
                
                remaining_time = block_time
                
                # Loop para exibir o tempo restante de bloqueio
                while remaining_time > 0:
                    mins, secs = divmod(remaining_time, 60)
                    time_format = f"{mins:02d}:{secs:02d}"
                    # Usa \r para que a linha seja atualizada no mesmo lugar no terminal
                    sys.stdout.write(f"\rTempo restante de bloqueio: {time_format}   ")
                    sys.stdout.flush()
                    
                    try:
                        time.sleep(1)
                    except KeyboardInterrupt:
                        # Evita que o usuário pule o tempo de espera usando Ctrl+C
                        pass
                    
                    remaining_time -= 1
                
                print("\n\n[INFO] Tempo de bloqueio finalizado. Tente realizar o login novamente.\n")
                
                # Reinicia a contagem de tentativas após o cumprimento do bloqueio
                attempts = 0
                # Multiplica o tempo de bloqueio por 6 para eventuais falhas futuras
                block_time *= 6
            else:
                print(f"Aviso: Você tem mais {tentativas_restantes} tentativa(s) antes do bloqueio.\n")

if __name__ == "__main__":
    main()
