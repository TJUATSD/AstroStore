from astrostore.manager import Manager
# from tistore.utils import parse_config
import asyncio

def main():
    filename = "./testcases/62000006.csv"
    manager = Manager()
    manager.parse_csv(filename)

if __name__ == '__main__':
    main()
