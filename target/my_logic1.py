import sys
sys.path.append(".") # add local directory as a module path

import my_module1

# 'execution' is the Concord process' context, 'x' is a Concord process' variable
my_module1.test(execution, x)
