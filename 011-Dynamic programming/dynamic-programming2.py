if __name__ == "__main__":
    word1 = list("fosh")
    word2 = list("fish")

    matrix = [[0 for _ in range(len(word1))] for _ in range(len(word2))]

    maxi_letters = ""
    maxi = 0

    for i in range(len(word2)):
        for j in range(len(word1)):
            if word2[i] == word1[j]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > maxi:
                    maxi = matrix[i][j]
                    maxi_letters += word1[j]
            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])

    print(*matrix, sep="\n")
    print(maxi_letters)
