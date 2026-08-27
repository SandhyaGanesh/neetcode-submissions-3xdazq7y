func canJump(nums []int) bool {
    l := len(nums)
    goal := l - 1
    hops := 0

    for goal > 0 {
        hops += 1
        if goal - hops < 0 {
            return false
        }
        if nums[goal-hops] >= hops {
            goal = goal-hops
            hops = 0
        }
        
    }
    return goal == 0
}
