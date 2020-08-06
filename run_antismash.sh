#!/bin/bash
#
#SBATCH -A jems
#SBATCH -t 30-00:00:00
#SBATCH -p long
#SBATCH -n 2
#SBATCH --ntasks-per-node=1
#SBATCH -c 44
#

module load Anaconda3
source activate antismash

THREADS=44
PREFIX=DSM

while getopts "p:" OPTION
do
        case $OPTION in
                p) PREFIX=$OPTARG ;;
        esac
done

if [ $# -lt 1 ]; then
        echo ""
        echo "Usage: sbatch run_antismash.sh -p PREFIX path/to/dir"
        echo ""
        exit 1
fi

GBKS_DIR=${@:$OPTIND:1} # POSITIONAL ARGUMENT

python -u main.py -t $THREADS -p $PREFIX $GBKS_DIR