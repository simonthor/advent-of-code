##
using Printf

##
function problem1()
    # Read input into an array of strings
    id_ranges = split(read("2.txt", String)[1:end-1], ",")
    
    invalid_id_sums = 0
    for id_range in id_ranges
        start, stop = split(id_range, "-")
        # If start has an odd number of digits and is the same length as the stop, skip
        if length(start) % 2 == 1 && length(start) == length(stop)
            continue
        # If start has an odd number of digits and the not the same length as the stop, change start to 100... where the length is length(start)+1
        elseif length(start) % 2 == 1 && length(start) != length(stop)
            start = string("1" * "0"^(length(start)))
        end
        # If stop has an odd number of digits, change stop to 100... where the length is length(stop)
        if length(stop) % 2 == 1
            stop = string("1" * "0"^(length(stop)-1))
        end

        start_num = parse(Int64, start)
        stop_num = parse(Int64, stop)
        # Now, start stop always have even number of digits
        # One can simply iterate over all the possible numbers between 10^(length(start)//2) and 10^(length(stop)//2)-1, starting from the first half of the digits of start
        # If the number is smaller than start, skip
        # If the number is larger than stop, break
        start_number = div(start_num, 10^div(length(start),2))
        stop_number = div(stop_num, 10^div(length(stop),2))
        
        # @printf("start: %s, stop: %s, start_number: %d, stop_number: %d\n", start, stop, start_number, stop_number)

        for i in start_number:stop_number
            invalid_number = i * 10^div(length(start),2) + i
            if invalid_number < start_num
                continue
            elseif invalid_number > stop_num
                break
            end
            @printf("sub number: %d, invalid number: %d\n", i, invalid_number)
            invalid_id_sums += invalid_number
        end
    end
    println(invalid_id_sums)

end

problem1()
