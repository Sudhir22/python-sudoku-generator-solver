from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context,loader
import random,copy
from .models import Results
# Create your views here.

def index(request):
    #Sample insert into the database
    '''
    result1=Results()
    result1.age = 20
    result1.student_name = "Sudhir"
    result1.task_selected = "Sudoku"
    result1.task_outcome = "Correct"
    result1.save()
    '''

    results = run(n=40)       # find puzzles with as few givens as possible.
    puzzle  = best(results)  # use the best one of those puzzles.
    template=loader.get_template("sudoku_solver/index.html")
    context={'cell1':puzzle[0][0],'cell2':puzzle[0][1],'cell3':puzzle[0][2],'cell4':puzzle[0][3],
             'cell5':puzzle[0][4],'cell6':puzzle[0][5],'cell7':puzzle[0][6],'cell8':puzzle[0][7],
             'cell9':puzzle[0][8],'cell10':puzzle[1][0],'cell11':puzzle[1][1],'cell12':puzzle[1][2],
             'cell13':puzzle[1][3],'cell14':puzzle[1][4],'cell15':puzzle[1][5],'cell16':puzzle[1][6],
             'cell17':puzzle[1][7],'cell18':puzzle[1][8],'cell19':puzzle[2][0],'cell20':puzzle[2][1],
             'cell21':puzzle[2][2],'cell22':puzzle[2][3],'cell23':puzzle[2][4],'cell24':puzzle[2][5],
             'cell25':puzzle[2][6],'cell26':puzzle[2][7],'cell27':puzzle[2][8],'cell28':puzzle[3][0],
             'cell29':puzzle[3][1],'cell30':puzzle[3][2],'cell31':puzzle[3][3],'cell32':puzzle[3][4],
             'cell33':puzzle[3][5],'cell34':puzzle[3][6],'cell35':puzzle[3][7],'cell36':puzzle[3][8],
             'cell37':puzzle[4][0],'cell38':puzzle[4][1],'cell39':puzzle[4][2],'cell40':puzzle[4][3],
             'cell41':puzzle[4][4],
             'cell42':puzzle[4][5],'cell43':puzzle[4][6],'cell44':puzzle[4][7],'cell45':puzzle[4][8],
             'cell46':puzzle[5][0],'cell47':puzzle[5][1],'cell48':puzzle[5][2],'cell49':puzzle[5][3],
             'cell50':puzzle[5][4],'cell51':puzzle[5][5],'cell52':puzzle[5][6],'cell53':puzzle[5][7],
             'cell54':puzzle[5][8],'cell55':puzzle[6][0],'cell56':puzzle[6][1],'cell57':puzzle[6][2],
             'cell58':puzzle[6][3],'cell59':puzzle[6][4],'cell60':puzzle[6][5],'cell61':puzzle[6][6],
             'cell62':puzzle[6][7],'cell63':puzzle[6][8],'cell64':puzzle[7][0],'cell65':puzzle[7][1],
             'cell66':puzzle[7][2],'cell67':puzzle[7][3],'cell68':puzzle[7][4],'cell69':puzzle[7][5],
             'cell70':puzzle[7][6],'cell71':puzzle[7][7],'cell72':puzzle[7][8],'cell73':puzzle[8][0],
             'cell74':puzzle[8][1],'cell75':puzzle[8][2],'cell76':puzzle[8][3],'cell77':puzzle[8][4],
             'cell78':puzzle[8][5],'cell79':puzzle[8][6],'cell80':puzzle[8][7],'cell81':puzzle[8][8]}
    return render(request,"sudoku_solver/index.html",context)

def homepage(request):
    return render(request,"sudoku_solver/homepage.html")

def homepage_2(request):
    return render(request,"sudoku_solver/homepage_2.html")

def task(request):
    return render(request,"sudoku_solver/game.html")

def second_task(request):
    return render(request,"sudoku_solver/second_game.html")

