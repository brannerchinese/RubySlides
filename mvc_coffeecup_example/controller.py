class Controller():
  def __init__(self):
    @coffee_cup = CoffeeCup.new
    @view = View.new
    run_interface
  end

  def run_interface(self, input='fill')
    @view.display(:welcome)
    while input != :exit
      if @coffee_cup.methods.include?(input)
        @coffee_cup.method(input).call
        @view.display(@coffee_cup)
      else
        @view.display(:sorry)
      end
      input = @view.get_input
    end
    @view.display(:goodbye)
  end
end
