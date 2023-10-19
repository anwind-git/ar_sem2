from fabric.IGameItem import IGameItem


class GoldReward(IGameItem):
    def open(self):
        print("Открыли сундку с золотом")