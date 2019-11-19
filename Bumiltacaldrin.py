# COE 003 / CPE22FA1
# Datascience

# Programs and Contents


a = []

while True:
    
    print("MENU")
    print(" ")
    print("1.) Add Bookmarks")
    print("2.) Edit Bookmarks")
    print("3.) Delete Bookmarks")
    print("4.) View Bookmarks")
    print("5.) Exit")
    print(" ")
    
    x = input("What do you want to do ? ")

    if x == '1':
        print("----- Add Bookmarks-----")
        a_bm = input("Add Bookmarks:")
        a.append(a_bm)
        print(" ")

    elif x == '2':
        print("-----Edit Bookmarks-----")
        a_eb = input("Edit Bookmarks:")
        dex = a.index(a_eb)
        a.remove(a_eb)
        a_eb1 = input("New Bookmarks:")
        a.insert(dex,a_eb1)
        print(" ")

    elif x == '3':
        print("----- Delete Bookmarks-----")
        a_db = input("Delete Bookmarks:")
        a.remove(a_db)
        print(" ")
        
    elif x == '4':
        print("-----View Bookmarks-----")
        print(a)
        print(" ")
        
    elif x == '5':
        print("Thank you !!")
        break

