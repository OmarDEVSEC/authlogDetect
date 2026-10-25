# Creating an auth log anomlay detection
# What: Pare thousands of fake SSH and Windows Logon logs adn flag 
# Brute force attempts

def brute_log(log_file):
    for log in log_file:
        return