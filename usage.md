## USAGE

---

### Initializing the Database
* Class: [`ShitDB.DB()`](https://github.com/v1s1t0r999/ShitDB/blob/master/ShitDB/core.py#L7)
* Parameters:
	* `github_token`: \
		*REQUIRED FIELD* \
		To interact with your GitHub repo. Check [this](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) out.
		
	* `database_repo`: \
		*REQUIRED FIELD* \
		The name of your repo which is to be used as the database.
	* `author`: \
		*REQUIRED FIELD* \
		A [tuple](https://docs.python.org/3/c-api/tuple.html) consisting of your email and username registered with your GitHub account. Eg: `("username","email")`
	* `branch`: \
		*OPTIONAL FIELD* \
		Any branch of the specified repo which is to be used to save data. Defaults to the default branch of your repo.
* Example:
```py
import ShitDB

my_db = ShitDB.DB("github_token", "my-repo", ("username","email@smth.com"), branch="my-database-branch")

(YOUR STUFF HERE)
```
	
---


### STORING DATA
* Function: [`ShitDB.push_remote_data()`](https://github.com/v1s1t0r999/ShitDB/blob/master/ShitDB/core.py#L19)
* Parameters:
	* `content`: \
		*REQUIRED FIELD* \
		The new data for the file.
	* `file_path`: \
		*REQUIRED FIELD* \
		The path of file on "GitHub".
	* `msg`: \
		*OPTIONAL FIELD* \
		The message on the commit. Defaults to "ShitDB"
	* `branch`: \
		*OPTIONAL FIELD* \
		Any diferent branch to commit on. Defaults to specified branch while db initializing.
	
* Example:
```py
>>> data = {"foo":"bar"}
>>> data.update({"baz":"lol"})
>>> db.push_remote_data(data, "somedata.json", msg="I added baz and lol!") # It'll be committed on GitHub!
$ {'foo':'bar', 'baz':'lol'}
```


---



### FETCHING DATA
* Function: [`ShitDB.load_remote_data()`](https://github.com/v1s1t0r999/ShitDB/blob/master/ShitDB/core.py#L36)
* Parameters:
	* `file_path`: \
		*REQUIRED FIELD* \
		The path of file on "GitHub".
	* `eval_output`: \
		*OPTIONAL FIELD* \
		Due to GitHub API limitations, the output is always [`str`](https://docs.python.org/3/library/string.html). So, to convert it to [`dict`](https://docs.python.org/3/c-api/dict.html), it has to be evaluated using: `eval(output)`. But for this, you have to be sure that the output can be evaluated, or else you'll have to face some ugly tracebacks...
	* `branch`: \
		*OPTIONAL FIELD* \
		Any diferent branch to fetch data from. Defaults to specified branch while db initializing.
	
* Example:
```py
>>> no_eval = db.load_remote_data("somedata.json")
>>> type(no_eval)
$ <class 'str'>
>>> yes_eval = db.load_remote_data("somedata.json", eval_output=True)
>>> type(yes_eval)
$ <class 'dict'>
```

---
# CONTRIBUTE TO COMPLETE THE DOCS [HERE](https://github.com/v1s1t0r999/ShitDB/tree/gh-pages)
---









