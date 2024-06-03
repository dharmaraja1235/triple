import pandas as pd

print("this is gym shedule")

g={"monday":["chest","tricep"],"tuesday":["back","bicep"],"wednesday":["shoulder","leg"],"thursday":["chest","tricep"],"friday":["back","bicep"],"saturday":["should","leg"],"sunday":["rest"]}

dhar=pd.DataFrame(g,
index=["day1 ","day 2"])
print(dhar)