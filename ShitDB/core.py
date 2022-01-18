from .auth import Data
from .errors import *




class DB:
	def __init__(self):
		self.data = Data()
	
	
    def push_remote_data(self,content,file_path,branch = None,msg="ShitDB"):
		if branch is None:
			branch = self.data.branch
		try:
			self.data.repo.create_file(file_path,msg,str(content),branch=branch)
        except:
            sha = self.data.repo.get_contents(file_path,ref=branch).sha
            self.data.repo.update_file(file_path,msg,str(content),sha,branch=branch)
        return content
	
	
	
	def load_remote_data(self,file_path,eval_output=False):
		if branch is None:
			branch = self.data.branch
		con = self.data.repo.get_contents(file_path,ref=branch).decoded_content.decode("utf-8")
		if eval_output is True:
			return eval(con)
		return con

	
	
	def to_json(self,file_path,new_json,indent=4):
		with open(file_path,"r") as f:
			old = json.load(f)
		old.update(new_json) # became new!
		with open(file_path,"w") as f:
			json.dump(old,file_path,indent=indent)
		return old
	
	
	
	def to_file(self,file_path,con,mode="w"):
		with open(file_path,mode) as f:
			f.write(con)
		return con

	
	
	def load_local_json(self,file_path):
		with open(file_path,"r") as f:
			con = json.load(f)
		return con
	
	
	def load_local_file(self,file_path,eval_output=False):
		with open(file_path,"r") as f:
			con = str(f.read())
		if eval_output is True:
			return eval(con)
		return con
	
	
	
	
	def sync(self,file_path,prefer="remote",dry=False):
		prefer=prefer.lower()
        fp=file_path
		j = False
		if fp.endswith(".json"):
			j = True
        dry=bool(dry)
        allowed=['remote','local']
        if prefer not in allowed:
            raise BadArgs(f"Args must be {', '.join(allowed)}; not \"{prefer}\"")
        if dry is True:
			if j:
				return self.load_local_json(fp)==self.get_remote_data(fp,True)
			return self.load_local_file(fp)==self.get_remote_data(fp)
        
		if prefer=="remote":
			if j:
				self.to_json(self.get_remote_data(fp,True),fp)
				return self.load_local_json(fp)==self.get_remote_data(fp,True), "Overrided LOCAL data"
			self.to_file(self.get_remote_data(fp),fp)
			return self.load_local_file(fp)==self.get_remote_data(fp), "Overrided LOCAL data"
      
        elif prefer=="local":
			if j:
				if self.load_local_json(fp)==self.get_remote_data(fp,True):
					return True,"Already Synced!!"
            else:
				if self.load_local_file(fp)==self.get_remote_data(fp):
					return True,"Already Synced!!"
            self.push_remote_data(self.load_local_file(fp))
            return self.load_local_file(fp)==self.get_remote_data(fp), "Overrided REMOTE data"


