from Reader import *
from CsvConverter import *

reader = Reader()
reader.header_checker('dSST.csv')
reader.get_lines('dSST.csv', 2)
csvconverter = CsvConverter()
csvconverter.csv_to_json()
print(csvconverter.json)