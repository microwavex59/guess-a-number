event1={'Alice','Bob','Charlie','David','Eve'}
event2={'Charlie','David','Frank','Grace','Hannah'}
print(event1|event2)
print(event1&event2)
print(event1-event2)
if (event1.issubset(event2)):
    print("true")
else:
    print("false")
print(event1^event2)
