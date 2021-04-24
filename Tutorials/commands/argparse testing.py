import argparse

parser = argparse.ArgumentParser(description="I don't know what to put here")
parser.add_argument("-p","--print", type=str,metavar="", required=True, help="prints something")
args = parser.parse_args()

def test(message):
    print(message)

if __name__ == "__main__":
    test(args.print)