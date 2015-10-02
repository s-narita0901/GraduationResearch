# !/use/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

import pymongo
client=pymongo.MongoClient()#pymongoをインポートし、クライアントに接続

postime_db=client['postime']#postimeというデータベースを作る

postime_col=postime_db['collection']#collectionを作る

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("todb.html")

@app.route("/sendtodb", methods=['POST'])
def sendtodb():
    #htmlの方で入力されたデータをmongodbへ送る
    lati=request.form['lati']
    longi=request.form['longi']
    t=request.form['t']
    insert_data={'latitude': lati, 'longitude': longi, 'time': t}
    post_id=postime_col.insert(insert_data)
    
    #すべてのデータを出力
    print "----all data"
    for elem in postime_col.find():
        print elem
    print "--------"
    
    return render_template("todb.html")

app.debug=True
app.run()
