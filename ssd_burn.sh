#!/bin/bash -e

SSD_NAME=${1}
NUM_ITER=${2:-10}

./ssd_burn_seq_w.sh $NUM_ITER | tee "${SSD_NAME}_seq_w.txt"
./ssd_burn_seq_r.sh $NUM_ITER | tee "${SSD_NAME}_seq_r.txt"
./ssd_burn_rand_w.sh $NUM_ITER | tee "${SSD_NAME}_rand_w.txt"
./ssd_burn_rand_r.sh $NUM_ITER | tee "${SSD_NAME}_rand_r.txt"

