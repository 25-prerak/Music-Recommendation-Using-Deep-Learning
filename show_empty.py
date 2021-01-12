import os 

folder_sample = "Dataset/fma_small"
directories = [d for d in os.listdir(folder_sample) if os.path.isdir(os.path.join(folder_sample, d))]
count = 0
for d in directories:
	label_directory = os.path.join(folder_sample, d)
	file_names = [os.path.join(label_directory, f) for f in os.listdir(label_directory) if f.endswith(".mp3")]
	m = 99999999
	fx = ""
	for f in file_names:
		s = os.stat(f)
		size = s.st_size
		if(size < 10000):
			print(size, f,"*************")
		count += 1
print(count)
		
