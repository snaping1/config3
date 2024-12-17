from typing import Any, Dict

constants = {}

def declare_constant(name: str, value: str) -> None:
    """
    Declare a constant during the translation stage.
    """
    constants[name] = value

def resolve_constants(data: Any, constants: Dict[str, str]) -> Any:
    """
    Recursively replace references to constants in a data structure.
    """
    if isinstance(data, dict):
        return {k: resolve_constants(v, constants) for k, v in data.items()}
    elif isinstance(data, list):
        return [resolve_constants(item, constants) for item in data]
    elif isinstance(data, str):
        return resolve_constants_in_string(data)
    return data

def resolve_constants_in_string(value: str) -> str:
    """
    Replaces all constants in a string (e.g., $app_name$) with their values from the constants dictionary.
    """
    for const_name, const_value in constants.items():
        value = value.replace(f"${{{const_name}}}", const_value)
    return value
