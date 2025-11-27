def create_codon_dict(file_path):
  codonaa = {}
  with open(file_path, "r") as file:
     rows = file.readlines()
  for r in rows[:] : 
     cell = r.strip().split('\t')
     key = cell[0]      
     value = cell[2]    
     codonaa[key] = value
  return codonaa

