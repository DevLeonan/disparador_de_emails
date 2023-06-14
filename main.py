import smtplib
from email.mime.text import MIMEText
from datetime import date, timedelta, datetime
import time

# Configurações do servidor de e-mail
SMTP_SERVER = 'smtp-mail.outlook.com'
SMTP_PORT = 587
SMTP_USERNAME = 'heedoy@hotmail.com'
SMTP_PASSWORD = '9895742Fel'

# Informações sobre as contas a vencer
contas = [
    {'nome': 'da internet', 'data_vencimento': date(2023, 6, 25), 'email_destinatario': 'dev.leonan@gmail.com', 'Valor': 'R$125.00'},
    {'nome': 'do Seguro', 'data_vencimento': date(2023, 6, 20), 'email_destinatario': 'dev.leonan@gmail.com', 'Valor': 'R$110.00'},
    {'nome': 'da Creditas', 'data_vencimento': date(2023, 6, 7), 'email_destinatario': 'dev.leonan@gmail.com', 'Valor': 'R$250.00'},
    {'nome': 'do IPVA', 'data_vencimento': date(2023, 6, 30), 'email_destinatario': 'dev.leonan@gmail.com', 'Valor': 'R$750.00'},
    {'nome': 'da Faculdade', 'data_vencimento': date(2023, 6, 10), 'email_destinatario': 'dev.leonan@gmail.com', 'Valor': 'R$300.00'},
    {'nome': 'da Vivo', 'data_vencimento': date(2023, 6, 17), 'email_destinatario': 'dev.leonan@gmail.com', 'Valor': 'R$70.00'},
    {'nome': 'da Comida do mês', 'data_vencimento': date(2023, 6, 30), 'email_destinatario': 'dev.leonan@gmail.com', 'Valor': 'R$800.00'},
    # Adicione mais contas aqui...
]

while True:
    # Calcula a data e hora atual
    now = datetime.now()

    # Verifica se é 10:00 da manhã
    if now.hour == 10 and now.minute == 0:

        # Itera sobre as contas
        for conta in contas:
            data_vencimento = conta['data_vencimento']
            dias_restantes = (data_vencimento - date.today()).days
            valores = conta['Valor']

            # Verifica se a conta está atrasada ou faltam menos de 5 dias para vencer
            if dias_restantes < 0 or dias_restantes <= 5:
                if dias_restantes < 0:
                    mensagem = f"A conta {conta['nome']} está atrasada há {abs(dias_restantes)} dias."
                else:
                    mensagem = f"A conta {conta['nome']} vence em {dias_restantes} dias."

                # Envia o e-mail
                msg = MIMEText(mensagem)
                msg['Subject'] = f"Aviso de vencimento da conta {conta['nome']}"
                msg['From'] = SMTP_USERNAME
                msg['To'] = conta['email_destinatario']

                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()
                    server.login(SMTP_USERNAME, SMTP_PASSWORD)
                    server.send_message(msg)

                print(f"E-mail enviado para {conta['email_destinatario']}")

    # Aguarda 1 hora antes de verificar novamente
    time.sleep(65)  # 1 hora em segundos
