#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys
import json
 
def GraphDef():
    json_dic = {
        'graphs': {
            'osx.temperature': {
                'label': 'OSX Temperature',
                 'unit': 'float',
                 'metrics': [
                     {
                        'name': 'cpu',
                        'label': 'CPU Temperature'
                     }
                ]
            }
        }
    }
    print "# mackerel-agent-plugin"
    print json.dumps(json_dic)
 
 
if __name__ == "__main__":
    if os.environ.get('MACKEREL_AGENT_PLUGIN_META', '')  == '1':
        GraphDef()
        sys.exit(0)
 
    os.system(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mackerel-osx-cpu-temp.sh'))