if __name__ == "__main__":
    def count_numbers(arr):
        if len(arr) == 0:
            return 0
        return 1 + count_numbers(arr[1:])

    print(count_numbers([1, 2, 3, 4]))