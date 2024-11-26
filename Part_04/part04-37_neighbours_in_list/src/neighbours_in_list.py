# Write your solution here
def longest_series_of_neighbours(a : list):
    current_series = [a[0]]
    longest_series = []

    all_series = []

    for i in range(1, len(a)):
        if(abs(a[i] - a[i - 1]) == 1):
            current_series.append(a[i])
        else:
            all_series.append(current_series)
            if(len(current_series) > len(longest_series)):
                longest_series = current_series
            current_series = [a[i]]
    all_series.append(current_series)
    if(len(current_series) > len(longest_series)):
        longest_series = current_series
    return len(longest_series)
