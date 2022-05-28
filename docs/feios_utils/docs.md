## Preface
FEI Operating System,known as feios,is developed by fyc in late 2021.  
It turned out that it is a bad-ended project,and its repo was deleted in Jan 2022.  
However,fyc is not knocked down.He decided to write a new,or remaded operating system.  
This will probably take a long time,but he finally established his first release on *May the 9th,2022*.  
That is the time when this fei-ros,or FEI Remade Operating System,is first created.  
Then he seperated the functions into *feios_funcs*.  
A while later,his father deleted all his accounts & repos around *May the 10th,2022*.  
So he started again,with even more passion.  
So...  
He still put the functions into different packages,but this time,***feios_utils***.  
That is the topic of this doc.  


## Usage
### Console
* For console commands,now there are five of them.
#### Printing
* Two print functions:`out` and `outline`.
* `out` is to print on the same line.
```python
>>>from feios_utils import *
>>>out('Hello');out('Goodbye')
HelloGoodbye>>>
```
* `outline` is just normal print.
```python
>>>outline('Hi')
Hi
>>>
```
#### Execution
* *WARNING* HERE `EXECUTION`MEANS EXECUTION OF FEI-ROS COMMANDS,NOT FOR ANY OTHER USE.
* DO NOT USE IT IN *ANY PRODUCTION ENVIRONMENT*!
* Three functions for executing:`run`,`runbatch` and `load_cmd`.
* `run` accepts a list of string,which must be commands(or receiving ERR002).
* `runbatch` accepts a path,to the file you want to run.
* `load_cmd` loads only 1 command.
Signed:fyc  
Last updated:May 5.27,2022  