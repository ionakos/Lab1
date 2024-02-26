import requests  # εισαγωγή της βιβλιοθήκης
from datetime import datetime


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break
while True:
    url = input("\nInsert url:")  # εισαγωγή του url από τον χρήστη

    with requests.get(url) as response:  # το αντικείμενο response
        html = response.text
        more(html)
        
        header = response.headers   #εύρεση λογισμικού web server
        print("Ο εξυπηρετητής χρησιμοποιεί λογισμικό:", header['server'])
        
        cookie = response.cookies   #εύρεση cookies του website
        print("Η σελίδα χρησιμοποιεί τα παρακάτω cookies:")
        
        for cookie in response.cookies:     #εύρεση ημερομηνία και ώρα λήξης κάθε cookie
            if cookie.expires == None: print("To cookie",cookie.name,"που δεν λήγει!")
            else:print("To cookie",cookie.name,"που λήγει στις ", datetime.fromtimestamp(cookie.expires))
