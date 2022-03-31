import json 
import linecache
import csv

class CsvToJson:

    def __init__(self, headers):
        self.headers = headers.strip().split(',')

    def csv_to_json(self, csv_rows):
        json_val = []
        for row in csv_rows:
            row = row.split(',')
            assert len(row) == len(self.headers), 'Length of data and headers should be the same'
            json_val.append(dict(zip(self.headers, [float(x) for x in row])))
        return json.dumps(json_val)

class Reader:
    def __init__(self, filename, stride_length):
        self.filename = filename
        self.stride_length = stride_length
        self.cursor = 2
        self.converter = CsvToJson(linecache.getline(self.filename, 1))
        self.observers = set()

# Add functionality to the Reader-class, so that the code below will work.
    def get_lines(self):
        reader = csv.reader(open(self.filename))
        no_lines = len(list(reader))
        while self.cursor < no_lines:
            rv = []
            for x in range(self.cursor, self.cursor+self.stride_length):
                rv.append(linecache.getline(self.filename, x).strip())
                # print(rv)
            self.cursor += self.stride_length
            yield rv
        # print (self.converter.csv_to_json(rv))

    def __iter__(self):
        return self.get_lines()


if __name__=='__main__':
    r = Reader('dSST.csv', 5)

    count = 1
    for i in r:
        count += 1
        print(len(i))
    print(count)