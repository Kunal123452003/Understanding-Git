def table(num=0):
    if num == 0:
         print("No table ")
    else:
        for i in range(num+1):
          for j in range(11):
            print(f"{i} X {j} = {i*j}")
    
table(3)

            