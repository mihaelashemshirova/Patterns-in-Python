def draw_figure(n):
    if n == 0:
        return
    print('*' * n)
    draw_figure(n - 1)
    print('*' * n)


n = int(input('Enter the size of figure: '))
draw_figure(n)

# This pattern drawing:
#***
#**
#*
#*
#**
#***
