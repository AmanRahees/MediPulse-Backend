import re

def parse_key(key):
    match = re.match(r'^\w+\[(\d+)\]\[(\w+)\]$', key)
    if match:
        index = int(match.group(1))
        subfield_name = match.group(2)
        return index, subfield_name
    return None, None

def format_nested_data(data, field_prefix):
    nested_data = []
    for key, value in data.items():
        if key.startswith(field_prefix):
            index, subfield_name = parse_key(key)
            while len(nested_data) <= index:
                nested_data.append({})
            if subfield_name:
                try:
                    if value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    if value == "":
                        value = None
                except:
                    pass
                nested_data[index][subfield_name] = value
    return nested_data
