import sys
import changer.changer as changer


def main():
    if len(sys.argv) < 2:
        print("Please provide an argument")
    else:
        print(changer.calculate(int(sys.argv[1])))


if __name__ == '__main__': main()