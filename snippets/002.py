import argparse

# Create the parser and add arguments
parser = argparse.ArgumentParser()

# def single_word(string):
#     # Check input does not contain spaces
#     return string

parser.add_argument('argument1',
	# type=single_word
	)
args = parser.parse_args()
print(args.argument1*2)