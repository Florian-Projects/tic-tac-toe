x = [[1,2,3],[4,5,6],[7,8,9]]

def print_board(arr):
    test_str = "{:^30}".format("test")
    board = """
    {:^5}{:^5}{:^5}
    {:^5}{:^5}{:^5}
    {:^5}{:^5}{:^5}         
    """.format("1","2","3","4","5","6","72","80","90")
    print(board)

print_board(x)