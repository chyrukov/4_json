import json, os, sys, pprint


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    s = pprint.pprint(data[0],indent=2, depth=4, width=120)
    return s


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print("Отсутствует путь к файлу. Смотрите инструкцию по запуску программы в README.md")
        exit();
    alco_market = load_data(filepath)
    if alco_market is None:
        print("Неверный путь к файлу")
        exit();
    out_str = pretty_print_json(alco_market)
    print(out_str)
    pass

