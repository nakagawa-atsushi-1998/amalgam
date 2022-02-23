#!/usr/bin/env python
# coding: utf-8
import sys
import enum
import chardet
import csv
import json
import yaml
import xmltodict
import dicttoxml
import pandas as pd
from bs4 import BeautifulSoup

class Importer:
    def __init__(self):
        self.dict_data=None
        self.in_path=self.in_ext=self.in_enc=None

    def import_file(self):
        with open(self.in_path, mode="r", encoding=self.in_enc) as file:
            if self.in_ext == "csv":
                self.csv_to_dict(file)
            elif self.in_ext == "tsv":
                self.tsv_to_dict(file)
            #elif self.in_ext == "xml":
            #    self.xml_to_dict(file)
            elif self.in_ext == "yml":
                self.yml_to_dict(file)
            elif self.in_ext == "json":
                self.json_to_dict(file)
            else:
                self.dict_data = None
                print('File import error: 非対応の拡張子です。')

    def csv_to_dict(self, file):
        reader = csv.reader(file, delimiter=',')
        array_data = [row for row in reader]
        column = array_data[0]
        array_data = array_data[1:-1]
        data_frame = pd.DataFrame(array_data, columns=column)
        self.dict_data = data_frame.reset_index(drop=True).to_dict()

    def tsv_to_dict(self, file):
        reader = csv.reader(file, delimiter='\t')
        array_data = [row for row in reader]
        column = array_data[0]
        array_data = array_data[1:-1]
        data_frame = pd.DataFrame(
            data=array_data,
            columns=column
        )
        self.dict_data = data_frame.to_dict()
        
    def xml_to_dict(self, file):
        self.dict_data = xmltodict.parse(
            file.read(),
            xml_attribs=True
        )
        
    def yml_to_dict(self, file):
        self.dict_data = yaml.safe_load(file)
    
    def json_to_dict(self, file):
        self.dict_data = json.load(file)

class Exporter:
    def __init__(self):
        self.dict_data=None
        self.out_path=self.out_ext=self.out_enc=None
    
    def export_file(self):
        if self.out_ext == "csv":
            print(self.out_path)
            self.dict_to_csv()
        elif self.out_ext == "tsv":
            self.dict_to_tsv()
        #elif self.out_ext == "xml":
        #    self.dict_to_xml()
        elif self.out_ext == "yml":
            self.dict_to_yml()
        elif self.out_ext == "json":
            self.dict_to_json()
        else:
            self.dict_data = None
            print('File export error: 非対応の拡張子です。')

    def dict_to_csv(self):
        data_frame = pd.DataFrame(data=self.dict_data)
        data_frame.to_csv(self.out_path, sep=',', index=False)
        print(data_frame)

    def dict_to_tsv(self):
        data_frame = pd.DataFrame(data=self.dict_data)
        data_frame.to_csv(self.out_path, sep='\t', index=False)
    
    def dict_to_xml(self):
        xml_data = dicttoxml.dicttoxml(
            obj=self.dict_data,
            #root=False, #bool
            #custom_root="custom_root" #''markup', #str
            #ids=False, #bool
            #attr_type=True, #bool
            #item_func=func, #function
            #cdata = False #bool
        )
        xml_data = BeautifulSoup(xml_data, "xml").prettify()
        with open(self.out_path, mode='w', encoding=self.out_enc) as file:
            file.write(xml_data)
    
    def dict_to_yml(self):
        with open(self.out_path, mode="w", encoding=self.out_enc) as file:
            yaml.dump(self.dict_data, file, allow_unicode=True)

    def dict_to_json(self):
        with open(self.out_path, mode="w", encoding=self.out_enc) as file:
            json.dump(self.dict_data, file, ensure_ascii=False, indent=4)
        

class Amalgam(Importer, Exporter):
    def __init__(self):
        super(Importer, self).__init__()
        super(Exporter, self).__init__()

    def check_ext(self):
        self.in_ext = self.in_path.split('.')[-1]
        self.file_name = "".join(("".join(self.in_path.split('/')[-1]).split("." + self.in_ext)))

    def check_enc(self):
        with open(self.in_path, mode="rb",) as file:
            reader = file.read()
            self.in_enc = chardet.detect(reader)['encoding']
