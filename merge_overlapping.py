def merge_overlapping(intervals):
    merge_list = []
    if len(intervals) == 0:
        return merge_list
    intervals.sort(key = lambda x: x[0])
    tenmp_interval = intervals[0]
    for interval in intervals:
        if interval[0] <= tenmp_interval[1]:
            tenmp_interval[1] = max(interval[1],tenmp_interval[1])
        else:
            merge_list.append(tenmp_interval)
            tenmp_interval = interval
    merge_list.append(tenmp_interval)
    return merge_list

if __name__ == "__main__" :
    l = [[1,3],[2,6],[8,10],[15,18]]
    print(merge_overlapping(l))
     


















































































































































































































































































