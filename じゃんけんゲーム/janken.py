import random

print("じゃんけんゲームを始めます！（0: グー, 1: チョキ, 2: パー）")

while True:
    # 入力バリデーション（数値・範囲チェック）
    while True:
        try:
            player_choice = int(input("あなたの選択（0/1/2）: "))
            if player_choice == 0 or player_choice == 1 or player_choice == 2:
                break
            else:
                print("0, 1, 2 のいずれかを入力してください。")
        except ValueError:
            print("数字で入力してください。")

    # コンピュータの手をランダムに決定
    computer_choice = random.randint(0, 2)

    # 数値 → 手の名前
    if player_choice == 0:
        player_hand = "グー"
    elif player_choice == 1:
        player_hand = "チョキ"
    else:
        player_hand = "パー"

    if computer_choice == 0:
        computer_hand = "グー"
    elif computer_choice == 1:
        computer_hand = "チョキ"
    else:
        computer_hand = "パー"

    # 双方の手を表示
    print("あなたの手:", player_hand)
    print("コンピュータの手:", computer_hand)

    # 勝敗の判定
    if player_choice == computer_choice:
        print("引き分けです！")
    elif (player_choice == 0 and computer_choice == 1) or \
         (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 0):
        print("あなたの勝ちです！")
    else:
        print("あなたの負けです！")

    # 続行確認
    again = input("もう一度遊びますか？（y/n）: ").lower()
    if again != 'y':
        print("ゲームを終了します。ありがとうございました！")
        break
