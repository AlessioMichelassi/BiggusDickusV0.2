def ifNotInCode(_code: list, _sentence: str):
    if _sentence not in _code:
        _code.append(_sentence)
        return True
    return False


def createDirectory(mainPath: str, softwareTitle: str):
    from pathlib import Path
    Path(F"{mainPath}{softwareTitle}/GUI").mkdir(parents=True, exist_ok=True)
    _mainDirectory = F"{mainPath}{softwareTitle}/"


class utility:

    def __init__(self):
        pass
