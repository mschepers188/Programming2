import linecache2

class Reader:
    def __init__(self) -> None:
        self.head = None
        self.five_lines = []
        self.jason = []

    def header_checker(self, file):
        self.head = (linecache2.getline(file, 1)).strip().split(',')

    def csv_to_json(self):
        for line in self.five_lines:
            self.json.append(dict(zip(self.head, line.split(','))))
        return self.json
    
    def get_lines(self, file, linenum):
        linenum=2
        for n in range(linenum, linenum+5):
            self.five_lines.append(linecache2.getline(file, n).strip())
        return self.five_lines

if __name__=='__main__':
    reader = Reader()
    reader.header_checker('dSST.csv')
    test = reader.get_lines('dSST.csv', 2)
    print(reader.csv_to_json())