# Time Complexity : O(L), for insert, search and startsWith where L is the length of the word
# Space Complexity : O(N*L), where N is the number of words in the trie and L is the length of the longest word
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach
# 1. Create a TrieNode class to represent each node in the trie.
# The TrieNode class has an array of children (size 26 for each letter of the alphabet) and a boolean isEnd to indicate if the node represents the end of a word.
# 2. In the Trie class, create a root node of type TrieNode. This will be the starting point for all insertions and searches.

# Definition of a trie node
class TrieNode:
    # Initialize the TrieNode with an array of children and a boolean isEnd
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:
    # Initialize the Trie with a root node
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the trie
    def insert(self, word: str) -> None:
        # Start from the root node
        curr = self.root
        # Iterate through each character in the word
        for i in range(len(word)):
            # Calculate the index of the character (0-25)
            idx = ord(word[i]) - ord('a')
            # If the child node at that index is None, create a new TrieNode
            # This means that the character is not present in the trie yet
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            # If the child node is already present, move to that child node
            curr = curr.children[idx]
        # After inserting all characters, mark the end of the word
        curr.isEnd = True

    # Search for a word in the trie
    def search(self, word: str) -> bool:
        # Start from the root node
        curr = self.root
        # Iterate through each character in the word
        for i in range(len(word)):
            # Calculate the index of the character (0-25)
            idx = ord(word[i]) - ord('a')
            # If the child node at that index is None, the word is not present in the trie, so we return False
            if not curr.children[idx]:
                return False
            # If the child node is present, move to that child node
            curr = curr.children[idx]
        # After checking all characters, return True if we are at the end of a word
        return curr.isEnd

    # Check if there is any word in the trie that starts with the given prefix
    # This is similar to the search function, but we don't need to check if we are at the end of a word
    def startsWith(self, prefix: str) -> bool:
        # Start from the root node
        curr = self.root
        # Iterate through each character in the prefix
        for i in range(len(prefix)):
            # Calculate the index of the character (0-25)
            idx = ord(prefix[i]) - ord('a')
            # If the child node at that index is None, the prefix is not present in the trie, so we return False
            if not curr.children[idx]:
                return False
            # If the child node is present, move to that child node
            curr = curr.children[idx]
        # If we are able to traverse the entire prefix, it means that the prefix is present in the trie, so we return True
        return True