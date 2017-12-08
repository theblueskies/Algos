'''
# Given a set of n ordered infinite streams, merge them into one ordered output stream.
# You may define the stream API however you like.
# The elements are ordered by some known comparator - for example, timestamp.


# 1, 2, 5, 7
# 1, 6, 25, 99
# 3, 4, 8

# 1, 1, 3, --- 2, 4, 6

1 1 3
     ---- 1
1 3
1 2 3 4 6
     ----- 1
2 3 4 6 5 25 8
2 3 4 6 5 8 25
     ------ 2

[] || 5 25 8
'''
from random import randint
from time import sleep
import sys


class Stream:
    i = 0
    def nextElement(self):
        self.i += randint(1, 100)
        return self.i

    def put(self, val):
        sleep(0.1)
        print val


def stream_merge(input_streams, output_stream):
    input_values = []
    output_values = []
    stream_dict = {}
    stream_id = 0
    for index in range(len(input_streams)):
        stream_dict[input_streams[index].nextElement()] = index

    while True:
      input_values = stream_dict.keys()
      sorted_values = sorted(input_values)

      output_stream.put(sorted_values[0])
      stream_id = stream_dict[sorted_values[0]]
      stream_dict.pop(sorted_values[0])

      stream_dict[input_streams[index].nextElement()] = index


def main():
    inputs = [Stream() for x in xrange(100)]
    output = Stream()
    stream_merge(inputs, output)

if __name__ == '__main__':
    main()
