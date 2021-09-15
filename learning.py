with open('SAFI_results.csv') as file: 
	file.readline() 
	
	n_grass = 0
	n_mabatipitched = 0
	n_mabatisloping = 0
	n_other = 0

	for line in file:
		roof_type=line.split(',')[18] #index 18 is the 19th column is C01_respondent_roof_type)
		if roof_type == "grass": 
			n_grass = n_grass + 1
		elif roof_type == "mabatisloping":
			n_mabatisloping += 1
		elif roof_type == "mabatipitched":
			n_mabatipitched += 1
		else:
			n_other += 1


	print("There are", n_grass, "grass roofs")
	print("There are", n_mabatisloping, "mabati sloping roofs")
	print("There are", n_mabatipitched, "mabati pitched roofs")
	print("There are", n_other, "other types of roofs")
