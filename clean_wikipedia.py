# Clean data from web-scraping
campioni = []

pattern = r"(.+?)\s\((.+)\)"  

with open('/home/anisa_bakiu/Downloads/university_towns.txt') as file:
    for line in file:
        line = line.strip()  
        if "[edit]\n" in line:
            state = line.replace("[edit]\n", "").strip()
        else:
            match = re.search(pattern, line)
            if match:
                city = match.group(1).strip()
                universities = match.group(2).strip()
                university_list = [u.strip() for u in universities.split(',')]
                for university in university_list:
                    campioni.append((state, city, university))
