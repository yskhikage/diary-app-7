import csv
import boto3
from boto3.dynamodb.conditions import Key

def addDynamoDB():
    dynamodb=boto3.resource('dynamodb',region_name='ap-northeast-1')
    table=dynamodb.Table('payment_details')

    filepath = "data/result.csv"
    with open(filepath, "r", encoding="utf-8") as f:
        #先頭業を除外
        reader = csv.reader(f)
        next(reader)
        # batch_writer()で、25項目ずつCSVの全てをputする
        with table.batch_writer() as batch:
            for row in reader:
                item = {
                    "id": row[0],
                    "利用日": row[1],
                    "利用店名・商品名": row[2],
                    "利用者": row[3],
                    "支払方法":row[4],
                    "利用金額":row[5]
                }
                batch.put_item(Item=item)

if __name__ == "__main__":
    addDynamoDB()