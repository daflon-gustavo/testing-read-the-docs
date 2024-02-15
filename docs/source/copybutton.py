import sys
import os
from docutils import nodes
from docutils.parsers.rst import Directive

sys.path.insert(0, os.path.abspath('.'))

class CopyButton(Directive):
    has_content = True

    def run(self):
        code_block = '\n'.join(self.content)
        code_block_node = nodes.literal_block(code_block, code_block)
        
        copy_button = nodes.raw(
            text='<button class="copybtn" data-clipboard-text="{}">Copy</button>'.format(code_block),
            format='html'
        )
        
        return [code_block_node, copy_button]

def setup(app):
    app.add_directive('copybutton', CopyButton)
    return {'version': '0.1'}
