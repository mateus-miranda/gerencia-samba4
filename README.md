# gerencia-samba4

O projeto utiliza a biblioteca paramiko que tem a funcionalidade de conectar em maquinas utilizando o SSH.

Esse script tem como objetivo conectar em uma maquina samba4 e atráves de algumas pergunta criar ou deletar um usuário.

### Após executar o programa ele abre um formulario no terminal solicitando: 

- IP da maquina samba 4
- Usuário que tem a chave SSH para se conectar
- O caminho da chave SSH na sua maquina

Logo em seguida o script pergunta o que deseja fazer, seja criar ou deletar um usuário e o nome do usuário que será criado ou apagado, depois dessas perguntas o script automaticamente faz a ação desejada e finaliza sua execução.
