
def sorted_two_sum(sorted_array: list, search_sum: int) -> tuple:
    left = 0
    right = len(sorted_array) - 1
    
    while left != right:
        if search_sum == sorted_array[left] + sorted_array[right]:
            return (sorted_array[left], sorted_array[right])
        elif search_sum < sorted_array[left] + sorted_array[right]:
            right -= 1
        else:
            left += 1
        
    return ()



def main():
    sorted_array = [1, 2, 3, 4, 6, 8]
    search_sum = 7
    # Time complexity is O(n)
    print(sorted_two_sum(sorted_array=sorted_array, search_sum=search_sum))

    

if __name__ == "__main__":
    main()
