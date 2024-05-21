
import re

with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r', encoding="UTF-8") as f:
    a=f.read()
    names=re.findall(r"gene:(\S+).*duplication",a)
    seqs = re.findall(r'duplication.+\n((?:[^>].*\n)+)', a)
    dict = {name: seq for name, seq in zip(names, seqs)}
    output_str = ""
    
    for key, value in dict.items():
        output_str += f">{key}_mRNA\n{value}\n"

with open('duplicate_genes.fa', 'w', encoding="UTF-8") as output_file:
    output_file.write(output_str)

with open('duplicate_genes.fa', 'r', encoding="UTF-8") as output_file:
    print(output_file.read())
