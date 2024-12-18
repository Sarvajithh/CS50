def main():
    x = int(input("Enter the number: "))
    print(f"{x} sqaured is ",square(x))

def square(x):
    return x*x

if __name__ == "__main__":  
    main()