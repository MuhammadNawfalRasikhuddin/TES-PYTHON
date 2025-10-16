def calculator (a,b, operation):
    if(operation == "tambah"):
        return a+b
    
    elif(operation == "kali"):
        return a*b
    
    elif(operation == "bagi"):
        return a%b
    
    elif(operation == "kurang"):
        return a-b
    return operation

print(calculator(9,9,"bagi"))