touch important_file.txt 

# Make the file immutable
sudo chattr +i important_file.txt 

# Check the file attributes
lsattr important_file.txt 

rm important_file.txt