import os
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Automate antismash')

parser.add_argument('input_dir', type=str, help='Input directory containing .fastq reads')
parser.add_argument('-t', '--threads', default=4, help='Number of threads to run Flye (default: 4)')
parser.add_argument('-p', '--prefix', required=True, type=str, help='Prefix name for BGC regions')
args = parser.parse_args()

annotated_dir = args.input_dir
prefix = args.prefix
num_threads = args.threads

with open(os.devnull, 'w') as f:
    try:
        subprocess.call(['antismash'], stderr=f, stdout=f)
    except:
        print('\nActivate conda environment (conda activate antismash)\n')
        sys.exit()


# Prokka output dir
os.mkdir(f'{annotated_dir}/../antismash_output')
antismash_output_dir = f'{annotated_dir}/../antismash_output'
antismash_output_dir = os.path.abspath(antismash_output_dir)

os.mkdir(f'{antismash_output_dir}/as_logs')
as_logs_dir = f'{antismash_output_dir}/as_logs'

os.mkdir(f'{antismash_output_dir}/bigscape_input')
bigscape_dir = f'{antismash_output_dir}/bigscape_input'

# Prokka output subdirectories --> prokka_logs and annotated_gbk
gbk_list = os.listdir(annotated_dir)
print(f'\nFound {len(gbk_list)} files in input directory')
count = 1
for gbk in gbk_list:

    strain_name = gbk[:gbk.index('.')]

    print(f'\n----- Running antismash on {strain_name} ----- ({count}/{len(gbk_list)})\n')

    os.system(f'antismash --cb-general --cb-knownclusters --genefinding-tool prodigal --output-dir {as_logs_dir}/{strain_name} --cpus {num_threads} {annotated_dir}/{strain_name}.gbk ')

    as_strain_dir = f'{as_logs_dir}/{strain_name}' # antismash output dir

    antismash_files = os.listdir(as_strain_dir)
    for bgc in antismash_files:
        if 'region' in bgc and 'gbk' in bgc:
            os.system(f'cp {as_strain_dir}/{bgc} {bigscape_dir}/{prefix}_{strain_name}_{bgc}')

    count += 1

print('Done.')