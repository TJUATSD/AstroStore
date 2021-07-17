from tistore.file import MultCsv
from tistore.utils import parse_config
import asyncio

def main():
    # files = ['testcases/62000006.csv', 'testcases/62000007.csv']
    # csvs = MultCsv(files)
    # asyncio.run(csvs.call())
    filename = "tistore/config.json"
    retional_config, no_retional_config = parse_config(filename)
    print(retional_config)
    print(no_retional_config)

if __name__ == '__main__':
    main()
