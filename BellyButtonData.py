# Now that I have a database I can first make sure that the database is working. 
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, join, outerjoin, MetaData, Table

# If you make your database right you can rely on SQL alchemy's inspection tools within the ORM. 
class BellyButtonData():
    

    def __init__(self, connect_string):
        self.engine = create_engine(connect_string)
        self.connect_string = connect_string
        self.inspector = inspect(self.engine)
        self.tables = self.inspector.get_table_names()
        self.Base = automap_base()
        self.Base.prepare(self.engine,reflect=True)
        self.Subjects = self.Base.classes['subjects']
        self.meta = MetaData
        self.TestResults = Table('test_results_view', self.meta,
                                    autoload_with=self.engine)

    def display_db_info(self):
        inspector = inspect(self.engine)
        tables = self.inspector.get_table_names()
        for table in self.tables:
            print("\n")
            print('-' * 12)
            print(f"table '{table}' has the following columns:'")
            print('-' * 12)
            for column in self.inspector.get_columns(table):
                print(f"name: {column['name']}, column type: {column['type']}")

if __name__ == '__main':
    info = BellyButtonData("sqlite://bellyButtons.db")
    info.display_db_info()
    print("\nSubject IDs\n")

