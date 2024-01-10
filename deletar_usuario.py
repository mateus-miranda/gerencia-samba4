import paramiko 

def deletar_usuario(cliente_ssh, usuario):
   try:
       stdin, stdout, stderr = cliente_ssh.exec_command(f"echo 'Apagando usuário {usuario}'")
       resultado = stdout.read().decode('utf-8')
       print(resultado)

       stdin, stdout, stderr = cliente_ssh.exec_command(f"deluser {usuario}")
       resultado = stdout.read().decode('utf-8')
       print(resultado)

       stdin, stdout, stderr = cliente_ssh.exec_command(f"samba-tool user delete {usuario}")
       resultado = stdout.read().decode('utf-8')
       print(resultado)

   except Exception as e:
       print(f"Falha ao apagar usuário: {str(e)}")
       return None