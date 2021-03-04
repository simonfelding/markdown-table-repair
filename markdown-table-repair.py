### Markdown table repair script. It sucks to align lengths manually.
### Lengths are set in first row. Cells are cut off if longer! There is a warning.

import sys

debug = 0
def debug(*args):
    if debug == 1:
        print(*args)
    else:
        pass
        

def get_table(filename):
    file1 = open(filename, 'r')
    lines = file1.readlines()
    table = []
    for line in lines:
        if line.startswith("|"):
            table.append(line.split("|")[:-1])
            debug(line.split("|")[:-1])
    print(f"Start table was like this:\n\n{table}")
    return table

def fix_table(table):
    # get amount of cells in first row
    cell_len = []
    for pos in range(0,len(table[0])):
        cell_len.append(len(table[0][pos]))
    debug("cell lengths: ",cell_len)

    # check if there are the correct amount of cells in rows
    rowno = 0
    for row in table:
        if len(row) != len(table[0]):
            debug(f"rowlen: {len(row)}, expected: {len(table[0])}")
            while len(row) < len(table[0]):
                debug("appending rows")
                debug(row)
                row.append("")
            if len(row) > len(table[0]):
                raise EOFError(f"too many rows in row {rowno}. content: \n {row}")
            debug(f"row {rowno} is now correct length.")
            debug(f"row was {table[rowno]}, now it is {row}")
            table[rowno] = row
        rowno += 1

    #  check if cells in rows are correct size
    global long_cells
    long_cells = {}
    rowno = 0
    for row in table:
        cellno = 0
        for cell in row:
            while len(cell) != cell_len[cellno]:
                if len(cell)>cell_len[cellno]:
                    debug("row ",rowno," cell",cellno, " is too long")
                    cell = table[rowno][cellno][:-1] # remove last character in cell if too long
                    long_cells[rowno] = cellno

                if len(cell)<cell_len[cellno]:
                    debug(len(cell), " < ",cell_len[cellno])
                    debug("row ",rowno," cell",cellno, " is too short")
                    cell = table[rowno][cellno]+" " # append space if too short
                table[rowno][cellno] = cell
            cellno += 1
        rowno += 1
    
    # finally, fix the |---| row. important if row size was changed.
    cellno = 0
    for cells in table[0]:
        newcell = ""
        for char in cells:
            newcell = newcell+"-"
        table[1][cellno] = newcell
        cellno += 1



    return table

def generate_table(table):
    output = ""
    for row in table:
        for cell in row:
            output = output + cell + "|"
        output = output + "\n"
    return output



if __name__ == "__main__":
    table = get_table(sys.argv[1])
    fixed_table = fix_table(table)
    print(f"\n\n---RESULT---\n\n\n\n{generate_table(fixed_table)}")
    
    if long_cells:
        print("\n\nWARNING: SOME CELLS WERE SHORTENED!\nIt was:")
        for key in long_cells:
            print(f"Row {key} cell {long_cells[key]}: {table[key][long_cells[key]]} -> {fixed_table[key][long_cells[key]]} ")

