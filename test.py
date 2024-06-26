word = 'aab cdf'

# Substring is searched in 'eks for geeks' 
print(word.find('ab')) 

# Substring is searched in 'eks for geeks' 
print(word.find('geeks ', 2)) 

# Substring is searched in 's for g' 
print(word.find('g*', 4, 10)) 

# Substring is searched in 's for g' 
print(word.find('for ', 4, 11))
