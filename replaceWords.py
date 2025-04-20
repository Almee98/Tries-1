# Time Complexity : O(N*L) + O(M*L)
# where N is the number of words in the dictionary, L is the length of the longest word in the dictionary, and M is the number of words in the sentence.
# Space Complexity : O(N*L) + O(M*L)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach
# 1. Create a TrieNode class to represent each node in the trie.
# 2. The TrieNode class has an array of children (size 26 for each letter of the alphabet) and a boolean isEnd to indicate if the node represents the end of a word.
# 3. Create a root node of type TrieNode. This will be the starting point for all insertions and searches.
# 4. Implement the insert method to add words to the trie.
# 5. Implement the search method to find the shortest prefix for each word in the sentence.
# 6. In the replaceWords method, iterate through the dictionary and insert each word into the trie.

# Definition of a trie node
class TrieNode:
    def __init__(self):
        # Each node has an array of children (size 26 for each letter of the alphabet)
        self.children = [None] * 26
        # A boolean isEnd to indicate if the node represents the end of a word
        self.isEnd = False

class Solution:
    # Initialize the Trie with a root node
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the trie
    def insert(self, word):
        # Start from the root node
        curr = self.root
        # Iterate through each character in the word
        for i in range(len(word)):
            # Calculate the index of the character (0-25)
            idx = ord(word[i]) - ord('a')
            # If the child node at that index is None, create a new TrieNode
            # This means that the character is not present in the trie yet
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            # If the child node is already present, move to that child node
            curr = curr.children[idx]
        # After inserting all characters, mark the end of the word
        curr.isEnd = True

    # Search for the shortest prefix in the trie
    def search(self, word):
        # Start from the root node
        curr = self.root
        # Along with searching for the word, we will also keep track of the prefix
        # Initialize an empty string to store the prefix
        s = ""
        # Iterate through each character in the word
        for i in range(len(word)):
            # Calculate the index of the character (0-25)
            idx = ord(word[i]) - ord('a')
            # If we reach a node that is the end of a word, we can stop searching
            # This means we have found the shortest prefix, so we return it
            if curr.isEnd:
                return s
            # If the child node at that index is not null, we can continue searching
            if curr.children[idx] != None:
                # Append the character to the prefix
                s += word[i]
                # Move to the child node
                curr = curr.children[idx]
            else:
                break
        # If we reach the end of the word and haven't found a prefix, return an empty string
        return ""

    def replaceWords(self, dictionary, sentence):
        # Iterate through the dictionary and insert each word into the trie
        for w in dictionary:
            self.insert(w)
        # Split the sentence into words
        s = sentence.split(" ")
        # Iterate through each word in the sentence
        for i in range(len(s)):
            # Search for the shortest prefix in the trie
            r = self.search(s[i])
            # If we found a prefix, replace the word with the prefix
            if r != "":
                s[i] = r
            # If no prefix was found, keep the original word
        # Join the words back into a single string and return it
        return " ".join(s)