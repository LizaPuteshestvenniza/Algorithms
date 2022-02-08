def merge(intervals):
    intervals = sorted(intervals)
    ans = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= ans[-1][1]:
            if intervals[i][1] > ans[-1][1]:
                ans[-1][1] = intervals[i][1]
        else:
            ans.append(intervals[i])
    return ans
