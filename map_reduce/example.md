# Example
echo "Patriots Celtics Sox Bruins Patriots Patriots Patriots" | path_to/mapper.py

echo "Patriots Celtics Sox Bruins Patriots Patriots Patriots" | path_to/mapper.py | sort -k1,1 | path_to/reducer.py

cat path_to/boston.txt | path_to/mapper.py