#

#__main__

h = open("glove.6B.50d.txt", "r")
dict_vec = h.readlines()
h = open("glove.6B.50d.txt", "r")
dict_word = h.readlines()
g = open("animal_names", "r")
keys = g.readlines()

for i in range(len(keys)):
	keys[i] = keys[i].strip('\n')
	#print keys[i]
for i in range(len(dict_word)): 
	dict_word[i] = dict_word[i].split(" ")[0]
	#print dict_word[i]

for i in range(len(dict_word)): 
	if (dict_word[i] in keys):
		pass#print dict_vec[j]

for j in range(len(keys)): 
	cntf = 0 
	cnts = 0	
	if("+" in keys[j]): 
		t = keys[j].split("+")
		f = t[0] 
		s = t[1]
		for i in range(len(dict_word)): 
			if (dict_word[i] == f): 
				cntf = 1
				v1 =dict_vec[i]
				#print v1
		for i in range(len(dict_word)): 
			if (dict_word[i] == s) :
				cnts = 1
				v2 = dict_vec[i]
				#print v2 
		

		v1 = v1.split(" ")[1:][:-1]
		v2 = v2.split(" ")[1:][:-1]
		
		#print v1[0], v2[0]
		for i in range(len(v1)):
			v1[i] = (float(v1[i]) + float(v2[i]))/2 
			v1[i] = str(v1[i])
		temp = [keys[j]]
		
		v1 = temp + v1 + ['\n']
		#print v1[1]
		
		#" ".join(v1)     <----- due to some reasons, this is not working 
		st = ""
		for elem in v1:
			st = st+elem+" "
		print st.strip(" ")
		
