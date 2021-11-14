def checksum(x):
    return (x%256)

output=checksum(int(input("Enter a value for checksum: ")))
print("The checksum is "+str(output))
input("Press enter to exit...")

