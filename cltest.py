import sys

args = sys.argv
first_num = float(args[1])
second_num = float(args[2])

product = first_num * second_num
print(f'The product of {args[1]} times {args[2]} equals {product}')

