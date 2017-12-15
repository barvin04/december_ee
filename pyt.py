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

for i in range(len(dict_word)): 
	dict_word[i] = dict_word[i].split(" ")[0]
	

wrt = open("write_50.txt", "w") #write format 
wrtn = open("write_50_names.txt", "w")
for i in range(len(dict_word)): 
	if (dict_word[i] in keys):
		st =dict_vec[i]
		wrt.write(st)
		wrt.write('\n')
		wrtn.write(dict_word[i])
		wrtn.write('\n')
wrt.close()
wrtn.close()

#for compound names 
wrt = open("write_50.txt", "a") #append format 
wrtn = open("write_50_names.txt", "a")
for j in range(len(keys)): 
	cntf = 0 
	cnts = 0	
	if("+" in keys[j]): 
		t = keys[j].split("+")
		f = t[0]  #get the first word
		s = t[1]	#get the second word
		for i in range(len(dict_word)):  	#if first word found 
			if (dict_word[i] == f): 
				cntf = 1
				v1 =dict_vec[i]
				
		for i in range(len(dict_word)):  	#if second word found 
			if (dict_word[i] == s) :
				cnts = 1
				v2 = dict_vec[i]

		v1 = v1.split(" ")[1:][:-1]		#using the numercals only 
		v2 = v2.split(" ")[1:][:-1]
		
		for i in range(len(v1)):
			v1[i] = (float(v1[i]) + float(v2[i]))/2 
			v1[i] = str(v1[i])
		temp = [keys[j]]
		
		v1 = temp + v1 + ['\n']
		
		#" ".join(v1)     <----- due to some reasons, this is not working 
		st = ""
		for elem in v1:
			st = st+elem+" " #averaged vector created 
		wrt.write(st)
		wrt.write('\n')
		
		name= st.split(" ")[0]	
		print name
		wrtn.write(dict_word[i])  #names in a file being stored 
		wrtn.write('\n')
wrt.close()
