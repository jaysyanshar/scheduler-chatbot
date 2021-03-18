from num2words import num2words

def generate_numwords(start, end):
  numwords = []
  for i in range(start, end):
    numwords.append(num2words(i))
  return numwords

import json

print(json.dumps(generate_numwords(0, 60), indent=2))
