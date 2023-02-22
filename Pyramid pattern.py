def pyramid_pattern(n):
    for i in range(1, n + 1):
        spaces = n - i
        stars = i
        print(' ' * spaces + '* ' * stars)


size = int(input('Enter the size of pyramid: '))
pyramid_pattern(size)

# Enter the size of pyramid: 4
#   * 
#  * * 
# * * * 
#* * * *
