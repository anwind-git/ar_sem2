from fabric.IGameItem import IGameItem


class SilverReward(IGameItem):
    def open(self):
        print("Открыли сундку с серебром")