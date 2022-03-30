from Reader import *

class CsvConverter:
    def __init__(self) -> None:
        self.head = reader.head
        self.five = reader.five_lines
        self.json = []

    def csv_to_json(self):
        for line in self.five:
            self.json.append(dict(zip(self.head, line.split(','))))


if __name__=='__main__':
    reader = Reader()
    reader.header_checker('dSST.csv')
    reader.get_lines('dSST.csv', 2)
    csvconverter = CsvConverter()
    csvconverter.csv_to_json()
    print(csvconverter.json)