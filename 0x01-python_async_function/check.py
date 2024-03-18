#!/usr/bin/python3

basic = __import__('0-basic_async_syntax')
wait_random = basic.wait_random
await wait_random.sleep(1)
result = wait_random(5)
print (result)
