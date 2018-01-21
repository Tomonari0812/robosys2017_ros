# robosys2017_ros
  全方向移動型ロボットをROSを用いてゲームパッドで操作するパッケージです。

# Demo movie
- YouTube
[robosys2017 ROS](https://youtu.be/I-pDHkgffcA)

# Comand
```
$sudo apt-get install ros-indigo-joy
$roscore
$rosrun joy joy_node
$rosrun eggsystem coresys2.py
$rosrun eggsystem controlsys2.py
```
# 使い方
　ゲームパッドにはlogicoolを用いました。
- Comandを上記の流れで起動する
- 初期姿勢に移動したのちゲームパッドでの操作が可能となる
- ゲームパッドの操作方法
 - 前後左右の移動はLBボタンを押しながら十字キーで操作します。
 - 旋回動作はRBボタンを押しながらX,Bボタンを押します。
 　- X : 左旋回
   - B : 右旋回
 - 機体の高さを変えるときはLB,RBボタンを同時押しした状態でY,Aボタンを押します。
 　- Y : 一段階高くする
 　- A : 一段階低くする
