#! /bin/bash
psre(){
	`date >> cenario02_medio.txt | ps -A >> cenario02_medio.txt`
	echo "True"
}
psre
