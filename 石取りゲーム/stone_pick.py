# 入力された石の数が有効かどうかを判定する関数
def is_valid_move(stones, move):
    return 1 <= move <= 3 and move <= stones

# プレイヤーの入力を受け取り、バリデーション関数でチェックする関数（高階関数）
def get_move(player, stones, validator):
    while True:
        try:
            move = int(input(f"{player}, 何個の石を取りますか？（1~3個まで選べます）："))
            if validator(stones, move):  # validator関数を利用
                return move
            else:
                print("無効な選択です。もう一度選んでください。")
        except ValueError:
            print("数値を入力してください。")

# 1ターン分の処理を行い、残りの石の数を更新する関数
def take_turn(player, stones, validator):
    print(f"\n{player}の番です。残りの石は {stones} 個です。")
    move = get_move(player, stones, validator)  # 高階関数の利用
    return stones - move

# ゲーム全体の進行を管理するメイン関数
def play_game():
    print("石取りゲームへようこそ！")
    stones = 15  # ゲーム開始時の石の数
    turn = 1     # 1ならプレイヤー1、2ならプレイヤー2

    while stones > 0:
        current_player = "プレイヤー1" if turn == 1 else "プレイヤー2"
        stones = take_turn(current_player, stones, is_valid_move)

        if stones == 0:
            print(f"\n{current_player}が最後の石を取りました。{current_player}の負けです！")
            break

        turn = 3 - turn  # 1⇔2を切り替え

# ゲームの実行
if __name__ == "__main__":
    play_game()
