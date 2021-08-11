handle = open('romeo.txt')

mail_count = dict()

for line in handle:
    if 'From' in line:
        mail = line.strip().split(' ')[1]
        mail_count[mail] = mail_count.get(mail, 0) + 1

greatest = 0
committer = None
for k, v in mail_count.items():
    if v > greatest:
        greatest = v
        committer = k
print(committer, greatest)
