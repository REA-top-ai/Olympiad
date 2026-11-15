from math import radians, cos, sin

def main(): 
    position = [0, 0]
    angle = radians(90)
    program = input()
    position, angle = ProgramReader(program, position, angle)
    
    print(position[0], position[1])

def ProgramReader (program, position, angle):
    vx = round(cos(angle))
    vy = round(sin(angle))
    
    for i in range(len(program)):
        if program[i] == 'F':
            position[0] += vx
            position[1] += vy
        elif program[i] == 'B':
            position[0] -= vx
            position[1] -= vy
        elif program[i] == 'L':
            position[0] -= vy
            position[1] += vx
        elif program[i] == 'R':
            position[0] += vy
            position[1] -= vx
        elif program[i] == ')':
            angle -= radians(90)
            vx = round(cos(angle))
            vy = round(sin(angle))
        elif program[i] == '(':
            angle += radians(90)
            vx = round(cos(angle))
            vy = round(sin(angle))
        elif program[i].isdigit():
            cycle_number, cycle_body, end_index = CycleHandler(program, i)
            position, angle = CycleReader(cycle_number, cycle_body, position, angle)
            position, angle = ProgramReader(program[end_index:], position, angle)
            break
    return position, angle

def CycleHandler(program, i):
    num = ''
    end_index = 0
    counter = 0
    
    for k in range(len(program[i:])):
        if program[i + k].isdigit():
            num += program[i + k]
        else: break
        
    for j in range(len(program[i+len(num):])):
        if program[i + len(num) + j] == '[':
            counter += 1
        elif program[i + len(num) + j] == ']':
            counter -= 1
        if counter == 0:
            end_index = i + len(num) + j
            break
        
    body = program[i + len(num) + 1:end_index]
    
    return int(num), body, end_index + 1

def CycleReader(cycle_number, cycle_body, position, angle):
    if cycle_number <= 4:
        for i in range(cycle_number):
            position, angle = ProgramReader(cycle_body, position, angle)
    elif cycle_number > 4:
        initial_position = position.copy()
        initial_vx = round(cos(angle))
        initial_vy = round(sin(angle))
        counter = 0
        
        for i in range(4):
            counter += 1
            position, angle = ProgramReader(cycle_body, position, angle)
            vx = round(cos(angle))
            vy = round(sin(angle))
            if (vx, vy) == (initial_vx, initial_vy):
                break
        dposition = [position[0] - initial_position[0], position[1] - initial_position[1]]
        repeat_count = cycle_number // counter
        position = [initial_position[0] + dposition[0] * repeat_count, initial_position[1] + dposition[1] * repeat_count]
        for i in range(cycle_number % counter):
            position, angle = ProgramReader(cycle_body, position, angle)
            
    return position, angle

main()

#F ==> new_position = [position[0] + vx, position[1] + vy]
#B ==> new_position = [position[0] - vx, position[1] - vy]
#L ==> new position = [position[0] + vy , position[1] - vx]
#R ==> new position = [position[0] - vy, position[1] + vx]
#) angle -= radians(90)
#( angle += radians(90)