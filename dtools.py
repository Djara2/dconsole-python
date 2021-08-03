externalProgramsList = ["binToDec", "decToBin", "mudae", "bt", "richbuilder", "htmlBuilder", "w3mh", "changelog", "discount", "search", "calculator", "tip", "help"]

knownCommandsList = ["commands", "speedtest", "binToDec", "decToBin", "h", "mudae", "binomial theorem", "bt", "richbuilder", "htmlBuilder", "programs", "translate" "programs", "len", "discount", "help", "exit", "quit", "history", "hre", "new", "numbers", "v", "discount", "system", "os", "search", "calculator", "tip", "w3m"]

def generateClickableLink(link, altText):
    linkString = "\x1b]8;;https://{}/\a{}\x1b]8;;\a".format(link, altText)
    return(linkString)
