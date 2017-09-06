#!/usr/bin/env python3
import boto3
from sys import argv
from jinja2 import Template

cf = boto3.resource('cloudformation')

def get_stack_output(stack_name, key):
    iterator = filter(lambda x: x['OutputKey'] == key,
                      cf.Stack(stack_name).outputs)
    return next(iterator)['OutputValue']

def render_template(template):
    return Template(template).render(stack_output = get_stack_output)

def main():
    with open(argv[1], 'r') as f:
        print(render_template(f.read()))

if __name__ == '__main__':
    main()
