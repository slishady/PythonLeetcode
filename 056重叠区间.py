# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        startpos = 0
        jet = 0
        while startpos < len(intervals)-1:
            nextpos = startpos+1
            maxbound = max(intervals[startpos].end, intervals[nextpos].end)
            while nextpos <= len(intervals)-1 and intervals[nextpos-1].end >= intervals[nextpos].start:
                nextpos += 1
                if nextpos > len(intervals) - 1:
                    jet = 1
                nextpos = min(nextpos, len(intervals) - 1)
                maxbound = max(maxbound, intervals[nextpos].end)
            if nextpos == len(intervals) - 1:
                if jet == 1:
                    intervals.append(Interval(intervals[startpos].start, intervals[nextpos].end))
                else:
                    intervals.append(Interval(intervals[startpos].start, intervals[nextpos-1].end))
            else:
                intervals.insert(nextpos,Interval(intervals[startpos].start, intervals[nextpos-1].end))
            intervals[startpos:nextpos] = []
            startpos += 1
        
        return intervals

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        return self.merge(intervals)
        
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        startpos = 0
        jet = 0
        while startpos < len(intervals)-1:
            nextpos = startpos+1
            if intervals[startpos].end < intervals[nextpos].start:
                startpos += 1
                continue
            maxbound = max(intervals[startpos].end, intervals[nextpos].end)
            while nextpos <= len(intervals)-1 and maxbound >= intervals[nextpos].start:
                nextpos += 1
                if nextpos > len(intervals) - 1:
                    jet = 1
                maxbound = max(maxbound, intervals[nextpos-1].end)
            nextpos = min(nextpos, len(intervals) - 1)
            if jet == 1:
                intervals.append(Interval(intervals[startpos].start, maxbound))
                intervals[startpos:nextpos+1] = []
            else:
                intervals.insert(nextpos, Interval(intervals[startpos].start, maxbound))
                intervals[startpos:nextpos] = []
            startpos += 1
        
        return intervals  
        

a = Solution()
print(a.merge([Interval(1,4), Interval(4,5)]))