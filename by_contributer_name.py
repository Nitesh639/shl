import os
import pandas as pd
import requests

username = 'Nitesh639'
token = 'user_token'
login = []
name = []
location = []
twitter_username = []
html_url = []
company = []
total_contribution = []
tools = []
not_tools = []
not_name = []

file_list = os.listdir('contributors_list')
count = 0
dir_num = 0
for file in file_list:
    dir_num += 1
    with open('contributors_list/' + file) as f:
        contributors = f.readlines()
    tool = file.split('.')[0]
    for contributor in contributors:
        count += 1
        print(dir_num, count, contributor)
        contributor_data = requests.get("https://api.github.com/users/" + contributor.strip('\n'),
                                        auth=(username, token)).json()

        if 'message' in contributor_data:
            not_name.append(contributor.strip('\n'))
            not_tools.append(tool)
            continue
        login.append(contributor_data['login'])
        name.append(contributor_data['name'])
        location.append(contributor_data['location'])
        twitter_username.append(contributor_data['twitter_username'])
        html_url.append(contributor_data['html_url'])
        company.append(contributor_data['company'])
        tools.append(tool)

dataset = pd.DataFrame(
    {'ML_Tool': tools, 'GitHub_ID': login, 'Name': name, 'Location': location,
     'Twitter': twitter_username,
     'GitHub_Link': html_url, 'Company': company})
dataset.to_csv('by_contributors_final.csv')

dataset = pd.DataFrame({'ML_Tool': not_tools, 'Name': not_name})
dataset.to_csv('not_fount_final.csv')
