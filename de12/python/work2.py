a=15
if a > 10:
    print("10より大きい")
    



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





