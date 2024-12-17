import re
from typing import Any, Dict

def parse_toml_with_comments(input_text: str) -> Dict[str, Any]:
    """
    Custom TOML parser to capture comments along with values.
    """
    lines = input_text.splitlines()
    parsed_data = {}
    current_section = None
    constants = {}

    for line in lines:
        # Skip empty lines
        line = line.strip()
        if not line:
            continue
        
        # Handle section headers
        section_match = re.match(r'^\[([^\]]+)\]$', line)
        if section_match:
            current_section = section_match.group(1).strip()
            parsed_data[current_section] = []
            continue

        # Handle key-value pairs
        key_value_match = re.match(r'([^#=]+)\s*=\s*(.*?)(\s*#\s*(.*))?$', line)
        if key_value_match:
            key = key_value_match.group(1).strip()
            value = key_value_match.group(2).strip()

            comment = key_value_match.group(4)  # Comment part after `#`

            # Detect if it's a constant (to be replaced later)
            if '$' in value:
                constants[key] = value.strip('"')
            
            parsed_data[current_section].append({
                'key': key,
                'value': value,
                'comment': comment.strip() if comment else None
            })
        else:
            continue  # Skip lines that do not match the expected pattern
    
    return parsed_data, constants
