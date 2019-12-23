# BERTの可視化
## 概要
BERTのattentionの可視化  
日本語pretrainedモデルは[こちら](http://nlp.ist.i.kyoto-u.ac.jp/index.php?BERT日本語Pretrainedモデル)のを使わせて頂きました  
## 実行環境
- GPU
- Docker Compose
  - Vue.js  
  - python

## 使い方
- transformer  

仮想環境
```
docker-compose up transformer
docker-compose exec transformer bash
```

実行
```
./run_jp_bert.sh [-t] [-e] [-d data_dir]
[-t] 学習
[-e] 評価
[-d data_dir] 利用するデータ 
```
- visualize
```
docker-compose up app
```
上記のコマンドを打ったら http://localhost:8000/ に接続
