
import random

basic_hiragana = [
    "あ", "い", "う", "え", "お",
    "か", "き", "く", "け", "こ",
    "さ", "し", "す", "せ", "そ",
    "た", "ち", "つ", "て", "と",
    "な", "に", "ぬ", "ね", "の",
    "は", "ひ", "ふ", "へ", "ほ",
    "ま", "み", "む", "め", "も",
    "や", "ゆ", "よ",
    "ら", "り", "る", "れ", "ろ",
    "わ", "を", "ん"
]

basic_romaji = [
    "a", "i", "u", "e", "o",
    "ka", "ki", "ku", "ke", "ko",
    "sa", "shi", "su", "se", "so",
    "ta", "chi", "tsu", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo",
    "ra", "ri", "ru", "re", "ro",
    "wa", "wo", "n"
]

dakuten_hiragana = [
    "が", "ぎ", "ぐ", "げ", "ご",
    "ざ", "じ", "ず", "ぜ", "ぞ",
    "だ", "ぢ", "づ", "で", "ど",
    "ば", "び", "ぶ", "べ", "ぼ",
    "ぱ", "ぴ", "ぷ", "ぺ", "ぽ"
]

dakuten_romaji = [
    "ga", "gi", "gu", "ge", "go",
    "za", "ji", "zu", "ze", "zo",
    "da", "ji", "zu", "de", "do",
    "ba", "bi", "bu", "be", "bo",
    "pa", "pi", "pu", "pe", "po"
]

yoon_hiragana = [
    "きゃ", "きゅ", "きょ",
    "しゃ", "しゅ", "しょ",
    "ちゃ", "ちゅ", "ちょ",
    "にゃ", "にゅ", "にょ",
    "ひゃ", "ひゅ", "ひょ",
    "みゃ", "みゅ", "みょ",
    "りゃ", "りゅ", "りょ",
    "ぎゃ", "ぎゅ", "ぎょ",
    "じゃ", "じゅ", "じょ",
    "びゃ", "びゅ", "びょ",
    "ぴゃ", "ぴゅ", "ぴょ"
]

yoon_romaji = [
    "kya", "kyu", "kyo",
    "sha", "shu", "sho",
    "cha", "chu", "cho",
    "nya", "nyu", "nyo",
    "hya", "hyu", "hyo",
    "mya", "myu", "myo",
    "rya", "ryu", "ryo",
    "gya", "gyu", "gyo",
    "ja", "ju", "jo",
    "bya", "byu", "byo",
    "pya", "pyu", "pyo"
]

katakana_basic = [
    "ア", "イ", "ウ", "エ", "オ",
    "カ", "キ", "ク", "ケ", "コ",
    "サ", "シ", "ス", "セ", "ソ",
    "タ", "チ", "ツ", "テ", "ト",
    "ナ", "ニ", "ヌ", "ネ", "ノ",
    "ハ", "ヒ", "フ", "ヘ", "ホ",
    "マ", "ミ", "ム", "メ", "モ",
    "ヤ", "ユ", "ヨ",
    "ラ", "リ", "ル", "レ", "ロ",
    "ワ", "ヲ", "ン"
]

katakana_basic_romaji = [
    "a", "i", "u", "e", "o",
    "ka", "ki", "ku", "ke", "ko",
    "sa", "shi", "su", "se", "so",
    "ta", "chi", "tsu", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo",
    "ra", "ri", "ru", "re", "ro",
    "wa", "wo", "n"
]

katakana_dakuten = [
    "ガ", "ギ", "グ", "ゲ", "ゴ",
    "ザ", "ジ", "ズ", "ゼ", "ゾ",
    "ダ", "ヂ", "ヅ", "デ", "ド",
    "バ", "ビ", "ブ", "ベ", "ボ",
    "パ", "ピ", "プ", "ペ", "ポ"
]

katakana_dakuten_romaji = [
    "ga", "gi", "gu", "ge", "go",
    "za", "ji", "zu", "ze", "zo",
    "da", "ji", "zu", "de", "do",
    "ba", "bi", "bu", "be", "bo",
    "pa", "pi", "pu", "pe", "po"
]

katakana_yoon = [
    "キャ", "キュ", "キョ",
    "シャ", "シュ", "ショ",
    "チャ", "チュ", "チョ",
    "ニャ", "ニュ", "ニョ",
    "ヒャ", "ヒュ", "ヒョ",
    "ミャ", "ミュ", "ミョ",
    "リャ", "リュ", "リョ",
    "ギャ", "ギュ", "ギョ",
    "ジャ", "ジュ", "ジョ",
    "ビャ", "ビュ", "ビョ",
    "ピャ", "ピュ", "ピョ"
]

