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

    def _get_where_clause_args(self, template):

        w_clause = ""
        args = None

        if template:

            terms = []
            args = []

            for k,v in template.items():

                terms.append(k + "=%s")
                args.append(v)

            w_clause = " where " + " and ".join(terms)

        return w_clause, args

    def _run_q(self, sql, args):

        conn = self.get_connection()
        cursor = conn.cursor()

        print("sql = ", cursor.mogrify(sql, args))

    def find_by_template(self, collection, template=None, fields=None, limit=None, offset=None, order_by=None):

        sql = "select {field_list} from " + collection

        if fields:
            field_list = ",".join(fields)
        else:
            fields = "*"

        sql1 = sql.format(field_list=field_list)
        wc = self._get_where_clause_args(template)
        sql2 = sql1 + wc

