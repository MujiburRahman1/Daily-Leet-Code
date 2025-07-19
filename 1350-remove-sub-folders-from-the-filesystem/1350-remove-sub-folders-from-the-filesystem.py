from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, path: str) -> None:
        node = self.root
        # Split on '/' and skip the empty first element
        for part in path.split('/')[1:]:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
            # If we reach an end marker, no need to keep adding deeper
            if node.is_end:
                return
        node.is_end = True
        # Once this node marks the end of a folder, prune any deeper nodes
        node.children.clear()

    def prefix_search(self, path: str) -> bool:
        node = self.root
        for part in path.split('/')[1:]:
            # If this node is already an end of a folder, then `path` is a sub-folder
            if node.is_end:
                return False
            if part not in node.children:
                return True
            node = node.children[part]
        return True  # This is a top-level folder

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        # Insert all folder paths into the trie
        for f in sorted(folder):
            trie.add(f)
        
        result = []
        # Check each folder; if it's not flagged as sub-folder, keep it
        for f in folder:
            if trie.prefix_search(f):
                result.append(f)
        return result

# Example usage:
if __name__ == "__main__":
    folders = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    sol = Solution()
    print(sol.removeSubfolders(folders))
    # Output: ['/a', '/c/d', '/c/f']
