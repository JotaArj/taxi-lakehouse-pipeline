from typing import Dict, List, Type
from src.domain.enum.enums import CodeDescriptionEnum

import pandas as pd


class LookupDataframe:

    @staticmethod
    def enum_to_dataframe(enum_cls: Type[CodeDescriptionEnum]):
        dict =[{"code": item.code, "description": item.description} for item in enum_cls]
        return pd.DataFrame.from_dict(dict)
