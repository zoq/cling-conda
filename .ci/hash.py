import os

with open('meta.yaml', 'r') as f:
    content = f.read()
    content = content.split('\n')
    hash = os.popen('sha256sum master.tar.gz').read().split(' ')[0].strip()

    update = ''
    for line in content:
        update += line + '\n'
        if '{% set sha256' in line:
            update += '{% set sha256 = "' + hash + '" %}\n'

update = update[0:-1]
with open('meta.yaml', 'w') as f:
    f.write(update)
