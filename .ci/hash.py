import os

with open('meta.yaml', 'r') as f:
    content = f.read()
    content = content.split('\n')
    hash = os.popen('sha256sum master.tar.gz').read().split(' ')[0].strip()
    commit = os.popen('cd cling && git rev-parse --short HEAD && cd ..').read().strip()

    update = ''
    for line in content:
        if '{% set sha256' in line:
            update += '{% set sha256 = "' + hash + '" %}\n'
        elif '{% set commit' in line:
            update += '{% set commit = "' + commit + '" %}\n'
        else:
            update += line + '\n'

update = update[0:-1]
with open('meta.yaml', 'w') as f:
    f.write(update)
