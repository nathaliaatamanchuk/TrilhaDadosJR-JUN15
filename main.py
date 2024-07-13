import os

data = 'course_data.txt'
archive = 'selling_courses_data.csv'
read_data = ''

if not os.path.isfile(archive):
    with open (data, 'r', encoding='utf-8-sig') as open_file, \
         open(archive, 'w', encoding='utf-8-sig') as file:
        for line in open_file:
            read_data = line.replace(',', ';')
            file.write(read_data)