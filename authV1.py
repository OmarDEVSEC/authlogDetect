# Creating an auth log anomlay detection
# What: Pare thousands of fake SSH and Windows Logon logs adn flag 
# Brute force attempts


import os

def brute_log(log_file):

    failed_login = "Error"
    for log in log_file:
        attempt = failed_login    
        
        return