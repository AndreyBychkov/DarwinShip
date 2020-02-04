from models.GlobalEnvironment import GlobalEnvironment

if __name__ == '__main__':
    print("Hello, Darwin!")

    globalEnvironment = GlobalEnvironment()
    for _ in range(100):
        globalEnvironment.tick()