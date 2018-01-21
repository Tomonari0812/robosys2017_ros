#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
# タイマのライブラリ
import time
# USBシリアルのライブラリ
import serial
# I2Cのライブラリ
import smbus
#　配列を送るメッセージファイル
from eggsystem.msg import Servo	


#--------------------------class--------------------------------------

class Serialcommunication(object):
    def __init__(self):
        self._sub = rospy.Subscriber('movedata', Servo, self.callback, queue_size=1)

        #-----シリアルポートの定義----------------------------------------
        self.com = serial.Serial(
          port = "/dev/ttyUSB0",
          baudrate = 115200,
          parity = serial.PARITY_EVEN,
          bytesize = serial.EIGHTBITS,
          stopbits = serial.STOPBITS_ONE,
          timeout = None,
          xonxoff = False,
        )


        #-----各サーボのID---------------------------------------------
        #左後ろ脚のサーボのID
        self.left_back_leg = "\x85"
        #右後ろ車輪のサーボのID
        self.left_back_wheel = "\x81"
        #左前脚のサーボのID
        self.left_front_leg = "\x86"
        #左前車輪のサーボのID
        self.left_front_wheel = "\x82"
        #右後ろ脚のサーボのID
        self.right_back_leg = "\x87"
        #右後ろ車輪のサーボのID
        self.right_back_wheel = "\x83"
        #右前脚のサーボのID
        self.right_front_leg = "\x88"
        #右前車輪のサーボのID
        self.right_front_wheel = "\x84"
        #中央サーボのID
        self.center_servo = "\x89"

        #-----サーボのマスク値------------------------------------------
        # サーボのPOS_Hのマスク値"0b1111111110000000"
        self.mask_h = 65408
        # サーボのPOS_Lのマスク値"0b0000000001111111"
        self.mask_l = 127

    #-----各サーボに値を書き込む(chr()は引数をasciiコードに変換)-----------
    #サーボに値を書き込む関数
    def serialOutput(self, pos, servo_id):
        #サーボのマスク処理
        pos_h = (pos & self.mask_h) >> 7
        pos_l = pos & self.mask_l
        #サーボに値を書き込む
        self.com.write(servo_id + chr(pos_h) + chr(pos_l))
        time.sleep(0.001)
        return pos

    def callback(self, data):
        self.serialOutput(data.Pulse[0], self.left_back_wheel)
        self.serialOutput(data.Pulse[1], self.left_front_wheel)
        self.serialOutput(data.Pulse[2], self.right_back_wheel)
        self.serialOutput(data.Pulse[3], self.right_front_wheel)
        self.serialOutput(data.Pulse[4], self.left_back_leg)
        self.serialOutput(data.Pulse[5], self.left_front_leg)
        self.serialOutput(data.Pulse[6], self.right_back_leg)
        self.serialOutput(data.Pulse[7], self.right_front_leg)
        self.serialOutput(data.Pulse[8], self.center_servo)



if __name__ == '__main__':
    rospy.init_node('move_sub')
    move_sub = Serialcommunication()
    rospy.spin()

