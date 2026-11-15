def get_right_vector(forward_vec: list) -> tuple:
    return (forward_vec[1], -forward_vec[0])

def process_move(move:str) -> tuple:
    # return local coords for move
    match move:
        case 'F': return (0,1)
        case 'B': return (0,-1)
        case 'R': return (1,0)
        case 'L': return (-1,0)

def transform_vec(vector:tuple, forward_vec: list) -> tuple: 
    # return global transform from local
    right_vec = get_right_vector(forward_vec)
    x,y = vector
    return (
        x * right_vec[0] + y * forward_vec[0],
        x * right_vec[1] + y * forward_vec[1],
    )  

def process_rotation(rotators:list, forward_vec:list) -> tuple:
    # new forward_vec after rotations
    for rotator in rotators:
        if rotator == ')':
            forward_vec = list(get_right_vector(forward_vec))
        else:
            forward_vec = [-forward_vec[1], forward_vec[0]]

    return forward_vec

def process_action(action:str, pos:list, forward_vec:list) -> tuple[tuple]:
    # proces single action
    # return new pos and forward_vec
    if action == '(' or action == ')':
        forward_vec = process_rotation([action], forward_vec)
    else:
        move_vec = transform_vec(process_move(action), forward_vec)
        pos[0] += move_vec[0]
        pos[1] += move_vec[1]
    return pos, forward_vec

def loop(n, loop_body:list, pos:list, forward_vec:list) -> tuple[tuple]: 
    # return new pos, forwrd_vec
    body_delta, body_forward_vec = loop_body
    if body_forward_vec == [0,1]:
        move_vec = transform_vec(body_delta, forward_vec)
        pos[0] += n*move_vec[0]
        pos[1] += n*move_vec[1]
    else:
        for _ in range(n%4):
            move_vec = transform_vec(body_delta, forward_vec)
            pos[0] += move_vec[0]
            pos[1] += move_vec[1]

            forward_vec = list(
                transform_vec(body_forward_vec, forward_vec)
            )
    
    return pos,forward_vec

def process_program(pg: str, i:int = 0) -> tuple:
    # parse program
    pos = [0,0]
    forward_vec = [0,1]

    while i < len(pg):
        if pg[i] == ']':
            return pos, forward_vec, i + 1

        if pg[i].isdigit():
            n = 0
            while pg[i].isdigit():
                n = n * 10 + int(pg[i])
                i += 1

            body_pos, body_forward, i = process_program(pg, i + 1)

            pos, forward_vec = loop(n, (body_pos, body_forward), pos, forward_vec)
        else:
            pos, forward_vec = process_action(pg[i], pos, forward_vec)
            i += 1

    return pos, forward_vec, i


def findCoords(pg:str) -> tuple:
    pos, forward_vec, i = process_program(pg)
    return pos[0], pos[1]



program = input()

print(*findCoords(program))