#!/bin/bash
# Termux has a problem with the ./dc and ./dce inputs so this is a more universal way
if $# eq 1
then
	python3 dconsole.py 
else
	python3 dconsole.py $1
fi
