from typing import List
import random
import yaml

if __name__ == '__main__':
    with open('members.yaml', 'r') as f:
        members: List[str] = yaml.load(f, Loader=yaml.SafeLoader)
    
    # membersをシャッフル
    random.shuffle(members)

    for i, member in enumerate(members):
        print(f'{i+1}番目: {member}')