"""
SUDOKU (NUMBER PLACE) PUZZLE GENERATOR
by Arel Cordero November 12, 2005

This program is released into the public domain.
Revision 3
"""
sample  = [ [3,4,1,2,9,7,6,8,5],
            [2,5,6,8,3,4,9,7,1],
            [9,8,7,1,5,6,3,2,4],
            [1,9,2,6,7,5,8,4,3],
            [8,7,5,4,2,3,1,9,6],
            [6,3,4,9,1,8,2,5,7],
            [5,6,3,7,8,9,4,1,2],
            [4,1,9,5,6,2,7,3,8],
            [7,2,8,3,4,1,5,6,9] ]
            
"""
Randomly arrange numbers in a grid while making all rows, columns and
squares (sub-grids) contain the numbers 1 through 9.

For example, "sample" (above) could be the output of this function. """
def construct_puzzle_solution():
    # Loop until we're able to fill all 81 cells with numbers, while
    # satisfying the constraints above.
    while True:
        try:
            puzzle  = [[0]*9 for i in range(9)] # start with blank puzzle
            rows    = [set(range(1,10)) for i in range(9)] # set of available
            columns = [set(range(1,10)) for i in range(9)] #   numbers for each
            squares = [set(range(1,10)) for i in range(9)] #   row, column and square
            for i in range(9):
                for j in range(9):
                    # pick a number for cell (i,j) from the set of remaining available numbers
                    choices = rows[i].intersection(columns[j]).intersection(squares[(int(i/3))*3 + int(j/3)])
                    choice  = random.choice(list(choices))
        
                    puzzle[i][j] = choice
        
                    rows[i].discard(choice)
                    columns[j].discard(choice)
                    squares[(int(i/3))*3 + int(j/3)].discard(choice)

            # success! every cell is filled.
            return puzzle
            
        except IndexError:
            # if there is an IndexError, we have worked ourselves in a corner (we just start over)
            pass

"""
Randomly pluck out cells (numbers) from the solved puzzle grid, ensuring that any
plucked number can still be deduced from the remaining cells.

For deduction to be possible, each other cell in the plucked number's row, column,
or square must not be able to contain that number. """
def pluck(puzzle, n=0):

    """
    Answers the question: can the cell (i,j) in the puzzle "puz" contain the number
    in cell "c"? """
    def canBeA(puz, i, j, c):
        v = puz[int(c/9)][c%9]
        if puz[int(i)][int(j)] == v: return True
        if puz[int(i)][int(j)] in range(1,10): return False
            
        for m in range(9): # test row, col, square
            # if not the cell itself, and the mth cell of the group contains the value v, then "no"
            if not (m==int(c/9) and j==c%9) and puz[m][j] == v: return False
            if not (i==int(c/9) and m==c%9) and puz[i][m] == v: return False
            if not ((int(i/3))*3 + int(m/3)==int(c/9) and (int(j/3))*3 + m%3==c%9) and puz[(int(i/3))*3 + int(m/3)][(int(j/3))*3 + m%3] == v:
                return False

        return True


    """
    starts with a set of all 81 cells, and tries to remove one (randomly) at a time
    but not before checking that the cell can still be deduced from the remaining cells. """
    cells     = set(range(81))
    cellsleft = cells.copy()
    while len(cells) > n and len(cellsleft):
        cell = random.choice(list(cellsleft)) # choose a cell from ones we haven't tried
        cellsleft.discard(cell) # record that we are trying this cell

        # row, col and square record whether another cell in those groups could also take
        # on the value we are trying to pluck. (If another cell can, then we can't use the
        # group to deduce this value.) If all three groups are True, then we cannot pluck
        # this cell and must try another one.
        row = col = square = False

        for i in range(9):
            if i != cell/9:
                if canBeA(puzzle, i, cell%9, cell): row = True
            if i != cell%9:
                if canBeA(puzzle, int(cell/9), i, cell): col = True
            if not ((int(int(cell/9)/3))*3 + int(i/3) == int(cell/9) and (int(cell/9)%3)*3 + i%3 == cell%9):
                if canBeA(puzzle, (int(int(cell/9)/3))*3 + int(i/3), (int(cell/9)%3)*3 + i%3, cell): square = True

        if row and col and square:
            continue # could not pluck this cell, try again.
        else:
            # this is a pluckable cell!
            puzzle[int(cell/9)][cell%9] = 0 # 0 denotes a blank cell
            cells.discard(cell) # remove from the set of visible cells (pluck it)
            # we don't need to reset "cellsleft" because if a cell was not pluckable
            # earlier, then it will still not be pluckable now (with less information
            # on the board).

    # This is the puzzle we found, in all its glory.
    return (puzzle, len(cells))
    
    
