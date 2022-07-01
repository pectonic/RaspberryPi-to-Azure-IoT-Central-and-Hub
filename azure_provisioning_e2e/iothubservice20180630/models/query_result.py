# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QueryResult(Model):
    """The query result.

    :param type: The query result type. Possible values include: 'unknown',
     'twin', 'deviceJob', 'jobResponse', 'raw', 'enrollment',
     'enrollmentGroup', 'deviceRegistration'
    :type type: str or ~service20180630.models.enum
    :param items: The query result items, as a collection.
    :type items: list[object]
    :param continuation_token: Request continuation token.
    :type continuation_token: str
    """

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "items": {"key": "items", "type": "[object]"},
        "continuation_token": {"key": "continuationToken", "type": "str"},
    }

    def __init__(self, type=None, items=None, continuation_token=None):
        super(QueryResult, self).__init__()
        self.type = type
        self.items = items
        self.continuation_token = continuation_token
