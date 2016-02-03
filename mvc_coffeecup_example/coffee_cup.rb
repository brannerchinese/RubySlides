class CoffeeCup
  attr_reader :amount_left

  def initialize
    fill
  end

  def fill
    @amount_left = 100 # Percent full
  end
  
  def empty
    @amount_left = 0
  end
  
  def gulp
    @amount_left -= Random.rand(17..35)
  end
  
  def sip
    @amount_left -= 5
  end
  
  def to_s
    if @amount_left == 100
      "This cup is now full."
    elsif @amount_left <= 0
      "This cup is now empty — please fill it."
    else
      "There is #{@amount_left}% left."
    end
  end
end
