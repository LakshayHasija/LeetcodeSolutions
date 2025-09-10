class TrieNode:
    def __init__(self):
        self.childnode={}
        self.count=0
class Tries:
    def __init__(self):
        self.root=TrieNode()
    def search(self,pref):
        node=self.root
        for i in range(len(pref)):
            prefix=pref[i]
            if prefix not in node.childnode:
                return 0
            node=node.childnode[prefix]
        return node.count
    def insert(self,word):
        node=self.root
        for i in range(len(word)):
            prefix=word[i]
            if prefix not in node.childnode:
                node.childnode[prefix]=TrieNode()
            node=node.childnode[prefix]
            node.count+=1
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie=Tries()
        ans=0
        for word in words[::-1]:
            trie.insert(word)
        ans+=trie.search(pref)
        return ans