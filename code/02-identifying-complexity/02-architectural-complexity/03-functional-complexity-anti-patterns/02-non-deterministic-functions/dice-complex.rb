# This file can be run with `ruby dice-complex.rb`

def rollDice
    return rollOneDie + rollOneDie
end

def rollOneDie
    return rand(6) + 1
end

# Outputs a different value each time it is run
# This make it hard to test
puts "Dice roll: #{rollDice}"

