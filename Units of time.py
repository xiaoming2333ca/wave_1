days = int(input('Days please >'))
hours = int(input('Hours please >'))
minutes = int(input('Minutes please >'))
seconds = int(input('Seconds please >'))

total = days * 86400 + hours * 3600 + minutes * 60 + seconds
print(f'The total time is {total} seconds')
