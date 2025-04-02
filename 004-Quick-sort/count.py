def count_numbers(arr):
        if len(arr) == 0:
            return 0
        return 1 + count_numbers(arr[1:])

if __name__ == "__main__":    
    print(count_numbers([1, 2, 3, 4]))