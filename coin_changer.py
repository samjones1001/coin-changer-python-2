import sys
import changer.changer as changer


def cli_main():
    if __invalid_args():
        raise Exception('Please provide a numeric argument')
    else:
        print(changer.calculate(int(sys.argv[1])))


def __invalid_args():
    return len(sys.argv) < 2 or sys.argv[1].isdigit() is False


if __name__ == '__main__': cli_main()