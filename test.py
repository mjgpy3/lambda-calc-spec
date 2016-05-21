#!/usr/bin/env python

from sys import argv

import json
import os
import os.path

if len(argv) < 2:
  print "Usage: ./test.sh path/to/details.json"
  exit()

details_file = argv[1]

with open(details_file, 'r') as f:
  json_details = json.loads(f.read())

with open('specs.json', 'r') as f:
  specs = json.loads(f.read())[json_details['specVersion']]['specs']

main_file = os.path.join(os.path.dirname(details_file), json_details['main'])
exe = json_details['exe']

os.chdir(os.path.dirname(main_file))

for spec in specs:
  file = os.path.basename(main_file)
  result = os.popen(exe + ' ' + file + ' "' + spec['expect'] + '"').read().strip()

  if result != spec['toEvaluateTo']:
    print "Fail: ", result, '!=', spec['toEvaluateTo'], '(' + spec['because'] + ')'
