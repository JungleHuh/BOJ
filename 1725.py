while True:
    bars = []
    while True:
        bar_input = input().strip()
        bar = int(bar_input)
        if bar == 0:
            break
        bars.append(bar)

    if len(bars) == 0:
        break

    stack = []
    num_bars = len(bars)
    max_area = 0

    for index in range(num_bars):
        if not stack: 
            stack.append((index, bars[index]))
        else:
            if stack[-1][1] <= bars[index]:
                stack.append((index, bars[index]))
            else:
                while stack and stack[-1][1] > bars[index]:
                    popped_bar = stack.pop()
                    if not stack:
                        width = index
                    else:
                        width = index - stack[-1][0] - 1
                    max_area = max(max_area, popped_bar[1] * width)
                stack.append((index, bars[index]))

    while stack:
        popped_bar = stack.pop()
        if len(stack) == 0:
            width = num_bars
        else:
            width = num_bars - stack[-1][0]
        max_area = max(max_area, popped_bar[1] * width)

    print(max_area)
