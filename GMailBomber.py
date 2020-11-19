from smtplib import SMTP
from getpass import getpass
from time import sleep, strftime

def log(log):
    print(f"[{strftime('%H:%M:%S')}] {log}")

log("Script started!")
try:
    log("Creating the SMTP object ...")
    server = SMTP("smtp.gmail.com", 587)
    log("Getting hello from SMPT server...")
    log(str(server.ehlo()))
    log("Starting the SSL tunnel ...")
    server.starttls()
    log("Make the login [the password will not be shown] ...")
    while True:
        try:
            usergmail = input("\tUsername: ")
            passgmail = getpass("\tPassword: ")
            server.login(usergmail, passgmail)
            log("Login succeded!")
            break
        except Exception as Err:
            log(f"Error 0x0: {str(Err)}")

    log("Making the EMail structure...")
    to      = input("\tSend EMail to: ")
    subject = "Subject: " + input("\tSubject: ") + "\n\n"
    content = input("\tContent: ")
    message = subject+content
    times   = input("\tHow many times [default 1]: ")
    seconds = input("\tSeconds to wait [default 1]: ")
    log("All parameters was setted")

    if times == "":
        times = 1
    if seconds == "":
        seconds = 1
    
    log("Starting...")
    for idx, x in enumerate(range(0, int(times)), 1):
        try:
            print(f"Sending...", end="\r")
            server.sendmail(usergmail, to, message)
            print("[%d/%s] EMail was sended to: %s" % (idx, int(times), to))
            sleep(int(seconds))
        except KeyboardInterrupt:
            log("Process interrupted by user...")
            break
        except Exception as Err:
            log(f"Error 0x1: {str(Err)}")
    server.quit()
    log("Done")
except Exception as Err:
    try:
        server.quit()
    except:
        pass
    log(f"Error 0x2: {str(Err)}")