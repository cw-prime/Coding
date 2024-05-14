# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"
import time

#Start code below this line:

duration = 5
start_time = time.time()
counter = 0
while (time.time() - start_time) < duration:  
    counter += 1
    print(f" {counter} Mississippi")
    time.sleep(1)   
    if counter == 5:
        time.sleep(2)
        print("Ready or not, here I come!")
        print(time.strftime("%Y-%A"))
      
      
        
