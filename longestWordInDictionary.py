# Time Complexity : O(26*L)
# Space Complexity : O(26*L)

# Approach:
# 1. Create a TrieNode class to represent each node in the trie.
# 2. Create a Trie class to manage the trie structure.
# 3. Implement the insert method to add words to the trie.
# 4. Insert all words into the trie.
# 5. Implement a depth-first search (DFS) method to find the longest word.
# 6. In the DFS method, check if the current node is a valid end of a word.
# 7. If it is, update the result with the current word.
# 8. Traverse the children of the current node and continue the DFS.
# 9. Return the longest word found in the trie.

# Definition for a trie node
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Solution:
    # Initialize the root of the trie
    def __init__(self):
        self.root = TrieNode()
    # Insert a word into the trie
    def insert(self, word):
        # Start from the root node
        # Assign the root node to the curr variable
        curr = self.root
        # Traverse the word character by character
        # For each character in the word
        for c in word:
            # Calculate the index of the character in the trie using the ASCII value
            idx = ord(c) - ord('a')
            # If the current character's child node is None, create a new TrieNode
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            # Move to the curr pointer
            curr = curr.children[idx]
        # Mark the end of the word
        curr.isEnd = True
    # Find the longest word in the dictionary
    def longestWord(self, words) -> str:
        # Insert all words into the trie
        for word in words:
            self.insert(word)
        self.res = ''
        # Perform a depth-first search (DFS) to find the longest word
        def dfs(curr, word):
            # base case
            # If the length of the current word is greater than the length of the result
            # Update the result with the current word
            if len(self.res) < len(word):
                self.res = word
            # Traverse the children of the current node
            for i in range(26):
                # If the current child node is not None and isEnd is True
                # Append the character to the current word and continue the DFS
                if curr.children[i] and curr.children[i].isEnd:
                    word = word+chr(i + ord('a'))
                    # Perform DFS on the child node
                    dfs(curr.children[i], word)
            # Backtrack by removing the last character from the current word
                    word = word[:len(word)-1]
        # Start DFS from the root node with an empty string for the current word
        dfs(self.root, '')
        # Return the longest word found in the trie
        return self.res