import qrcode

separator = 'X'
fields = 3
spaceLen = 4

def generate(frm,to,location):
    for count in range(frm,to,1):
        exit = 'CZP'
        fill = ''
        for exc in range((fields*spaceLen)-len(str(count))):
            fill += '0'
        
        fill += str(count)
        for number in fill:
            exit += number

        for x in [3,8,13]:
            lst = list(exit)
            lst.insert(x, separator)
            exit = ''.join(lst)
        code = qrcode.make(exit)
        code.save(location+'/'+exit+'.png')