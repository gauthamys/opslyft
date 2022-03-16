'''Secrets checking module for source code in python using regexes'''
import re
import sys

files = sys.argv[1:]
PATTERN = r'[a-zA-Z0-9_]*KEY=[a-zA-Z0-9]*'

secrets = []

for file in files:
    if sys.argv[0] not in file:
        with open(file, encoding='utf-8') as f:
            for lineno, line in enumerate(f.readlines()):
                if re.search(PATTERN, line):
                    secrets.append((line, lineno, file))

if len(secrets) > 0:
    print('SECRETS FOUND: ')
    for secret in secrets:
        print(f'line {secret[1]} in {secret[2]}:\t{secret[0]}')
    sys.exit(20)

else:
    print('No secrets found in your python files.')
