import heapq
import sys
class Graph:
    def __init__(self,V):
        self.V=V
        self.adj=[[] for _ in range(V)]
        self.parent=None
        self.dist=None
        
    def add_edge(self,u,v,w):
        self.adj[u].append((v,w))
        self.adj[v].append((u,w))
        
    def print_path(self,node):
        if self.parent[node]==-1:
            print(node,end=" ==> ")
            return
        self.print_path(self.parent[node])
        print(node,end=" ==> ") 
    
            
    def shortest_path(self,src):
        pq=[]
        heapq.heappush(pq,(0,src))
        self.dist=[sys.maxsize]*self.V
        self.parent=[-1]*self.V
        self.dist[src]=0
        while pq:
            d,u = heapq.heappop(pq)
            for v,w in self.adj[u]:
                if self.dist[v]>self.dist[u]+w:
                    self.dist[v]= self.dist[u]+w
                    self.parent[v]=u
                    heapq.heappush(pq,(self.dist[v],v))
        print("Src\t\tDist\t\tParent")
        for i in range(self.V):
            print(f"{i}\t\t{self.dist[i]}\t\t{self.parent[i]}")
V=9
src=0
destination=5
g=Graph(V)
g.add_edge(0,1,4)
g.add_edge(0,7,8)
g.add_edge(1,2,8)
g.add_edge(1,7,11)
g.add_edge(2,3,7)
g.add_edge(2,8,2)
g.add_edge(2,5,4)
g.add_edge(3,4,9)
g.add_edge(3,5,14)
g.add_edge(4,5,10)
g.add_edge(5,6,2)
g.add_edge(6,7,1)
g.add_edge(6,8,6)
g.add_edge(7,8,7)
g.shortest_path(src)
#print("\npath")
g.print_path(destination)
#print(f"\n Distance from {src} to {destination} = {g.dist[destination]}=>


            
