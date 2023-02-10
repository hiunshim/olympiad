import heapq

def h_index(n, citations):
    hindex = 0
    minHeap = []
    ans = []
    for i in range(n):
        if citations[i] > hindex:
            heapq.heappush(minHeap, citations[i])
        while minHeap and minHeap[0] <= hindex:
            heapq.heappop(minHeap)
        if len(minHeap) >= hindex + 1:
            hindex += 1
        ans.append(hindex)
    return ans

def main():
    T = int(input())
    for t in range(T):
        num_paper = int(input())
        citations = list(map(int, input().split()))
        h_index_scores = h_index(num_paper, citations)
        print(f"Case #{str(t)}: {' '.join(map(str, h_index_scores))}")
        
if __name__ == '__main__':
    main()

