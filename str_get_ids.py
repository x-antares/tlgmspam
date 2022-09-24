import re
pattern = re.compile("user_id=([0-9]{8,10})")
result = ""
with open('user_ids.txt', 'w', encoding="utf-8") as file:
    for i, line in enumerate(open('read.txt')):
        for match in re.finditer(pattern, line):
            result = match.group(1)
            file.write(result + '\n')
print('Prepare you data....:)')            
            
