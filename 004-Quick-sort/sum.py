def sum_numbers(arr):
        if len(arr) == 0:
            return 0
        return arr[0] + sum_numbers(arr[1:])

if __name__ == "__main__":
    print(sum_numbers([1, 2, 3, 4]))