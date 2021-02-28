#!/bin/bash

rm -rf result.dat

echo -e "rho\tq_size\tav_serv_t\td_av_serv_t\tf_prob\td_f_prob" >> result.dat



for q_size in  2 3 5 10 15 
do
	for lambda in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
	do
		./execute.py $lambda 1.0 $q_size 100 --runMode static >> result.dat
	done
done

