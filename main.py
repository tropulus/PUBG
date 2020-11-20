import requests

playername = 'tropulus'
platform = 'steam'


url = f"https://api.pubg.com/shards/{platform}/players?filter[playerNames]={playername}"
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjMWZhOTRmMC0wOTcxLTAxMzktNjQwYS0wNzEyMWUyYmRmNjMiLCJpc3MiO' \
          'iJnYW1lbG9ja2VyIiwiaWF0IjoxNjA1NDQ1Nzg2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Im1hY2hpbmVfbG' \
          'Vhcm5pIn0.wbwQ8DSfxpEtmUoa4zq40wFiKl7jud9djIHQT37BLDM'

headers = {"Authorization": f"Bearer {api_key}",
           "Accept": "application/vnd.api+json"}

response = requests.get(
    url=url,
    headers=headers
)

json = response.json()
player_id = json['data'][0]['id']
matches = json['data'][0]['relationships']['matches']['data']
ids = [matches[i].get('id') for i in range(len(matches))]
# --------------------------------------

url_matches = f"https://api.pubg.com/shards/{platform}/matches/{ids[0]}"

response = requests.get(
    url=url_matches,
    headers=headers
)

participants = response.json()['included']




# OK DO THIS INSTEAD: CHECK IF NAME EXIST, IF NAME EXIST PUT IN VECTOR








print(len(participants))
for i, e in enumerate(participants):
    keys = participants[i]['attributes']['stats'].keys()
    if 'name' not in keys:
        participants[i].pop('stats', None)
print(len(participants))
# a = participants[3]['attributes']['stats']
# print(a)
#
# participants[3].pop('stats', None)
# print(participants[0:5])
#print(participants[3]['attributes']['stats']['name'])


# if participants[0]['attributes']['stats']['playerId'] == player_id
#stats = [participants[3]['attributes']['stats']['name'] for i in range(len(participants))]
