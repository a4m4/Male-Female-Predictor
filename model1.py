from sklearn import tree

X = [ [170,80,44], [155,85,43], [178, 93,50], [120,55,34], [142,40,26], [136,39,27] , 
     [188,90,60], [144,50,30], [190,60,46], [122,32,24] ]

Y = [ 'male' , 'male' ,'male' , 'female' , 'female' , 'female' , 'male', 'female' , 'male', 'female' ]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

pred = clf.predict([[190,70,45]])

print(pred)