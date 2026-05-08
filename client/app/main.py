import asyncio

async def client():
    reader, writer = await asyncio.open_connection(
        host='127.0.0.1',
        port=9999
    )
    try:
        while True:
            message = input('> ')
            writer.write((message + '\n').encode())
            await writer.drain()

            response = await reader.readline()
            print(f"Ответ сервера: {response.decode().strip()}")

            if message.lower() == "exit":
                break
    
    finally:
        writer.close()
        await writer.wait_closed()
        print("Соединение закрыто")


if __name__ == "__main__":
    asyncio.run(client())
