import csv
from statistics import mean
with open ("DATA475_lab_rectangles_data.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader) 


    # count=0
    # total_area=0
    # max_area=0
    # min_area=10000000

    rects = []
    
    for row in reader:
        width = float(row[1])
        length = float(row[2])
        area = width * length

        rects.append(area)
     
     

    #  mcount +- 1
   #  total_area +- area

  # if area < min_area:
# min_area = area

# if area > max_area

#print(=len(rects))
#print(max(rects))
#print(min(rects))
#print(sum(rects))
#print(mean(rects))

summary=[
    ("count", len(rects)),
    ("max", max(rects)),
    ("min", min(rects)),
    ("sum", sum(rects)),
    ("ave", mean(rects)),
]
for key, value in summary:
    print(f"{key}; {value}") 

    with open ("summary.csv", "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([item[0] for item in summary])
        writer.writerow([item[1] for item in summary])
