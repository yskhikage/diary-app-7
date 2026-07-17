
import pandas as pd
import shutil
import uuid
import os 

input_file='sample.csv'
df = pd.read_csv(input_file)

#データ整形
df=df[['利用日','利用店名・商品名','利用者','支払方法','利用金額']]
#先頭業にidを追加
df.insert(0,'id',[ str(uuid.uuid4()) for value in range(len(df))])

print(df)


#出力
df.to_csv('data/result.csv',index=False)
#後処理
shutil.move('sample.csv','old')