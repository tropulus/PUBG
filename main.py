import requests
import sqlite3

conn = sqlite3.connect('example.db')
#c = conn.cursor()
#c.execute('CREATE TABLE test (DBNOs, assist, boosts)')
#c.execute("INSERT INTO test VALUES ('3', '4', '6')")
#conn.commit()
# for row in c.execute('SELECT * FROM test'):
#         print(row)

playername = 'TheBebopBengal'
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
matches = json['data'][0]['relationships']['matches']['data']
ids = [matches[i].get('id') for i in range(len(matches))]
# --------------------------------------



url_matches = f"https://api.pubg.com/shards/{platform}/matches/{ids[4]}"

response = requests.get(
    url=url_matches,
    headers=headers
)


participants = response.json()['included']
#print(response.json()['data']['attributes']['mapName'])


Sanhok = 'Savage_Main'
Erangel = 'Baltic_Main'
Vikendi = 'DihorOtok_Main'
Mirmar = 'Desert_Main'


partic1 = []
partic2 = []
for count, ele in enumerate(participants):
    if 'stats' in ele['attributes']:
        partic1.append(ele)

for count, ele in enumerate(partic1):
    if 'name' in ele['attributes']['stats']:
        partic2.append(ele)

for count, ele in enumerate(partic2):
    if ele['attributes']['stats']['name'] == playername:
        idx = count

print(partic2[idx]['attributes']['stats'])





