# GET    --> request data from a specified resource
# POST   --> create a resource
# PUT    --> update a resource
# DELETE --> delete a resource

# chrome://net-internals/#sockets
# flush socket pools if getting 400 error

from twilio.rest import Client
import keys, json, requests

response = requests.get(keys.URL, params=keys.params)
json_data = json.loads(response.text)
media_url = json_data['url']
body = json_data['explanation']

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
    media_url=media_url,
    body=body,
    from_=keys.twilio_number,
    to=keys.target_number
)

# print(json_data)
