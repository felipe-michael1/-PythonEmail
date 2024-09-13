#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import smtplib
import email.message

def enviar_email():
corpo_email = """
<p>Digite aqui o corpo do email ou coloque uma variável para trazer informações do banco de dados</p>
"""

msg = email.message.Message()
msg['Subject'] = "Assunto"
msg['From'] = 'remetente'
msg['To'] = 'destinatario'
password = 'senha' #COLE AQUI A SENHA DO SEU EMAIL
msg.add_header('Content-Type', 'text/html')
msg.set_payload(corpo_email )

s = smtplib.SMTP('smtp.gmail.com: 587') # aqui é adicionado o smtp do gmail ou hotmail (Cada um possui configurações diferentes. Qualquer dúvida veja no Readme)
s.starttls()
# Login Credentials for sending the mail
s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
print('Email enviado')

# In[ ]:

enviar_email()
