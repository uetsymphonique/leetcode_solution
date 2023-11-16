from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams_dict = dict()
    for word in strs:
        anagram_key = ''.join(sorted(word))
        if anagram_key not in anagrams_dict:
            anagrams_dict[anagram_key] = [word]
        else:
            anagrams_dict[anagram_key].append(word)

    return list(anagrams_dict.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
