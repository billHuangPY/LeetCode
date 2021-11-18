class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))

        queue = []
        for i in sorted_people:
            queue.insert(i[1], i)

        return queue
