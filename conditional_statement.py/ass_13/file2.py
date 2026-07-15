
signal = input("give me the signal")
match signal:
    case "red":
        print("stop")
    case "yellow":
        print("wait")
    case "green":
        print("go")
    case _:
        print("no signal")