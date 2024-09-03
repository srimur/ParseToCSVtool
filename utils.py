import json
import csv
import io

def convert_to_csv(response_text, file_path):
    if "|" in response_text:
        delimiter = "|"
    elif "," in response_text:
        delimiter = ","
    else:
        raise ValueError("Unsupported delimiter. Only '|' and ',' are supported.")
    
    input_stream = io.StringIO(response_text)
    reader = csv.reader(input_stream, delimiter=delimiter, quotechar='"')
    
    headers = next(reader)
    data = [row for row in reader]

    with open(file_path, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)

def convert_to_json(response_text, file_path):
    if "|" in response_text:
        delimiter = "|"
    elif "," in response_text:
        delimiter = ","
    else:
        raise ValueError("Unsupported delimiter. Only '|' and ',' are supported.")
    
    input_stream = io.StringIO(response_text)
    reader = csv.reader(input_stream, delimiter=delimiter, quotechar='"')
    
    headers = next(reader)
    data = [dict(zip(headers, row)) for row in reader]

    with open(file_path, mode="w") as jsonfile:
        json.dump(data, jsonfile, indent=4)
