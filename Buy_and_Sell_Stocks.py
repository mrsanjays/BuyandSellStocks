def Buy_and_Sell_Stocks(array):
    l,r=0,1
    amount=0
    while r<len(array):
        price=array[r]-array[l]
        if price>amount:
            amount=price
        else:
            l=r
        r+=1
    return amount
if __name__ == '__main__':
    array=list(map(int,input().split()))
    print(Buy_and_Sell_Stocks(array))