import sys
sys.path.append(".") # add local directory as a module path

import my_module

# 'execution' is the Concord process' context, 'x' is a Concord process' variable
x = execution.getVariable("jsonResponse.content")
my_module.test(execution, x)
