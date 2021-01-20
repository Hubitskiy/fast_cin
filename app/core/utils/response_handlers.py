from typing import List, Dict


def prepare_list_response(query_list: List, limit: int, offset: int) -> Dict:

    list_obj = [obj.__dict__ for obj in query_list]

    return {
        "limit": limit,
        "offset": offset,
        "result": list_obj
    }


def prepare_object_to_response(obj):
    return obj.__dict__
