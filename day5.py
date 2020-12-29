path = "day5.txt"
data_file = open(path, 'r')

data = data_file.read().splitlines()

ticket_id = lambda x: x[0] * 8 + x[1]

def get_ticket_row_column(data_row):
    row_string = ''
    column_string = ''
    for r in data_row[0:-3]:
          row_string = row_string + ('0' if r == 'F' else '1')
    row = int(row_string, 2)
    
    for c in data_row[-3:]:
        column_string = column_string + ('0' if c == 'L' else '1')
    column = int(column_string, 2)

    return (row, column)

tickets = [get_ticket_row_column(r) for r in [list(d) for d in data]]

ticket_ids = [ticket_id(t) for t in tickets]

print('max ticket ID:', max(ticket_ids))

for i in range(0,935):
    if i not in ticket_ids and i-1 in ticket_ids and i+1 in ticket_ids:
        print('Your seat ID:', i)