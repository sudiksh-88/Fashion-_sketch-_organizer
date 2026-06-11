designs = []
while True:
  print("\n--- Fashion Sketch Organizer ---")
  print("1. Add Design")
  print("2. View Designs")
  print("3. Exit")

  choice = input("Enter your choice: ")
  if choice == "1":
    name = input("Design Name: ")
    category = input("Catergory: ")
    color = input("Main Color: ")

    design = {
        "name": name,
        "category": category,
        "color": color,
    }
    designs.append(design)
    print("Design added successfully!")
  elif choice ==  "2":
      if len(designs) == 0:
          print("No designs found.")
      else:
          print("\n Saved Designs:" )
          for design in designs:
              print(
                   f"Name: {design['name']}, "
                   f"Category: {design['category']}, "
                   f"Color: {design['color']},"
                   )
  elif choice == "3":
      print("Goodbye!")
      break

  else:
      print("Invalid choice.")
                   
