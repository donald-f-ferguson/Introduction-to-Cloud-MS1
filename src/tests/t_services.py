from src.middleware.context import Context
from src.resources.student_resource import StudentResource
from src.service_factory import ServiceFactory


def t1():
    df = ServiceFactory()
    sd = df.get_service("students")
    s = sd.get_by_id("dff9")
    print("t1: ", s)


if __name__ == "__main__":
    t1()

