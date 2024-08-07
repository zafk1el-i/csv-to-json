import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    """
    Преобразует CSV-файл в JSON.
    """
    # Чтение CSV-файла и преобразование его в список словарей
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
        
    # Запись данных в JSON-файл
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


# Чтобы файл не запускали как модуль
if __name__ == "__main__":
    csv_file = 'input.csv'  
    json_file = 'output.json'  
    
    csv_to_json(csv_file, json_file)
    print(f"CSV файл '{csv_file}' был преобразован в JSON файл '{json_file}'.")