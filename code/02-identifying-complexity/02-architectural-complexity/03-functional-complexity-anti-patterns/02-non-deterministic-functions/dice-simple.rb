# This file can be run with `ruby dice-simple.rb`

def randomnessSource(seed)
    srand(seed)
    return lambda { |max| rand(max) }
end

def rollDice(randomness = randomnessSource(now))
    return rollOneDie(randomness) + rollOneDie(randomness)
end

def rollOneDie(randomness = randomnessSource(now))
    return randomness.call(6) + 1
end

# Outputs "Dice roll: 8"
puts "Dice roll: #{rollDice(randomnessSource(12))}"
