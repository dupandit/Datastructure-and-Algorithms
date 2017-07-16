class Graph :
    def __init__(self,vertices):
        self.V=vertices  # Denotes number of vertices
        self.graph=[]    # Our graph representation as (u,v,w)--> u,v are two vertices and w is the weight. So basically this array stores edges

    def addEdge(self,u,v,w):  # forms our graph given (u,v,w) representation
        self.graph.append([u,v,w])

    def Make_Adj_List(self,edge):
        global arr
        index1=edge[0]
        index2=edge[1]
        arr[index1].append(index2)
        arr[index2].append(index1)

    # IDEA :  detect a cycle : For every visited vertex 'v',  if there is an adjacent 'u' such that 'u' is already visited and u is not a parent of v, then there is a cycle in a graph

    def Check_Cycle(self,MSTgraph,num):

        def Available_Nodes(arr):
            nodes_present = []

            for j in range(len(arr)):
                if arr[j] != []:
                    nodes_present.append(j)
            return nodes_present
            #print 'arr:', arr, 'Nodes present :', nodes_present


        def DFS(current,visit,arr,nodes_present) :
            global temp
            global par
            if temp==0 :
                current=nodes_present[0]
                par[current]=-1
                temp+=1
            current_adj=arr[current]

            for node in current_adj:
                if visit[node]==True and par[current]!=node:
                    return True
                elif visit[node]==False :
                    par[node]=current
                return DFS(node,visit,arr,nodes_present)
            return False






        global arr
        global temp
        global par
        arr = [[] for _ in range(num)]
        for edge in MSTgraph :
            self.Make_Adj_List(edge)
        #print 'MST:',MSTgraph,'ARR:',arr
        visit={}
        for i in range(num):
            visit[i]=False
        temp=0
        par={}
        nodes_present= Available_Nodes(arr)
        if DFS(-1,visit,arr,nodes_present)== True :
            return True
        else :
            return False


    def KruskalMST(self,num):
        global arr
        MSTgraph=[]
        self.graph=sorted(self.graph, key=lambda item:item[2])
        print self.graph

        for edge in self.graph :
            MSTgraph.append(edge)
            if self.Check_Cycle(MSTgraph,num) == True:
                MSTgraph.pop()
        return MSTgraph




# Our main function
g=Graph(9)
g.addEdge(0,1,4)
g.addEdge(0,7,8)
g.addEdge(1,2,8)
g.addEdge(1,7,11)
g.addEdge(7,6,1)
g.addEdge(7,8,7)
g.addEdge(8,2,2)
g.addEdge(2,5,4)
g.addEdge(6,5,2)
g.addEdge(2,3,7)
g.addEdge(3,5,14)
g.addEdge(3,4,9)
g.addEdge(4,5,10)
g.addEdge(8,6,6)
#print g.graph
num=g.V
global arr
global temp
global par
par={}    # one that stores parent of current nodes
temp=0
arr=[[] for _ in range(num)]
#print arr
#print
print g.KruskalMST(num)