# frozen_string_literal: true

module Calculator
  # Refactored calculator implementation. Uses a function lookup to determine
  # which operation to perform.
  class Refactored
    def initialize(value = 0)
      @value = value
    end

    OPERATIONS = {
      "add" => :add,
      "subtract" => :subtract,
      "multiply" => :multiply,
      "divide" => :divide
    }.freeze

    def execute(command)
      values = command.split(" ")
      operation = values[0]
      first_operand = values[1].to_f
      second_operand = values.length > 2 ? values[2].to_f : nil

      raise "Invalid operation" unless OPERATIONS.key?(operation)

      send(OPERATIONS[operation], first_operand, second_operand)
    end

    def add(first_operand, second_operand)
      if !second_operand.nil?
        @value = first_operand + second_operand
      else
        @value += first_operand
      end
    end

    def subtract(first_operand, second_operand)
      if !second_operand.nil?
        @value = first_operand - second_operand
      else
        @value -= first_operand
      end
    end

    def multiply(first_operand, second_operand)
      if !second_operand.nil?
        @value = first_operand * second_operand
      else
        @value *= first_operand
      end
    end

    def divide(first_operand, second_operand)
      if !second_operand.nil?
        @value = first_operand / second_operand
      else
        @value /= first_operand
      end
    end

    def result
      @value
    end
  end
end
