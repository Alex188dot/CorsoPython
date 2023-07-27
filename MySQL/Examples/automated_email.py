import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def invia_email(destinatario, oggetto, corpo):
    # Configura il server SMTP per inviare l'email (in questo esempio utilizzo Gmail)
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your-email-address"  # Inserisci il tuo indirizzo email
    sender_password = "your-app-password"  # Inserisci la tua app password (not email password!)

    # Messaggio email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = destinatario
    message["Subject"] = oggetto
    message.attach(MIMEText(corpo, "plain"))

    # Connessione e invio dell'email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, destinatario, message.as_string())
        print("Email inviata con successo!")
    except Exception as e:
        print("Errore nell'invio dell'email:", str(e))
    finally:
        server.quit()

if __name__ == "__main__":
    destinatario = "your-email-address"  # Inserisci l'indirizzo email del destinatario
    oggetto = "Test Email"
    corpo = "Questo è un esempio di invio email da Python."

    invia_email(destinatario, oggetto, corpo)