from typing import overload
import re

class ExList(list):
    def __init__(self, iterable=None) -> None:
        if iterable is not None:
            super().__init__(iterable)
        else:
            super().__init__()
    def filter_list(self,attr,regex):
        regex = re.compile(regex)
        return ExList(filter(lambda x: regex.match(getattr(x,attr)),self))

    def mapped_list(self, attr):
        return ExList(map(lambda x: getattr(x,attr), self))

    def ex_count(self):
        set_list = list(set(self))
        return ExList([(i, self.count(i)) for i in set_list])

    def sorted_list(self, lamb):
        self.sort(key = lamb)
        return self
