ALPHABET_SIZE = 26

class TrieNode:
    def __init__(self):
        self.edges = [None]*(ALPHABET_SIZE) # Each index respective to each character
        self.meaning = None # Meaning of the word
        self.ends_here = False # Tells us if the word ends here

    def add_word(self,word,meaning):
        if len(word) == 0:
            self.ends_here = True # Because we have reached the end of the word
            self.meaning = meaning # Adding the meaning to that node 
            return 
        ch = word[0] # First Character
        # ASCII value of the first character (minus) the ASCII value of 'a'-> the first character of our ALPHABET gives us the index of the edge we have to look up.   
        index = ord(ch) - ord('a')
        if self.edges[index] == None:
        	# This implies that there's no prefix with this character yet.
            new_node = TrieNode()
            self.edges[index] = new_node
        self.edges[index].add_word(word[1:],meaning) #Adding the remaining word        

    def search_word(self,word):
        if len(word) == 0:
            if self.ends_here:
                return True
            else:
                return "Not exist"
        ch = word[0]
        index = ord(ch) - ord('a')
        if self.edges[index] == None:
            return False 
        else:
            return self.edges[index].search_word(word[1:])

    def get_meaning(self,word):
		if len(word)==0 :
			if self.ends_here:
				return self.meaning
			else:
				return "Word doesn't exist in the Trie"
		ch = word[0]
		index = ord(ch) - ord('a')
		if self.edges[index] == None:
			return "Word doesn't exist in the Trie"
		else:
			return self.edges[index].get_meaning(word[1:])
    
    def delete_word(self,word):
		if len(word)==0:
			if self.ends_here:
				self.ends_here = False
				self.meaning = None
				return "Deleted"
			else:
				return "Word doesn't exist in the Trie"
		ch = word[0]
		index = ord(ch) - ord('a')
		if self.edges[index] == None:
			return "Word doesn't exist in the Trie"
		else:
			return self.edges[index].delete_word(word[1:])
    
if __name__ == '__main__':
    root = TrieNode()
    root.add_word("algorithm", "An algorithm (pronounced AL-go-rith-um) is a procedure or formula for solving a problem.")
    root.add_word("algo","Algo is short for algorithm, an algorithm (pronounced AL-go-rith-um) is a procedure or formula for solving a problem.")

    # print(root.get_meaning("algo"))
    # print(root.get_meaning("algorithm"))
    # print(root.delete_word("algo"))
    # print(root.get_meaning("algo"))
    # print(root.get_meaning("development"))  
    print(root.search_word('hello')) 
    