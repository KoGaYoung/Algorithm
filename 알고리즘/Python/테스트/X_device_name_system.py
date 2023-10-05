def deviceNamesSystem(devicenames):
    # Write your code here 100%
    a = {}
    result = []
    for item in devicenames:
        if item not in a:
            a[item] = 0
            result.append(item)
        else:
            a[item] += 1
            result.append(item + str(a[item]))
    return result

if __name__ == '__main__':
    # mixer toaster mixer1 tv
    print(deviceNamesSystem(["mixer","toaster","mixer","tv"]))
    # ["tv", "lamp"]
    print(deviceNamesSystem(["tv", "lamp"]))
    # lamp lamp1 tv lamp2
    print(deviceNamesSystem(["lamp","lamp","tv","lamp"] ))