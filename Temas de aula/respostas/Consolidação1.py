fhand = open('Consolidação1.txt', 'r')
x = []
y = []

for line in fhand:
    if line.startswith('x'):
        continue
    temp_x, temp_y = line.split(' ')
    temp_x = float(temp_x)
    temp_y = float(temp_y)
    
    x.append(temp_x)
    y.append(temp_y)
    
fhand.close()
print('x:', x, '\ny:', y)