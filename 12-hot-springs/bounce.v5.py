# check sum is an array of runs of # character
# a[3,2,1]
# m is the minimun size of a string that has a least one separator '.'
# between runs
# m = sum(a) + len(a) - 1
# add a 1 between all elements
# a = [3,1,2,1,1]
# add a 0 to the begining and end 
# a = [0,3,1,2,1,1,0]
# p = "?###????????"
# l = len(p)
# d = l - m
# create the permuations of a, with these rules
#
# sum(a) == b
# a[0] max 1
# starting at 2 alternating indexes have a min of 1
# values a starting at index 1 and alternating should not be changed
#
# distribute d amongst the values of the array a following the rules above

def generate_strings(runs, target_length):
  """
  Generates all possible strings with separators from a given array of character runs,
  with a specified target length.

  Args:
      runs: A list of integers representing the lengths of character runs.
      target_length: The desired length of the generated strings.

  Returns:
      A list of strings representing all possible valid combinations.
  """

  strings = []

  def backtrack(current_string, remaining_runs, separators_left, current_length):
    if not remaining_runs and not separators_left and current_length == target_length:
      strings.append(current_string)
      return

    # Ensure a separator is added before a new run if not the first run
    if remaining_runs and current_string:
      backtrack(current_string + '.', remaining_runs, separators_left, current_length + 1)

    if separators_left > 0 and current_length + 1 <= target_length:
      backtrack(current_string + '.', remaining_runs, separators_left - 1, current_length + 1)

    if remaining_runs and current_length + remaining_runs[0] + 1 <= target_length:
      run_length = remaining_runs.pop(0)
      backtrack(current_string + '#' * run_length, remaining_runs, separators_left, current_length + run_length)
      remaining_runs.append(run_length)

  backtrack('', runs, len(runs) - 1, 0)
  return strings

# Example usage
runs = [3, 2, 1]
target_length = 12

strings = generate_strings(runs, target_length)
print(strings)