import requests
import json
#
#https://vtapi.floscodes.net/docs/advanced/
#
res = requests.get("https://vtapi.floscodes.net/?station=Plößlgasse&line=D&countdown")

if res:
    resJSON = res.json()
    print("Success")
else:
    print('An error has occurred.')

data = json.dumps(resJSON)
data = json.loads(data)

print(data["attributes"][0])
