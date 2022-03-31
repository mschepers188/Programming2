import json 
import linecache

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

    def get_lines(self):
        rv = []
        for x in range(self.cursor, self.cursor+self.stride_length):
            rv.append(linecache.getline(self.filename, x).strip())
        self.cursor += self.stride_length
        print (self.converter.csv_to_json(rv))

    def add_observer(self, other):
        self.observers.add(other)

    def remove_observer(self, other):
        self.observers.remove(other)

    def notify_observers(self):
        # YOUR CODE HERE
        pass

    


if __name__=='__main__':
    r = Reader('dSST.csv', 5)
    r.get_lines()
    #r.get_lines()
    #r.get_lines()

    #csv_headers = "key1,key2"
    #csv_lines = ['1880,3.14','1881,2.87']
    #test = CsvToJson(csv_headers)
    #print (test.csv_to_json(csv_lines))