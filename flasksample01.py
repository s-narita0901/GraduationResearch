# !/use/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

import pymongo
import xml.etree.ElementTree as ET#ElementTreeをインポート

client=pymongo.MongoClient()#pymongoをインポートし、クライアントに接続
postime_db=client['postime']#postimeというデータベースを作る
postime_col=postime_db['collection']#collectionを作る

tree = ET.parse('output.xml')
root = tree.getroot()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("todb.html")

@app.route("/sendtodb", methods=['POST'])
def sendtodb():
    #htmlの方で入力されたデータをmongodbへ送る
    d_id=request.form['d_id']
    t=request.form['t']
    insert_data={'time': t,'d_id': d_id}
    post_id=postime_col.insert(insert_data)
    
    #すべてのデータを出力
    print "----all data"
    for elem in postime_col.find():
        print elem
    print "--------"
    
    #dbからXMLへ
    
    #print "latest lati : "+lati
    #print "latest longi : "+longi
    #print "latest time : "+t

    for contentsRoot in root.iter('ContentsRoot'):
        count=int(postime_col.find().count())
        skipcount=count-1
        outputFileName=str(postime_col.find().skip(skipcount).limit(1))
        contentsRoot.set('OutpuFileName',outputFileName)

    tree.write('sample.xml')
    
    return render_template("todb.html")

#app.debug=false
app.run(host='0.0.0.0')
