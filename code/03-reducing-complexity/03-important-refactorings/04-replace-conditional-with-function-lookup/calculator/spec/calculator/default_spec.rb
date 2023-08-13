# frozen_string_literal: true

require "spec_helper"
require_relative "./calculator_examples"

RSpec.describe Calculator::Default do
  it_behaves_like "a calculator", Calculator::Default
end
