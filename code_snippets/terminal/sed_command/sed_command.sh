cat weather.txt 
# Today is a sunny day. I want to be outside.

sed 's/sunny/rainy/' weather.txt 
# Today is a rainy day. I want to be outside.

sed -i 's/sunny/rainy/' weather.txt 
sed -i 's/outside/inside/' weather.txt 

cat weather.txt
# Today is a rainy day. I want to be inside