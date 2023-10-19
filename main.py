import random
from fabric.GoldGenerator import GoldGenerator
from fabric.GemGenerator import GemGenerator
from fabric.SilverGenerator import SilverGenerator


class Main:
    def main(self):
        fabricList = []
        fabricList.append(GoldGenerator())
        fabricList.append(GemGenerator())
        fabricList.append(SilverGenerator())

        for i in range(20):
            index = random.randint(0, len(fabricList) - 1)
            fabric = fabricList[index].create_item()
            fabric.open()


if __name__ == "__main__":
    main = Main()
    main.main()
