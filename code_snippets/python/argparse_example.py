import argparse

parser = argparse.ArgumentParser()

# Add optional argument
parser.add_argument(
    "-p",
    "--Parameter",
    default=4,  # default value
    type=int,  # data type
    help="Choose the parameter",
)  # description

# Read arguments on the command line
args = parser.parse_args()
print(f'Your chosen parameter is {args.Parameter}')

"""On your terminal
$ python argparse_example.py
Your chosen parameter is 4

$ python argparse_example.py -p 5
Your chosen parameter is 5
"""