def main():
    x = int(input("What's your first number? "))
    y = int(input("What's your second number? "))
    
    print(f"the sum of x and y is equal to: {_sum(x,y):,}")

def _sum(x,y):
    return x + y

main()

