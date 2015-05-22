# -*- coding: utf-8 -*-

# 標準ライブラリのインポート
import serial.tools.list_ports


class BLED112_driver:
	def __init__(self, com=None):
		if (com == None):
			for device in list(serial.tools.list_ports.comports()):
				if 'Bluegiga' in device[1]:
					self.com = device[0]
					print self.com

		if (com == None):
			print u'error : "BLED112"の検索に失敗しました。'

			exit()

		