import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    with open(file) as n:
        data_python = []
        lines = [line.rstrip() for line in n]
        headline = lines[0].split(',')
        for line in lines[1:]:
            data_python.append(dict(zip(headline, line.split(','))))
    return data_python


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
#Последняя строка