##
using Printf

##
function problem1()
    # Read 1.txt into an array of strings
    rotations = split(read("1.txt", String), "\n")[1:end-1]

    current_position = 50
    counter = 0
    for rot in rotations
        if rot[1] == 'R'
            current_position += parse(Int64, rot[2:end])
        elseif rot[1] == 'L'
            current_position -= parse(Int64, rot[2:end])
        end
        current_position %= 100

        if current_position == 0
            counter += 1
        end
    end

    println(counter)
end

function problem2()
    # Read 1.txt into an array of strings
    rotations = split(read("1.txt", String), "\n")[1:end-1]
    current_position = 50
    counter = 0

    for (i, rot) in enumerate(rotations)
        if i < 100
            @printf("%d %d %s\n", current_position, counter, rot)
        end

        shift = parse(Int64, rot[2:end]) * (rot[1] == 'R' ? 1 : -1)
        circles, rest = divrem(shift, 100)
        
        counter += abs(circles)

        if rest == 0
            continue
        end

        if rest > 0 && current_position + rest >= 100
            counter += 1
        elseif rest < 0 && current_position + rest <= 0 && current_position != 0
            counter += 1
        end

        current_position += rest

        if current_position >= 100
            current_position -= 100
        elseif current_position < 0
            current_position += 100
        end
    end

    @printf("%d %d\n", current_position, counter)
end

problem1()

problem2()

##
