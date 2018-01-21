#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-----ライブラリのインポート-----
# GPIOの入出力ライブラリ
#import RPi.GPIO as GPIO

import rospy
from sensor_msgs.msg import Joy
from eggsystem.msg import Servo		#　配列を送るメッセージファイル
import time				# タイマのライブラリ
import serial				# USBシリアルのライブラリ
import smbus				# I2Cのライブラリ

#加速度センサ"ADXL345"のライブラリ
#from adxl345 import ADXL345

#"ADXL345"関数の値を代入
#adxl345 = ADXL345()


#-----GPIOの設定-----
#GPIOのpinの番号の定義
#GPIO.setmode(GPIO.BCM)

#GPIOの入出力の定義
#GPIO.setup(25, GPIO.OUT)





#------------------------------
# 変数定義
#------------------------------

#-----脚サーボの初期値-----
#左後ろ脚の初期値
pos_lbl_d = 7500
#左前脚の初期値
pos_lfl_d = 7500
#右後ろ脚の初期値
pos_rbl_d = 7500
#右前脚の初期値
pos_rfl_d = 7500

#-----車輪サーボの初期値-----
#左後ろ車輪の初期値
pos_lbw_d = 7500
pos_lfw_d = 7500
#右後ろ車輪の初期値
pos_rbw_d = 7500
#右前車輪の初期値
pos_rfw_d = 7500

#-----中央サーボの初期値-----
pos_cs_d = 7150


#-----移動用の関数-----
def forward():
    global pos_lbw,pos_lfw,pos_rbw,pos_rfw
    #変数へサーボの値を代入
    pos_lbw = 7400
    pos_lfw = 7400
    pos_rbw = 7600
    pos_rfw = 7600
    print("forward")

def back():
    global pos_lbw,pos_lfw,pos_rbw,pos_rfw
    #変数へサーボの値を代入
    pos_lbw = 7600
    pos_lfw = 7600
    pos_rbw = 7400
    pos_rfw = 7400

def left():
    global pos_lbw,pos_lfw,pos_rbw,pos_rfw
    #変数へサーボの値を代入
    pos_lbw = 7400
    pos_lfw = 7600
    pos_rbw = 7400
    pos_rfw = 7600

def right():
    global pos_lbw,pos_lfw,pos_rbw,pos_rfw
    #変数へサーボの値を代入
    pos_lbw = 7600
    pos_lfw = 7400
    pos_rbw = 7600
    pos_rfw = 7400

def left_rotation():
    global pos_lbw,pos_lfw,pos_rbw,pos_rfw
    #変数へサーボの値を代入
    pos_lbw = 7600
    pos_lfw = 7600
    pos_rbw = 7600
    pos_rfw = 7600

def right_rotation():
    global pos_lbw,pos_lfw,pos_rbw,pos_rfw
    #変数へサーボの値を代入
    pos_lbw = 7400
    pos_lfw = 7400
    pos_rbw = 7400
    pos_rfw = 7400

def stop():
    global pos_lbw,pos_lfw,pos_rbw,pos_rfw
    #変数へサーボの値を代入
    pos_lbw = 7500
    pos_lfw = 7500
    pos_rbw = 7500
    pos_rfw = 7500
    print("stop")
#-----リフトアップ用の関数-----
def lift_up_0():
    #変数へサーボの値を代入
    global pos_lbl,pos_lfl,pos_rbl,pos_rfl
    pos_lbl = pos_lbl_d + 1000
    pos_lfl = pos_lfl_d + 1000
    pos_rbl = pos_rbl_d + 1000
    pos_rfl = pos_rfl_d + 1000

def lift_up_1():
    global pos_lbl,pos_lfl,pos_rbl,pos_rfl
    #変数へサーボの値を代入
    pos_lbl = pos_lbl_d + 800
    pos_lfl = pos_lfl_d + 800
    pos_rbl = pos_rbl_d + 800
    pos_rfl = pos_rfl_d + 800

def lift_up_2():
    global pos_lbl,pos_lfl,pos_rbl,pos_rfl
    #変数へサーボの値を代入
    pos_lbl = pos_lbl_d + 600
    pos_lfl = pos_lfl_d + 600
    pos_rbl = pos_rbl_d + 600
    pos_rfl = pos_rfl_d + 600

def lift_up_3():
    global pos_lbl,pos_lfl,pos_rbl,pos_rfl
    #変数へサーボの値を代入
    pos_lbl = pos_lbl_d + 400
    pos_lfl = pos_lfl_d + 400
    pos_rbl = pos_rbl_d + 400
    pos_rfl = pos_rfl_d + 400

def lift_up_4():
    global pos_lbl,pos_lfl,pos_rbl,pos_rfl
    #変数へサーボの値を代入
    pos_lbl = pos_lbl_d + 200
    pos_lfl = pos_lfl_d + 200
    pos_rbl = pos_rbl_d + 200
    pos_rfl = pos_rfl_d + 200

def lift_up_5():
    global pos_lbl,pos_lfl,pos_rbl,pos_rfl
    #変数へサーボの値を代入forward
    pos_lbl = pos_lbl_d + 000
    pos_lfl = pos_lfl_d + 000
    pos_rbl = pos_rbl_d + 000
    pos_rfl = pos_rfl_d + 000

