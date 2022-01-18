from github import *


class Data:
	def __init__(self):
		self.repo=""
		self.key = ""
		self.author=""
		self.github=""
		self.branch = list(self.repo.get_branches())[0]




class ConnectDB:
	def __init__(self,github_token:str,database_repo:str,author:tuple,branch:str = None):
		data = Data()
		data.github = Github(github_token)
		data.key = github_token
		data.author = InputGitAuthor(name=author[0],email=author[1])
		data.repo = self.github.get_repo(f"{author[0]}/{database_repo}")
		data.branch = branch
		



