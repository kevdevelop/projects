import random

class IDGenerator(object):
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"

    def __init__(self, length=8):
        self._alphabet_length = len(self.ALPHABET)
        self._id_length = length

    def _encode_int(self, n):
        
        encoded = ''
        while n > 0:
            n, r = divmod(n, self._alphabet_length)
            encoded = self.ALPHABET[r] + encoded
        return encoded

    def generate_id(self):
        """Generate an ID without leading zeros.

        For example, for an ID that is eight characters in length, the
        returned values will range from '10000000' to 'zzzzzzzz'.
         """

        start = self._alphabet_length**(self._id_length - 1)
        end = self._alphabet_length**self._id_length - 1
        return self._encode_int(random.randint(start, end))

if __name__ == "__main__":
    # Sample usage: Generate unique ID eight characters in length.
    idgen = IDGenerator(8)
    urloop = 1
    while urloop == 1:
        url_orig = input("Enter a URL: ")
        shorturl = idgen.generate_id()
        print("You entered", url_orig, "->")
        print(url_orig, "has been shortened to https://bit.ly/%s" % shorturl)
        continuer = input("Enter another URL? y/n: ")
        if continuer == "y":
            urloop += 0
        if continuer == "n":
            print("We hope you have enjoyed this program.")
            urloop = 0