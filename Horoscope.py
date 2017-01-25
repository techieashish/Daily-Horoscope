 #!/usr/bin/python

import requests, bs4, esse


def display():
    title = "Welcome to Daily Horoscope"
    print(title.center(80))
    user_Input = input("\n\nEnter your sun sign? OR press enter to view list: ")
    if user_Input == "":

        sign_list = signs()
        for index, sun_sign in enumerate(sign_list, 1):
            print("%s.%s" % (index, sun_sign))
        user_choice = int(input("\n\nEnter the number corresponding to the sun sign: ")) - 1
        horoscope(sign_list[user_choice])
    else:
        horoscope(user_Input)



def extract(url, selector=None):
    from time import sleep
    headers = {'USER-AGENT': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
    while True:
        global res
        try:

            res = requests.get(url, headers=headers, stream=True)
        except (Exception, requests.RequestException, TimeoutError, ConnectionError):
            print("\n\nConnection Error\t Retrying 10 seconds")
            sleep(10)
            print("\nStarted again")
        else:
            break
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    data = soup.select(selector)
    return data


def horoscope(sign):
    url = "http://www.ganeshaspeaks.com/%s/%s-daily-horoscope.action" % (sign, sign)
    #css = "div", {'class': 'block100 box-pading'}
    selector_span = 'div.block100.box-pading > span'
    selector_head = 'div.block100.box-pading > h3'

    data_head = extract(url, selector_head)
    data_span = extract(url, selector_span)

    print("\n\nSign : %s\tDate: %s\n                            Horoscope:\n" % (sign, data_head[0].text))
    print('##############################################################################')
    print("\n\n%s\n" % data_span[0].text)
    print('##############################################################################')
    input()


def signs():
    url = 'http://www.ganeshaspeaks.com'
    selector = "div.sunsign-box > ul > li > a"
    data = extract(url, selector)
    sign_list = [d.text for d in data]
    return sign_list

display()
