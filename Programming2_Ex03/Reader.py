# from unicodedata import name
import linecache2

class Reader:
    def __init__(self) -> None:
        self.head = None
        self.five_lines = []

    def header_checker(self, file):
        self.head = (linecache2.getline(file, 1)).strip().split(',')

    def get_lines(self, file, linenum):
        for n in range(linenum, linenum+5):
            self.five_lines.append(linecache2.getline(file, n).strip())


if __name__=='__main__':
    reader = Reader()
    reader.header_checker('dSST.csv')
    reader.get_lines('dSST.csv', 2)
    print(reader.head)
    print(reader.five_lines)