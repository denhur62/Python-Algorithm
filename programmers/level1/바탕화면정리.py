def solution(wallpaper):
    row_min,row_max  = float('inf'), -1
    col_min, col_max = float('inf'), -1
    for row_idx,row in enumerate(wallpaper):
        for col_idx,col in enumerate(row):
            if col == '#':
                if row_min > row_idx :
                    row_min = row_idx
                if row_max < row_idx :
                    row_max = row_idx
                if col_min > col_idx :
                    col_min = col_idx
                if col_max < col_idx :
                    col_max = col_idx
    
    answer = [row_min, col_min, row_max+1, col_max+1]
    return answer



wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
print(solution(wallpaper))
#1358