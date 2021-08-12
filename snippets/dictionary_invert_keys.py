ad = {
	1 : "one",
	2 : "two"
}

b = {a: b for b, a in ad.items()}
print(b)