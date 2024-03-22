import json

all_following_file = 'following.json'
all_followers_file = 'followers_1.json'


def get_data(input_file, input_relationship=None):
    with open(input_file, 'r') as file:
        if input_relationship:
            data = json.loads(file.read())[input_relationship]
        else:
            data = json.loads(file.read())
        return [item['string_list_data'][0]['value'] for item in data]


def get_not_following_back(following_list, followers_list):
    return [item for item in following_list if item not in followers_list]


all_following = get_data(all_following_file, 'relationships_following')
all_followers = get_data(all_followers_file)

for person_not_following_back in get_not_following_back(all_following, all_followers):
    print(person_not_following_back)
