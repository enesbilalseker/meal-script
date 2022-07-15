import requests
token = '5177297873:AAFWvh4bo87e3gCebj1xoDnmm6JkeNt_jDo'
base_url = 'https://api.telegram.org/bot{}/'.format(token)


def send_photo():
    try:
        payload = {
            "chat_id": "-544581213",
            "photo": "https://cdn.duzce.edu.tr/File/GetFile/b72cb8d1-d010-41c6-aef3-bb192a9d9005",
            "caption": "todays menu."
        }
        to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(token)

        resp = requests.post(to_url, data=payload)

        print("bitti")
    except Exception as e:
        print(e)


send_photo()
