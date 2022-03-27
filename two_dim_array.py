def two_d_array(row, col):
    arr = []
    for i in range(row):
        colum = []
        arr.append(colum)  # Rows
        for j in range(col):
            colum.append(int(input("Enter the number: ")))  # Columns number
    return arr


if __name__ == "__main__":
    rows = int(input("Enter the No of rows: "))
    columns = int(input("Enter the No of Columns: "))
    print(two_d_array(rows, columns))

