entries = []
with open('bookChapters.csv') as f:
    for line in f:
        formatedNewEntry = line[0:-1]
        print(formatedNewEntry)
        newData = formatedNewEntry.split(sep = ';')
        print(newData)
        entries.append(newData)
with open('listOfBookChaptersInHtmlFormat1.html', 'w') as f:
    for entry in entries:
        f.write(f'<li> \n   <a href= "{entry[3]}" > {entry[0]} </a> in {entry[1]}\n</li> \n')
