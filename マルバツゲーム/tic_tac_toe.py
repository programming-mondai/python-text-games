import random

# グリッドを表示する関数
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# 勝利を判定する関数（タプルのタプルを使用）
def check_win(board, mark):
    WIN_PATTERNS = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # 横
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # 縦
        (0, 4, 8), (2, 4, 6)               # 斜め
    )
    return any(all(board[i] == mark for i in pattern) for pattern in WIN_PATTERNS)

# 引き分けを判定する関数
def check_draw(board):
    return all(space in ("○", "×") for space in board)

# コンピュータがランダムにマスを選ぶ関数
def computer_move(board):
    available_moves = [i for i, space in enumerate(board) if space not in ("○", "×")]
    return random.choice(available_moves)

# マルバツゲームのメイン関数
def play_game():
    board = [str(i) for i in range(1, 10)]  # 1〜9の番号で初期化
    print("マルバツゲームを開始します！")

    while True:
        # 現在のグリッドを表示
        display_board(board)

        # プレイヤーのターン
        while True:
            try:
                player_move = int(input("どのマスに置きますか？（1-9で入力してください）> ")) - 1
                if board[player_move] not in ("○", "×"):
                    board[player_move] = "○"
                    break
                else:
                    print("そのマスはすでに埋まっています。別のマスを選んでください。")
            except (ValueError, IndexError):
                print("無効な入力です。1から9の数字を入力してください。")

        # 勝利判定
        if check_win(board, "○"):
            display_board(board)
            print("プレイヤーの勝ちです！")
            break

        # 引き分け判定
        if check_draw(board):
            display_board(board)
            print("引き分けです！")
            break

        # コンピュータのターン
        print("コンピュータのターンです...")
        comp_move = computer_move(board)
        board[comp_move] = "×"
        print(f"コンピュータが選んだマス: {comp_move + 1}")

        # 勝利判定
        if check_win(board, "×"):
            display_board(board)
            print("コンピュータの勝ちです！")
            break

        # 引き分け判定
        if check_draw(board):
            display_board(board)
            print("引き分けです！")
            break

if __name__ == "__main__":
    play_game()
