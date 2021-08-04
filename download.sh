#!/bin/bash
echo "Does your system work with sudo? "
read supportsSudo
if $supportsSudo == "y"
then
	sudo apt install python3-pip
	sudo apt install w3m
	pip3 install rich
	pip3 install pyautogui
	pip3 install pyperclip
	sudo apt-get install python3-tk python3-dev
else
	apt install python3-pip
	apt install w3m
	pip3 install rich
	pip3 install pyautogui
	pip3 install pyperclip
	sudo apt-get install python3-tk python3-dev
fi

