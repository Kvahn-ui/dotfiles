from __future__ import annotations
import sys
from typing import Generic, overload, Union, Protocol, TypeVar
from _typing import Timedelta, Timestamp
import datetime

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

OrderableScalar = TypeVar("OrderableScalar", int, float)
OrderableTimes = TypeVar("OrderableTimes", datetime.date, datetime.datetime, datetime.timedelta, Timestamp, Timedelta)
Orderable = TypeVar("Orderable", int, float, datetime.date, datetime.datetime, datetime.timedelta, Timestamp, Timedelta)

class IntervalMixinProtocol(Protocol): ...

class IntervalMixin:
    @property
    def closed_left(self: IntervalMixinProtocol) -> bool: ...
    @property
    def closed_right(self: IntervalMixinProtocol) -> bool: ...
    @property
    def open_left(self: IntervalMixinProtocol) -> bool: ...
    @property
    def open_right(self: IntervalMixinProtocol) -> bool: ...
    @property
    def mid(self: IntervalMixinProtocol) -> float: ...
    @property
    def is_empty(self: IntervalMixinProtocol) -> bool: ...

class Interval(IntervalMixin, Generic[Orderable]):
    @overload
    def left(self: Interval[OrderableScalar]) -> OrderableScalar: ...
    @overload
    def left(self: Interval[OrderableTimes]) -> OrderableTimes: ...
    @property
    @overload
    def left(self: Interval[Orderable]) -> Orderable: ...
    @overload
    def right(self: Interval[OrderableScalar]) -> OrderableScalar: ...
    @overload
    def right(self: Interval[OrderableTimes]) -> OrderableTimes: ...
    @property
    @overload
    def right(self: Interval[Orderable]) -> Orderable: ...
    @property
    def closed(self) -> str: ...
    def __init__(
        self,
        left: Orderable,
        right: Orderable,
        closed: Union[str, Literal["left", "right", "both", "neither"]] = ...,
    ) -> None: ...
    @overload
    def length(self: Interval[OrderableScalar]) -> float: ...
    @overload
    def length(self: Interval[OrderableTimes]) -> Timedelta: ...
    @property
    @overload
    def length(self: Interval[Orderable]) -> Orderable: ...
    def __hash__(self) -> int: ...
    def __contains__(self, key: Orderable) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __add__(self: Interval[Orderable], y: float) -> Interval[Orderable]: ...
    def __sub__(self: Interval[Orderable], y: float) -> Interval[Orderable]: ...
    def __mul__(self: Interval[Orderable], y: float) -> Interval[Orderable]: ...
    def __truediv__(self: Interval[Orderable], y: float) -> Interval[Orderable]: ...
    def __floordiv__(self: Interval[Orderable], y: float) -> Interval[Orderable]: ...
    def overlaps(self: Interval[Orderable], other: Interval[Orderable]) -> bool: ...
