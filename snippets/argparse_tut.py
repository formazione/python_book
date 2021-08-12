import argparse

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument(
	dest='argument1',
	help="This is the first argument")

# Parse and print the results
args = parser.parse_args()
print(args.argument1)