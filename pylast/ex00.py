import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "PUT YOUR API KEY HERE"  # this is a sample key
API_SECRET = "PUT YOUR API SECRET KEY HERE"

# In order to perform a write operation you need to authenticate yourself
username = "PUT YOUR USERNAME HERE"
password_hash = pylast.md5("PUT YOUR PASSWORD HERE")

network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=username,
    password_hash=password_hash,
)

## SESSION_KEY_FILE = os.path.join(os.path.expanduser("~"), ".session_key")

SESSION_KEY_FILE = "mysessionkey.txt"

skg = pylast.SessionKeyGenerator(network)
url = skg.get_web_auth_url()

print(f"Please authorize this script to access your account: {url}\n")
import time
import webbrowser

webbrowser.open(url)

while True:
    try:
        session_key = skg.get_web_auth_session_key(url)
        with open(SESSION_KEY_FILE, "w") as f:
            f.write(session_key)
        break
    except pylast.WSError:
        time.sleep(1)
