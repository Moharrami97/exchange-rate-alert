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
    "notification": {
            "enable":False,
            "receiver":"enter receiver" ,
            "preferred": {
                "BTC":{"min":1.8386e-05, "max":1.9485e-05},
                "IRR":{"min":49222.9, "max":49399.8},
            }
    }
}

password = "enter password"