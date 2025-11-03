import random
import time

print("----------------------")
print("---【チンチロ対決】---")
print("----------------------")
time.sleep(1)

#---------------------------------------------------------------
# ユーザー側
print("")
print("---【あなた】の番です---")
print("")
player=0
for i in range(1,4):
    print(f"\n{i}回目、あなたがサイコロを振る...")
    time.sleep(1.2)
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    print("あなたの出目は",a,b,c)
    time.sleep(0.8)

    # 並び替え
    dice = sorted([a,b,c])#数字を小さい順に並べ替え
    a,b,c = dice

    # 特殊役・ゾロ目・目判定
    if (a,b,c) == (1,2,3):  # ヒフミ
        player = -1
        print("ヒフミ（最弱）")
        break
    elif (a,b,c) == (4,5,6):  # シゴロ
        player = 10
        print("シゴロ")
        break
    elif a == b == c == 1:  # 1のゾロ目
        player = 20 + a
        print(f"{a}のゾロ目")
        break
    elif a == b == c == 6:  # 6のゾロ目
        player = 13 + a
        print(f"{a}のゾロ目")
        break
    elif a == b == c == 5:  # 5のゾロ目
        player = 13 + a
        print(f"{a}のゾロ目")
        break
    elif a == b == c == 4:  # 4のゾロ目
        player = 13 + a
        print(f"{a}のゾロ目")
        break
    elif a == b == c == 3:  # 3のゾロ目
        player = 13 + a
        print(f"{a}のゾロ目")
        break
    elif a == b == c == 2:  # 2のゾロ目
        player = 13 + a
        print(f"{a}のゾロ目")
        break
    elif a == b:
        player = c
        print(f"{c}の目")
        break
    elif b == c:
        player = a
        print(f"{a}の目")
        break
    elif c == a:
        player = b
        print(f"{b}の目")
        break
    else:
        print("目なし！")
        player = 0
        if i == 3:
            print("3回とも目なしでした…")
        time.sleep(0.8)
        continue

time.sleep(1.5)

#---------------------------------------------------------------
# 親側
print("")
print("---【親】の番です---")
print("")
dealer=0
for i in range(1,4):
    print(f"\n{i}回目、親がサイコロを振る...")
    time.sleep(1.2)
    d=random.randint(1,6)
    e=random.randint(1,6)
    f=random.randint(1,6)
    print("親の出目は",d,e,f)
    time.sleep(0.8)

    dice = sorted([d,e,f])
    d,e,f = dice

    if (d,e,f) == (1,2,3):
        dealer = -1
        print("ヒフミ（最弱）")
        break
    elif (d,e,f) == (4,5,6):
        dealer = 10
        print("シゴロ")
        break
    elif d == e == f == 1:
        dealer = 20 + d
        print(f"{d}のゾロ目")
        break
    elif d == e == f == 6:
        dealer = 13 + d
        print(f"{d}のゾロ目")
        break
    elif d == e == f ==5:
        dealer = 13 + d
        print(f"{d}のゾロ目")
        break
    elif d == e == f ==4:
        dealer = 13 + d
        print(f"{d}のゾロ目")
        break
    elif d == e == f ==3:
        dealer = 13 + d
        print(f"{d}のゾロ目")
        break
    elif d == e == f ==2:
        dealer = 13 + d
        print(f"{d}のゾロ目")
        break
    elif d == e:
        dealer = f
        print(f"{f}の目")
        break
    elif e == f:
        dealer = d
        print(f"{d}の目")
        break
    elif f == d:
        dealer = e
        print(f"{e}の目")
        break
    else:
        print("目なし！")
        dealer = 0
        if i == 3:
            print("3回とも目なしでした…")
            time.sleep(0.8)
        continue

time.sleep(1.5)

#---------------------------------------------------------------
# 勝敗判定
print("---------------------------------------------------------------")
print(f"あなたの役：{player}")
print(f"親の役　　：{dealer}")
print("---------------------------------------------------------------")

if player > dealer:
    print("あなたの勝ち！")
elif player < dealer:
    print("親の勝ち！")
else:
    print("引き分け！")

print("-----------------------------------------------------------")
time.sleep(1)
print("ゲーム終了。")