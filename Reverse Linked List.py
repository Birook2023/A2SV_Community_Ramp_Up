        nodes = [None]
        while head: 
            nodes.append(head)
            head = head.next 
        for i in range(1,len(nodes)):
            nodes[i].next = nodes[i-1] 
        return nodes[-1]
