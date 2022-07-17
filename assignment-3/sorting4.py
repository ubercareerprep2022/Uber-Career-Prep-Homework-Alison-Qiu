"""
Sorting Exercise 4: Group Anagrams
Write a method to sort an array of strings so that all the anagrams are next to each other. Assume the average length of the word as “k”, and “n” is the size of the array, where n >> k (i.e. “n” is very large in comparison to “k”). Do it in a time complexity better than O[n.log(n)]

"""
def groupAnagrams(self, strs):
        char_to_index = defaultdict(list)
        for index in range(len(strs)):
            str_set = tuple(sorted(list(strs[index])))
            char_to_index[str_set].append(index)
        #print(char_to_index)
        ans = [[strs[index] for index in val] for val in char_to_index.values()]
        return ans