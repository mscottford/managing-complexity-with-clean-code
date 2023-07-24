# The `sanitize_sql_for_order` method below was copied from the Rails source 
# code. Specifically, the file `activerecord/lib/active_record/sanitization.rb`. 
# It was retrieved from
# https://github.com/rails/rails/blob/04c97aec8aa696165e98f46ecec2b13410629be0/activerecord/lib/active_record/sanitization.rb#L84-L101
# on July 23, 2023. 
# 
# It is used here to demonstrate the calculation of ABC complexity.
# 
# All original comments have been removed and replaced with comments that
# illustrate the calculation of ABC complexity.
#
# The license that this code is published under appears at the bottom of this
# file.

def sanitize_sql_for_order(condition)
  # Assignments starts out at 0
  # Branches starts out at 0
  # Conditions starts out at 0

  # Conditionals increments to 1 because of the `if` statement
  # Conditionals increments to 2 because of the `&&` boolean operator
  # Branches is increments to 1 because of the call to `is_a?`
  # Branches is increments to 2 because of the call to `first`
  # Branches is increments to 3 because of the call to `to_s`
  # Branches is increments to 4 because of the call to `include?`
  if condition.is_a?(Array) && condition.first.to_s.include?("?")
    # Branches is increments to 5 because of the call to `disallow_raw_sql!`
    disallow_raw_sql!(
      # Branches is increments to 6 because of the call to `first`
      # Branches is increments to 7 because of the call to `Array.new` via implicit array creation
      [condition.first],
      # Branches is increments to 8 because of the call to `connection`
      # Branches is increments to 9 because of the call to `column_name_with_order_matcher`
      permit: connection.column_name_with_order_matcher
    )

    # Conditionals increments to 3 because of the `if` statement
    # Conditionals increments to 4 because of the `&&` boolean operator
    # Branches is increments to 10 because of the first call to `first`
    # Branches is increments to 11 because of the call to `kind_of?`
    # Branches is increments to 12 because of the second call to `first`
    # Branches is increments to 13 because of the call to `instance_of?`
    # Branches is increments to 14 because of the call to the `!` operator
    if condition.first.kind_of?(String) && !condition.first.instance_of?(String)
      # Assignments is increments to 1 because of the `=` operator
      # Branches is increments to 15 because of the call to `Array.new` via implicit array creation
      # Branches is increments to 16 because of the call to `String.new`
      # Branches is increments to 17 because of the call to `first`
      # Branches in incremented to 18 because of the call to `Array.[]`
      # Branches is increments to 19 because of the call to `Range.new` via the `..` operator
      condition = [String.new(condition.first), *condition[1..-1]]
    end

    # Branches is increments to 20 because of the call to `Arel.sql`
    # Branches is increments to 21 because of the call to `sanitize_sql_array`
    Arel.sql(sanitize_sql_array(condition))
  else
    condition
  end

  # Assignments total is 1
  # Branches total is 21
  # Conditions total is 4

  # ABC complexity is sqrt(1^2 + 21^2 + 4^2) = 21.4
end

# The license content below was retrieved from 
# https://github.com/rails/rails/blob/04c97aec8aa696165e98f46ecec2b13410629be0/MIT-LICENSE
# on July 23, 2023.

# Copyright (c) David Heinemeier Hansson
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
