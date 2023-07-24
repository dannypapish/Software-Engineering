import requests


def indeed_request():
    # TODO 2: Put the code from the Postman steps of the lab here.
    # - Make sure you used the correct URL
    # - Also, erase any unnecessary code like the import statement
    

    url = "https://www.indeed.com/jobs?q=SoftwareEngineer&l=Charlotte"

    payload = {}
    headers = {
    'Cookie': '__cf_bm=nE.cJZvHw50r0fSly2jS2O0W3Jxz8KuoRblQL7TytGA-1686957113-0-AbLkQa5ml5xXs401DT9qsdkP4q9DtgVxXKd3VwJ9FKZz6JUNW0NMomFCSwXg2vhg3A8/leyvd0lQz2Cv5DOiUYo='
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


    


if __name__ == '__main__':
    indeed_request()
