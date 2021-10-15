import ssl, socket

class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
           self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return "has host" if host in self._cache else "has not host"

def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v

def hypervolume_better(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v

def tag(name,**kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))

    result = '<' + name
    for key, value in kwargs.items():
        result += ' {k}="{v}" '.format(k=key,v=str(value))
    result += ' >'
    return result

def maker(N):
    def action(X):
        print('X={X},N={N}'.format(X=X,N=N))
        return X * N
    return action

class clsmaker(object):
    def __init__(self, N):
        self.N = N
    def __call__(self, X):
        return X * self.N

      
