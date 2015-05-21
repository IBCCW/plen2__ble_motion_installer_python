# -*- coding: utf-8 -*-

"""
モーションインストール用CUIアプリケーション
"""
__author__ = "Kazuyuki TAKASE <takase@plen.jp>"
__status__ = "2.0.0"
__date__   = "2015/05/19"


from optparse import OptionParser

if __name__ == "__main__":
	# コマンドラインオプションの定義
	option_parser = OptionParser()
	option_parser.add_option(
		"-c", "--com",

	)
	option_parser.add_option(
		"-f", "--file",
		dest    = "motions",
		help    = "MOTIONS に指定したモーションファイルをインストールします。",
		metavar = "MOTIONS"
	)
	option_parser.add_option(
		"-v", "--verify",

	)

