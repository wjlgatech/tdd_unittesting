class Vector:
    def __init__(self, nums=[1]):
        self._nums = nums

    def __len__(self):
        return len(self._nums)

    @staticmethod
    def from_file(filename):
        vectors = []
        with open(filename) as f:
            for line in f:
                nums = line.strip().split(',')
                nums = [float(v) for v in nums]
                v = Vector(nums)
                vectors.append(v)
            return vectors

    def __add__(self, other):
        nums = [a + b for a, b in zip(self._nums, other._nums)]
        return Vector(nums)
