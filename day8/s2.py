from sys import stdin

def intersect(a, b):
    return ''.join(set(a) & set(b))

def diff(a, b):
    return ''.join(set(a) - set(b))

def equal(a, b):
    return set(a) == set(b)

def get_numbers_map(uniques):
	one = next(x for x in uniques if len(x) == 2)
	four = next(x for x in uniques if len(x) == 4)
	seven = next(x for x in uniques if len(x) == 3)
	eight = next(x for x in uniques if len(x) == 7)

	a = diff(seven, one)
	fiveLetters = list(filter(lambda i: len(i) == 5, uniques))
	diff4and7 = diff(four, seven)
	five = next(x for x in fiveLetters if len(intersect(diff4and7, x)) == 2)
	fiveLetters.remove(five)
	f = intersect(five, one)
	three = next(x for x in fiveLetters if len(intersect(f, x)) == 1)
	fiveLetters.remove(three)
	two = fiveLetters[0]
	c = intersect(two, one)
	sixLetters = list(filter(lambda i: len(i) == 6, uniques))
	six = next(x for x in sixLetters if len(intersect(c, x)) == 0)
	sixLetters.remove(six)
	b = diff(diff(eight, two), f)
	d = diff(diff4and7, b)
	zero = next(x for x in sixLetters if len(intersect(d, x)) == 0)
	sixLetters.remove(zero)	
	nine = sixLetters[0]
	numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
	return numbers

def get_number(digit_str, numbers):
    return next(ind for ind,val in enumerate(numbers) if equal(digit_str, val))

ans = 0
for line in stdin:
	uniques, entry = line.strip('\n').split(" | ")
	numbers = get_numbers_map(uniques.split(' '))
	num = int(
     		''.join(
           		list(map(
                 		lambda x: str(get_number(x, numbers)), 
                   		entry.split(' ')
                ))
            )
       	)
	ans += num

print(ans)
