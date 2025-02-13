
def frequent_character(word: str):
    max_count = 0
    letter = ""
    counter_dict = {}

    for char in word:
        counter_dict[char] = counter_dict.get(char, 0) + 1
        
        if counter_dict[char] > max_count:
            max_count = counter_dict[char]
            letter = char

    return (letter, max_count)




def main():
    word = "absbsaa1Aassss"
    # Time complexity is O(n)
    print(frequent_character(word))

if __name__ == "__main__":
    main()
