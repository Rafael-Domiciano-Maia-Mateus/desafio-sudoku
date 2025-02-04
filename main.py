'''
Sudoku Solver
Implemente um solucionador de Sudoku. O programa deve receber um tabuleiro parcialmente preenchido como uma matriz 9x9 e 
tentar preencher os espaços vazios de forma válida, seguindo as regras do Sudoku.

Regras do Sudoku:

Cada linha deve conter números de 1 a 9 sem repetições.
Cada coluna deve conter números de 1 a 9 sem repetições.
Cada bloco 3x3 deve conter números de 1 a 9 sem repetições.

Objetivo: Preencher os zeros com números válidos.
'''


from collections import defaultdict

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_valid(board, num, row, col):
    if num in board[row]:
        return False
    
    if num in [board[i][col] for i in range(9)]:
        return False
    
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            if board[i][j] == num:
                return False
    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, row, col):
                        board[row][col] = num  
                        if solve_sudoku(board):  
                            return True
                        board[row][col] = 0  
                return False  
    return True  


def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


if solve_sudoku(board):
    print("Sudoku resolvido com sucesso:")
    print_board(board)
else:
    print("Não foi possível resolver o Sudoku.")
