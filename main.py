import requests


def send_message(num: str):
    url = "https://rest.clicksend.com/v3/sms/send"
    payload = "{\n  \"messages\": [\n    {\n      \"body\":\"Gentile socio\\n L'ASD Il Delfino ti informa che prestissimo partiranno dei corsi e dei programmi di allenamento on line.\\n Se sei interessato non esitare a contattarci.\\n Chiara 3409342799\\n Yero 3464954075\",\n      \"to\": \"" + num + "\",\n      \"from\": \"IlDelfino\"\n    }\n  ]\n} "
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YW5kcmVhdGdpdXN0aUBnbWFpbC5jb206NUFBQThDRUYtNjA5RS02MDE5LTkyODUtRTBGQzE5RTc4RURG'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.status_code


already_sent = []
failed = open('errors.txt', 'w')
with open('numbers1.txt', 'r') as f:
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
            continue
        already_sent.append(line)
        print(f'DONE.\n\n')
