paragraph='''Philosophy of Education is a label applied to the study of the purpose, process, nature and ideals of education. It can be considered a branch of both philosophy and education. Education can be defined as the teaching and learning of specific skills, and the imparting of knowledge, judgment and wisdom,and is something broader than the societal institution of education we often speak of.Many educationalists consider it a weak and woolly field, too far removed from the practical applications of the real world to be useful. But philosophers dating back to Plato and the Ancient Greeks have given the area much thought and emphasis, and there is little doubt that their work has helped shape the practice of education over the millennia.'''
results={}
for i in paragraph:
    if i.isalpha():
        results[i]=paragraph.count(i)
print(results)
    
