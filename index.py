from yandex_music import Client
from yandex_music.exceptions import *
# import logger


try:
    TOKEN = 'y0_AgAAAAArD6_QAAG8XgAAAAD6oTYSAADe_cMPQFJBjLqJ4xNgLbxlureI1g'

    client = Client(token=TOKEN).init()
    print(client.users_likes_tracks()[0].fetch_track())
    


except YandexMusicError():
    print('YandexMusicError')
except UnauthorizedError():
    print('UnauthorizedError')
except InvalidBitrateError():
    print('InvalidBitrateError')
except NetworkError():
    print('NetworkError')
except BadRequestError():
    print('BadRequestError')
except NotFoundError():
    print('NotFoundError')
except TimedOutError():
    print('TimedOutError')