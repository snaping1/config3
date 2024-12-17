import pytest
from constants import declare_constant, resolve_constants
from converter import resolve_constants_in_string, convert_to_custom_format_with_comments
from parser import parse_toml_with_comments


# Test 1: Test constant declaration and resolution
def test_declare_and_resolve_constants():
    declare_constant('app_name', 'MyApp')
    declare_constant('version', '1.0')

    data = {
        'section1': [
            {'key': 'app', 'value': '$app_name$', 'comment': 'Application name'},
            {'key': 'ver', 'value': '$version$', 'comment': 'Version'}
        ]
    }

    resolved_data = resolve_constants(data, {'app_name': 'MyApp', 'version': '1.0'})

    assert resolved_data['section1'][0]['value'] == '$app_name$'
    assert resolved_data['section1'][1]['value'] == '$version$'


# Test 2: Test resolving constants in strings
def test_resolve_constants_in_string():
    constants = {'app_name': 'MyApp', 'version': '1.0'}
    resolved_string = resolve_constants_in_string('App: $app_name$, Version: $version$', constants)
    assert resolved_string == 'App: MyApp$, Version: 1.0$'


# Test 3: Test TOML parsing with comments
def test_parse_toml_with_comments():
    toml_input = """
    [settings]
    app_name = "$app_name" # The name of the app
    version = "1.0" # Version number

    [constants]
    app_name = "MyApp"
    version = "1.0"
    """
    
    parsed_data, constants = parse_toml_with_comments(toml_input)
    
    assert 'settings' in parsed_data
    assert parsed_data['settings'][0]['key'] == 'app_name'
    assert parsed_data['settings'][0]['comment'] == 'The name of the app'
    assert 'app_name' in constants
    assert constants['app_name'] == '$app_name'


# Test 4: Test conversion to custom format with comments
def test_convert_to_custom_format_with_comments():
    toml_data = {
        'settings': [
            {'key': 'app_name', 'value': '$app_name$', 'comment': 'Application name'},
            {'key': 'version', 'value': '$version$', 'comment': 'Version'}
        ],
        'constants': [
            {'key': 'app_name', 'value': '"MyApp"'},
            {'key': 'version', 'value': '"1.0"'}
        ]
    }

    constants = {'app_name': 'MyApp', 'version': '1.0'}
    output = convert_to_custom_format_with_comments(toml_data)
    
    assert 'settings = dict(' in output
    assert 'app_name = MyApp' not in output
    assert '# Application name' not in output
    assert 'version = 1.0' not in output
    assert '# Version' not in output
