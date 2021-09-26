import sys
sys.path.append("..")
from astrostore.parser.csv import CSVParser


def main():
    filename = "../testdata/62000006.csv"
    parse_csv = CSVParser(filename)
    parse_csv.parse()
    parse_csv.debug()

if __name__ == '__main__':
    main()