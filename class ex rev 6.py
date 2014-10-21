#Gemma Buckle 21/10/2014
#iteration class ex rev 5 pounds to kg

pound=1
kg=0.45
print("pounds = kg")
for pound in range(1,21):
    kg_value=pound*kg
    print("{0:>6} = {1:<3.2f}".format(pound, kg_value))
