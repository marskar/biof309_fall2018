from typing import Iterable


def pydy(names: Iterable[str]) -> None:
    for name in names:
        if pd:
            setattr(pd.DataFrame, name, eval(name))
        elif pandas:
            setattr(pandas.DataFrame, name, eval(name))
        elif DataFrame:
            setattr(DataFrame, name, eval(name))
        del globals()[name]

