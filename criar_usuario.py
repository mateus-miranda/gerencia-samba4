# usuario.py
import paramiko

def criar_usuario(cliente_ssh, usuario):
   try:
       stdin, stdout, stderr = cliente_ssh.exec_command(f"echo 'Criando usuário {usuario}'")
       resultado = stdout.read().decode('utf-8')
       print(resultado)

       stdin, stdout, stderr = cliente_ssh.exec_command(f"adduser --force-badname --gecos '' --disabled-password {usuario}")
       resultado = stdout.read().decode('utf-8')
       print(resultado)

       stdin, stdout, stderr = cliente_ssh.exec_command(f"echo '{usuario}:Teste@123' | chpasswd")
       resultado = stdout.read().decode('utf-8')
       print(resultado)

       stdin, stdout, stderr = cliente_ssh.exec_command(f"samba-tool user create {usuario} Teste@123")
       resultado = stdout.read().decode('utf-8')
       print(resultado)

   except Exception as e:
       print(f"Falha ao criar usuário: {str(e)}")
       return None
