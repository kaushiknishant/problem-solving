def generate(num_rows):
    triangle = []

    for row_num in range(num_rows):
        # The first and last row elements are always 1.
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, len(row)-1):
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

        triangle.append(row)

    return triangle
def factorial(num):
    if num <= 1:
        return 1
    return num*factorial(num-1)

def calculate_element(row,col):
    print(factorial(row-1))
    return factorial(row-1)/factorial(col-1)*factorial(((row-1)-(col-1)))

if __name__ == '__main__':
    depth = 5
    # res = generate(depth)
    res = calculate_element(5,3)
    print(res)    