from django.shortcuts import render
from calc.models import CalcString, StoredNum, Result, Previous
# Create your views here.

def thecalc(request):

    try:
        string = CalcString.objects.get(pk=1)
    except CalcString.DoesNotExist:
        string = CalcString(ctext='', num='', first=0, second=0, op='')
        string.save()

    try:
        mem = StoredNum.objects.get(pk=1)
    except StoredNum.DoesNotExist:
        mem = StoredNum(stored='0.0')
        mem.save()

    try:
        res = Result.objects.get(pk=1)
    except Result.DoesNotExist:
        res = Result(ans='0.0')
        res.save()

    try:
        prev = Previous.objects.get(pk=1)
    except Previous.DoesNotExist:
        prev = Previous(val='0.0', pop='')
        prev.save()                        

    if 'number' in request.POST:
        string.num += request.POST['number']
        string.ctext += request.POST['number']
        string.save()
    elif 'op' in request.POST:
        optype = request.POST['op']
        if optype == '=':
            if string.second == '':
                res.ans = prev.val
            else:
                string.second = float(string.num)
                res.ans = calculate(string.first, string.second, string.op)
            res.save()
            prev.val = res.ans
            string.delete()
            prev.save()
        else:
            if string.num == '':
                string.first = prev.val
                string.ctext += str(string.first)
            else:
                string.first = float(string.num)
            string.num = ''
            string.op = optype
            string.ctext += optype
            string.save()
            prev.pop = optype
            prev.save()
    elif 'rst' in request.POST:
        res.ans = '0.0'
        string.delete()
        prev.val = '0.0'
        prev.pop = ''
        res.save()
    elif 'memt' in request.POST:
        mtype = request.POST['memt']
        if  mtype == 'm+':
            mem.stored = float(string.num)
        elif mtype == 'm-':
            mem.stored = 0
        else:
            string.num += str(mem.stored)
            string.ctext += str(mem.stored)
            string.save
        mem.save()

    context = {'newResult':res.ans, 'newString':string.ctext, 'newPrevVal':prev.val, 'newPrevOp':prev.pop}
    
    return render(request, 'calc/calc.html', context)

def calculate(num1, num2, op):
    result = 0.0	
    if op == '+':
    	result = num1 + num2
    if op == '-':
    	result = num1 - num2
    if op == '*':
    	result = num1 * num2
    if op == '/':
    	if num2 == 0:
    		result = 0
    	else:
    		result = num1 / num2
    return result
        
