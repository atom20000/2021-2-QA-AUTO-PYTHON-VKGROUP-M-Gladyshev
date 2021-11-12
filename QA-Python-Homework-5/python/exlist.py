from typing import overload
import re

class ExList(list):
    #@overload
    def __init__(self) -> None:
        super().__init__()
    #@overload
    def __init__(self, iterable) -> None:
        super().__init__(iterable)

    def filter_list(self,attr,regex):
        return ExList(filter(lambda x: re.match(rf'{regex}',getattr(x,attr)),self))

    def mapped_list(self, attr):
        return ExList(map(lambda x: getattr(x,attr), self))

    def ex_count(self):
        set_list = list(set(self))
        return ExList([(i, self.count(i)) for i in set_list])

    def sorted_list(self, lamb):
        self.sort(key = lamb)
        return self
