# class Solution:
#         def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#                 groups =  {}

#                 for word in strs:
#                         key = "".join(sorted(word))
#                         print(groups.values())

#                         if key not in groups:
#                                 groups[key] = []


#                         groups[key].append(word)

#                 return list(groups.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[str, List[str]] = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())



                # groups = {}

                # for word in strs:
                #         key = "".join(sorted(word))

                #         if key not in groups:
                #                 groups[key] = []


                #         groups[key].append(word)
                # return list(groups.values())
               

                
        