entries = []
with open('publicationsDatabaseElmer.csv') as f:
    for line in f:
        formatedNewEntry = line[0:-1]
        print(formatedNewEntry)
        newData = formatedNewEntry.split(sep = ';')
        print(newData)
        entries.append(newData)
with open('listOfArticlesInHtmlFormat1.html', 'w') as f:
    for entry in entries:
        f.write(f'<li> \n   <a href= "{entry[2]}" > {entry[0]} </a> \n</li> \n')
