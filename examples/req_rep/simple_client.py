# client

from nanoservice import Client

c = Client('ipc:///tmp/service.sock')

res, err = c.call('greet', 'John Doe')
print('Greeting: {}'.format(res))

res, err = c.call('add', 2, 3)
print('Addition: 2 + 3  = {}'.format(res))

