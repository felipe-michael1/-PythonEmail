# -PythonEmail
Classe em Python para envio de emails. Classe de envio de emails simples que pode ser colocada em qualquer projeto em Python.
Funciona nos seguintes clientes de e-mail:
- Outlook
- Gmail

DOCUMENTAÇÃO PARA ADICIONAR PORTAS (OUTLOOK):

Se você quiser adicionar sua conta do Outlook.com para outro programa de email que ofereça suporte a POP ou IMAP, aqui estão as configurações manuais do servidor necessárias.

Observações: 

O acesso pop & IMAP é desabilitado por padrão. Confira a seção abaixo sobre como habilitar o acesso POP ou IMAP no Outlook.com.
Outlook.com requer o uso do Auth /OAuth2 moderno.  A auth básica está no processo de ser preterido do serviço Outlook.com.
Servidores de entrada e saída são os mesmos.

Nome de usuário:

Seu endereço de e-mail

Senha:

Sua senha da conta microsoft. 
Se sua senha não estiver sendo reconhecida ou se você quiser adicionar sua conta Outlook.com a um dispositivo inteligente como uma câmera de segurança doméstica, talvez você precise de uma senha do aplicativo. Saiba como adicionar sua conta Outlook.com a outro aplicativo de email ou dispositivo inteligente.

Servidor IMAP:
outlook.office365.com

Porta IMAP:
993

Criptografia IMAP:

SSL/TLS
Método de Autenticação:
OAuth2/Modern Auth


Nome do servidor POP:
outlook.office365.com

Servidor POP:
Porta POP:
995

Criptografia POP:
SSL/TLS

Método de Autenticação:
OAuth2/Modern Auth

Nome do servidor SMTP:
smtp-mail.outlook.com

Porta SMTP:
587

Criptografia SMTP:
STARTTLS

Método de Autenticação:
OAuth2/Modern Auth
