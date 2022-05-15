"""
Typically, classes like this are not in the microservice code. They come from
some framework that the project uses through an installed package.
"""

class ApplicationResourceBase:

    def __init__(self, context):
        self._context = context