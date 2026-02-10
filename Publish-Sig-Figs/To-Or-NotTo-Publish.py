def publish(OverallResults, SpecificResult):
    '''
    takes in your overall experiment results
    and checks if the specific result is below 0.3% /
    if it's within 3 standard deviations
    of the mean.

    If < 0.3%, you'll be told to publish.
    If > 0.3%, you'll be told to not publish.
    '''
    # find the mean of your results
    Mean = np.mean(OverallResults)

    # find the standard deviation
    STD = np.std(OverallResults)

    # find 3 standard deviations
    ThreeSTD = STD * 3

    print(f'The mean of your overall results was {Mean}.')
    print(f'One standard deviation was {STD}.')

    # checks if the specific result is greater than the mean
    if SpecificResult > Mean:
        check = SpecificResult - Mean

    # checks if the specific result is lower than the mean
    elif Mean > SpecificResult:
        check = Mean - SpecificResult

    if check > ThreeSTD:
        print(f'Your specific result had to be within the bounds of {Mean - ThreeSTD} and {Mean + ThreeSTD}.')
        print(f'Your specific result {SpecificResult} was not within 3 standard deviations.')
        print(f'\033[1mYou should NOT publish.\033[0m')
        
    elif check < ThreeSTD:
        print(f'Your specific result had to be within the bounds of {Mean - ThreeSTD} and {Mean + ThreeSTD}.')
        print(f'Your specific result {SpecificResult} was within 3 standards deviations.')
        print(f'\033[1mYou CAN publish.\033[0m')
