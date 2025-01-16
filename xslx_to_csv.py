import os
import pandas as pd
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

class ExelToCsv():
    def __init__(self):
        self.today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.excel_directory = os.environ.get('EXCEL_DIRECTORY')
        self.csv_directory = os.environ.get('CSV_DIRECTORY')
        self.existing_files = os.listdir(self.csv_directory)

        self.excel_files = []
        self.config_files = []
        self.params_files = []

    def find_excel_files(self, directory):
        listdir = os.listdir(directory)
        for i in listdir:
            path = os.path.join(directory, i)
            if os.path.isdir(path):
                if i != 'csv':
                    self.find_excel_files(path)
            elif os.path.isfile(path) and path.endswith('.xlsx'):
                self.excel_files.append(path.split("/")[-1])
        return self.excel_files

    def convert_files(self):
        excel_files = self.find_excel_files(self.excel_directory)
        for file in excel_files:
            config_file = file.replace('.xlsx', '_ConfigurationErrorsWarnings.csv')
            params_detail_file = file.replace('.xlsx', '_Parameter_Details.csv')
            if config_file not in self.existing_files:
                self.config_files.append(config_file)
                excel_file = pd.ExcelFile(f'{self.excel_directory}/{file}')
                if "ConfigurationErrorsWarnings" in excel_file.sheet_names:
                    try : 
                        df = pd.read_excel(excel_file, sheet_name='ConfigurationErrorsWarnings')
                        path = f'{self.csv_directory}/{config_file}'
                        df.to_csv(path,sep=';',index=False)
                        print('Sheet converted to csv', path)
                    except :
                        pass
            if params_detail_file not in self.existing_files:
                self.params_files.append(params_detail_file)
                excel_file = pd.ExcelFile(f'{self.excel_directory}/{file}')
                if "Parameter Details" in excel_file.sheet_names:
                    try :
                        df = pd.read_excel(excel_file, sheet_name='Parameter Details')
                        path = f'{self.csv_directory}/{params_detail_file}'
                        df.to_csv(path,sep=';',index=False)
                        print('Sheet converted to csv', path)
                    except :
                        pass


