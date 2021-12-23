done = 'not done'
total = 0
count = 0
while done != 'done' :
    
    try:
        done = input("Enter a number: ")
        b = int(done)
        total += b
        count+=1
    except: 
        if done == 'done' :
            break
        print("Invalid input")
print(total, count, total/count)

