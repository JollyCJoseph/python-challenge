import os
import csv
counties=[]
county_unique=[]
candidates=[]
candidates_unique=[]
total_votes=[]
vote1=[]
vote2=[]
vote3=[]
csvpath=os.path.join("Resources","election_data.csv")
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)
    for row in csvreader:
        total_votes.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
    for county in counties:
        if county not in county_unique:
                county_unique.append(county)
    for candidate in candidates:       
        if candidate not in candidates_unique:
                candidates_unique.append(candidate)
with open(csvpath) as csvfile:
        csvreader=csv.reader(csvfile,delimiter=',')
        csvheader=next(csvreader)
        for row in csvreader:            
            if row[2]==candidates_unique[0]:
                vote1.append(row[0])
            if row[2]==candidates_unique[1]:
                vote2.append(row[0])
            if row[2]==candidates_unique[2]:
                vote3.append(row[0])
if len(vote1)>len(vote2) and len(vote1)>len(vote3):
   winner=candidates_unique[0]
elif len(vote2)>len(vote1) and len(vote2) >len(vote3):
   winner=candidates_unique[1]  
else:
   winner=candidates_unique[2] 
#To export a txt file with the result
output_path=os.path.join("analysis","analysis.txt")
with open(output_path,'w') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["--------------"])
    csvwriter.writerow([f"Total votes: {len(total_votes)}"])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow([f"{candidates_unique[0]}: {(round(len(vote1)/len(total_votes)*100,3))}% ({(len(vote1))})"])
    csvwriter.writerow([f"{candidates_unique[1]}: {(round(len(vote2)/len(total_votes)*100,3))}% ({(len(vote2))})"])
    csvwriter.writerow([f"{candidates_unique[2]}: {(round(len(vote3)/len(total_votes)*100,3))}% ({(len(vote3))})"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([f"winner: {winner}"])
    csvwriter.writerow(["----------------------------------"])
#To print output to terminal   
print("Election Results\n")
print("-------------------\n")
print(f"Total votes: {len(total_votes)}\n")
print("-------------------\n")
print(f"{candidates_unique[0]}: {(round(len(vote1)/len(total_votes)*100,3))}% ({(len(vote1))})\n ")   
print(f"{candidates_unique[1]}: {(round(len(vote2)/len(total_votes)*100,3))}% ({(len(vote2))})\n ")
print(f"{candidates_unique[2]}: {(round(len(vote3)/len(total_votes)*100,3))}% ({(len(vote3))})\n ")
print("-------------------\n")
print(f"winner: {winner}\n")
print("-------------------\n")