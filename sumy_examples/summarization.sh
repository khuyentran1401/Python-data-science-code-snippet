#!/bin/bash

echo "Summarize text from URL: https://www.dataquest.io/blog/learn-data-science/"

echo "Summazing text using LexRank..."
sumy lex-rank --length=10 --url=https://www.dataquest.io/blog/learn-data-science/ >> lex-rank.txt 
echo "Done"
echo "Summazing text using Luhn’s Heuristic Method ..."
sumy luhn --length=10 --url=https://www.dataquest.io/blog/learn-data-science/ >> luhn.txt 
echo "Done"
echo "Summazing text using Edmundson Heuristic Method ..."
sumy edmundson --length=10 --url=https://www.dataquest.io/blog/learn-data-science/ >> edmundson.txt 
echo "Done"
echo "Summazing text using Latent Semantic Analysis ..."
sumy lsa --length=10 --url=https://www.dataquest.io/blog/learn-data-science/ >> lsa.txt 
echo "Done"
echo "Summazing text using TextRank ..."
sumy text-rank --length=10 --url=https://www.dataquest.io/blog/learn-data-science/ >> text-rank.txt 
echo "Done"
