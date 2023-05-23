import requests
import json


def delivery(matter, adress1, phone1, adress2, phone2):
    body = {
        "matter": f"{matter}",
        "points": [{
                "address": f"{adress1}",
                "contact_person": {
                    "phone": f"{phone1}"
                }
            },
            {
                "address": f"{adress2}",
                "contact_person": {
                    "phone": f"{phone2}"
                }
            }
        ]
    }

    answer = requests.post('https://robotapitest.dostavista.ru/api/business/1.3/create-order', headers = {'Content-Type': 'application/json', "X-DV-Auth-Token": "154135C420E0336B11A6646BD80304A3438FA180"}, data = json.dumps(body))
    result = json.loads(answer.text)
    print(result)


delivery("Банан", "Москва, ул. Солянка, 4", 79030000001, "Москва, ул. Покровка, 11", 79030000001)
