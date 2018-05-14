FROM=$1
TILL=$2
P1ADDRESS=$3
P2ADDRESS=$4
GAMES=$5

for row in $(seq 3 $FROM);
do
  for col in $(seq 3 $TILL);
  do
    for i in $(seq 1 $GAMES);
    do
      echo "started game $i for $col x $row"
    	python3 dotsandboxescompete.py $P1ADDRESS $P2ADDRESS -c $col -r $row
      echo "finished game $i"
    done
  done
done

for row in $(seq 3 $TILL);
do
  for col in $(seq 3 $FROM);
  do
    for i in $(seq 1 $GAMES);
    do
      echo "started game $i for $col x $row"
      python3 dotsandboxescompete.py $P1ADDRESS $P2ADDRESS -c $col -r $row
      echo "finished game $i"
    done
  done
done


#bash script.sh 10 10 ws://localhost:2001 ws://localhost:2002
