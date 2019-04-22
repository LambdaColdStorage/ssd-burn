import argparse
import re

def parse(file_name, key_word, num_iter):
	r = []
	with open(file_name) as search:
	    for line in search:
	        if re.search(key_word, line):
	        	l = line.split()
	        	r.append(float(l[2][1:-6]))
	return r

def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('ssd_name', type=str,
	                    help='name of the ssd')
	parser.add_argument('num_iter', type=int,
	                    help='number of iterations')

	args = parser.parse_args()
	
	ssd_name = args.ssd_name
	num_iter = args.num_iter

	# seq write
	r = parse('data/' + args.ssd_name + '_seq_w.txt', "WRITE:", 3)
	print("seq write: ")
	print(r)

	# seq read
	r = parse('data/' + args.ssd_name + '_seq_r.txt', "READ:", 3)
	print("seq read: ")
	print(r)

	# random write
	r = parse('data/' + args.ssd_name + '_rand_w.txt', "WRITE:", 3)
	print("random write: ")
	print(r)

	# random read
	r = parse('data/' + args.ssd_name + '_rand_r.txt', "READ:", 3)
	print("random read: ")
	print(r)

if __name__ == '__main__':
	main()