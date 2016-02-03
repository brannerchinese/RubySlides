class View
  MESSAGES = {welcome: "\nThis program models a cup of coffee. \n\n" +
                       "Your options are:\n" +
                       "  fill\n" +
                       "  empty\n" +
                       "  gulp\n" +
                       "  sip\n" +
                       "  exit",
              sorry:   "Sorry, I don't know that command.",
              goodbye: "End of program."}

  def display(msg)
    if msg == nil
      puts "Not possible at this time."
    elsif MESSAGES.include?(msg)
      puts MESSAGES[msg]
    else
      puts msg
    end
    puts
  end

  def get_input
    print "What do you want to do? "
    input = gets.chomp.to_sym
    puts
    input
  end
end
