"""
Create an object that returns the positions and the values of the "peaks"
(or local maxima) of a numeric array.

For example, the array arr = [ 0 , 1 , 2 , 5 , 1 , 0 ] has a peak in position 3
with a value of 5 (arr[3] = 5)

The output will be returned as an object with two properties: pos and peaks.
Both of these properties should be arrays. If there is no peak in the given
array, then the output should be {pos: [], peaks: []}.

All input arrays will be valid numeric arrays (although it could still be
empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks
(in the context of a mathematical function, we don't know what is after and
before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1,2,2,2,1] has a peak while [1, 2, 2, 2, 3] does
not. In case of a plateau-peak, please only return the position and value of
the beginning of the plateau. For example: pickPeaks([1,2,2,2,1])
returns {pos:[1],peaks:[2]}
"""


def pick_peaks(arr):
    peaks = []
    pos = []
    answer = []
    # for n in range(1, len(arr) - 1):
    #     if arr[n] >= arr[n + 1] and arr[n] > arr[n - 1]:
    #         peaks.append(arr[n])
    #         pos.append(n)
    # return {"pos": pos, "peaks": peaks}

    values = [[n, arr[n]] for n in range(len(arr))]
    new_values = [values[r] for r in range(1, len(values)) if values[r][1] != values[r - 1][1]]
        # if values[r][1] == values[r + 1][1]:
        #     print values[r][1]
    print values
    print new_values

    #new_values2 = [new_values[x] for x in range(len(new_values), - 1) if new_values[x + 1][1] >= new_values[x][1] and new_values[x][1] > new_values[x - 1][1]]
    for x in range(len(new_values)):
        if new_values[x][1] >= new_values[x - 1][1] and new_values[x][1] > new_values[x + 1][1]:
            print "TEST"
            answer.append(new_values[x])
    print answer


    for n in range(1, len(arr) - 1):
        if arr[n] >= arr[n + 1] and arr[n] > arr[n - 1]:
            peaks.append(arr[n])
            pos.append(n)
    return {"pos": pos, "peaks": peaks}
