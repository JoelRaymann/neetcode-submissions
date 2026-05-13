class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        components: list[set[int]] = []
        visited = set[int]()
        result = []
        for n1, n2 in edges:
            if n1 in visited or n2 in visited:
                # Find component of n1 and component of n2.
                n1_component = set[int]()
                n2_component = set[int]()
                for component in components:
                    if n1 in component and n2 in component:
                        result = [n1, n2]
                        break
                    elif n1 in component:
                        n1_component = component
                    elif n2 in component:
                        n2_component = component
                    else:
                        pass
                # Connect the components
                if n1_component:
                    components.remove(n1_component)
                else:
                    n1_component = {n1}
                if n2_component:
                    components.remove(n2_component)
                else:
                    n2_component = {n2}
                components.append(n1_component.union(n2_component))
                visited.add(n1)
                visited.add(n2)
            else:
                visited.add(n1)
                visited.add(n2)
                components += [{n1, n2}]
        return result