katakana_yoon_romaji = [
    "kya", "kyu", "kyo",
    "sha", "shu", "sho",
    "cha", "chu", "cho",
    "nya", "nyu", "nyo",
    "hya", "hyu", "hyo",
    "mya", "myu", "myo",
    "rya", "ryu", "ryo",
    "gya", "gyu", "gyo",
    "ja", "ju", "jo",
    "bya", "byu", "byo",
    "pya", "pyu", "pyo"
]


def run_quiz(kana_list, romaji, indexes, score=0, total_asked=0):
    missed_indexes = []
    leftover_indexes = list(indexes)

    while len(leftover_indexes) > 0:
        random_index = random.choice(leftover_indexes)
        user_guess = input(f"{kana_list[random_index]}\nResponse: ").strip().lower()
        total_asked += 1

        if user_guess == romaji[random_index].lower():
            score += 1
            print("══════════════════════════════")
            print(f"Correct. ({score}/{total_asked})\n")
        else:
            print("══════════════════════════════")
            print(
                f"Incorrect. The correct answer is: "
                f"{romaji[random_index]} ({score}/{total_asked})\n"
            )
            missed_indexes.append(random_index)

        leftover_indexes.remove(random_index)

    return score, total_asked, missed_indexes


assert len(basic_hiragana) == len(basic_romaji)
assert len(dakuten_hiragana) == len(dakuten_romaji)
assert len(yoon_hiragana) == len(yoon_romaji)
assert len(katakana_basic) == len(katakana_basic_romaji)
assert len(katakana_dakuten) == len(katakana_dakuten_romaji)
assert len(katakana_yoon) == len(katakana_yoon_romaji)


print("Choose your quiz mode:")
print("1. Basic Hiragana")
print("2. Dakuten and Handakuten")
print("3. Yoon combinations")
print("4. All Hiragana")
print("5. Basic Katakana")
print("6. Katakana with Dakuten and Handakuten")
print("7. Katakana Yoon combinations")
print("8. All Katakana")
print("9. All Hiragana + Katakana Combined")

choice = input("Enter 1-9: ").strip()

while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    choice = input("Invalid choice. Enter 1-9: ").strip()


if choice == "1":
    kana_list, romaji = basic_hiragana, basic_romaji

elif choice == "2":
    kana_list, romaji = dakuten_hiragana, dakuten_romaji

elif choice == "3":
    kana_list, romaji = yoon_hiragana, yoon_romaji

elif choice == "4":
    kana_list = basic_hiragana + dakuten_hiragana + yoon_hiragana
    romaji = basic_romaji + dakuten_romaji + yoon_romaji

elif choice == "5":
    kana_list, romaji = katakana_basic, katakana_basic_romaji

elif choice == "6":
    kana_list, romaji = katakana_dakuten, katakana_dakuten_romaji

elif choice == "7":
    kana_list, romaji = katakana_yoon, katakana_yoon_romaji

elif choice == "8":
    kana_list = katakana_basic + katakana_dakuten + katakana_yoon
    romaji = (
        katakana_basic_romaji
        + katakana_dakuten_romaji
        + katakana_yoon_romaji
    )

elif choice == "9":
    kana_list = (
        basic_hiragana + dakuten_hiragana + yoon_hiragana
        + katakana_basic + katakana_dakuten + katakana_yoon
    )
    romaji = (
        basic_romaji + dakuten_romaji + yoon_romaji
        + katakana_basic_romaji + katakana_dakuten_romaji
        + katakana_yoon_romaji
    )


indexes = list(range(len(kana_list)))
score, total_asked, missed_indexes = run_quiz(kana_list, romaji, indexes)

if len(missed_indexes) == 0:
    print("You mastered all the kana!")
    print(f"Final Score: {score}/{total_asked}")

while len(missed_indexes) > 0:
    retry = input("Retry missed kana? (y/n): ").strip().lower()

    if retry == "y":
        score, total_asked, missed_indexes = run_quiz(
            kana_list, romaji, missed_indexes, score, total_asked
        )

        if len(missed_indexes) == 0:
            print("You mastered all the missed kana!")
            print(f"Final Score: {score}/{total_asked}")

    elif retry == "n":
        print("Exiting practice mode.")
        print(f"Final Score: {score}/{total_asked}")
        break

    else:
        print("Please enter y or n.")
