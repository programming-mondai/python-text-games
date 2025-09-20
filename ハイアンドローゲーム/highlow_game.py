import random

print("=== ハイアンドローゲームへようこそ！ ===")

while True:
    player_card = random.randint(1, 13)
    computer_card = random.randint(1, 13)

    print(f"【プレイヤー】{player_card} VS ??【コンピュータ】")
    print("あなたのカードはコンピュータのカードより大きい？小さい？（1: 大きい、2: 小さい）")

    # 入力バリデーション（例外処理）
    while True:
        try:
            choice = int(input("⇒ "))
            if choice in (1, 2):
                break
            else:
                print("1 か 2 を入力してください。")
        except ValueError:
            print("数値で入力してください（1 または 2）。")

    print(f"【プレイヤー】{player_card} VS {computer_card}【コンピュータ】")

    if player_card == computer_card:
        print("引き分け！")
    elif (player_card > computer_card and choice == 1) or (player_card < computer_card and choice == 2):
        print("正解！あなたの勝ち！")
    else:
        print("残念！あなたの負け！")

    again = input("もう一度遊びますか？（y/n）: ").lower()
    if again != 'y':
        print("ゲームを終了します。ありがとうございました！")
        break
