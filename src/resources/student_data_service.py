from src.resources.rdb_service_base import RDBServiceBase


class StudentDataService(RDBServiceBase):

    def __init__(self, context):
        super().__init__(context)

    def get_by_id(self, id):

        # DFF TODO I should be converting some of the exceptions to better results

        conn = self.get_connection()
        cursor = conn.cursor()
        uni = id

        # DFF TODO The name of the table should also be an environment variable.
        result = cursor.execute("select * from students where uni=%s", args=(uni))
        res = cursor.fetchall()

        final_result = None

        if res and len(res) == 1:
            final_result = res[0]

        return final_result