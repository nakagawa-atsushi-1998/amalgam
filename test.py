import os
import core
import interfaces
from pprint import pprint

def test1():
    """
    手動で実行
    """
    aml = core.Amalgam()
    pprint(dir(aml))
    aml.in_path = "./data/import/2022-01-21_01-02-41.800000.csv"
    print("入力ファイルのパス:"+aml.in_path)
    aml.check_ext()
    aml.check_enc()
    aml.out_path = "./data/export"
    aml.out_ext = "json"
    aml.out_enc = "utf-8"
    aml.out_path = aml.out_path + "/" + aml.file_name + "." + aml.out_ext
    aml.import_file()
    aml.export_file()
    print("finished.")

def test2():
    """
    対話形式で実行
    """
    amlCLI = interfaces.CLI()

if __name__ == "__main__":
    cd = os.path.abspath(os.path.join(__file__, os.pardir)) #カレントディレクトリ取得
    os.chdir(cd)
    test1()
    test2()
