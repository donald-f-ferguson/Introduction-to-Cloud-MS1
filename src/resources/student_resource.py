from src.resources.application_resource_base import ApplicationResourceBase


class StudentResource(ApplicationResourceBase):

    def __init__(self, context):
        super().__init__(context)
        self.data_service = context.get("data_service")

    def get_by_id(self, uni):
        result = self.data_service.get_by_id(uni)
        return result

