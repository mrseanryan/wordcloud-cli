def read_lines_from_file(filepath):
    lines = []
    with open(filepath, encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    return lines
