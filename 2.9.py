import argparse
import secrets
import string

def create_password(length, include_special_chars, strength):
    # パスワードの強度に基づいて文字セットを選択
    char_set = string.ascii_lowercase if strength == "weak" else string.ascii_letters + string.digits
    # 特殊文字を含めるかどうかの判定
    char_set += string.punctuation if include_special_chars and strength == "strong" else ''
    # 指定された長さでランダムなパスワードを生成
    return ''.join(secrets.choice(char_set) for _ in range(length))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="パスワード生成ツール")
    parser.add_argument("length", type=int, nargs='?', default=12, help="生成するパスワードの文字数 (デフォルト: 12)")
    parser.add_argument("--no-special-chars", action="store_true", help="記号を除外する")
    parser.add_argument("--strength", choices=["weak", "medium", "strong"], default="strong", help="パスワードの強度設定 (weak, medium, strong)")
    
    args = parser.parse_args()

    if args.length < 1:
        print("エラー: パスワードの長さは1文字以上にしてください")
    else:
        for i in range(10):  # 10個のパスワードを生成
            print(f"生成されたパスワード {i+1}: {create_password(args.length, not args.no_special_chars, args.strength)}")
