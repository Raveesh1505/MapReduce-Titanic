cat titanic_data.txt | python3 src/mapper.py | sort -k1,1 | python2 src/reducer.py