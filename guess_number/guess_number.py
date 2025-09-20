import random

# 1から100までのランダムな数字を生成
correct_number = random.randint(1, 100)

# 予測できる回数を設定
max_attempts = 10

# ゲーム開始メッセージ
print("1から100までの数字を当ててください！")
print(f"あなたには {max_attempts} 回のチャンスがあります。")

# 現在の試行回数をカウント
attempts = 0

# 正解したかどうかのフラグ
is_correct = False

# プレイヤーの予測をループで繰り返す
while attempts < max_attempts:
    try:
        # プレイヤーの入力を数値として取得
        guess = int(input("あなたの予測: "))
        
        # 試行回数を1増やす
        attempts += 1
        
        # 予測が正解の場合
        if guess == correct_number:
            print(f"おめでとうございます！正解です！{attempts} 回目で当てました。")
            is_correct = True  # 正解したのでフラグをTrueに
            break
        # 予測が正解より小さい場合
        elif guess < correct_number:
            print("もっと大きい数字です。")
        # 予測が正解より大きい場合
        else:
            print("もっと小さい数字です。")
        
        # 残りの試行回数を表示
        remaining_attempts = max_attempts - attempts
        print(f"残りのチャンスは {remaining_attempts} 回です。")
    
    except ValueError:
        # 入力が数値でない場合のエラーメッセージ
        # ※無効入力はチャンスを消費しない
        print("無効な入力です。数字を入力してください。")

# 回数制限に達した場合のメッセージ（未正解のみ表示）
if not is_correct:
    print(f"残念！正解は {correct_number} でした。次回はもっと頑張りましょう！")
