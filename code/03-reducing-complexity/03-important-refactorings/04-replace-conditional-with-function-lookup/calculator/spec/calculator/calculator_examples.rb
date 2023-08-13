# frozen_string_literal: true

RSpec.shared_examples "a calculator" do |calculator_class|
  describe "add" do
    it "should work with two integers" do
      calculator = calculator_class.new
      calculator.execute("add 5 3")
      expect(calculator.result).to eq(8)
    end

    it "should work with two floats" do
      calculator = calculator_class.new
      calculator.execute("add 5.5 3.3")
      expect(calculator.result).to eq(8.8)
    end

    it "should work with two negative numbers" do
      calculator = calculator_class.new
      calculator.execute("add -5 -3")
      expect(calculator.result).to eq(-8)
    end

    it "should work with first number negative" do
      calculator = calculator_class.new
      calculator.execute("add -5 3")
      expect(calculator.result).to eq(-2)
    end

    it "should work with second number negative" do
      calculator = calculator_class.new
      calculator.execute("add 5 -3")
      expect(calculator.result).to eq(2)
    end

    it "should work with two negative floats" do
      calculator = calculator_class.new
      calculator.execute("add -5.5 -3.3")
      expect(calculator.result).to eq(-8.8)
    end
  end

  describe "subtract" do
    it "should work with two integers" do
      calculator = calculator_class.new
      calculator.execute("subtract 5 3")
      expect(calculator.result).to eq(2)
    end

    it "should work with two floats" do
      calculator = calculator_class.new
      calculator.execute("subtract 5.5 3.3")
      expect(calculator.result).to eq(2.2)
    end

    it "should work with two negative numbers" do
      calculator = calculator_class.new
      calculator.execute("subtract -5 -3")
      expect(calculator.result).to eq(-2)
    end

    it "should work with first number negative" do
      calculator = calculator_class.new
      calculator.execute("subtract -5 3")
      expect(calculator.result).to eq(-8)
    end

    it "should work with second number negative" do
      calculator = calculator_class.new
      calculator.execute("subtract 5 -3")
      expect(calculator.result).to eq(8)
    end

    it "should work with two negative floats" do
      calculator = calculator_class.new
      calculator.execute("subtract -5.5 -3.3")
      expect(calculator.result).to eq(-2.2)
    end
  end

  describe "multiply" do
    it "should work with two integers" do
      calculator = calculator_class.new
      calculator.execute("multiply 5 3")
      expect(calculator.result).to eq(15)
    end

    it "should work with two floats" do
      calculator = calculator_class.new
      calculator.execute("multiply 5.5 3.3")
      expect(calculator.result).to eq(18.15)
    end

    it "should work with two negative numbers" do
      calculator = calculator_class.new
      calculator.execute("multiply -5 -3")
      expect(calculator.result).to eq(15)
    end

    it "should work with first number negative" do
      calculator = calculator_class.new
      calculator.execute("multiply -5 3")
      expect(calculator.result).to eq(-15)
    end

    it "should work with second number negative" do
      calculator = calculator_class.new
      calculator.execute("multiply 5 -3")
      expect(calculator.result).to eq(-15)
    end

    it "should work with two negative floats" do
      calculator = calculator_class.new
      calculator.execute("multiply -5.5 -3.3")
      expect(calculator.result).to eq(18.15)
    end
  end

  describe "divide" do
    it "should work with two integers" do
      calculator = calculator_class.new
      calculator.execute("divide 5 3")
      expect(calculator.result).to be_within(0.000001).of(1.6666666666666667)
    end

    it "should work with two floats" do
      calculator = calculator_class.new
      calculator.execute("divide 5.5 3.3")
      expect(calculator.result).to be_within(0.000001).of(1.6666666666666667)
    end

    it "should work with two negative numbers" do
      calculator = calculator_class.new
      calculator.execute("divide -5 -3")
      expect(calculator.result).to be_within(0.000001).of(1.6666666666666667)
    end

    it "should work with first number negative" do
      calculator = calculator_class.new
      calculator.execute("divide -5 3")
      expect(calculator.result).to be_within(0.000001).of(-1.6666666666666667)
    end

    it "should work with second number negative" do
      calculator = calculator_class.new
      calculator.execute("divide 5 -3")
      expect(calculator.result).to be_within(0.000001).of(-1.6666666666666667)
    end

    it "should work with two negative floats" do
      calculator = calculator_class.new
      calculator.execute("divide -5.5 -3.3")
      expect(calculator.result).to be_within(0.000001).of(1.6666666666666667)
    end
  end

  describe "multiple operations" do
    it "should work adds using initial value" do
      calculator = calculator_class.new(5)
      calculator.execute("add 5")
      calculator.execute("add 3")
      expect(calculator.result).to eq(13)
    end

    it "should work adds ignoring initial value" do
      calculator = calculator_class.new(5)
      calculator.execute("add 5 3")
      calculator.execute("add 5")
      expect(calculator.result).to eq(13)
    end

    it "should work subtracts using initial value" do
      calculator = calculator_class.new(7)
      calculator.execute("subtract 5")
      calculator.execute("subtract 3")
      expect(calculator.result).to eq(-1)
    end

    it "should work subtracts ignoring initial value" do
      calculator = calculator_class.new(7)
      calculator.execute("subtract 5 3")
      calculator.execute("subtract 5")
      expect(calculator.result).to eq(-3)
    end

    it "should work multiplies using initial value" do
      calculator = calculator_class.new(2)
      calculator.execute("multiply 5")
      calculator.execute("multiply 3")
      expect(calculator.result).to eq(30)
    end

    it "should work multiplies ignoring initial value" do
      calculator = calculator_class.new(2)
      calculator.execute("multiply 5 3")
      calculator.execute("multiply 5")
      expect(calculator.result).to eq(75)
    end

    it "should work divides using initial value" do
      calculator = calculator_class.new(100)
      calculator.execute("divide 5")
      calculator.execute("divide 3")
      expect(calculator.result).to be_within(0.000001).of(6.666666666666667)
    end

    it "should work divides ignoring initial value" do
      calculator = calculator_class.new(100)
      calculator.execute("divide 10 5")
      calculator.execute("divide 3")
      expect(calculator.result).to be_within(0.000001).of(0.666666666666667)
    end
  end
end
