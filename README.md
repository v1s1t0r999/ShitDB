# ShitDB
> A json database to fix the persistence problem on Heroku using GitHub!!

---

## The problem:
***In Heroku's free dev plan, files are not saved for more than 24 hours (or so). So, a json file will reset, the way it was uploaded, vanishing all the stored data. Read more [here](https://devcenter.heroku.com/articles/active-storage-on-heroku).***

## Solution:
***Using [ShitDB](https://github.com/v1s1t0r999/ShitDB) and your [GitHub](https://github.com) account, this problem can be fixed!!***
***But, there are other databases too. Using free add-ons like [PostgreSQL](https://elements.heroku.com/addons/heroku-postgresql) or using [MongoDB Atlas](https://www.mongodb.com/developer/how-to/use-atlas-on-heroku), is a way too, and is of-course free.***
***Using JSON storage is quite easy. For beginners, setting up MongoDB or Heroku Postgres addon can be quite a tricky task. This is an easier way!!***


## How?
***As your json file gets updated, it is simultaneously uploaded to a specified repository in your account. On restart of your Heroku Dynos, the data from the json file will be retrieved from your GitHub and saved to the local json file.***



## Requirements:
- Your GitHub Token. [how?](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- A repo as a database. Can be Private or Public!
- Your email and username associated with your GitHub account.
- Of-course a Heroku app. [how?](https://devcenter.heroku.com/articles/getting-started-with-python)
- Uhh...nothing else I guess


---
## CODE ARENA
```shell
$ pip install ShitDB
```
```py
"""
A MINIMAL USAGE OF ShitDB!
"""

import json
import ShitDB


TOKEN = "ghp_github_token_999xyz"
AUTHOR = ("username","email")
REPO = "Repo-As-Database"


db = ShitDB.DB(github_token=TOKEN,database_repo=REPO,author=AUTHOR) # optional => branch="my-branch"


## YOUR STUFF

def register_user(user,id):
    with open("users.json","r") as f:
		old = json.load(f)
	old.update({user:id}) # old became new!
	
	db.push_remote_data(content=old,file_path="my_files/users.json") # file path on github
	

def get_user_data(user):
	data = db.load_remote_data("my_files/users.json",eval_output=True) # By-Default the return type is <str> | eval_output=True to convert <str> to <dict>
	id = data[user]
	return id
	

```


## ***THIS WAS MADE BY ME FOR MY [DISCORD BOT](https://dsc.gg/letleaf-the-bot). DO INVITE IT!***


