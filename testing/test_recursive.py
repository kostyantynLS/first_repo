def sum(num, StartFrom = 0) -> int:
    if num==0:   
        return 0
    else:
        return (StartFrom+num)+sum(num-1, StartFrom=StartFrom)
    
print(sum(2, StartFrom=30))

line="ABC"

for index, char in enumerate(reversed(line)):
    print(index, '=', char)
