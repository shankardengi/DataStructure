lists = []
def read_element(n):
    for i in range(n):
        lists.append(int(input("Enter Element:")))

def buble_sort(n):
    for i in range(n):
        for j in range(n-i):
            if j < n-1 :
                if lists[j]>lists[j+1]:
                    temp =  lists[j]
                    lists[j] = lists[j+1]
                    lists[j+1] = temp

if __name__ == "__main__":
    n = int(input("Enter size of elements for buble sort:"))
    read_element(n)
    buble_sort(n)
    for i in lists:
        print(i)