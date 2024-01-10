import paramiko
from criar_usuario import criar_usuario
from deletar_usuario import deletar_usuario

def conectar_ssh(ip, usuario_ssh, chave_privada):
    try:
        # Cria uma instância SSH
        cliente_ssh = paramiko.SSHClient()
        cliente_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Carrega a chave privada do tipo ed25519
        chave = paramiko.Ed25519Key(filename=chave_privada)
        cliente_ssh.connect(ip, username=usuario_ssh, pkey=chave)

        print("Conexão SSH estabelecida com sucesso.")
        return cliente_ssh

    except Exception as e:
        print(f"Falha na conexão SSH: {str(e)}")
        return None

    
ip_samba4 = input("Digite o IP do Samba4: ")
usuario_ssh = input("Digite o usuário SSH: ")
caminho_chave_privada = input("Digite o caminho da chave privada SSH: ")  

# Função para executar comandos via SSH
def executar_comando_ssh(cliente_ssh, comando):
    try:
        stdin, stdout, stderr = cliente_ssh.exec_command(comando)
        resultado = stdout.read().decode('utf-8')

        print(resultado)
        return resultado

    except Exception as e:
        print(f"Falha ao executar comando SSH: {str(e)}")
        return None

# Conectar via SSH
cliente_ssh = conectar_ssh(ip_samba4, usuario_ssh, caminho_chave_privada)

# Verifica se a conexão foi bem-sucedida antes de continuar
if cliente_ssh:
    # Pergunta qual ação realizar
    acao = input("Digite 'criar' para criar usuário ou 'deletar' para deletar usuário: ")
    
    # Executa comandos com base na escolha
    if acao == "criar":
        # Pergunta pelos usuários apenas se a ação for "criar"
        usuarios = input("Digite os nomes dos usuários separados por espaço: ").split()
        print(usuarios)
        # Executa comandos para cada usuário fornecido
        for usuario in usuarios:
            criar_usuario(cliente_ssh, usuario)
            
    elif acao == "deletar":
        # Pergunta pelos usuários apenas se a ação for "deletar"
        usuarios = input("Digite os nomes dos usuários separados por espaço: ").split()

        # Executa comandos para cada usuário fornecido
        for usuario in usuarios:
            deletar_usuario(cliente_ssh, usuario)

    else:
        print("Opção inválida. Por favor, escolha 'criar' ou 'deletar'.")
else:
    print("Falha na conexão SSH. Verifique as informações fornecidas e tente novamente.")

# Fechar a conexão SSH
if cliente_ssh:
    cliente_ssh.close()
