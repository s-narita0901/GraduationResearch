#!/use/bin/env python
#-*- coding: utf-8 -*-

import pymongo

# mongodbへ接続
client=pymongo.MongoClient()

# データベースの取得、または作成
# この例では、testというデータベースを作っている
test_db=client['test']

#データベースからコレクションを得る。RDBのテーブルに相当。
#下の例ではcollectionを作る（もうすでにあるときはそれを使う）
test_col=test_db['collection']

#入れるデータの例。ハッシュ（辞書）の形であればOK
insert_data={'name': 'Endo', 'age': '22'}

#データの挿入
post_id=test_col.insert(insert_data)

#入れたデータのObjectIdを表示
print post_id

#二個目のデータを入れる
insert_data={'name': 'Kurakata', 'age': '24'}
post_id=test_col.insert(insert_data)

#すべての表示
print "----all data"
for elem in test_col.find():
    print elem
print "--------"

#一致するものを見つけて、データの更新をする
data=test_col.find_one({'name':'Kurakata'})
print data['_id']
data['age']='26'
test_col.update({'_id': data['_id']},data)

#条件の指定
for elem in test_col.find({'name': 'Kurakata'}):
    print elem

#データベースの削除
#client.drop_database(test_db)
