#!/usr/bin/python

# subnet_expand1.py

from netaddr import IPNetwork
import argparse
import sys

parser =  argparse.ArgumentParser()
parser.add_argument("-s", "--subnet", help="pass in a subnet")
parser.add_argument("-if", "--input_file", help="accept file input")
parser.add_argument("-of", "--output_file", help="pass results to output file")
parser.add_argument("-o", "--omit_ids", help="omit broadcast and subnet IDs", action='store_true')
parser.add_argument("-d", "--debug", help="debug mode", action='store_true')
args = parser.parse_args()

if args.debug:
    print("\narguments:\n")
    print("\tinput file:\t" + str(args.input_file))
    print("\toutput file:\t" + str(args.output_file))
    print("\tomit ids:\t" + str(args.omit_ids))
    print("\tsubnet:\t\t" + str(args.subnet))
    print("\tdebug:\t\t" + str(args.debug))
else:
    []

def example():
    print('')
    print('example 1 (single subnet):')
    print('')
    print('\tpython subnet_expand.py -s 192.168.1.0/24')
    print('')
    print('example 2 (input file):')
    print('')
    print('\tpython subnet_expand.py -if <file containing valid subnets>')
    print('')
    print('example 3:(input file and output file)')
    print('')
    print('\tpython subnet_expand.py -if <file containing valid subnets> -of <output file>')
    print('')
    print('NOTE: \tinput file must contain a single valid subnet per line!')
    print('')

def expand(subnet):
    out_list = []
    for ip in IPNetwork(subnet):
        out_list.append(ip)
    if args.debug:
        print(out_list)
    if args.omit_ids:
        del out_list[0]
        del out_list[-1]
        if args.debug:
            print('')
            print(out_list)
            print('')
        return(out_list)
    else:
        return(out_list)

def expand_with_file_input(input_file):
    in_file = open(input_file, 'r')
    #with open(input_file, 'r') as file:
    lines = in_file.readlines()
    for line in lines:
        if args.debug:
            print('')
            print(line)
            print('')
        else:
            []
        print('')
        print("subnet:\t" + str(line))
        #print('')
        expanded = expand(line)
        for ip in expanded:
            print(ip)
    print('')
    
def expand_with_file_input_and_output(input_file, output_file):
    in_file = open(input_file, 'r')
    out_file = open(output_file, 'w')
    #with open(input_file, 'r') as file:
    lines = in_file.readlines()
    for line in lines:
        if args.debug:
            print('')
            print(line)
            print('')
        else:
            []
        print('')
        print("subnet:\t" + str(line))
        #print('')
        expanded = expand(line)
        for ip in expanded:
            print(ip)
            out_file.write(str(ip) + '\n')
    in_file.close()
    out_file.close()
    print('')

if args.input_file and args.output_file:
    expand_with_file_input_and_output(args.input_file, args.output_file)

elif args.input_file:
    expand_with_file_input(str(args.input_file))

elif args.subnet:
    print('')
    print("subnet:\t" + args.subnet)
    #print('')
    expanded = (expand(args.subnet))
    for ip in expanded:
        print(ip)
    print('')

else:
    print('')
    print("ERROR: \trequires at least one subnet as input.")
    example()
    print("no valid input received. try again!")
    print('')