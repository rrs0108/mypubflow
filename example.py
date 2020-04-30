import sys
sys.path.append(".") # add local directory as a module path

import my_module

# 'execution' is the Concord process' context, 'x' is a Concord process' variable
x = execution.getVariable("response")
my_module.test(execution, x)
