if __name__ == "__main__":
    def quick_sort(arr):
        if len(arr) <= 1 :
            return arr
        else:
            mid = arr[len(arr)//2]

            l = list()
            r = list()
            e = list()

            for n in arr:
                if n < mid:
                    l.append(n)
                elif n > mid:
                    r.append(n)
                else:
                    e.append(n)

            return quick_sort(l) + e + quick_sort(r)

    print(quick_sort([4, 1, 6, 3, 2, 7, 8]))

            
