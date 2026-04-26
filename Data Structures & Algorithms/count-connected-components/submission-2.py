class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for a,b in edges:
            uf.union(a, b)
            # print(uf.par)
        return uf.count()
            
class UF:
    def __init__(self, n) -> None:
        self.cnt = n
        self.par = [i for i in range(n)]

    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, p, q):
        par_p = self.find(p)
        par_q = self.find(q)
        if par_p == par_q:
            return
        self.par[par_p] = par_q # merge root, instead of the node itself
        self.cnt -= 1

    def count(self):
        return self.cnt

