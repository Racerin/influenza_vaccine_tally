import os
import logging
from dataclasses import dataclass, field

import dotenv
import pandas as pd

from params import *

dotenv.load_dotenv()

def get_default_excel_file():
    """ Reads current working directory and returns the most preferred excel sheet. """
    # TODO
    pass

@dataclass
class EntireProgram:
    excel_file_path : str = DEFAULT_EXCEL_FILE_PATH
    # df_excel_file : pd.ExcelFile = 
    df_main : pd.DataFrame = None

    def __post_init__(self):
        self.read_environment_variables()
        self.read_excel_file()
    
    def read_excel_file(self) -> None:
        """ Reads 'str' file path and creates panda DataFrame from file path """
        assert(os.path.exists(self.excel_file_path), "Main excel file '{}' doesn't exist.".format(self.excel_file_path))
        self.df_main = pd.read_excel(self.excel_file_path)

    def get_sheets_name(self) -> list[str]:
        """ Returns a list of 'str' Excel sheet names. """
        return pd.ExcelFile(self.excel_file_path).sheet_names

    def read_environment_variables(self) -> None:
        """ Read each environmental variable and apply values to 'EntireProgram' properties. """
        self.excel_file_path = os.environ.get('excel_file_path', self.excel_file_path)
        if self.excel_file_path == DEFAULT_EXCEL_FILE_PATH: logging.info("No environmental variable was found for the property 'excel_file_path' in class 'EntireProgram'.") 
