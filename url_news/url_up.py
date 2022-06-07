import os

class sosa_file:
	'''SO SÁNH URL MỚI VÀ CŨ'''

	def url_up():

		path = "/home/norii/NORII/test/data/output"
		al = []
		for i in os.listdir(path):
			
			with open(path+'/'+i,'r') as f:
				t =f.read()
				al.append(t)

		return al


	def url_if(new,old):

		if new != old: return new

		else: print("Url trùng!")

