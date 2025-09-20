import random

# タイル（持ち牌）を表示する関数
def display_tiles(title, tiles):
    print(f"{title}⇒【", end="")
    print(" ,".join([str(tile) if tile != -1 else "-" for tile in tiles]), end="")
    print("】")

# プレイヤーとコンピュータの得点を表示する関数
def display_scores(players):
    print(f"プレイヤーの得点　： {players['player']['score']}点")
    print(f"コンピュータの得点： {players['computer']['score']}点")

# プレイヤーが手持ちから牌を選ぶ関数（入力処理付き）
def get_player_choice(tiles):
    while True:
        try:
            choice = int(input("持ち牌の中から出す牌を選択してください > "))
            if choice in tiles:
                return choice
            else:
                print("無効な選択です。再度選択してください。")
        except ValueError:
            print("数字を入力してください。")

# コンピュータがランダムに牌を選ぶ関数
def get_computer_choice(tiles):
    return random.choice(tiles)

# ナインゲームのメイン処理を行う関数
def main():
    # プレイヤーとコンピュータの状態を辞書で管理
    players = {
        "player": {"tiles": [1,2,3,4,5,6,7,8,9], "score": 0},
        "computer": {"tiles": [1,2,3,4,5,6,7,8,9], "score": 0}
    }
    
    # タプルで対戦履歴を残す
    history = []

    print("ナインゲームを開始します！")

    for round_num in range(1, 10):
        print(f"\n【第{round_num}回戦】")

        display_scores(players)

        display_tiles("☆プレイヤーの持ち牌", players["player"]["tiles"])
        display_tiles("コンピュータの持ち牌", players["computer"]["tiles"])

        player_choice = get_player_choice([tile for tile in players["player"]["tiles"] if tile != -1])
        computer_choice = get_computer_choice([tile for tile in players["computer"]["tiles"] if tile != -1])

        print(f"プレイヤーの打牌：{player_choice}", end="")
        if player_choice > computer_choice:
            print(f"　＞　{computer_choice}：コンピュータの打牌")
            players["player"]["score"] += player_choice
            print(f"プレイヤーは{player_choice}点獲得")
        elif player_choice < computer_choice:
            print(f"　＜　{computer_choice}：コンピュータの打牌")
            players["computer"]["score"] += computer_choice
            print(f"コンピュータは{computer_choice}点獲得")
        else:
            print(f"　＝　{computer_choice}：コンピュータの打牌")
            print("引き分けです。得点はなし")

        # 使用済み牌を -1 に
        players["player"]["tiles"][players["player"]["tiles"].index(player_choice)] = -1
        players["computer"]["tiles"][players["computer"]["tiles"].index(computer_choice)] = -1

        # タプルで履歴保存
        history.append((player_choice, computer_choice))

    print("\nゲーム終了！")
    display_scores(players)

    if players["player"]["score"] > players["computer"]["score"]:
        print("プレイヤーの勝利です！")
    elif players["player"]["score"] < players["computer"]["score"]:
        print("コンピュータの勝利です！")
    else:
        print("引き分けです！")

    print("\n=== 対戦履歴（タプル） ===")
    for i, (p, c) in enumerate(history, 1):
        print(f"第{i}回戦: プレイヤー={p}, コンピュータ={c}")

if __name__ == "__main__":
    main()
