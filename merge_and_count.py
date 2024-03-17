def merge_and_count(A, B):
    # Merge two sorted halves A and B into a sorted whole L
    i = 0
    j = 0
    inversions = 0
    merged_list = []

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged_list.append(A[i])
            i += 1
        else:
            # If element in A is greater than element in B,
            # it forms inversions with all the remaining elements in A
            merged_list.append(B[j])
            j += 1
            inversions += len(A) - i
    
    # Append remaining elements from A and B (if any)
    merged_list.extend(A[i:])
    merged_list.extend(B[j:])
    
    return inversions, merged_list

def sort_and_count(L):
    if len(L) <= 1:
        # Base case: if the list has one or fewer elements, no inversions
        return 0, L
    
    # Divide the list into two halves A and B
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]
    
    # Recursively sort and count inversions in halves A and B
    rA, A_sorted = sort_and_count(A)
    rB, B_sorted = sort_and_count(B)
    
    # Merge the sorted halves A and B and count inversions
    rAB, L_sorted = merge_and_count(A_sorted, B_sorted)
    
    # Total inversions = inversions in A + inversions in B + inversions formed by merging A and B
    total_inversions = rA + rB + rAB
    
    return total_inversions, L_sorted

# Example usage
L = [3, 4, 5, 6, 2, 1, 3, 5]
inversions, sorted_L = sort_and_count(L)
print("Number of inversions:", inversions)
print("Sorted list:", sorted_L)