import sys
import changer.changer as changer


def main():
    if len(sys.argv) < 2 or sys.argv[1].isdigit() is False:
        print("Please provide a numeric argument")
    else:
        print(changer.calculate(int(sys.argv[1])))


if __name__ == '__main__': main()