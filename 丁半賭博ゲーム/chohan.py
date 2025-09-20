import random

# 掛け金を入力する関数
def get_bet(money):
    while True:
        try:
            bet = int(input("いくらかけますか？ ⇒ "))
            if 0 < bet <= money:
                return bet
            else:
                print("無効な入力です！所持金以内の正しい金額を入力してください。")
        except ValueError:
            print("無効な入力です！数字を入力してください。")

# 丁か半かを選択する関数
def get_choice():
    while True:
        try:
            choice = int(input("丁か半か？（丁：0，半：1） ⇒ "))
            if choice in (0, 1):
                return choice
            else:
                print("無効な入力です！0か1を入力してください。")
        except ValueError:
            print("無効な入力です！数字を入力してください。")

# サイコロを振る関数
def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

# 続けるかどうかを確認する関数
def ask_continue():
    while True:
        try:
            continue_game = int(input("続けますか？（はい：0，いいえ：1） ⇒ "))
            if continue_game in (0, 1):
                return continue_game
            else:
                print("無効な入力です！0か1を入力してください。")
        except ValueError:
            print("無効な入力です！数字を入力してください。")

# メインのゲーム関数
def cho_han_game():
    print("丁半賭博ゲームを始めます！")
    money = 1000  # 初期所持金
    is_even = lambda n: n % 2 == 0
    choice_to_label = lambda c: '丁' if c == 0 else '半'

    while money > 0:
        print(f"プレイヤーの所持金: {money}円")

        # 掛け金を取得
        bet = get_bet(money)

        # 丁か半かの選択
        choice = get_choice()
        choice_label = choice_to_label(choice)

        # サイコロを振る
        dice1, dice2 = roll_dice()
        dice_sum = dice1 + dice2
        outcome_label = '丁' if is_even(dice_sum) else '半'
        print(f"サイコロの目: {dice1}, {dice2} ⇒ {outcome_label}")

        # 勝敗判定
        if outcome_label == choice_label:
            print(f"あなたの勝ち！賞金は{bet}円")
            money += bet
        else:
            print(f"あなたの負け！{bet}円没収！")
            money -= bet

        # 所持金が尽きたら終了
        if money <= 0:
            break

        # 続けるかどうかを確認
        if ask_continue() == 1:
            break

    print(f"最終所持金は{money}円でした。")
    print("丁半賭博ゲームを終わります。")

# ゲームを実行
if __name__ == "__main__":
    cho_han_game()
