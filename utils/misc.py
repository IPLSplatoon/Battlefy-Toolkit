import re
from typing import Union


def is_valid_battlefy_id(battlefy_id: str) -> bool:
    """
    Verify a str is a Battlefy Id (20 <= length < 30) and is alphanumeric.
    :param battlefy_id:
    :return: Validity true/false
    """
    return 20 <= len(battlefy_id) < 30 and re.match("^[A-Fa-f0-9]*$", battlefy_id)


def assert_is_dict_recursive(val: Union[dict, list, str, int], comment: str = ''):
    """
    Assert if a dictionary only contains basic serializable values (dict, list, str, int) and recurse dicts and lists.
    :param val: The current node
    :param comment: Comment for this node, e.g. its current position.
    :raises AssertionError: If this test fails.
    """
    if isinstance(val, str) or isinstance(val, int):
        # This is good.
        pass
    elif isinstance(val, dict):
        for element in val:
            assert_is_dict_recursive(val[element], f'{comment}/{element}')
    elif isinstance(val, list):
        for element in val:
            assert_is_dict_recursive(element, f'{comment}/values')
    else:
        assert False, f"This val is not a str/int, dict, or list: {comment} is {val=}"
