'''Secrets checking module for source code in python using regexes'''
import re
import sys

files = sys.argv[1:]
pattern = r'[a-z0-9_]*KEY=[a-zA-Z0-9]*'

secrets = []

for file in files:
    with open(file) as f:
        for lineno, line in enumerate(f.readlines()):
            if re.search(pattern, line):
                secrets.append((line, lineno, file))

if len(secrets) > 0:
    print('SECRETS FOUND: ')
    for secret in secrets:
        print(f'line {secret[1]} in {secret[2]}:\t{secret[0]}')

else:
    print('No secrets found in your python files.')
