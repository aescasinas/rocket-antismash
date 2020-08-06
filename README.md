# Rocket HPC - antiSMASH 5.1.2
Automate antiSMASH 5.1.2 on the Rocket HPC.

### Installation
```sh
git clone https://github.com/aescasinas/rocket-antismash.git
```

### Usage
**Input:** directory containing `.gbk` files
```sh
sbatch run_antismash -p <PREFIX> path/to/dir
```
Note: `<PREFIX>` is a name to go before a BGC name for BiG-SCAPE. For example, if `-p DSM` the output will produce **DSM_STRAIN-NAME.region001.gbk** in the directory called **bigscape_input**.
### Example
```sh
sbatch run_antismash -p DSM path/to/dir
```
