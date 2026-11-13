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

def process_rotation(rotators:list) -> tuple:
    # return delta rotation in degrees
    rotation = 0
    for rotator in rotators:
        if rotator==')':
            rotation += 90
        else:
            rotation -= 90
    return rotation % 360

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