# -*- coding: utf-8 -*-

"""
モーションインストール用CUIアプリケーション
"""
__author__  = "Kazuyuki TAKASE"
__license__ = "MIT"
__status__  = "2.0.0"
__date__    = "2015/05/22"
__email__   = "takase@plen.jp"


# 標準ライブラリのインポート
import sys
from argparse import ArgumentParser

# 自作ライブラリのインポート
sys.path.append("./lib/")
import BLED112_Driver


# メインスレッド
def main(args):
	send_device = None
	if args.send == "bled112":
		send_device = BLED112_Driver()
	if args.send == "internal_ble":
		# send_device = InternalDriver()

	if (send_device == None):
		exit()


# アプリケーション・エントリーポイント
if __name__ == "__main__":
	# コマンドラインオプションの定義
	argument_parser = ArgumentParser()
	argument_parser.add_argument(
		"-s", "--send",
		dest    = "send",
		choices = ("bled112", "internal_ble"),
		default = "bled112",
		help    = u'送信デバイスを"bled112", "internal_ble"から選択します。',
		metavar = "<SEND DEVICE>"
	)
	argument_parser.add_argument(
		"-r", "--receive",
		dest    = "receive",
		help    = u"受信デバイスを指定します。",
		metavar = "<RECEIVE DEVICE>" 
	)
	argument_parser.add_argument(
		"-f", "--file",
		dest     = "motions",
		nargs    = "+",
		required = True,
		help     = u"指定したモーションファイルをインストールします。",
		metavar  = "<MOTION>"
	)
	argument_parser.add_argument(
		"-v", "--verify",
		dest    = "verify_flag",
		action  = "store_true",
		default = False,
		help    = u"モーションファイルのインストール後、書き込みの検証を行います。"
	)

	# コマンドラインオプションの検証，および取得
	args = argument_parser.parse_args()

	# メインスレッドの起動
	main(args)