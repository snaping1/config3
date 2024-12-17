from typing import Any, Dict

def process_value(value: Any) -> str:
    """
    Converts a value to a string representation in the custom configuration language.
    """
    if isinstance(value, str):
        return value
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, list):
        return f"[{', '.join(map(process_value, value))}]"
    elif isinstance(value, dict):
        return f"dict(\n{',\n'.join([f'{k} = {process_value(v)}' for k, v in value.items()])}\n)"
    return str(value)

def process_value_with_comments(value: Any) -> str:
    """
    Converts a value to a string representation, including comments.
    """
    result = process_value(value['value'])  # Get value part

    # Handling comments
    comment = value.get('comment', '')
    if comment:
        result = f"{result} : {comment}"

    return result

def resolve_constants_in_string(value: str, constants: Dict[str, str]) -> str:
    """
    Replaces all constants in a string (e.g., $app_name$) with their values from the constants dictionary.
    """
    # Loop through all constants and replace occurrences in the string
    for const_name, const_value in constants.items():
        value = value.replace(f"${const_name}$", const_value)
    return value

def convert_to_custom_format_with_comments(toml_data: Dict[str, Any]) -> str:
    """
    Converts TOML data to a custom format, including comments and constant resolution.
    """
    output = []
    constants = {}  # We should extract the constants part here

    for section, items in toml_data.items():
        if section == 'constants':
            # Extract constants, which will be used later for resolution
            constants = {item['key']: item['value'].replace('"','') for item in items}
            continue
        print(constants)
        output.append(f"{section} = dict(")
        for item in items:
            # Replace any constants in values
            item['value'] = resolve_constants_in_string(item['value'], constants)
            output.append(f"    {item['key']} = {process_value_with_comments(item)}")
        output.append(")")
    return "\n".join(output)

