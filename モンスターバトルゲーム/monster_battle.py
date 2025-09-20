import random
from abc import ABC, abstractmethod

# 抽象クラス: キャラクターの共通基盤
class Character(ABC):
    # コンストラクタ: 名前・HP・攻撃力を設定する
    def __init__(self, name, hp, attack_power):
        self._name = name
        self._hp = hp
        self._attack_power = attack_power

    # 名前を取得する
    def get_name(self):
        return self._name

    # HPを取得する
    def get_hp(self):
        return self._hp

    # HPを更新する（0未満にはしない）
    def set_hp(self, value):
        if value >= 0:
            self._hp = value
        else:
            self._hp = 0

    # 生存判定（HPが0より大きいかどうか）
    def is_alive(self):
        return self._hp > 0

    # 抽象メソッド: 攻撃処理を子クラスに実装させる
    @abstractmethod
    def attack(self, opponent, defend=False):
        pass

    # 静的メソッド: ダメージを与える処理
    @staticmethod
    def damage(target, amount):
        target.set_hp(target.get_hp() - amount)

# プレイヤークラス
class Player(Character):
    # プレイヤーの攻撃処理
    def attack(self, opponent, defend=False):
        print(f"{self._name}の攻撃！")
        Character.damage(opponent, self._attack_power)
        print(f"{opponent.get_name()}に{self._attack_power}のダメージ！")

    # プレイヤーの防御処理
    def defend(self):
        print(f"{self._name}は防御を選んだ！")
        return True

# モンスタークラス
class Monster(Character):
    # コンストラクタ: モンスターの初期化（攻撃成功率を持つ）
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.attack_chance = 60

    # モンスターの攻撃処理（成功率つき）
    def attack(self, opponent, defend=False):
        roll = random.randint(1, 100)
        print(f"{self._name}の攻撃！")

        if roll <= self.attack_chance:
            if defend:
                print("攻撃は防がれた！")
                self.attack_chance = 60
            else:
                print("攻撃が成功！")
                Character.damage(opponent, self._attack_power)
                print(f"{opponent.get_name()}に{self._attack_power}のダメージ！")
                self.attack_chance = 60
        else:
            print("攻撃はミス！")
            self.attack_chance += 20

# ゲーム進行を管理する関数
def battle_game():
    # プレイヤーとモンスターを生成
    player = Player("勇者", 100, 20)
    monster = Monster("ドラゴン", 120, 25)

    # 両者が生存している間ゲームを続ける
    while player.is_alive() and monster.is_alive():
        print(f"\n{player.get_name()}のHP: {player.get_hp()}, {monster.get_name()}のHP: {monster.get_hp()} (成功率: {monster.attack_chance}%)")
        action = input("行動を選んでください (1: 攻撃, 2: 防御): ")

        defend = False
        # プレイヤーの行動
        if action == "1":
            player.attack(monster)
        elif action == "2":
            defend = player.defend()
        else:
            print("無効な入力です。もう一度選んでください。")
            continue

        # モンスターの行動
        if monster.is_alive():
            monster.attack(player, defend)

    # ゲーム終了時の勝敗判定
    if player.is_alive():
        print(f"\n{monster.get_name()}を倒した！{player.get_name()}の勝利！")
    else:
        print(f"\n{player.get_name()}は倒された…{monster.get_name()}の勝利！")

# メイン処理: ゲームを開始する
if __name__ == "__main__":
    battle_game()
