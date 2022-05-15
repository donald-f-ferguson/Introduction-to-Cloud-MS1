import os
import json

class Context:

    def __init__(self):
        pass

    def get_context_variable(self, variable_name):

        result = None
        json_result = None

        try:
            result = os.environ.get(variable_name)
            json_result = json.loads(result)
        except (json.decoder.JSONDecodeError, TypeError) as je:
            pass

        if json_result:
            result = json_result

        return result
