from typing import Any

CANCEL: Any
NO_RETVAL: Any

def listen(target, identifier, fn, *args, **kw) -> None: ...
def listens_for(target, identifier, *args, **kw): ...
def remove(target, identifier, fn) -> None: ...
def contains(target, identifier, fn): ...