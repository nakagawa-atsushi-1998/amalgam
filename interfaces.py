#!/usr/bin/env python
# coding: utf-8
import sys
import argparse
import core

class GUI(core.Amalgam):
    def __init__(self):
        super(core.Amalgam, self).__init__()
        pass

class CLI(core.Amalgam):
    def __init__(self):
        super(core.Amalgam, self).__init__()
        self.dialogue()
    
    def dialogue(self):
        print("データ形式変換を行います。\n以下の項目を指定してください。")
        self.in_path = input("\t入力ファイルのパス:")
        self.out_path = input("\t出力フォルダのパス:")
        self.out_ext = input("\t出力ファイルの拡張子:")
        self.out_enc = input("\t出力ファイルの文字コード:")
        while True:
            excutable = input("上記内容で実行します。\n\tよろしいですか?(y/n)")
            if excutable == 'y':
                try:
                    self.check_ext()
                    self.check_enc()
                    self.import_file()
                    self.export_file()
                    print("出力に成功しました。")
                    break
                except:
                    print("出力に失敗しました。")
            elif excutable == 'n':
                print("処理を中止します。")
                break
            else:
                print("yかnでお答えください。")
