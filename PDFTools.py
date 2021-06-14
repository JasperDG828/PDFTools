import tools as t
print("===PDFTools By JasperDG===")
print("Ver. 21.6.14")
print()
print("use 'help' for more info")
while True:
    cmd = input("> ")
    if cmd=="merge":
        t.merge()
    elif cmd=="info":
        t.getInformation()
    elif cmd=="mergeOddEven":
        t.mergeOddEven(None, None, None, True)
    elif cmd=="help":
        print("")
        print("===PDFTools Help===")
        print("")
        print("> info            Displays information about the selected document")
        print("> merge           Merges the selected documents")
        print("> mergeOddEven    Merges document containing odd pages and document containing even pages")
        print("> help            Displays this message")
        print("> quit            Exit")
        print("")
    elif cmd=="quit":
        exit()
    else:
        print("Invalid command, use 'help' for more information")
    