import random

# グリッドサイズを定義
GRID_SIZE = 5

# グリッドを初期化する関数（リスト使用）
def initialize_grid():
    grid = []
    count = 1
    for i in range(GRID_SIZE):
        row = []
        for j in range(GRID_SIZE):
            row.append(f"{count:02d}")  # 01, 02, 03...の形式で初期化
            count += 1
        grid.append(row)
    return grid

# グリッドを表示する関数
def display_grid(grid):
    print("現在のグリッド:")
    for row in grid:
        print(" ".join(row))
    print()

# ヒントを提供する関数
def give_hint(player_x, player_y, treasure_x, treasure_y):
    hint = []
    if player_x < treasure_x:
        hint.append("右")
    elif player_x > treasure_x:
        hint.append("左")

    if player_y < treasure_y:
        hint.append("下")
    elif player_y > treasure_y:
        hint.append("上")

    return " ".join(hint) + " に宝があります。"

# 宝探しゲームを実行する関数
def treasure_hunt_game():
    # グリッド（リスト）と宝の位置を初期化
    grid = initialize_grid()
    treasure_x = random.randint(0, GRID_SIZE - 1)
    treasure_y = random.randint(0, GRID_SIZE - 1)

    # 選択済みマスを集合で記録
    chosen_cells = set()

    print("宝探しゲームへようこそ！1から25までの数字で宝を探し当ててください。")
    print("宝を探すチャンスは3回です。")
    display_grid(grid)

    attempts = 0
    found_treasure = False

    while attempts < 3 and not found_treasure:
        try:
            choice = int(input("1から25のマス番号を入力してください: ")) - 1
            if choice < 0 or choice >= GRID_SIZE * GRID_SIZE:
                print("無効な番号です。1から25までの数字を入力してください。")
                continue

            player_x = choice % GRID_SIZE
            player_y = choice // GRID_SIZE

            # 集合で既に選んだか確認
            if (player_x, player_y) in chosen_cells:
                print("そのマスは既に選択されています。別のマスを選んでください。")
                continue

            # 選択済みに追加
            chosen_cells.add((player_x, player_y))

            # 宝を見つけた場合
            if player_x == treasure_x and player_y == treasure_y:
                print("🎉 おめでとうございます！宝を見つけました！ 🎉")
                grid[player_y][player_x] = "☆"  # 宝の位置を☆で表示
                found_treasure = True
            else:
                # 選んだ場所を＊でマークし、ヒントを出す
                grid[player_y][player_x] = "＊"
                print(give_hint(player_x, player_y, treasure_x, treasure_y))
                attempts += 1
                print(f"残りのチャンス: {3 - attempts}回")

            display_grid(grid)
        except ValueError:
            print("無効な入力です。1から25までの数字を入力してください。")

    if not found_treasure:
        print("💀 残念ながら、チャンスを使い切りました。宝は見つかりませんでした。")

# ゲームを実行
if __name__ == "__main__":
    treasure_hunt_game()
