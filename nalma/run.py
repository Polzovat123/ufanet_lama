import uvicorn


if __name__ == '__main__':
    uvicorn.run(
        "application.route:app",
        host='127.0.0.1',
        port=6432
    )