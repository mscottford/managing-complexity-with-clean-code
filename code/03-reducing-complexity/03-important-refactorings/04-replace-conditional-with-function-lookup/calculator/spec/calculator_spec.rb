# frozen_string_literal: true

RSpec.describe Calculator do
  it "has a version number" do
    expect(Calculator::VERSION).not_to be nil
  end
end
