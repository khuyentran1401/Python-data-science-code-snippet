# command | tee filename.txt
nvidia-smi | tee system_information.txt # write
uname -a | tee -a system_information.txt # append