func canCompleteCircuit(gas []int, cost []int) int {
    if sum(gas) < sum(cost) {
        return -1
    }

    resultIndex := -1
    runningSum := 0
    for i, _ := range gas {
        runningSum += gas[i] - cost[i]
        if runningSum < 0 {
            runningSum = 0
            resultIndex = i
        }
    }

    return resultIndex + 1
    
}

func sum(nums []int) int {
    resultSum := 0
    for _, num := range nums {
        resultSum += num
    }
    return resultSum
}