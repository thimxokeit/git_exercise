import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'aa4b6b300fdb4797bfe7625e121c99cd'
secret = 'ddbca51759f340e58471ec1b929bad7b'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#track_input

track_search = sp.search("attention", limit=10, type='track', market=None)

for track in track_search['tracks']['items']:
    artists = [artist['name'] for artist in track['artists']]
    artists_result = [str(a) for a in artists]
    track_result = track['name']

    print(track_result)
    print("," . join(artists_result))









