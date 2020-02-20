#!/bin/bash	 
#SBATCH --comment "HashCode"
#SBATCH -J "HashCode" 	
#SBATCH --error=job.%J.err  
#SBATCH -p short
#SBATCH -c 28
#SBATCH -N 1

module load venv
python main.py