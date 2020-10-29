import requests


def send_message(num: str):
    url = "https://rest.clicksend.com/v3/sms/send"
    payload = "{\n  \"messages\": [\n    {\n      \"body\":\"ASD IL DELFINO E' ONLINE\\n Aderendo a questa iniziativa il tuo abbonamento resta attivo.\\n Per conferma scrivi SI ai seguenti numeri\\n Chiara 3409342799\\n Yero 3464954075\\n\",\n      \"to\": \""+num+"\",\n      \"from\": \"IlDelfino\"\n    }\n  ]\n} "
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YW5kcmVhdGdpdXN0aUBnbWFpbC5jb206NUFBQThDRUYtNjA5RS02MDE5LTkyODUtRTBGQzE5RTc4RURG'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.status_code


already_sent = []
failed = open('errors.txt', 'w')
with open('numbers2.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) != 10:
            print(f'Fake number {line} cause has len = {len(line)}')
            continue
        if line in already_sent:
            print(f'Number {line} already sent.')
            continue
        print(f'Sending to {line}')
        res = send_message(line)
        if res != 200:
            print(f'Send to Number {line} failed.')
            failed.write(f'{line}\r\n')
            already_sent.append(line)
            continue
        already_sent.append(line)
        print(f'DONE.\n\n')
