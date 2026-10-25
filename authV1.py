# Creating an auth log anomlay detection
# What: Pare thousands of fake SSH and Windows Logon logs adn flag 
# Brute force attempts


import os


def line_log(text):
   auth_found = 0
   for char in text:
    if char == "Successful Login":
       auth_found += 1

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
