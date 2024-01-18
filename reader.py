import json

class JSONFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_lines(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield json.loads(line)


def main():
    file_path = 'input.json'
    json_reader = JSONFileReader(file_path)

    for json_line in json_reader.read_lines():
        print(json_line)

if __name__ == "__main__":
    main()