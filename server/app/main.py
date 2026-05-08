import asyncio

async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    print(f"Клиент подключился: {addr}")
    try:
        while True:
            data = await reader.readline()
            print(data)
            message = data.decode().strip()
            print(message)

            if message.lower() == "exit":
                writer.write("Соединение закрыто\n".encode())
                await writer.drain()
                break


            response = f"Server get a message: {message}\n"
            writer.write(response.encode())
            await writer.drain()

    except ConnectionResetError:
        print("Ошибка")

    finally:
        writer.close()
        await writer.wait_closed()
        print("Соединение открыто")



async def server():
    server = await asyncio.start_server(
        handler,
        host='127.0.0.1',
        port=9999
    )
    async with server:
        await server.serve_forever()



if __name__ == "__main__":
    asyncio.run(server())