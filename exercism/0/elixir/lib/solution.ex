defmodule Solution do
  @moduledoc """
  Documentation for `Solution`.
  """

  @doc """
  Smash.

  ## Examples

      iex> Solution.smash([])
      ""

  """
  def smash(words), do: Enum.join(words, " ")
  # def smash(words) do
  #   Enum.join(words, " ")
  # end
end
