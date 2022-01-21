# USAGE

---
---
---

## THE DATABASE
### Initialize Database
*Use [AsyncDB](https://v1s1t0r999.github.io/ShitDB/usage#initialize-database) for projects like a discord bot.*
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
		
* Methods:
	* [`ShitDB.DB.push_remote_data()`](https://github.com/v1s1t0r999/ShitDB/blob/master/ShitDB/core.py#L19)
		1. `content`: \
			*REQUIRED FIELD* \
			The new data for the file.
		2. `file_path`: \
			*REQUIRED FIELD* \
			The path of file on "GitHub".
		3. `msg`: \
			*OPTIONAL FIELD* \
			The message on the commit. Defaults to "ShitDB"
		4. `branch`: \
			*OPTIONAL FIELD* \
			Any diferent branch to commit on. Defaults to specified branch while db initializing.
	
	
	* [`ShitDB.DB.load_remote_data()`](https://github.com/v1s1t0r999/ShitDB/blob/master/ShitDB/core.py#L36)
		1. `file_path`: \
			*REQUIRED FIELD* \
			The path of file on "GitHub".
		2. `eval_output`: \
			*OPTIONAL FIELD* \
			Due to GitHub API limitations, the output is always [`str`](https://docs.python.org/3/library/string.html). So, to convert it to [`dict`](https://docs.python.org/3/c-api/dict.html), it has to be evaluated using: `eval(output)`. But for this, you have to be sure that the output can be evaluated, or else you'll have to face some ugly tracebacks...
		3. `branch`: \
			*OPTIONAL FIELD* \
			Any diferent branch to fetch data from. Defaults to specified branch while db initializing.
	
	
	* [`ShitDB.DB.sync()`](https://github.com/v1s1t0r999/ShitDB/blob/master/ShitDB/core.py#L81)
		1. `file_path`: \
			*REQUIRED FIELD* \
			The path of file on "GitHub" and "Local Machine". The files have to be the same, else it'll raise [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html)
		2. `prefer`: \
			*REQUIRED FIELD* \
			Which file is to be preferred. It can be: `"remote"` or `"local"` only. \
			For Eg: If `prefer` is `"remote"`, then the data in the local file named `"file_path"` will be overridden in place of the data on GitHUb's `"file_path"`.
		3. `dry`: \
			*OPTIONAL FIELD* \
			Just checks whether the `"file_path"` on GitHub is same as the `"file_path"` in the local machine, if True. Defaults to "False". Returns a [bool](https://docs.python.org/3/c-api/bool.html)
	
	
	
	
	See [Manuals](https://v1s1t0r999.github.io/ShitDB/manuals#db) for How-Tos or Examples?
	

---
---


### Initialize "AsyncDB" Database
* Class: [`ShitDB.AsyncDB()`](https://github.com/v1s1t0r999/ShitDB/blob/master/ShitDB/_async.py#L7)
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
		
* Methods:
	* [`ShitDB.AsyncDB.push_remote_data()`](https://github.com/v1s1t0r999/ShitDB/blob/master/ShitDB/_async.py#L23)
		1. `content`: \
			*REQUIRED FIELD* \
			The new data for the file.
		2. `file_path`: \
			*REQUIRED FIELD* \
			The path of file on "GitHub".
		3. `msg`: \
			*OPTIONAL FIELD* \
			The message on the commit. Defaults to "ShitDB"
		4. `branch`: \
			*OPTIONAL FIELD* \
			Any diferent branch to commit on. Defaults to specified branch while db initializing.
	
	
	* [`ShitDB.AsyncDB.load_remote_data()`](https://github.com/v1s1t0r999/ShitDB/blob/master/ShitDB/_async.py#L42)
		1. `file_path`: \
			*REQUIRED FIELD* \
			The path of file on "GitHub".
		2. `eval_output`: \
			*OPTIONAL FIELD* \
			Due to GitHub API limitations, the output is always [`str`](https://docs.python.org/3/library/string.html). So, to convert it to [`dict`](https://docs.python.org/3/c-api/dict.html), it has to be evaluated using: `eval(output)`. But for this, you have to be sure that the output can be evaluated, or else you'll have to face some ugly tracebacks...
		3. `branch`: \
			*OPTIONAL FIELD* \
			Any diferent branch to fetch data from. Defaults to specified branch while db initializing.
	
	
	* [`ShitDB.AsyncDB.sync()`](https://github.com/v1s1t0r999/ShitDB/blob/master/ShitDB/_async.py#L89)
		1. `file_path`: \
			*REQUIRED FIELD* \
			The path of file on "GitHub" and "Local Machine". The files have to be the same, else it'll raise [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html)
		2. `prefer`: \
			*REQUIRED FIELD* \
			Which file is to be preferred. It can be: `"remote"` or `"local"` only. \
			For Eg: If `prefer` is `"remote"`, then the data in the local file named `"file_path"` will be overridden in place of the data on GitHUb's `"file_path"`.
		3. `dry`: \
			*OPTIONAL FIELD* \
			Just checks whether the `"file_path"` on GitHub is same as the `"file_path"` in the local machine, if True. Defaults to "False". Returns a [bool](https://docs.python.org/3/c-api/bool.html)
	
	
	
	
	See [Manuals](https://v1s1t0r999.github.io/ShitDB/manuals#async-db) for How-Tos or Examples?






