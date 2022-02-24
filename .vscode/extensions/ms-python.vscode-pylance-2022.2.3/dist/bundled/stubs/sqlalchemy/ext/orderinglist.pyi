from typing import Any, Optional

def ordering_list(attr, count_from: Optional[Any] = ..., **kw): ...

class OrderingList(list):
    ordering_attr: str = ...
    ordering_func: Any = ...
    reorder_on_append: Any = ...
    def __init__(self, ordering_attr: Optional[str] = ..., ordering_func: Optional[Any] = ...,
                 reorder_on_append: bool = ...) -> None: ...
    def reorder(self): ...
    def append(self, entity): ...
    def insert(self, index, entity): ...
    def remove(self, entity): ...
    def __setitem__(self, index, entity): ...
    def __delitem__(self, index): ...
    def __setslice__(self, start, end, values): ...
    def __delslice__(self, start, end): ...
    def __reduce__(self): ...