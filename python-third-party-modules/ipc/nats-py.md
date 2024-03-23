- [参考](https://nats-io.github.io/nats.py/)
- [[async-await]]
- `pip install nats-py[nkeys]`
# hello-world
-   ```python
    import asyncio
    import nats

    async def main():
        # Connect to NATS!
        nc = await nats.connect("demo.nats.io")

        # Receive messages on 'foo'
        sub = await nc.subscribe("foo")

        # Publish a message to 'foo'
        await nc.publish("foo", b'Hello from Python!')

        # Process a message
        msg = await sub.next_msg()
        print("Received:", msg)

        # Close NATS connection
        await nc.close()

    if __name__ == '__main__':
        asyncio.run(main())
    ```
# [[with-context-manager]]
- https://nats-io.github.io/nats.py/modules.html#asyncio-client
```python
import asyncio
import nats

async def main():

    is_done = asyncio.Future()

    async def closed_cb():
        print('Connection to NATS is closed.')
        is_done.set_result(True)

    async with (await nats.connect('nats://demo.nats.io:4222', closed_cb=closed_cb)) as nc:
        print(f'Connected to NATS at {nc.connected_url.netloc}...')

        async def subscribe_handler(msg):
            subject = msg.subject
            reply = msg.reply
            data = msg.data.decode()
            print("Received a message on '{subject} {reply}': {data}".format(
                subject=subject, reply=reply, data=data))

        await nc.subscribe('discover', cb=subscribe_handler)
        await nc.flush()

        for i in range(0, 10):
            await nc.publish('discover', b'hello world')
            await asyncio.sleep(0.1)

    await asyncio.wait_for(is_done, 60.0)

if __name__ == '__main__':
    asyncio.run(main())
```
## separated-files
- 注意此时不能直接把`for i in range(0, 10):`及后面的行拷到别处不加修改刚刚的，否则就一开马上关上了。应该`await asyncio.sleep(10)`一下

```python
import asyncio
import nats

async def main():

    is_done = asyncio.Future()

    async def closed_cb():
        print('Subscriber connection to NATS is closed.')
        is_done.set_result(True)

    async with (await nats.connect('nats://demo.nats.io:4222', closed_cb=closed_cb)) as nc:
        print(f'Subscriber connected to NATS at {nc.connected_url.netloc}...')

        async def subscribe_handler(msg):
            subject = msg.subject
            reply = msg.reply
            data = msg.data.decode()
            print("Received a message on '{subject} {reply}': {data}".format(
                subject=subject, reply=reply, data=data))

        await nc.subscribe('discover', cb=subscribe_handler)
        await nc.flush()

        await asyncio.sleep(10)

    await asyncio.wait_for(is_done, 60.0)

if __name__ == '__main__':
    asyncio.run(main())
```

```python
# publisher
import asyncio
import nats

async def main():

    is_done = asyncio.Future()

    async def closed_cb():
        print('Publisher connection to NATS is closed.')
        is_done.set_result(True)

    async with (await nats.connect('nats://demo.nats.io:4222', closed_cb=closed_cb)) as nc:
        print(f'Publisher connected to NATS at {nc.connected_url.netloc}...')
        await asyncio.sleep(2)
        for i in range(0, 10):
            await nc.publish('discover', b'hello world')
            await asyncio.sleep(0.1)

    await asyncio.wait_for(is_done, 60.0)

if __name__ == '__main__':
    asyncio.run(main())
```
- 然后可以分别运行两个文件