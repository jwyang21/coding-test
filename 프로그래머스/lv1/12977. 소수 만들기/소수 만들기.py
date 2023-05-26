def count_num_divisor(n):
    answer = 0
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            answer += 1
            if i ** 2 != n:
                answer += 1
    return answer

def solution(nums):
    if len(nums)==3:
        tmp = sum(nums)
        tmp_ = count_num_divisor(tmp)
        answer = 1 if tmp_ == 2 else 0
    else:
        answer = 0
        #tmp = []
        tmp_ = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    tmp = nums[i]+nums[j]+nums[k]
                    tmp_.append(count_num_divisor(tmp))
                    #if count_num_divisor(tmp) == 2: # DEBUG
                        #print('{} + {} + {} = {} is a prime number'.format(nums[i], nums[j], nums[k], tmp))
        for i in range(len(tmp_)):
            if tmp_[i] == 2:
                answer += 1
    return answer