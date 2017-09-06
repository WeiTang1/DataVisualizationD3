import csv
BORO=['BROOKLYN', 'MANHATTAN', 'QUEENS', 'BRONX', 'STATEN ISLAND', 'Missing']
CUISINE_TYPE=['American', 'Chinese', 'Latin (Cuban, Dominican, Puerto Rican, South & Central American)', 'Mexican', 'Tex-Mex', 'Japanese', 'Seafood', 'Pizza', 'Pizza/Italian', 'Caf\xc3\x83\xc2\xa9/Coffee/Tea', 'Donuts', 'Hamburgers', 'Ethiopian', 'Italian', 'French', 'Hotdogs/Pretzels', 'Asian', 'Chicken', 'Greek', 'Sandwiches', 'Caribbean', 'Bagels/Pretzels', 'Thai', 'Spanish', 'Juice, Smoothies, Fruit Salads', 'Korean', 'Indian', 'Tapas', 'African', 'Middle Eastern', 'Ice Cream, Gelato, Yogurt, Ices', 'Sandwiches/Salads/Mixed Buffet', 'Delicatessen', 'Bottled beverages, including water, sodas, juices, etc.', 'Bakery', 'Polish', 'Hotdogs', 'Continental', 'Jewish/Kosher', 'Pakistani', 'Vegetarian', 'Irish', 'Other', 'Barbecue', 'Russian', 'Creole', 'Steak', 'Turkish', 'Vietnamese/Cambodian/Malaysia', 'Chinese/Cuban', 'Fruits/Vegetables', 'Mediterranean', 'Peruvian', 'Armenian', 'Egyptian', 'Soul Food', 'English', 'Brazilian', 'Indonesian', 'Chinese/Japanese', 'Afghan', 'Salads', 'Australian', 'Filipino', 'German', 'Bangladeshi', 'Scandinavian', 'Southwestern', 'Chilean', 'Soups & Sandwiches', 'Eastern European', 'Iranian', 'Portuguese', 'Pancakes/Waffles', 'Moroccan', 'Not Listed/Not Applicable', 'Creole/Cajun', 'Cajun', 'Nuts/Confectionary', 'Czech', 'Hawaiian', 'Californian', 'Polynesian', 'Soups']
Critical_flag = ['Not Critical', 'Critical', 'Not Applicable']
Grade = ['A', 'B', 'P', 'C', 'Z', 'Not Yet Graded']

# with open('result.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         if row[14] not in Grade:
#             Grade.append(row[14])


# csvfile.close()
# print Grade

result = open("test.csv","wb")
spamwriter = csv.writer(result)
with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    spamwriter.writerow( next(reader,None))
    for row in reader :
        if row[0]=='' or row[2]=='' or row[3] == '' or row[5]=='' or row[6]=='' or row[7]==''or row[10]=='' or row [12]=='' or row[13]=='' or row[14]=='' or (not row[6].isdigit()) or (not row[3].isdigit()):
            continue
        else:
            row[2] = BORO.index(row[2])
            row[7] = CUISINE_TYPE.index(row[7])
            row[10] = row[10][:-1]
            row[12] = Critical_flag.index(row[12])
            row[14] = Grade.index(row[14])


        spamwriter.writerow(row)
result.close()
csvfile.close()

for i in CUISINE_TYPE:
    print i,CUISINE_TYPE.index(i)