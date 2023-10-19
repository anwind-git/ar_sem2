from fabric.IGameItem import IGameItem


class GemReward(IGameItem):
    def open(self):
        print("Открыли сундук с изумрудом")