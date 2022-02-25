def solution(s):
    numArr = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for i,j in enumerate(numArr):
        if j in s:
            s = s.replace(j, str(i))
            
    return int(s)