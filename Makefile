
README.md: gene_readme.py Wojtek_i_Smok_Adas.json Inne_bajki.json
	./gene_readme.py > README.md

url_count:
	jq -C '.url' *.json | sort | uniq -c | sort -nr | less -SR

title_count:
	jq -C '.title' *.json | sort | uniq -c | sort -nr | less -SR
