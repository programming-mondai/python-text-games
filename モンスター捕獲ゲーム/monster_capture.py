import random
from abc import ABC, abstractmethod

# サイコロクラス（ユーティリティ）
class Dice:
    @staticmethod
    def roll():
        return random.randint(1, 6)

# モンスター基底クラス（抽象クラス）
class Monster(ABC):
    def __init__(self, name: str, hp: int = 10):
        self._name = name      # プライベート属性（名前）
        self._hp = hp          # プライベート属性（HP）

    def get_name(self):
        return self._name

    def get_hp(self):
        return self._hp

    def set_hp(self, value: int):
        if value >= 0:
            self._hp = value
        else:
            print("HPは0以上でなければなりません")

    def dice_roll(self):
        return Dice.roll()

    @abstractmethod
    # 各モンスターが持つ特別な動きを表現する抽象メソッド
    def special_move(self):
        pass

# スライムクラス（Monsterを継承）
class Slime(Monster):
    def special_move(self):
        return f"{self.get_name()}は体当たりを仕掛けた！"

# ゴブリンクラス（Monsterを継承）
class Goblin(Monster):
    def special_move(self):
        return f"{self.get_name()}は棍棒を振り回した！"

# ドラゴンクラス（オーバーライドあり）
class Dragon(Monster):
    def dice_roll(self):
        # ドラゴンは2回振って大きい方を採用
        roll1, roll2 = Dice.roll(), Dice.roll()
        return max(roll1, roll2)

    def special_move(self):
        return f"{self.get_name()}は火を吹いた！"

# ゲーム本体
class MonsterCaptureGame:
    def __init__(self):
        self.monsters = [Slime("スライム"), Goblin("ゴブリン"), Dragon("ドラゴン")]
        self.captured_monsters = []

    def play(self):
        for monster in self.monsters:
            print(f"{monster.get_name()}が現れた！")
            print(monster.special_move())

            monster_roll = monster.dice_roll()
            print(f"{monster.get_name()}がサイコロを振った。出目は {monster_roll}")

            response = input("サイコロを振りますか？ (yes/no): ").strip().lower()
            if response == "no":
                print(f"{monster.get_name()}をスキップしました。")
                continue  # 次のモンスターへ

            player_roll = Dice.roll()
            print(f"プレイヤーがサイコロを振った。出目は {player_roll}")

            if player_roll > monster_roll:
                print(f"{monster.get_name()}を捕まえた！")
                self.captured_monsters.append(monster.get_name())
            elif player_roll == monster_roll:
                print("引き分けでもう一度！")
                # 再戦扱いで同じモンスターに再挑戦
                continue
            else:
                print(f"{monster.get_name()}を捕まえられなかった。ゲームオーバー！")
                break

        print("捕まえたモンスター: " + ", ".join(self.captured_monsters))
        print("ゲーム終了")

# 実行
if __name__ == "__main__":
    game = MonsterCaptureGame()
    game.play()
