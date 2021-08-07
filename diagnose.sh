#!/bin/bash
echo "This is a script for fixing potential issues with the system even after running download.sh"
read -p "Is pyperclip working?: " pyperclip
if $pyperclip == "n"
then
	read -p "Does sudo work on this system?: " sudoWorks
	if $sudoWorks == "y"
	then
		sudo apt install xsel
	else
		apt install xsel
	fi
fi
echo "Diagnostic complete. Try to rerun program."
echo "Note that you must run the run.sh script with the argument np (as in no pyautogui) if trying to run on Termux"

