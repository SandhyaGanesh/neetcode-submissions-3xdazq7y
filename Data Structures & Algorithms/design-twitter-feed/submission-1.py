class Twitter:

    def __init__(self):
        self.userTweets = {}
        self.userFollows = {}
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer -= 1
        self.userTweets[userId] = self.userTweets.get(userId, []) + [(self.timer, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        latestTweets = []
        l = list(self.userFollows[userId])+[userId] if userId in self.userFollows else [userId]
        for user in l:
            if user in self.userTweets:
                t, tweetId = self.userTweets[user][-1]
                index = len(self.userTweets[user]) - 1
                latestTweets.append((t, tweetId, index, user))

        heapq.heapify(latestTweets)
        while len(res) < 10 and latestTweets:
            t, latestTweet, i, user = heapq.heappop(latestTweets)
            res.append(latestTweet)
            if i > 0:
                t, tweetId = self.userTweets[user][i - 1]
                heapq.heappush(latestTweets, (t, tweetId, i - 1, user))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.userFollows[followerId] = self.userFollows.get(followerId, set())
            self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.userFollows.get(followerId, set()).discard(followeeId)
