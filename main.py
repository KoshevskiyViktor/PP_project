def main():
    file_path = 'input.json'
    json_reader = JSONFileReader(file_path)

    for json_line in json_reader.read_lines():
        print(json_line)
        
if __name__ == "__main__":
    main()