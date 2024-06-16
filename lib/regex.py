
import re

# Define the refined pattern
my_pattern = r"[A-Z][a-z\s',?]*today[a-z\s',?]*[?\.]"
my_regex = re.compile(my_pattern)