from config import rules
from kavenegar import *

def send_sms(text):
    try:
        api = KavenegarAPI('enter KavenegarAPI')
        params = {
            'sender': '10008663',#optional
            'receptor': rules["notification"]["receiver"],#multiple mobile number, split by comma
            'message': text,
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)