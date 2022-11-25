from typing import Any, TypeVar

_T = TypeVar("_T")

__about__: str

def heapify(__heap: list[Any]) -> None: ...
def heappop(__heap: list[_T]) -> _T: ...
def heappush(__heap: list[_T], __item: _T) -> None: ...
def heappushpop(__heap: list[_T], __item: _T) -> _T: ...
def heapreplace(__heap: list[_T], __item: _T) -> _T: ...
