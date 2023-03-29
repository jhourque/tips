import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--arg1', dest='arg1',                                help='my arg1 param', required=True)
parser.add_argument('--arg2', dest='arg2', choices=['choice1','choice2'], help='my arg2 param (choice1 or choice2)')
parser.add_argument('--arg3', dest='arg3', default=os.getenv('ARG3'),     help='my arg3 param (get env var ARG3 if --arg3 not defined)')
# Python >= 3.9
#parser.add_argument('--arg4', dest='arg4', default=False, action=argparse.BooleanOptionalAction, help='my boolean arg True, False')
# Python < 3.9
parser.add_argument('--arg4', dest='arg4',    action='store_true')
#parser.add_argument('--no-arg4', dest='arg4', action='store_false')
parser.set_defaults(arg4=False)



args = parser.parse_args()

arg1 = args.arg1
arg2 = args.arg2
arg3 = args.arg3
arg4 = args.arg4

print(f"arg1 = {arg1}")
print(f"arg2 = {arg2}")
print(f"arg3 = {arg3}")
print(f"arg4 = {arg4}")
