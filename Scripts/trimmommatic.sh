#!/bin/bash

if [ -z "$1" ]
  then echo "No target directory has been provided. Assuming current path!"
  path=./
else
  path="$1"
fi

samples=$(ls ${path}*.fastq.gz | sed  's/_1.fastq.gz$//' | sed 's/_2.fastq.gz$//' | sort -u | xargs -n 1 basename)

for sample in ${samples[@]}
do
	echo ${sample}
done

if [ ! -d ${path}/TrimmedSamples ]
	then mkdir ${path}/TrimmedSamples
fi

# Standard Unique mode
for sample in ${samples[@]}
do
  ulimit -n 10000
  java -jar ~/Software/Trimmomatic-0.39/trimmomatic-0.39.jar PE\
  -threads 60 \
  ${path}/${sample}_1.fastq.gz ${path}/${sample}_2.fastq.gz \
  ${path}/TrimmedSamples/${sample}_1.paired.fastq.gz ${path}/TrimmedSamples/${sample}_1.unpaired.fastq.gz\
  ${path}/TrimmedSamples/${sample}_2.paired.fastq.gz ${path}/TrimmedSamples/${sample}_2.unpaired.fastq.gz\
  ILLUMINACLIP:TruSeq3-PE-2.fa:2:30:10:2:True LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
done