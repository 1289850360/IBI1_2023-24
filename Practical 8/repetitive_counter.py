
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
def repeat_counts(seq):
   repeat1 = 'GTGTGT'
   repeat2 = 'GTCTGT'
   count= 0    
   for i in range(len(seq)):
       if seq[i:i+6]==repeat1 or seq[i:i+6]==repeat2:
          count+=1
    
   return count 

print(f"count totall number repeat of GTGTGT and GTCTGT is {repeat_counts(seq)}") 








