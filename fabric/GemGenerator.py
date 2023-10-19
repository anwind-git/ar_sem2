from fabric.ItemFabric import ItemFabric
from fabric.GemReward import GemReward


class GemGenerator(ItemFabric):
    def create_item(self):
        print("Cоздали сундук(изумруд)")
        return GemReward()