def lift_up_6():
    global pos_lbl,pos_lfl,pos_rbl,pos_rfl
    #変数へサーボの値を代入
    pos_lbl = pos_lbl_d - 200
    pos_lfl = pos_lfl_d - 200
    pos_rbl = pos_rbl_d - 200
    pos_rfl = pos_rfl_d - 200

def lift_up_7():
    global pos_lbl,pos_lfl,pos_rbl,pos_rfl
    #変数へサーボの値を代入
    pos_lbl = pos_lbl_d - 400
    pos_lfl = pos_lfl_d - 400
    pos_rbl = pos_rbl_d - 400
    pos_rfl = pos_rfl_d - 400

def lift_up_8():
    global pos_lbl,pos_lfl,pos_rbl,pos_rfl
    #変数へサーボの値を代入
    pos_lbl = pos_lbl_d - 600
    pos_lfl = pos_lfl_d - 600
    pos_rbl = pos_rbl_d - 600
    pos_rfl = pos_rfl_d - 600

def lift_up_9():
    global pos_lbl,pos_lfl,pos_rbl,pos_rfl
    #変数へサーボの値を代入
    pos_lbl = pos_lbl_d - 800
    pos_lfl = pos_lfl_d - 800
    pos_rbl = pos_rbl_d - 800
    pos_rfl = pos_rfl_d - 800

def lift_up_10():
    global pos_lbl,pos_lfl,pos_rbl,pos_rfl
    #変数へサーボの値を代入
    pos_lbl = pos_lbl_d - 1000
    pos_lfl = pos_lfl_d - 1000
    pos_rbl = pos_rbl_d - 1000
    pos_rfl = pos_rfl_d - 1000

#------------main-------------------------------------------

#サーボを電源を安定させるための処理
time.sleep(2)
lift = 5

#初期姿勢に移動
pos_lbw = pos_lbw_d
pos_lfw = pos_lfw_d
pos_rbw = pos_rbw_d
pos_rfw = pos_rfw_d
pos_lbl = pos_lbl_d-1300
pos_lfl = pos_lfl_d-1300
pos_rbl = pos_rbl_d-1300
pos_rfl = pos_rfl_d-1300
pos_cs = pos_cs_d


#------------------------publish---------------------------

rospy.init_node('move')
pub = rospy.Publisher('movedata',Servo,queue_size = 10)

#----logicool----------------------------------------
def joy_callback(msg):
    global lift
    X = msg.buttons[0]
    A = msg.buttons[1]
    B = msg.buttons[2]
    Y = msg.buttons[3]
    LB = msg.buttons[4]
    RB = msg.buttons[5]
    RL = msg.axes[4]
    FB = msg.axes[5]

    if LB == 1 and RB == 0:
        if FB == 1.0 and RL == 0.0:
            forward()

        elif FB == -1.0 and RL == 0.0:
            back()

        elif FB == 0.0 and RL == 1.0 :
            left()

        elif FB == 0.0 and RL == -1.0:
            right()

        else: stop()

    elif LB == 0 and RB == 1:
        if X == 1 and B == 0:
            left_rotation()

        elif X == 0 and B == 1:
            right_rotation()

        else: stop()


    elif LB == 1 and RB == 1:
        if (Y == 1 and A != 1) and lift >= 0:
            lift += 1

            if lift == 0: lift_up_0()
            if lift == 1: lift_up_1()
            if lift == 2: lift_up_2()
            if lift == 3: lift_up_3()
            if lift == 4: lift_up_4()
            if lift == 5: lift_up_5()
            if lift == 6: lift_up_6()
            if lift == 7: lift_up_7()
            if lift == 8: lift_up_8()
            if lift == 9: lift_uppos_lbw,pos_lfw,pos_rbw,pos_rfw,_9()
            if lift == 10: lift_up_10()


        if (Y != 1 and A == 1) and lift <= 10:
            lift -= 1

            if lift == 0: lift_up_0()
            if lift == 1: lift_up_1()
            if lift == 2: lift_up_2()
            if lift == 3: lift_up_3()
            if lift == 4: lift_up_4()
            if lift == 5: lift_up_5()
            if lift == 6: lift_up_6()
            if lift == 7: lift_up_7()
            if lift == 8: lift_up_8()
            if lift == 9: lift_up_9()
            if lift == 10: lift_up_10()

    else: stop()

sub = rospy.Subscriber('/joy', Joy, joy_callback)
rate = rospy.Rate(10)

osa = 0
while osa <= 1300:
  pos_lbl = pos_lbl_d-1300+osa
  pos_lfl = pos_lfl_d-1300+osa
  pos_rbl = pos_rbl_d-1300+osa
  pos_rfl = pos_rfl_d-1300+osa
  osa += 1
  n = Servo()
  n.Pulse = [pos_lbw,pos_lfw,pos_rbw,pos_rfw,pos_lbl,pos_lfl,pos_rbl,pos_rfl,pos_cs]
  pub.publish(n)
  rate.sleep()
  time.sleep(0.01)
  if osa % 10 == 0:
    time.sleep(0.1)

while not rospy.is_shutdown():
    n = Servo()
    n.Pulse = [pos_lbw,pos_lfw,pos_rbw,pos_rfw,pos_lbl,pos_lfl,pos_rbl,pos_rfl,pos_cs]
    pub.publish(n)
    rate.sleep()
