defmodule SolutionTest do
  use ExUnit.Case
  doctest Solution

  test "simple smashing" do
    assert Solution.smash([]) == ""
    assert Solution.smash(["hello"]) == "hello"
    assert Solution.smash(["hello", "world"]) == "hello world"
  end
end
