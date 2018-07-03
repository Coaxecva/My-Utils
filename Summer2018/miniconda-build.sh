#!/usr/bin/env bash

echo "Build miniconda3 with tools"

set -ex
set -o pipefail

INICONDA_INSTALL_SCRIPT=Miniconda3-latest-Linux-x86_64.sh

# Current script DIR
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Miniconda
MINICONDA_DIR=${DIR}/MINICONDA

## Miniconda
if [ -d ${MINICONDA_DIR} ]
then
	echo "Found: "${MINICONDA_DIR}	
	rm -r ${MINICONDA_DIR}
	echo "Removed: "${MINICONDA_DIR}
fi

# Download and install Miniconda
curl -OL https://repo.continuum.io/miniconda/${MINICONDA_INSTALL_SCRIPT}

echo "Created: "${MINICONDA_DIR}

sh ${MINICONDA_INSTALL_SCRIPT} -b -p ${MINICONDA_DIR}

# Remove install script
if [ -f ${MINICONDA_INSTALL_SCRIPT} ]
then
	rm ${MINICONDA_INSTALL_SCRIPT}
	echo "Removed: "${MINICONDA_INSTALL_SCRIPT}
fi

# matplotlib numpy scipy 
${MINICONDA_DIR}/bin/conda install -c conda-forge matplotlib --yes
${MINICONDA_DIR}/bin/conda install -c anaconda numpy --yes
${MINICONDA_DIR}/bin/conda install -c anaconda scipy --yes

# pysam
${MINICONDA_DIR}/bin/easy_install pip --yes
${MINICONDA_DIR}/bin/pip install pysam --yes

# Channels
${MINICONDA_DIR}/bin/conda config --add channels defaults
${MINICONDA_DIR}/bin/conda config --add channels conda-forge
${MINICONDA_DIR}/bin/conda config --add channels bioconda

declare -a readonly tool_arr=("bwa" "minimap2" "graphmap" "ngmlr" "samtools" "sniffles" "bowtie2")
tool_arr_len=${#tool_arr[@]}

for (( i=1; i<${tool_arr_len}+1; i++ ))
do
    echo "Installing -- bash script called: ${tool_arr[$i-1]}"
    ${MINICONDA_DIR}/bin/conda install -c bioconda ${tool_arr[$i-1]} --yes
done
