# CloudFormation stack output resolver

This tools renders text files with stack outputs from AWS CloudFormation,
replacing every `{{ stack_output(stack_name, output_key) }}` expression with the
value of the stack output corresponding to the given `stack_name` and
`output_key` (provided as strings).

This tool uses Boto 3 as AWS SDK and Jinja2 as template engine.

## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

```
./stack_output_resolver.py <template_file>
```
