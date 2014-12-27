#!/usr/bin/env python
"""
code to modify NASA ASD bibtex format files so that, 
	(a) the journal entry shows the arXiv number with hyperlink if the
	eprint is unpublished. 
	(b) optionally, adds the eprint to the journal entry, so that the 
	citation shows the arXiv reference in addition to the journal entry.


R. Biswas, Thu Aug 15 19:18:45 CDT 2013


"""

import sys


def getarticlesfrombib(fname): 
	"""
	obtains a list of articles and their entries from a bibtex file by 
	searching for the string "@article" in any (mixed, lower, upper) case,  	and assuming that everything till the next occurance of article or EOF
	is part of that entry.

	args:
		fname:

	returns:
	example usage :
	status:
	todo:

	"""
	f = open (fname)
	articles = []
	s = ""
	line = f.readline()
	#print line
	#sys.exit()
	while line !="" :
		if "@ARTICLE" in line.upper():
			#print "FOUND", line
			if s.find("ARTICLE"):
				articles.append(s)
			s = ""
		s += line 
		line  = f.readline()
	
	f.close()
	if "ARTICLE" in s.upper():
		articles.append(s)

	return articles

def dividearticlestofields(article):
	"""

	"""
	fields = article.split("\n")
	divided = {}
	for field in fields:
		#print "FIELD: ", field
		if "=" in field:
			fsplit = field.split("=")
			#print "fs", fsplit
			divided[fsplit[0].strip()] = fsplit[-1].strip()

	return fields , divided


fname = "PTtest.bib"
articles =  getarticlesfrombib ( fname )
for article in articles:
	print article
print "++++++++"
print dividearticlestofields(articles[-1])[1]["journal"]
print dividearticlestofields(articles[-1])[1]["eprint"]
