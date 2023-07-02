# shl

### Working Repos:
- [nltk/nltk](https://github.com/nltk/nltk)
- [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
- [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow)
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
- [keras-team/keras](https://github.com/keras-team/keras)

### Files:

- github_api.py: Using this we are able to get the most valuable contributors (around 400-500 contributors/ repo).
- git_final.csv: Output file of github_api.py containing data from 1948 contributors.
- by_contributer_name.py: Using this we are able to get all contributor's data by GitHubID.
- For all contributors ID:
```
git log --all --format='%aL' | sort -u -o contributors_list.txt
```
- contributors_list: It's contains all the files of contributors' name.
- by_contributors_final.csv and not_fount_final: Output files of by_contributer_name.py containing data around 12000+ GitHub IDs. First file for found(valid) contributors and second file for the not found github ids(due to invalid or api limit cross).