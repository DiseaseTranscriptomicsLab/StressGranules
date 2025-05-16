#!/bin/bash

if [ -z "$1" ]
  then echo "No target directory has been provided. Assuming current path!"
  path=./
else
  path="$1"
fi

samples=$(ls ${path}*.fastq.gz)

for sample in ${samples[@]}
do
	echo ${sample}
done

if [ ! -d ${path}/fastqc_results ]
	then mkdir ${path}/fastqc_results
fi

# Standard Unique mode
for sample in ${samples[@]}
do
  ulimit -n 10000
  fastqc ${path}/${sample}  \
  -o fastqc_results
done