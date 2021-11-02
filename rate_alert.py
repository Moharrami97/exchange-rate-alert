import requests
import json
from khayyam import jalali_datetime
from config import url, rules
from send_email import send_smtp_email
from SMS_notification import send_sms

def get_rate():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


# archive1 file added and write rate alert
def archive(filename, rates):
    with open(f"archive1/{filename}.json", "w") as f:
        f.write(json.dumps(rates))


def check_notification(rates):
    preferred = rules["notification"]["preferred"]
    msg = ""
    for exo in preferred.keys():
        if rates[exo] <= preferred[exo]["min"]:
            msg += f"{exo} reached with min: {rates[exo]}"
        if rates[exo] >= preferred[exo]["max"]:
            msg += f"{exo} reached with max: {rates[exo]}"
    return msg


#send SMS when the rate alert reaches a certain level
def send_notification(msg):
    now = jalali_datetime.JalaliDatetimenow().strftime('%Y-%B-%d  %A  %H:%M')
    msg += now
    send_sms(msg)

#all rate alert send email 
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

    if rules["email"]["enable"]:
        send_mail(res["timestamp"], res["rates"])

    if rules["notification"]["enable"]:
        notification_msg = check_notification(res["rates"])
        if check_notification(res["rates"]):
            send_notification(notification_msg)
