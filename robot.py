for box in range (1,5):
    print(box,"Box")
    for product in range(1,6):
        if product == 5:
           print("Box is full")
        else:
           print(product,"Product is added to the box")
           continue
