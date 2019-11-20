
import os
import smtplib, ssl
from filter import Filter
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


load_dotenv()
port = os.getenv('PORT')
password = os.getenv("EMAIL_PASSWORD")
sender_email = os.getenv("MY_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")

csv_path = "/Users/Pete/Desktop/Pi/tweetbot/bot/twit.csv"
search_fraze = "movement director"
subject = "Movement Director tweets"
#port = 1025 test port


def searching():
    results=[]
    #print(os.getcwd())
    search_this = Filter(csv_path, search_fraze)
    for item in search_this.filter_file():
        results.append(item[0])
        results.append('\n')
    # return ''.join(str(results))
    return results

def creating_body():
    body = ''
    results = searching()
    for item in results:
        body += item
    return body

def email_real():
    text = searching()
    meseg = MIMEMultipart()
    meseg['From'] = sender_email
    meseg['To'] = receiver_email
    meseg['Subject'] = subject

    body = creating_body()
    context = ssl.create_default_context()
    if len(text) >0:
        put = input("there are {} new tweet/s, do you want send email ? y/n ".format(len(text)))

        if put == 'y':
            meseg.attach(MIMEText(body, 'plain'))
            #print(body)
            with smtplib.SMTP('smtp.zenbox.pl', port) as server:
                server.set_debuglevel(1)
                server.starttls(context=context) # Secure the connection
                server.login(sender_email, password)
                server.send_message(meseg)

        else:
            pass
    else:
        print("no keyword")


def email_send():

    """ local server for testing."""

    subject = "proba dzialania"
    text = searching()
    print(len(text))
    #text = next(v)
    meseg = "subject: {} \n\n {}".format(subject, text)

    context = ssl.create_default_context()
    if len(text) >0:
        with smtplib.SMTP('localhost', port) as server:
            server.sendmail(sender_email, receiver_email, meseg)
    else:
        print("no keyword")


#email_send()
email_real()
