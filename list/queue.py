import collections

if __name__ == '__main__':
    a = collections.deque()
    a.append('1')
    a.pop()
    a.append('12')
    a.append('14')
    a.append('18')
    a.append('22')
    a.popleft()