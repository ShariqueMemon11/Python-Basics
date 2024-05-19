Members = []
max_trip = 1

#getting data for trips: Members , Expenses etc
#And also making sure that members in a single trip should be less than 1000
#And expense for a single member should be less than $10000.00
while max_trip != 5:

    trip_data = {'trip': max_trip, 'members': [] , 'total_expense':0 , 'avg_expense_per_member':0, 'Amount_exchanged_to_equalize':0}
    overspent = {'trip': max_trip, 'members': [] , 'difference':0}
    underspent = {'trip': max_trip, 'members': [] , 'difference':0}
    counter = 0

    print("Trip", max_trip)

    while True:
        name = input("Enter Member name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        member_expense = float(input("Enter Expense: "))
        if member_expense>10000.00:
            member_expense = float(input("Enter Expense : it should not be more than 10000.00\n"))
        trip_data['members'].append({'Name': name, 'Expense': member_expense})

        #adding Expense of every member in total expense if that trip
        trip_data['total_expense']+= member_expense
        counter += 1

        #calculating avg expense per member for that trip 
        trip_data['avg_expense_per_member']=trip_data['total_expense']/counter
        if counter == 1000:
            break

    Members.append(trip_data)
    extra_trip = input(f"Want to enter data for trip {max_trip + 1} (or type 0 to stop): ")
    if extra_trip == "0":
        break
    max_trip += 1

#making two lists to sort the one's that overspent and the one's that underspent 
for trip in Members:
    overspent = [] 
    underspent = []
    for member in trip['members']:
         difference = member['Expense'] - trip['avg_expense_per_member']
         if difference > 0:
            overspent.append({'Name': member['Name'], 'Expense': member['Expense'], 'Difference': difference})
         elif difference < 0:
            underspent.append({'Name': member['Name'], 'Expense': member['Expense'], 'Difference': abs(difference)}) 
    
    #sorting the list in Decending order on the bases of Difference
    overspent.sort(key=lambda x: x['Difference'],reverse=True)
    underspent.sort(key=lambda x: x['Difference'],reverse=True)
    
    #Redistributing: Transfer money between members to balance out the differences: 
    i=0        
    j=0
    total_exchanged=0
    while i<len(underspent) and j<len(overspent):  
      Extra_amount=min(underspent[i]['Difference'],overspent[j]['Difference'])
      underspent[i]['Difference']-=Extra_amount
      overspent[j]['Difference']-=Extra_amount
      total_exchanged+=Extra_amount
      if overspent[j]['Difference']==0:
        j+=1
      if underspent[i]['Difference']==0:
        i+=1
    trip['Amount_exchanged_to_equalize']=total_exchanged    

# printing data of every trip with there total expense and total amount that need to be exchanged to equalize
print("\nList of Members with their Expenses for each Trip:")
for trip in Members:
    print(f"  Total Expense for Trip {trip['trip']}: {trip['total_expense']}")
    for member in trip['members']:
        print(f"  Name: {member['Name']}, Expense: {member['Expense']}")
    print(f"Total amount that need to be exchanged = {trip['Amount_exchanged_to_equalize']}")    
   