def main(l):
    if len(l) >= 3:
        print(l[2])
        main(l[3:])
    return

if __name__ == "__main__":
    l = [i for i in range(1, 10)]
    main(l)