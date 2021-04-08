import requests
import exceptions



class Skin:
    def __init__(self, username):
        self.username = username 

    def skingrab(self):
        try:
            playerdata = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{self.username}').json()
        except:
            raise exceptions.PlayerNotFound("Player was not found!")
        self.id = playerdata["id"]
        self.skin = f'https://crafatar.com/skins/{self.id}'
        return self.skin


    def body(self):
        try:
            playerdata = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{self.username}').json()
        except:
            raise exceptions.PlayerNotFound("Player was not found!")
        self.id = playerdata["id"]
        self.body = f'https://crafatar.com/renders/body/{self.id}'
        return self.body

    def head(self):
        try:
            playerdata = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{self.username}').json()
        except:
            raise exceptions.PlayerNotFound("Player was not found!")
        self.id = playerdata["id"]
        self.head = f'https://crafatar.com/renders/head/{self.id}'
        return self.head

    def avatar(self):
        try:
            playerdata = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{self.username}').json()
        except:
            raise exceptions.PlayerNotFound("Player was not found!")
        self.id = playerdata["id"]
        self.avatar = f'https://crafatar.com/renders/avatars/{self.id}'
        return self.avatar
    

