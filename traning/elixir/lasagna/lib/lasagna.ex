defmodule Lasagna do
  @spec expected_minutes_in_oven :: integer()
  def expected_minutes_in_oven, do: 40

  @spec remaining_minutes_in_oven(minutes :: integer) :: integer
  def remaining_minutes_in_oven(minutes), do: expected_minutes_in_oven() - minutes

  @spec preparation_time_in_minutes(layers :: integer) :: integer
  def preparation_time_in_minutes(layers), do: layers * 2

  @spec total_time_in_minutes(layers :: integer, minutes :: integer) :: integer
  def total_time_in_minutes(layers, minutes), do: preparation_time_in_minutes(layers) + minutes

  @spec alarm :: String.t()
  def alarm, do: "Ding!"
end
