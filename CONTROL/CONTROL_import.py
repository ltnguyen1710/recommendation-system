from pathlib import Path
import pandas as pd

# ------------------------Import Package DATABASE------------------------
import sys
sys.path.insert(0, 'DATABASE')
from DTB_dataset import DTB_dataset

class CONTROL_import:
    def __init__(self):
        self.dtb = DTB_dataset()
        pass

    def add_data(self,tb_name,df):     
        # Khởi tạo bảng
        table_name = tb_name
        list_col = list(df.columns)
        state_create_table = self.dtb.create_table(table_name,list_col)
        
        if(state_create_table==True):    
            # Update data vào bảng
            state_update_table = self.dtb.update_table(table_name,df)
            if(state_update_table==True):
                self.alert = "Your file has been imported successfully!!!"
            else:
                self.alert = "ERROR: \n"+state_update_table
        else:
            self.alert = "ERROR: \n"+state_create_table
        
    def show_alert(self):
        return self.alert
        
        

