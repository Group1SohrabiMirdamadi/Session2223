import requests
from pprint import pprint

'service.GDwNbS3U7svILS8SwBIYqpH5PpL3rrq2Fz9v3kK8'

api_key = 'service.GDwNbS3U7svILS8SwBIYqpH5PpL3rrq2Fz9v3kK8'

params = {
    'lat': 36.2880443,
    'lng': 59.61574,
}

res = requests.request('GET','https://api.neshan.org/v2/reverse?',params=params,headers={'Api-Key':api_key})

pprint(res.json()['addresses'])