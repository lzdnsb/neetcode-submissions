'''
Step1: compare each pair of words, get a directed graph{nodes: letters; edges: n->f means n < f}
Step2: topologically sorted, output the order of the letters. if the graph contains cycle, return "" (invalid)
'''
from collections import defaultdict
from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def compare(i, j):
            nonlocal graph
            m, n = len(words[i]), len(words[j])
            p = 0 # pointer, points to the position we are comparing
            while p < min(m, n):
                if words[i][p] == words[j][p]:
                    p += 1
                else:
                    graph[words[i][p]].add(words[j][p])
                    return True
            if m > n: #words[j] is a prefix of words[i] or they are equal
                return False
            # words[i] is a prefix of words[j]
            return True
            
        graph = defaultdict(set) # key: char, value: set
        for word in words:
            for ch in word:
                if ch not in graph:
                    graph[ch] = set()
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                # compare words[i] and words[j]
                ans = compare(i, j)
                if not ans:
                    return ""
        #print(graph)

        # topologically sort
        ans = []
        indegree = defaultdict(int)
        for k, v in graph.items():
            indegree[k] += 0
            for ch in v:
                indegree[ch] += 1
        #print(indegree)
        queue = deque()
        for k, v in indegree.items():
            if v == 0:
                queue.append(k)

        while queue:
            ch = queue.popleft()
            ans.append(ch)
            for nxt in graph[ch]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        #print(ans)
        # check if there's cycle
        if len(ans) != len(indegree):
            return ""
        else:
            return "".join(ans)


        # n, f
        # h, e, r, n, f