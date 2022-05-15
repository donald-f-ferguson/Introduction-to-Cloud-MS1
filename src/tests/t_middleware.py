from src.middleware.context import Context
from src.resources.student_data_service import StudentDataService

def t1():
    ctx = Context()
    res = ctx.get_context_variable("DB_CONNECT_INFO")
    print(res)


def t2():
    ctx = Context()
    c = {"DB_CONNECT_INFO": ctx.get_context_variable("DB_CONNECT_INFO")}
    sd = StudentDataService(c)
    result = sd.get_by_id("dff9")
    print("t2: result = ", result)


if __name__ == "__main__":
    t2()