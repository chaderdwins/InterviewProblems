from csv import reader
from csv import DictReader

# with open("data.csv") as file:
#     my_csv = reader(file)#yields iterator object
#     next(my_csv)#skips the headers
#     for item in my_csv:
#         print(f"On {item[0]} at {item[1]} the {item[4]} will begin. It is a {item[7]}.")

with open("data.csv") as file:
    my_csv = DictReader(file)#yields iterator object
    # next(my_csv)#skips the headers
    for item in my_csv:
        print(f"On {item['Start Date ']} at {item['Start Time']} the {item['Event Title ']} will begin. It is a {item['Event Description']}.")
