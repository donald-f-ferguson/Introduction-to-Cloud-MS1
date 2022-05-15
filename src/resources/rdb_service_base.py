"""
Typically, classes like this are not in the microservice code. They come from
some framework that the project uses through an installed package.
"""
from src.resources.data_service_base import DataServiceBase
import pymysql


class RDBServiceBase(DataServiceBase):

    def __init__(self, context):
        super().__init__(context)
        self.db_connect_info = context.get("DB_CONNECT_INFO")
        self.db_connect_info["cursorclass"] = pymysql.cursors.DictCursor
        self.db_connect_info["autocommit"] = True

    def get_connection(self):
        result = pymysql.connect(**self.db_connect_info)
        return result

    def close_connection(self, connection):
        connection.close()

    def get_by_id(self, id):
        raise NotImplemented()