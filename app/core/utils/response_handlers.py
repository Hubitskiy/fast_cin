from typing import List, Dict


def prepare_list_response(query_list: List) -> Dict:

    list_obj = [obj.__dict__ for obj in query_list]

    return {
        "result": list_obj
    }
