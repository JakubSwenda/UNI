while (TRUE) {
  pH <- readline(prompt = "Enter pH value: ")
  pH <- as.numeric(pH)
  
  # check if pH is greater than 7, less than 7, or equal to 7
  if (is.numeric(pH) && !is.na(pH)) {
    if (pH < 7) {
      print("Your pH is acidic")
    } else if (pH > 7) {
      print("Your pH is basic")
    } else if (pH==7) {
      print("Your pH is neutral")
    }
  } else {
    print("Invalid input. Please enter a numeric value for pH.")
  }
}

