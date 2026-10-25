# Creating an auth log anomlay detection
# What: Pare thousands of fake SSH and Windows Logon logs adn flag 
# Brute force attempts


import os


def line_log(text):
   Truauth_found = 0
   Fauth_found = 0
   if "Successful Login" in text:
    Truauth_found += 1
   elif "Failed Login" in text:
     Fauth_found +=1 
     
   return Truauth_found


print(line_log("Successful Login, Failed Login,Failed Login, Failed Login"))


def brute_log(log_file):
   failed_attempt = 0
   Brute_attempt = 0 

   with open(log_file) as f:

      failed_login = "Error"

      for log in log_file:
        if failed_login > 3:
           Brute_attempt += 1
        else:
           failed_attempt += 1
