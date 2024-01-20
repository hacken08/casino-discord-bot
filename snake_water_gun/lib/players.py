from snake_water_gun.lib import game_style as gm_s
import interactions as interact


class Player:
    def __init__(self, name='', username='', mention=''):
        """
        Create player object
        Args:
            name:
            username:
            id:
        """
        self.name = name
        self.username = username
        self.mention = mention
        self.choice = ''

    def take_choice(self, key_cio):
        """
        Player take choice
        Args:
            key_cio:
        """
        self.choice = gm_s.choice[key_cio]

    def get_stats(self):
        pass


