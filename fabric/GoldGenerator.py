from fabric.ItemFabric import ItemFabric
from fabric.GoldReward import GoldReward


class GoldGenerator(ItemFabric):
    def create_item(self):
        print("Создали сундук(золото)")
        return GoldReward()
