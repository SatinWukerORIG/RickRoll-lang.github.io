<img src="static\logo.png" align="right" width="160" height="160">


# Official Site Of [The Rick Roll Language](https://github.com/Rick-Lang/rickroll-lang)
This is the address for the repo: https://github.com/Rick-Lang/rickroll-lang/
<br>
This is the address for our organization: https://github.com/Rick-Lang/

# The Rick Roll Programming Language

![Build](https://img.shields.io/badge/Build-passing-orange?style=for-the-badge&logo=appveyor)
![Python](https://img.shields.io/badge/Python-3.6%2B-brightgreen?style=for-the-badge&logo=appveyor)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge&logo=appveyor)
<br>
A language for rickrolling!
<br>

![](https://repository-images.githubusercontent.com/367934588/4a27ae00-b73b-11eb-801b-36dd1756dc93)

## Hello World
**The syntax of RickRoll-Lang is not completely similar to Python**
1. It doesn't need indentation
2. The code must be written inside the main method, otherwise the interpreter will not execute
3. **The keywords can be separated freely**

Rick Roll-Lang:
```
take me to ur heart
    give msg up "Never gonna give you up, never gonna let you down~\n"
    i just wanna tell u how im feeling msg
say goodbye
```
Equivalent to Python
```python
if __name__ == '__main__':
  msg = "Never gonna give you up, never gonna let you down~\n"
  print(msg, end='')

```

Equivalent to C++
```c++
#include<iostream>
using namespace std;
int main(int argc, char* argv[]){
    string msg = "Never gonna give you up, never gonna let you down~\n";
    cout<<msg;
}
```
**And you can get the output on your terminal:**

![](https://preview.redd.it/w2n81iqx37p51.gif?format=png8&s=a5619fa00938c2aa817496ddd9eceda8a727324c)
<br>
**Sorry, it's this:**
```
Never gonna give you up, never gonna let you down~
```
**The keywords can be separated freely**
```
takemetourheart
    give msg up "Never gonna give you up, never gonna let you down~\n"
    i justwanna telluhowim feeling msg
say good bye
```
This is also executable

## Generate Audio
How to use this generator:
```
python3 RickRoll.py -r [Source Code File Name] --audio
```
This generates an audio from the .rickroll program and plays it in your terminal

![](https://github.com/Rick-Lang/rickroll-lang/blob/main/img/au_generator.PNG)

## Requirements
- [Python libraries](https://github.com/Rick-Lang/rickroll-lang/blob/main/requirements.txt)
- [Python 3.6+](https://www.python.org/downloads/release/python-3610/)
- G++ compiler (For translating RickRoll to C++)
