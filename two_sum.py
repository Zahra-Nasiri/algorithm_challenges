
def two_sum(array: list, search_sum: int) -> tuple:
    num_map = {}
    # num_map = {value: index}

    i = 0

    for i, num in enumerate(array):
        complement = search_sum - num  

        if complement in num_map:  
            return (num_map[complement], i)

        num_map[num] = i 


    return ()




def main():
    array = [2, 1, 5, 3]
    search_sum = 8
    # Time complexity is O(n)
    print(two_sum(array=array, search_sum=search_sum))

    

if __name__ == "__main__":
    main()
