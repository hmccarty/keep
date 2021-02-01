import gkeepapi
import keyring
import os 
from decouple import config

if __name__ == '__main__':
    keep = gkeepapi.Keep()

    if os.path.exists('state'):
        with open('state', 'r') as f:
            state = json.load(f)
    else:
        state = None

    gmail = config('GMAIL')
    try:
        token = keyring.get_password('google-keep-token', config('GMAIL'))
    except keyring.errors.NoKeyringError:
        token = None

    if token is None:
        keep.login(gmail, config('PWORD'), state=state)
        token = keep.getMasterToken()
        kering.set_password('google-keep-token', config('GMAIL'), token)
    else:
        keep.resume(gmail, token, state=state)
    keep.sync()

    print(keep.all())