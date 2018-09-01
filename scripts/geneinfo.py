l = []

def geneinfo(sourcefile):
    with open(sourcefile,'r') as source:
        for line in source:
            fields = line.split('\t')
            if (fields[1] == "11" and fields[11] == "GENE"):
                l.append(fields)
                print(fields[1], fields[2], fields[9])
        return l

txt = geneinfo("scer_gene_fixed.md")

