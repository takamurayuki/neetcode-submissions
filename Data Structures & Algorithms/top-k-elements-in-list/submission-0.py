class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # ソートを使う場合
        # ordered = sorted(count, key=lambda x: count[x], reverse=True)
        # return ordered[0:k]

        # 空リストをn+1個持つリストを作成
        buckets = [[] for _ in range(len(nums) + 1)]
        # 辞書のキー,値の組を一つずつ取り出す
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        # 1ずつ減らしながら回す
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res