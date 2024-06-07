from configparser import ConfigParser

import psycopg2


class Connection: 
    def __init__(self):
        parser=ConfigParser()
        parser.read("./DB_Service/db.ini")
        self.config={}
        if parser.has_section('postgresql'):
            params=parser.items('postgresql')
            for param in params:
                self.config[param[0]]=param[1]
        else:
            raise Exception("Section {0} not found in the {1} file".format('postgresql','db.ini'))
        
    def getConfig(self):
        return self.config

    def connect(self):
        print("Connect to Server")
        try:
            with psycopg2.connect(**self.config) as conn:
                print("Successfull connected")
                return conn
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)