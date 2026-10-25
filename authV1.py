# Creating an auth log anomlay detection
# What: Pare thousands of fake SSH and Windows Logon logs adn flag 
# Brute force attempts


import os

def brute_log(log_file):

    failed_login = "Error"
    for log in log_file:
        failed_attempt = 0
        Brute_attempt = 0
        if failed_login < 3:
            failed_attempt += 1
        else: 
            Brute_attempt += 1 
        
    print(f"Amount of failed attempts: {failed_attempt} Amount of brute attempts: {Brute_attempt}")