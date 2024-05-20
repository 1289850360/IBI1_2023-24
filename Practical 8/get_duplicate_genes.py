import re  
  
def process_fasta(input_file, output_file):  
    gene_name = None  
    current_seq = []  
    with open(input_file, 'r', encoding="UTF-8") as f:  
        for line in f:  
            if line.startswith('>'):  
                if gene_name and current_seq:  
                    if 'duplication' in gene_name:  
                        yield gene_name, ''.join(current_seq).strip()  
                    current_seq.clear()   
                gene_name = line.strip('>').strip()  
            else:  
                current_seq.append(line.strip())  
        if gene_name and current_seq:  
            if 'duplication' in gene_name:  
                yield gene_name, ''.join(current_seq).strip()  
  
with open("duplicate_genes.fa", 'w', encoding="UTF-8") as output_file:  
    for gene_name, seq in process_fasta("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", ""):  
        if 'duplication' in gene_name:  
            output_file.write(f">{gene_name}_mRNA\n{seq}\n")  
 
with open('duplicate_genes.fa', 'r', encoding="UTF-8") as output_file:  
    print(output_file.read())