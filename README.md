# -PythonEmail
Classe em Python para envio de emails. Classe de envio de emails simples que pode ser colocada em qualquer projeto em Python.
Funciona nos seguintes clientes de e-mail:
- Outlook
- Gmail

<strong>DOCUMENTAÇÃO PARA ADICIONAR PORTAS (OUTLOOK):</strong>

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

<strong>DOCUMENTAÇÃO PARA ADICIONAR PORTAS (GMAIL):</strong>

Configuração de cliente POP:

Abra o Gmail no computador.
No canto superior direito, clique em Configurações Configurações e Ver todas as configurações.
Clique na guia Encaminhamento e POP/IMAP.
Na seção "Download POP", selecione Ativar POP para todos os e-mails ou Ativar POP para e-mails que chegarem a partir de agora.
Na parte inferior da página, clique em Salvar alterações.

Depois, faça as alterações em sua classe:

Servidor de recebimento de e-mails (POP):	
pop.gmail.com
Requer SSL: Sim
Porta: 995

Servidor de envio de e-mails (SMTP)	
smtp.gmail.com
Requer SSL: Sim
Requer TLS: Sim (se disponível)
Requer autenticação: sim
Porta para TLS/STARTTLS: 587

Configuração de cliente IMAP:

Servidor IMAP: imap.gmail.com
Porta: 993
Método de criptografia: SSL/TLS

<hr />

Python class for sending emails. Simple email sending class that can be placed in any Python project. Works on the following email clients:

Outlook
Gmail
DOCUMENTATION FOR ADDING PORTS (OUTLOOK):

If you want to add your Outlook.com account to another email program that supports POP or IMAP, here are the manual server settings required.

Notes:

POP & IMAP access is disabled by default. See the section below on how to enable POP or IMAP access in Outlook.com. Outlook.com requires the use of modern Auth/OAuth2. Basic auth is in the process of being deprecated from the Outlook.com service. Incoming and outgoing servers are the same.

Username:

Your email address

Password:

Your Microsoft account password. If your password isn't being recognized, or if you want to add your Outlook.com account to a smart device like a home security camera, you may need an app password. Learn how to add your Outlook.com account to another email app or smart device.

IMAP Server: outlook.office365.com

IMAP Port: 993

IMAP Encryption:

SSL/TLS Authentication Method: OAuth2/Modern Auth

POP Server Name: outlook.office365.com

POP Server: POP Port: 995

POP Encryption: SSL/TLS

Authment Method: OAuth2/Modern Auth

SMTP Server Name: smtp-mail.outlook.com

SMTP Port: 587

SMTP Encryption: STARTTLS

Authment Method: OAuth2/Modern Auth

DOCUMENTATION FOR ADDING PORTS (GMAIL):

POP Client Configuration:

Open Gmail on your computer. In the top right corner, click Settings Settings and then See all settings. Click the Forwarding and POP/IMAP tab. In the "POP Download" section, select Enable POP for all mail or Enable POP for mail arriving from now on. At the bottom of the page, click Save Changes.

Then, make the changes to your class:

Incoming mail server (POP): pop.gmail.com Requires SSL: Yes Port: 995

Outgoing mail server (SMTP) smtp.gmail.com Requires SSL: Yes Requires TLS: Yes (if available) Requires authentication: Yes Port for TLS/STARTTLS: 587

IMAP client configuration:

IMAP server: imap.gmail.com Port: 993 Encryption method: SSL/TLS
