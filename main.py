from tistore import file
from tistore.file import MultCsv
import asyncio

def main():
    files = ['testcases/62000006.csv', 'testcases/62000007.csv']
    csvs = MultCsv(files)
    asyncio.run(csvs.call())

if __name__ == '__main__':
    main()
