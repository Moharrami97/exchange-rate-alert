import requests
import json

from config import url, rules


def get_rate():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    with open(f"archive1/{filename}.json", "w") as f:
        f.write(json.dumps(rates))


def send_mail(timestamp, rates):
    now = jalali_datetime.JalaliDatetime.now().strftime('%Y-%B-%d  %A  %H:%M')
    subject = f"{timestamp} -{now}rates"

    if rules["email"]["preferred"] is not None:
        tmp = dict()
        for exo in rules["email"]["preferred"]:
            print(rates[exo])
            tmp[exo] = rates[exo]
        rates = tmp

    text = json.dumps(rates)
    send_smtp_email(subject, text)


if __name__ == "__main__":
    res = get_rate()

    if rules["archive"]:
        archive(res["timestamp"], res["rates"])
