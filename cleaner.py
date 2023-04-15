import argparse
import logging
from pathlib import Path
from shutil import copyfile
from threading import Thread

parser = argparse.ArgumentParser(description='App for sorting folder by extensions')
parser.add_argument('-o', '--origin', required=True)
parser.add_argument('-r', '--result', default='sorted')
args = vars(parser.parse_args())
origin = args.get('origin')
result = args.get('result')

folders = []


def iterate_folder(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            iterate_folder(el)


def sort_file(path: Path):
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix
            new_path = result_folder / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as e:
                logging.error(e)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    origin_folder = Path(origin)
    result_folder = Path(result)
    folders.append(origin_folder)
    iterate_folder(origin_folder)
    print(folders)
    threads = []
    for folder in folders:
        th = Thread(target=sort_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print('You can delete the original folder')
