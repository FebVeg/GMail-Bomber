# -*- coding: utf-8 -*-

from smtplib import SMTP
from getpass import getpass
from time import sleep, strftime

print("\n\tGMail Spammer Bot - FebVeg\n")

print("Server".ljust(15)+": First manually configuration...")
username = input("Username".ljust(15)+": ")
password = getpass("Password".ljust(15)+": ")
sender   = input("Sender".ljust(15)+": ")
subject  = input("Subject".ljust(15)+": ") + "\n\n"
content  = input("Message".ljust(15)+": ")
wait_sec = input("Wait seconds".ljust(15)+": ")
times    = input("Times".ljust(15)+": ")

if times == "":
    times = 1
if wait_sec == "":
    wait_sec = 1

message = subject+content

try:
    print("Server".ljust(15)+": Connecting to server...")
    server = SMTP("smtp.gmail.com", 587)
    print("Server".ljust(15)+f": {server.ehlo()}")
    print("Server".ljust(15)+": Enabling SSL...")
    server.starttls()
    print("Server".ljust(15)+": Login...")
    server.login(username, password)
    print("Server".ljust(15)+": Login success")
except Exception as Err:
    print("Config-Error".ljust(15)+f": {str(Err)}")

try:
    for idx, x in enumerate(range(0, int(times)), 1):
        try:
            
            server.sendmail(username, sender, message)
            print("[%d/%s] Sended to: %s" % (idx, int(times), sender) + "\r")
            sleep(int(wait_sec))
        except KeyboardInterrupt:
            print("\nProcess interrupted by user...")
            server.quit()
            break
        except Exception as Err:
            server.quit()
            print("Spam-Error".ljust(15)+f": {str(Err)}")
    try:
        server.quit()
    except Exception as Err:
        print("Quit-Error".ljust(15)+f": {str(Err)}")
except Exception as Err:
    print("Error".ljust(15)+f": {str(Err)}")

del username
del password
exit()
