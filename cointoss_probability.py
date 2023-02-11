import random
outcomes=["HEAD","TAIL"]
count_h=0
count_t=0
n=input("Enter the Number of Coin Tosses: ")
try:
   n=int(n)
except:
   print("Please Enter a Valid Integral Value")
for i in range(n):
  result=random.choice(outcomes)
  if result=="HEAD":
    count_h+=1
  else:
    count_t+=1
    result=random.sample(outcomes,k=1)
    if "HEAD" in result:
        count_h+=1
    else:
        count_t+=1
prob_head=round((count_h/(count_h+count_t)*100),2)
prob_tail=round((count_t/(count_h+count_t)*100),2)
print(f"Probability of HEAD is {prob_head}% and TAIL Count is {prob_tail}%")