"""
That's it.

If we want to make a puzzle we can do this:
    pluck(construct_puzzle_solution())
    
The following functions are convenience functions for doing just that...
"""



"""
This uses the above functions to create a new puzzle. It attempts to
create one with 28 (by default) given cells, but if it can't, it returns
one with as few givens as it is able to find.

This function actually tries making 100 puzzles (by default) and returns
all of them. The "best" function that follows this one selects the best
one of those.
"""
def run(n = 2, iter=40):
    all_results = {}
    print ("Constructing a sudoku puzzle.")
    print ("* creating the solution...")
    a_puzzle_solution = construct_puzzle_solution()
    print(a_puzzle_solution)
    print ("* constructing a puzzle...")
    for i in range(iter):
        puzzle = copy.deepcopy(a_puzzle_solution)
        (result, number_of_cells) = pluck(puzzle, n)
        all_results.setdefault(number_of_cells, []).append(result)
        if number_of_cells <= n: break

    return all_results

def best(set_of_puzzles):
    # Could run some evaluation function here. For now just pick
    # the one with the fewest "givens".
    return set_of_puzzles[min(set_of_puzzles.keys())][0]

def display(puzzle):
    for row in puzzle:
        print (' '.join([str(n or '_') for n in row]))

def end_game(request):

    # Get the post variables
    #solution = request.POST['solution']
    resu = request.POST.get('resu',False)
    hours=request.POST.get('hours',False)
    age=request.POST.get('age',False)
    gender=request.POST.get('gender',False)
    lass=request.POST.get('lass',False)
    subjects=request.POST.get('subjects',False)
    fav=request.POST.get('fav',False)
    ID=request.POST.get('ID',False)
    task_selected=request.POST.get('task_selected',False)
    task1_selection=request.POST.get('task1_selection',False)
    task2_selection=request.POST.get('task2_selection',False)
    task2_colour=request.POST.get('task2_colour',False)
    '''
    Not required now since separate systems

    age2=request.POST.get('age2',False)
    gender2=request.POST.get('gender2',False)
    lass2=request.POST.get('lass2',False)
    subjects2=request.POST.get('subjects2',False)
    fav2=request.POST.get('fav2',False)
    '''

    
    resuk=Results()
    resuk.task_selected=task_selected
    resuk.time_taken=hours
    resuk.token=ID
    resuk.age=age
    resuk.gender=gender
    resuk.standard=lass
    resuk.subjects=subjects
    resuk.favorite=fav
    resuk.task_outcome=resu
    resuk.task1_selection=task1_selection
    resuk.task2_selection=task2_selection
    resuk.task2_colour=task2_colour
    
    '''
            Not required now since separate systems

    resuk.age_2=age2
    resuk.gender_2=gender2
    resuk.standard_2=lass2
    resuk.subjects_2=subjects2
    resuk.favorite_2=fav2
    '''
    resuk.save()
    # You may want to validate data here

    try:

        # Setting output
        response = {
            'status': 1,
            'message': 'saved'
        }
    except Exception as e:

        # Something went wrong
        response = {
            'status': 0,
            'message': 'Something went wrong - ' +str(e) 
        }
    return HttpResponse(response,content_type='application/json')

    
""" Controls starts here """
#results = run(n=0)       # find puzzles with as few givens as possible.
#puzzle  = best(results)  # use the best one of those puzzles.
#display(puzzle)          # display that puzzle.