def readlines(filename):
	lines = ''
	with open(filename, 'r') as f:
		for line in f:
			lines += line
	return lines

txt = readlines("scer_gene.md")

def replace_all(text, dic):
	for i, j in dic.items():
		text = text.replace(i, j)
	return text

reps = {'4932\tI\t':'4932\t1\t',
		'4932\tII\t':'4932\t2\t',
		'4932\tIII\t':'4932\t3\t',
		'4932\tIV\t':'4932\t4\t',
		'4932\tV\t':'4932\t5\t',
		'4932\tVI\t':'4932\t6\t',
		'4932\tVII\t':'4932\t7\t',
		'4932\tVIII\t':'4932\t8\t',
		'4932\tIX\t':'4932\t9\t',
		'4932\tX\t':'4932\t10\t',
		'4932\tXI\t':'4932\t11\t',
		'4932\tXII\t':'4932\t12\t',
		'4932\tXIII\t':'4932\t13\t',
		'4932\tXIV\t':'4932\t14\t',
		'4932\tXV\t':'4932\t15\t',
		'4932\tXVI\t':'4932\t16\t'}

txt = replace_all(txt, reps)

with open("scer_gene_fixed.md", "w") as file:
	file.write(txt)
