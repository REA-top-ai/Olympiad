def get_right_vector(forward_vec: list) -> tuple:
    return (forward_vec[1], -forward_vec[0])

def process_move(moves:list, forward_vec:list) -> tuple:
    # return move_vec
    right_vec = get_right_vector(forward_vec)
    result = [0,0]
    for command in moves:
        move_vec = []
        match command:
            case 'F': move_vec = forward_vec
            case 'B': move_vec = [x*-1 for x in forward_vec]
            case 'R': move_vec = right_vec
            case 'L': move_vec = [x*-1 for x in right_vec]
        result[0] += move_vec[0]
        result[1] += move_vec[1]
    return result         

def process_rotation(rotators:list, forward_vec:list) -> tuple[tuple]:
    # return new forward_vec
    right_vec = get_right_vector(forward_vec)
    for rotator in rotators:
        if rotator==')':
            forward_vec, right_vec = right_vec, [x*-1 for x in forward_vec]
        else:
            forward_vec, right_vec = [x*-1 for x in right_vec], forward_vec
    return forward_vec

def process_action(action:str, pos:list, forward_vec:list) -> tuple[tuple]:
    # proces single action
    # return new pos and forward_vec
    right_vec = get_right_vector(forward_vec)
    if action == '(' or action == ')':
        forward_vec = process_rotation([action], forward_vec)
    else:
        move_vec = process_move([action], forward_vec)
        pos[0] += move_vec[0]
        pos[1] += move_vec[1]
    return pos, forward_vec

def loop(n, body:list, pos:list, forward_vec:list) -> tuple[tuple]: 
    # return new pos, forwrd_vec, rgiht_vec
    for i in range(n):
        for c in body:
            pos,forward_vec = process_action(c,pos,forward_vec)
    return pos,forward_vec



def findCoords(pg:str) -> tuple:
    pos = [0,0]

    forward_vec = [0,1]

    i = 0
    while i < len(pg):
        if pg[i].isdigit():
            n=''
            while pg[i] != '[':
                n,i = n+pg[i], i+1
            i+=1
            n = int(n)
            loop_body = []
            while pg[i] != ']':
                loop_body.append(pg[i])
                i+=1
            pos,forward_vec = loop(n, loop_body, pos, forward_vec)
        else:
            pos,forward_vec = process_action(pg[i], pos, forward_vec)
        i+=1

    return pos[0], pos[1]



#program = input()
program = "1000000000[F)]"

print(findCoords(program))