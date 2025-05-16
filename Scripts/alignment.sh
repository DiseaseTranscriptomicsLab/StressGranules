#!/bin/bash

if [ -z "$1" ]
  then echo "No target directory has been provided. Assuming current path!"
  path=./
else
  path="$1"
fi

samples=$(ls ${path}*.fastq.gz | sed  's/_1.fastq.gz$//' | sed  's/_2.fastq.gz$//' | sort -u | xargs -n 1 basename)

for sample in ${samples[@]}
do
	echo ${sample}
done

if [ ! -d ${path}/alignment_STAR ]
	then mkdir ${path}/alignment_STAR
fi

# Standard Unique mode
for sample in ${samples[@]}
do
  ulimit -n 10000
  STAR \
  --genomeDir ~/Genomes/Human/STARindex \
  --readFilesIn ${path}/${sample}_1.fastq.gz ${path}/${sample}_2.fastq.gz  \
  --readFilesCommand zcat \
  --outFileNamePrefix ${path}/alignment_STAR/${sample} \
  --outSAMtype BAM SortedByCoordinate \
  --runThreadN 60 \
  --outFilterType BySJout \
  --alignSJoverhangMin 8 \
  --alignSJDBoverhangMin 1\
  --alignIntronMin 20 \
  --alignIntronMax  1000000 \
  --alignMatesGapMax  1000000 \
  --outFilterMultimapNmax 1 \
  --outFilterMismatchNmax 999 \
  --outFilterMismatchNoverLmax 0.04
done