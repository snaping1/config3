import argparse
from parser import parse_toml_with_comments
from converter import convert_to_custom_format_with_comments
from constants import resolve_constants, declare_constant

def main():
    parser = argparse.ArgumentParser(description="Convert TOML to a custom configuration language")
    parser.add_argument('output_file', type=str, help="Path to the output file")
    args = parser.parse_args()

    print("Enter TOML data (empty line to finish input):")
    input_text = ""
    while True:
        line = input()
        if line == "":
            break
        input_text += line + "\n"

    try:
        # Parse TOML with comments
        toml_data, constants = parse_toml_with_comments(input_text)

        # Declare constants
        for name, value in constants.items():
            declare_constant(name, value)

        # Resolve constants in the data
        resolved_data = resolve_constants(toml_data, constants)

        # Convert to custom format with comments
        converted_data = convert_to_custom_format_with_comments(resolved_data)

        # Write the result to the output file
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(converted_data)
        
        print(f"Configuration successfully converted and written to {args.output_file}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
