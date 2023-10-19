from fabric.ItemFabric import ItemFabric
from fabric.SilverReward import SilverReward


class SilverGenerator(ItemFabric):
    def create_item(self):
        print("Создали сундук(серебро)")
        return SilverReward()
