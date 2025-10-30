#繰り返し
for i in range(1,4): #コロンが入っていることに注意
    print(i,"人目") #タブでずらしていることに注意！
    name=input("名前を教えて下さい")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))


    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if waist>=85 and age>=40:
        print(name,"さん、あなたはデブだ。ダイエットしろ！！")
    elif waist<=40 :
        print(name,"さん、あなたは瘦せすぎだ。もっと飯を食え！")
    else:
        print(name,"さん、あなたは健康です。このまま続けましょう！")


# 出力結果
# 0 人目
# 1 人目
# 2 人目