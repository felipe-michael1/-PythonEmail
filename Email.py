#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import smtplib
import email.message

def enviar_email():
corpo_email = """
<p>Parágrafo1</p>
<p>Parágrafo2</p>
"""

msg = email.message.Message()
msg['Subject'] = "Assunto"
msg['From'] = 'remetente'
msg['To'] = 'destinatario'
password = 'senha' #COLE AQUI A SENHA DO SEU EMAIL
msg.add_header('Content-Type', 'text/html')
msg.set_payload(corpo_email )

s = smtplib.SMTP('smtp.gmail.com: 587') #aqui será adicionado o smtp do gmail,hotmail (cada um possui um diferente)
s.starttls()
# Login Credentials for sending the mail
s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
print('Email enviado')

# In[ ]:

enviar_email()
