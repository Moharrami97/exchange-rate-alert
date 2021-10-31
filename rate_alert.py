import requests
import json

from config_url import url, rules

def get_rate():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    with open(f"archive1/{filename}.json", "w") as f:
        f.write(json.dumps(rates))

if __name__ == "__main__":
    res = get_rate()

    if rules["archive"]:
        archive(res["timestamp"], res["rates"])