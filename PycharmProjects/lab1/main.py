import argparse
import sys
import subprocess


def create_parser():
    _parser = argparse.ArgumentParser()
    subparsers = _parser.add_subparsers(dest='chose_task')
    subparsers.add_parser("task1")
    subparsers.add_parser("task3")
    subparsers.add_parser("task1add")
    task4_parser = subparsers.add_parser("task4")
    task4_parser.add_argument('-f', '--file', type=open)
    return _parser


if __name__ == '__main__':
    folder_path = '/home/eugene/PycharmProjects/lab1/'
    parser = create_parser()
    parameters = parser.parse_args(sys.argv[1:])
    if parameters.chose_task == "task1":
        subprocess.Popen([sys.executable, folder_path + 'task1.py'])
    elif parameters.chose_task == "task3":
        subprocess.Popen([sys.executable, folder_path + 'task3.py'])
    elif parameters.chose_task == "task1add":
        subprocess.Popen([sys.executable, folder_path + 'task1add.py'])
    elif parameters.chose_task == "task4":
        subprocess.Popen([sys.executable, folder_path + 'task4.py', folder_path + 'forTask3'])
    else:
        print('Error!')
