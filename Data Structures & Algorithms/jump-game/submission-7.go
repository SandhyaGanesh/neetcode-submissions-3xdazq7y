func canJump(nums []int) bool {
    l := len(nums)
    goal := l - 1
    hops := 0

    for goal - hops >= 0 {
        if goal == 0 {
            return true
        }
        hops += 1
        if goal - hops >= 0 && nums[goal-hops] >= hops {
            goal = goal-hops
            hops = 0
        }
        
    }
    return false
}
