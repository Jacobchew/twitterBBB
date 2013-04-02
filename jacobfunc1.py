import requests
from requests_oauthlib import OAuth1

BASE_URL = u'https://api.twitter.com/1.1/'

client_key = u'Kuj6lqfd2hs7DZsDGm5pvg'
client_secret = u'WCRUpd6GKrXHxjGhWqqp9Ww2vYC6zJIHM9qmwbS6pJQ'
resource_owner_key = u'1322197472-jrSq06ugOf171GHIGsODyp5KXLdjUSVKWqRWz2D'
resource_owner_secret = u'qioFQBrtJtgoCK7uhSg4ovGLiV4q9Ph0oprYPRQIrE'

oauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret)

headeroauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret,
                     signature_type='auth_header')


queryoauth = OAuth1(client_key, client_secret,
                    resource_owner_key, resource_owner_secret,
                    signature_type='query')


bodyoauth = OAuth1(client_key, client_secret,
                   resource_owner_key, resource_owner_secret,
                   signature_type='body')

				   
def jinbanyakmain():
	payload = {'status': 'Jin is fat'}
	url = BASE_URL + "statuses/update.json"
	r = requests.post(url, auth=oauth, data=payload)
	return r.json() 

