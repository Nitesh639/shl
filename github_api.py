import pandas as pd
import requests

username = 'Nitesh639'
token = 'userToken' # please provide the user Token other it will show error
login = []
name = []
location = []
twitter_username = []
html_url = []
company = []
total_contribution = []
tools = []


def load_repo(working_tool, page_no):
    contributors = requests.get("https://api.github.com/repos/" + working_tool + "/contributors?page=" + str(page_no),
                                auth=(username, token))
    return contributors.json()


def load_profile(contributor, tool):
    contributor_data = requests.get(contributor['url'], auth=(username, token))
    contributor_data = contributor_data.json()
    login.append(contributor_data['login'])
    name.append(contributor_data['name'])
    location.append(contributor_data['location'])
    twitter_username.append(contributor_data['twitter_username'])
    html_url.append(contributor_data['html_url'])
    company.append(contributor_data['company'])
    total_contribution.append(contributor['contributions'])
    tools.append(tool)


def excute(working_tool, page_no):
    contributors = load_repo(working_tool, page_no)
    tool = working_tool.split('/')[-1]
    for contributor in contributors:
        load_profile(contributor, tool)


def data_csv(working_tools, output):
    for working_tool in working_tools:
        repo_pages = requests.get("https://api.github.com/repos/" + working_tool, auth=(username, token))
        repo_pages = repo_pages.json()
        if repo_pages['watchers'] < 10000:
            print(working_tool, "repo have less than 10000 stars")
            continue
        i_pages = repo_pages["subscribers_count"] // 30
        print("Data crawling started for", working_tool)
        for page_no in range(1, i_pages):
            excute(working_tool, page_no)
        print("Data crawling completed for", working_tool)
    dataset = pd.DataFrame(
        {'ML_Tool': tools, 'GitHub_ID': login, 'Name': name, 'Location': location,
         'Twitter': twitter_username,
         'GitHub_Link': html_url, 'Company': company, 'Total_Contribution': total_contribution})
    dataset.to_csv(output)


ML_Tools = ["nltk/nltk", "scikit-learn/scikit-learn", "tensorflow/tensorflow", "pytorch/pytorch", "keras-team/keras"]
output_file = 'git_final.csv'
data_csv(ML_Tools, output_file)

