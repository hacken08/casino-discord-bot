
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from cred import crds


#  ... initializing firebase firestore ...../
cred = credentials.Certificate(crds)
firebase_admin.initialize_app(cred)
db = firestore.client()


def create_player(player_uid, name, email, bot: bool, avatar, date):
    """
    Create new player
    """
    info = {
        'games': {
            'snake water gun': {
                'stats': {
                    'max score': 0,
                    'current score': 0,
                    'wines': 0,
                    'lose': 0
                },
            },
            'slot machine': {
                'stats': {}
            },
            'betting': {
                'stats': {}
            }
        },
        'balance': {
            'value': 0,
            'currency': 'INR',
            'symbol': '₹'
        },
        'player info': {
            'member since': date,
            'avatar': avatar,
            'bot': bot,
            'email': email,
            'name': name,
        }
    }
    players = db.collection('bot users').document(player_uid)
    players.set(info)

def is_plyr_new(uid):
    """
    Check if player is new or not
    :param uid:
    :return: new True, old False
    """
    players = db.collection('bot users').stream()

    for player in players:
        if player.id == uid:
            return False
    else:
        return True

def get_plyr_data(uid):
    """
    Fetching player data
    :param uid:
    :return: player data dict
    """
    players = db.collection('bot users').stream()
    for player in players:
        if player.id == uid:
            return player.to_dict()
    else:
        return 'Player not found'


def     update_plyr_data(uid, key, value):
    """
    Update player data
    :param value:
    :param uid:
    :param key:
    """
    player = db.collection('bot users').document(uid)
    player.update({key: value})


def del_plyr(user):
    db.collection('bot users').document(user).delete()
    return True


