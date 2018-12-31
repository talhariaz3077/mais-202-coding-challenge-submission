#importing libraries for reading csv and plotting graph
import csv
import matplotlib.pyplot as plt

#accessing file
with open('data.csv') as file:
    reader = csv.DictReader(file)
    #making corresponding lists for data
    purpose_list = ['car', 'credit_card', 'debt_consolidation', 'home_improvement', 'house', 'major_purchase', 'medical', 'moving', 'other', 'small_business', 'vacation', 'wedding']
    
    int_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    int_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    int_avg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #saving relevant data in lists
    for row in reader:
        index = purpose_list.index(row['purpose'])
        int_sum[index] = int_sum[index] + float(row['int_rate'])
        int_count[index] = int_count[index] + 1

count = 0
#calculating average
while count < len(purpose_list):
    int_avg[count] = round(int_sum[count]/int_count[count], 3)
    count += 1
#plotting bar chart
barlist = plt.bar(purpose_list, int_avg)
#labelling axes
plt.xlabel('purpose')
plt.ylabel('mean(int_rate)')
#setting tick parameters
plt.tick_params(axis='x', labelsize=5)

plt.grid(b=bool, which='major', axis='y', linestyle='dashed')

#setting bar colors
barlist[0].set_color('seagreen')
barlist[1].set_color('coral')
barlist[2].set_color('grey')
barlist[3].set_color('hotpink')
barlist[4].set_color('yellowgreen')
barlist[5].set_color('gold')
barlist[6].set_color('wheat')
barlist[7].set_color('silver')
barlist[8].set_color('seagreen')
barlist[9].set_color('coral')
barlist[10].set_color('grey')
barlist[11].set_color('hotpink')

#displaying plotted chart
plt.show()
