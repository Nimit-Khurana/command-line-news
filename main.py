#
# Copyright 2018 <copyright holder> <email>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
from paper import newspaper

class main:
    def __init__(self):
        pass
    def options(self):
        opt_list=('Hindu','Tribune','Indian Express','Greater Kashmir')
        for i in xrange(len(opt_list)):
            print str([i])+'\t\t'+opt_list[i]
        self.selected()
        
    def selected(self):
        inp = int(input('Enter your preference or \'99\' to quit:'))
        if inp == 0:
            thehindu = newspaper()
            print thehindu.hindu()
        elif inp == 1:
            trib = newspaper()
            print trib.tribune()
        elif inp == 2:
            express = newspaper()
            print express.express()
        elif inp == 3:
            gkashmir = newspaper()
            print gkashmir.kashmir()
        elif inp == 99:
            print '----------You chose to quit-----------'
            sys.exit()
        else:
            print 'Please select from above'
            selected()

Input = main()
print Input.options()
