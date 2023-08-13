# frozen_string_literal: true

module Calculator
  # Default calculator implementation. Uses a conditional to determine which
  # operation to perform.
  class Default
    def initialize(value = 0)
      @value = value
    end

    def execute(command)
      values = command.split(" ")
      operation = values[0]
      first_operand = values[1].to_f
      second_operand = values.length > 2 ? values[2].to_f : nil

      case operation
      when "add"
        if !second_operand.nil?
          @value = first_operand + second_operand
        else
          @value += first_operand
        end

      when "subtract"
        if !second_operand.nil?
          @value = first_operand - second_operand
        else
          @value -= first_operand
        end

      when "multiply"
        if !second_operand.nil?
          @value = first_operand * second_operand
        else
          @value *= first_operand
        end

      when "divide"
        if !second_operand.nil?
          @value = first_operand / second_operand
        else
          @value /= first_operand
        end
      else
        raise "Invalid operation"
      end
    end

    def result
      @value
    end
  end
end
