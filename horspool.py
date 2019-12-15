# horspool.py
# Laura Lundell
# CS 411 A7
# December 15, 2019
# Implementation of Horspool's matching algorithm
# Used the textbook algorithm as a basis, pg. 261-262
# and http://code.activestate.com/recipes/117223-boyer-moore-horspool-string-searching/


class Horspool:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.pattern_len = len(pattern)
        self.text_len = len(text)
        self.shift = []

    def shift_table(self, pattern):
        # using the number of ascii characters
        for ch in range(256):
            self.shift.append(self.pattern_len)
        # shift table is filled with the pattern_len for each character
        # or the distance between the specific character
        # within the pattern and the end of the pattern.
        for ch in range(self.pattern_len - 1):
            self.shift[ord(pattern[ch])] = self.pattern_len - ch - 1
        self.shift = tuple(self.shift)
        return self.shift;

    def search(self, pattern, text):
        if self.pattern_len > self.text_len:
            return -1
        self.shift = self.shift_table(pattern)

        last_pattern_pos = self.pattern_len - 1
        while last_pattern_pos < self.text_len:
            j = self.pattern_len - 1
            i = last_pattern_pos
            while j >= 0 and text[i] == pattern[j]:
                j -= 1
                i -= 1
            if j == -1:
                return i + 1
            last_pattern_pos += self.shift[ord(text[last_pattern_pos])]
        return -1

def main():
    text = "Where is the needle in the haystack?"
    pattern = "in"
    bmh = Horspool(pattern,text)
    s = bmh.search(pattern,text)
    if s > -1:
        print ('\"',pattern,'\"','pattern found at position',s)
    else:
        print ('\"',pattern,'\"','not found.')

if __name__ == '__main__':
    main()
