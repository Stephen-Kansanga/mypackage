def top_n(items, n):
    """ Return the top n array in desc order

    Args:
        items(array): A list or array-like object
        n(int): number of items to return
    
    Return: An array of top n in desc order


    Egs:
        >>> top_n([2,5,9,4,7], 3)
        [9,7,5]

    """
    n = min(n, len(items))
    for i in range(n):
        for j in range(len(items)-i-1): 
            if items[j+1] > items[j]:
                items[j],items[j+1] = items[j+1], items[j]
    return items[:n]


