#!/bin/bash -e

NUM_ITER=${1:-1}

for i in {1..$NUM_ITER}
do
	fio --name TEST --eta-newline=5s --filename=fio-tempfile.dat --rw=randwrite --blocksize=4k --ioengine=libaio --iodepth=32 --direct=1 --numjobs=1 --size=10g --runtime=180 ; rm fio-tempfile.dat
done


