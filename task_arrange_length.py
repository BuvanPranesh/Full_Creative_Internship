import re  
original_str="""Philosophy of Education is a label applied to the study of the purpose, process, nature and ideals of education. It can be considered a branch of both philosophy and education. Education can be defined as the teaching and learning of specific skills, and the imparting of knowledge, judgment and wisdom,and is something broader than the societal institution of education we often speak of. Many educationalists consider it a weak and woolly field, too far removed from the practical applications of the real world to be useful. But philosophers dating back to Plato and the Ancient Greeks have given the area much thought and emphasis, and there is little doubt that their work has helped shape the practice of education over the millennia."""
original=re.split('[ , .]',original_str)#splitting the string based on spaces commas and dots
results={}#store the keys and values in the dictionary 
duplicates_removed=set(original)
for i in duplicates_removed:
    if i.isalpha():
        key =str(len(i))
        results.setdefault(key,[])
        results[key].append(i)
print(results)
