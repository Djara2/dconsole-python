import webbrowser
import os
helpText = "search is a lightweight terminal utility "
CLEAR = "\u001b[0m"
CYAN = "\u001b[36;1m"
GREEN = "\u001b[32;1m"
PINK = "\u001b[35;1m"
os.system("clear")
bb = "        "
engines = ["bing", "google", "youtube", "bing images", "google images", "exit", "quit", "b", "g", "y", "amazon", "help", "jisho", "j", "w3m"]
boxText = "- David \"Davemob\" Jara 2021 -"
print("\u001b[36;1m", end="")
for x in range(0, len(boxText)):
	print("-", end="")
print("\n", end="")
print(boxText)
for x in range(0, len(boxText)):
	print("-", end="")
print("\n", end = "")
print("\u001b[0m", end="")
print("Enter "+GREEN+"\"HELP\""+CLEAR+" for program guide.")
while(True):
	argument = input(PINK+"Search: "+CLEAR)
	argumentL = argument.split()
	argumentL[0] = argumentL[0].lower()
	if(not argumentL[0] in engines):
		print(bb+argumentL[0]+" is not a supported engine. Enter \"ENGINES\" to see which engines are supported.")
	else:
		if(argumentL[0] == "exit" or argumentL[0] == "quit"):
			quit()
		if(argumentL[0] == "help"):
			pass
		#CASE: BING SEARCH
		if(argumentL[0] == "bing" or argumentL == "b"):
			if(argumentL[1] == "images" or argumentL[1] == "i"):
				query = "www.bing.com/images/search?q="
				for x in range(2, len(argumentL)):
					if(not x == len(argumentL)-1):
						query+=argumentL[x]+"+"
					else:
						query+=argumentL[x]
			else:
				query = "www.bing.com/search?q="
				for x in range(1, len(argumentL)):
					if(not x == len(argumentL)-1):
						query+=argumentL[x]+"+"
					else:
						query+=argumentL[x]
			webbrowser.open(query)
		#CASE: GOOGLE SEARCH
		if(argumentL[0] == "google" or argumentL[0] == "g"):
			if(argumentL[1] == "images" or argumentL[1] == "i"):
				query = "www.google.com/images/search?q="
				for x in range(2, len(argumentL)):
					if(not x == len(argumentL)-1):
						query+=argumentL[x]+"+"
					else:
						query+=argumentL[x]
			else:
				query = "www.google.com/search?q="
				for x in range(1, len(argumentL)):
					if(not x == len(argumentL)-1):
						query+=argumentL[x]+"+"
					else:
						query+=argumentL[x]
			webbrowser.open(query)
		#CASE: YOUTUBE SEARCH
		if(argumentL[0] == "youtube" or argumentL[0] == "y"):
			query = "https://www.youtube.com/results?search_query="
			for x in range(1, len(argumentL)):
				if(not x == len(argumentL)-1):
					query+=argumentL[x]+"+"
				else:
					query+=argumentL[x]
			webbrowser.open(query)
		#CASE: AMAZON SEARCH
		if(argumentL[0] == "amazon" or argumentL[0] == "a"):
			query = "https://www.amazon.com/s?k="
			queryEnd = "&ref=nb_sb_noss"
			for x in range(1, len(argumentL)):
				if(not x == len(argumentL)-1):
					query+=argumentL[x]+"+"
				else:
					query+=argumentL[x]
			query+=queryEnd
			webbrowser.open(query)
		#CASE: JISHO SEARCH
		if(argumentL[0] == "jisho" or argumentL[0] == "j"):
			query = "https://jisho.org/search/"
			for x in range(1, len(argumentL)):
				if(not x == len(argumentL)-1):
					query+=argumentL[x]+"%20"
				else:
					query+=argumentL[x]
			webbrowser.open(query)
		#CASE W3M BUILT IN BROWSER - GOES TO WEBSITE LINK TYPED IN DIRECTLY - AUTO ADDS HTTPS:/WWW.

