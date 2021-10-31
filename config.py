BASE_PATH = "http://data.fixer.io/api/latest?access_key="
API_KEY = "Enter api keys"
url = BASE_PATH + API_KEY

rules = {
    "archive": True,
    "email": {
        "receiver": "a18743ad95-111ea6@inbox.mailtrap.io",
        "enable": False,
        # preferred default is None
        # "preferred" : None
        "preferred": ["BTC", "IRR"]},
}

password = "enter password"