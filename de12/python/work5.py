



from openai import OpenAI

#APIを使うkeyを入力します。これは絶対にwebページなどで公開してはいけません。
client = OpenAI(api_key="")

a=input("現在地を教えて")
b=input("目的地を教えて")

question = str(a)+"から"+str(b)+"までの時間と料金と移動方法を教えて。最善も教えて"

#ここがAPIです----------------------------
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": question}]
)
#---------------------------------------

print("AIの答え：", response.choices[0].message.content)

