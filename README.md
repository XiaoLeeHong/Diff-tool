# Diff tool

simple terminal tool to compare two text files

## install
pip install .

## quick start

create two files:

echo "hello" > file1.txt  
echo "hello world" > file2.txt  

run:

python main.py file1.txt file2.txt

or if installed:

diff file1.txt file2.txt

## no color
diff file1.txt file2.txt --no-color
