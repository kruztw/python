import sys

def audit_hook(event, args):
    print(event)

sys.addaudithook(audit_hook)

src = input('>')
code = compile(src, '<string>', 'single')
