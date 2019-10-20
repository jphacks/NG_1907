# EMOVE

![EMOVE](logo.jpg)

[![Product Name](image.png)](https://www.youtube.com/watch?v=G5rULR53uMk)

## 製品概要
### バイタル x エンターテインメント x Tech

### 背景（製品開発のきっかけ、課題等）
バイタルデータを取得するものと言えば,健康グッズが頭に浮かぶ.
私たちはそれを遊びに用いた.

### 製品説明（具体的な製品の説明）
クラブやライブハウスに訪れた人々に腕時計型心拍計を配布し，その心拍データを収集する．
このデータを用いて，場内に流す音楽のテンポを決めて，そのテンポの楽曲をまとめたプレイリストを作成し，再生する．

### 特長

#### BPM（テンポ）を使用した楽曲の自動再生
対象エリアの心拍数の平均を取り出し，その数値を元に流す楽曲のBPM（Beat Per Minute）を指定する機能．  
クラブやライブハウスの場合は，フロアの雰囲気に合った楽曲を再生できるほか，心拍数の変化でフロア全体の楽曲に対する抑揚を記録でき，次以降に再生する楽曲の傾向を指定できる．

#### 心拍数によるマッチング
同じ曲の再生中に同じ心拍数の変化をする人同士を繋げるマッチング機能．

### 解決出来ること
ウェアラブル端末から得られるバイタルデータの新たな使い方を開拓する．

### 今後の展望
#### 楽曲による心拍数のコントロール
クラブなどでは，速いテンポの曲を流して聴き手の心拍数を上げて盛り上げる．
この原理を利用して，ランニング中に楽曲のテンポの変化で心拍数を制御して最適な速度での運動を目指す．

#### 飲酒量の管理
クラブやライブ会場での使用を想定し，アルコールによる心拍数の変化を監視して危険状態の場合に何かしらのアクションを起こすようにする．

## 開発内容・開発技術
### 活用した技術
#### API・データ

* なし

#### フレームワーク・ライブラリ・モジュール
* Python
    * socket
    * json
    * Firebase
    * Flask
* Arduino
    * M5Stack
    * WiFi
* Vue.js
    * Node-RED

#### デバイス
* M5Stack
* Raspberry Pi


### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* M5Stack用 腕時計バンド
* M5Stack 心拍計・ソケット通信
* RaspberryPi 心拍データ・ユーザの紐づけ
* RaspberryPi 楽曲の登録・再生
* Firebase 心拍データ・ユーザのデータベース，楽曲選定

* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください（任意）
   * M5Stackでのアナログデータの処理
      * [m5stack/](https://github.com/jphacks/NG_1907/tree/master/m5stack)
      * [m5stack_e/](https://github.com/jphacks/NG_1907/tree/master/m5stack_e)
      * [m5stack_v3/](https://github.com/jphacks/NG_1907/tree/master/m5stack_v3)
