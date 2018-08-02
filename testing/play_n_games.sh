N=$1
P1ADDRESS=$2
P2ADDRESS=$3
C=$4
R=$5
for row in $(seq 1 $N);
do
  python3 ../dotsandboxescompete.py -v -q $P1ADDRESS $P2ADDRESS -c $C -r $R
done
