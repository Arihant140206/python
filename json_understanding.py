"""
this is how a json file looks ,like a map
{
  "name": "Arihant",
  "age": 20,
  "isStudent": true,
  "skills": ["Python", "C++", "Web"]
}

"""
book={}
book["tom"]={
"name":'tom',"age":15,"gender":"male"}
book["gaga"]={
"name":"gaga","age":20,"gender":"female"}

import json
s=json.dumps(book)#dumps--dump string , joins it
print(s)


'''
in pyhhon     __name__=='__main__' is basically int main() 
'''
