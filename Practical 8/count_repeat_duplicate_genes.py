import re  
  
def count_repeats(seq, repeat):  
    count = 0  
    start = 0  
    while True:  
        start = seq.find(repeat, start)  
        if start == -1:  
            break  
        else:  
            count += 1  
            start += len(repeat)  
    return count  
  
def process_fasta_file(input_file, output_file, repeat_sequence):  
    pattern_name = re.compile(r'^>(\S+).*duplication', re.IGNORECASE)  
    pattern_seq = re.compile(r'^>(?:[^>].*\n)+', re.MULTILINE | re.DOTALL)  
      
    with open(input_file, 'r', encoding="UTF-8") as f_in, open(output_file, 'w', encoding="UTF-8") as f_out:  
        current_name = None  
        current_seq = []  
          
        for line in f_in:  
            if line.startswith('>'):  
                if current_name and current_seq:  
                    # Process previous sequence  
                    seq_without_newlines = ''.join(current_seq).replace('\n', '')  
                    repeat_count = count_repeats(seq_without_newlines, repeat_sequence)  
                    if repeat_count != 0:  
                        f_out.write(f">{current_name}_mRNA (Repeat Count: {repeat_count})\n{seq_without_newlines}\n")  
                  
                # Start new sequence  
                match = pattern_name.match(line)  
                if match:  
                    current_name = match.group(1)  
                current_seq = []  
            else:  
                # Append sequence line  
                current_seq.append(line.strip())  
          
        # Process the last sequence  
        if current_name and current_seq:  
            seq_without_newlines = ''.join(current_seq).replace('\n', '')  
            repeat_count = count_repeats(seq_without_newlines, repeat_sequence)  
            if repeat_count != 0:  
                f_out.write(f">{current_name}_mRNA (Repeat Count: {repeat_count})\n{seq_without_newlines}\n")  
  
# Ask the user for input on which repeat sequence to look for  
repeat_sequence = input("Please input the repeat sequence (e.g., GTGTGT or GTCTGT): ")  
output_file_name = f'{repeat_sequence}_duplicate_genes.fa'  
  
try:  
    process_fasta_file("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", output_file_name, repeat_sequence)  
    print(f"Processed and saved to {output_file_name}")  
except FileNotFoundError:  
    print("Input file not found.")  
except Exception as e:  
    print(f"An error occurred: {e}")  
  
# Optionally, you can print the output file content here, but it's not recommended for large files  
# with open(output_file_name, 'r', encoding="UTF-8") as output_file:  
#     print(output_file.read())