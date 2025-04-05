def diamond():
    for i in range(5):
        x='* '
        x=x*i
        print(f"{x:^10}")
    for i in range(5):
        x='* '
        x=x*(5-i)
        print(f"{x:^10}")
    


if __name__ == "__main__":
    diamond()