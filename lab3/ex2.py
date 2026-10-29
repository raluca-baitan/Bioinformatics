from itertools import product
import matplotlib.pyplot as plt

bases = "UCAG"

# Create all 64 possible RNA codons, with an initial count of zero
codon_counts = {
    "".join(codon): 0
    for codon in product(bases, repeat=3)
}

sequences = []
current_sequence = []

file_name = "GCF_000240185.1_ASM24018v2_genomic.fna"

# Read the FASTA file and keep each sequence record separate
with open(file_name, "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        if line.startswith(">"):
            if current_sequence:
                sequences.append("".join(current_sequence))
                current_sequence = []
        else:
            # Convert DNA to RNA and remove spaces
            line = "".join(line.upper().split()).replace("T", "U")
            current_sequence.append(line)

# Save the final sequence record
if current_sequence:
    sequences.append("".join(current_sequence))

valid_windows = 0
skipped_windows = 0

# Slide the 3-letter window forward by one position each time
for sequence in sequences:
    for i in range(len(sequence) - 2):
        codon = sequence[i:i + 3]

        if all(base in bases for base in codon):
            codon_counts[codon] += 1
            valid_windows += 1
        else:
            # Skip windows containing ambiguous letters, such as N
            skipped_windows += 1

if valid_windows == 0:
    print("No valid codons were found in the file.")
else:
    # Sort by count, highest first
    top_10 = sorted(
        codon_counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:10]

    print("\nTop 10 codons:")
    print("Codon  Count  Frequency")

    codons = []
    frequencies = []

    for codon, count in top_10:
        frequency = count / valid_windows * 100
        codons.append(codon)
        frequencies.append(frequency)

        print(f"{codon}    {count:5}  {frequency:.2f}%")

    print(f"\nValid windows counted: {valid_windows}")
    print(f"Windows skipped due to ambiguous bases: {skipped_windows}")

    # Plot the top 10 codons
    plt.bar(codons, frequencies, color="mediumpurple")
    plt.title("Top 10 Codons in the Genome")
    plt.xlabel("Codon")
    plt.ylabel("Frequency (%)")
    plt.tight_layout()
    plt.show()