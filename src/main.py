import json
from last_operations_func import output_last_operations

with open('operations.json', encoding='utf-8') as file:
    data = json.load(file)

sorted_data = sorted(data, key=lambda x: x.get("date", ""), reverse=True)

output_last_operations(sorted_data)

