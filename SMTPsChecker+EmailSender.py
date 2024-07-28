import smtplib
import random
import concurrent.futures
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
from time import sleep
from colorama import init, Fore

init(autoreset=True)

def a(x1, x2, x3, x4):
    try:
        with smtplib.SMTP(x1, x2, timeout=10) as s:
            s.starttls()
            s.login(x3, x4)
            return True
    except Exception:
        return False

def b(x5, x6, x7):
    try:
        with open(x5, 'r', encoding='utf-8') as f:
            x8 = [line.strip().split('|') for line in f if len(line.strip().split('|')) == 4]
    except UnicodeDecodeError:
        print("Error-Usebraininputfile")
        return

    if not x8:
        print("smtp not found")
        return

    def c(x9):
        x1, x2, x3, x4 = x9
        if a(x1, int(x2), x3, x4):
            print(Fore.GREEN + f"Valid SMTP: {x1}:{x2}")
            return f"{x1}|{x2}|{x3}|{x4}\n"
        return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=x7) as e:
        x10 = list(e.map(c, x8))
    
    with open(x6, 'w', encoding='utf-8') as o:
        for x in x10:
            if x:
                o.write(x)

def d(x):
    return Header(x, 'utf-8').encode()

def e(x11):
    try:
        with open(x11, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except UnicodeDecodeError:
        print("error use brain")
        return []

def f(x12, x13, x14):
    x15 = MIMEText(x13, 'plain', 'utf-8')
    x16 = MIMEText(f"<html><body><p>Hello {x12},</p><p>{x13}</p></body></html>", 'html', 'utf-8')
    return x15, x16

def g(x17, x18, x19, x20, x21):
    x22 = e(x18)
    if not x22:
        print("Add emails")
        return

    with open(x17, 'r', encoding='utf-8') as f:
        x23 = [line.strip().split('|') for line in f if len(line.strip().split('|')) == 4]

    if not x23:
        print("no smtps found")
        return

    while True:
        random.shuffle(x23)
        for x1, x2, x3, x4 in x23:
            try:
                with smtplib.SMTP(x1, x2, timeout=10) as s:
                    s.starttls()
                    s.login(x3, x4)

                    for x24 in x22:
                        m = MIMEMultipart()
                        m['From'] = formataddr((d(x19), x3))
                        m['To'] = x24
                        m['Subject'] = d(x20)
                        x15, x16 = f(x19, x20, x21)

                        m.attach(x15)
                        m.attach(x16)

                        s.sendmail(x3, x24, m.as_string())
                        print(f"Email sent to {x24} using {x1}:{x2}")
                        sleep(1)
                    break
            except Exception as ex:
                print(f"Failed to send email using {x1}:{x2} - {ex}")
                sleep(5)

def main():
    x5 = input("Enter your smtps list ").strip()
    x6 = 'validsmtps.txt'
    x7 = int(input("How many threads you want? ").strip())

    b(x5, x6, x7)

    x8 = input("Do you want to test sending emails? (y/n): ").strip().lower()
    if x8 == 'y':
        x9 = input("Enter emails list ").strip()
        x10 = input("Enter your custom name: ").strip()
        x11 = input("Enter the custom subject: ").strip()
        x12 = input("Enter the body of the email: ").strip()
        g(x6, x9, x10, x11, x12)

if __name__ == '__main__':
    main()
