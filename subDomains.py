import requests  # Python requests module have several built-in HTTP request methods[GET, PUT, POST, DELETE].
import time      # Python time module provides functions for handling time-related tasks.
from prettytable import PrettyTable   # Python prettytable library is used to create relational tables.

# List of subdomains to check
subdomains = ["store.playstation.com", "uk.yahoo.com", "us.yahoo.com", "support.yotpo.com", "es.wikipedia.org", "eu.wikipedia.org"]

# check_status fuction is utilized to check the status of subdomains.
def check_status(subdomains):
    # Create a table to display the results.
    table = PrettyTable()
    table.field_names = ["Subdomain", "Status"]
    
    # Check the status of each subdomain using for loop.
    for subdomain in subdomains:
        # using try and except block to verify the status of the domains using requests.get() function from requests module.
        try:
            response = requests.get(f'http://{subdomain}', timeout=5)
            if response.status_code == 200:
                # add_row() function from prettytable module is used to add rows of data to the table.
                table.add_row([subdomain, 'UP'])
            else:
                table.add_row([subdomain, 'DOWN'])
        except requests.exceptions.RequestException:
            table.add_row([subdomain, 'DOWN'])
    
    # Print the table.
    print(table)

# Continuously check the status of the subdomains every minute.
while True:
    check_status(subdomains)
    time.sleep(60)           # time.sleep() function suspends execution for the given number of seconds.