import json
from typing import Union, List, AnyStr, Iterable


def load_json_from_file(path: str) -> Union[dict, list, str, int]:
    """Load JSON from specified path"""
    with open(path, 'r', encoding='utf-8') as infile:
        return json.load(infile)


def save_text_to_file(path: str, content: Union[AnyStr, Iterable[AnyStr]], overwrite: bool = True):
    """Save content as text to specified path"""
    with open(file=path,
              mode='w' if overwrite else 'a',
              encoding='utf-8') as the_file:
        if isinstance(content, str):
            the_file.write(content)
        else:
            the_file.writelines(content)


# Using List for the content type as json doesn't like dumping other collections.
def save_as_json_to_file(path: str,
                         content: Union[dict, str, List[AnyStr], List[dict]],
                         overwrite: bool = True,
                         indent: int = 2):
    """Save content by dumping as json and saving to specified path"""
    with open(file=path, mode='w' if overwrite else 'a', encoding='utf8') as json_file:
        json.dump(content, json_file, ensure_ascii=False, default=str, indent=indent)
