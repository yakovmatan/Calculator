# Shape Area & Perimeter Calculator

This Python project implements a shape calculator that calculates the **area** and **perimeter** of various 2D geometric shapes. The project demonstrates object-oriented principles such as inheritance, polymorphism, method overriding, and operator overloading using magic (dunder) methods.

---

## 📦 Project Structure

```
Calculator/
│
├── Shape.py         # Abstract base class for all shapes
├── Rectangle.py     # Rectangle class inheriting from Shape
├── Square.py        # Square class inheriting from Rectangle
├── Triangle.py      # Triangle class inheriting from Shape
├── Circle.py        # Circle class inheriting from Shape
├── Hexagon.py       # Hexagon class inheriting from Shape
└── main.py          # Main module to run the program and demonstrate functionality
```

---

## ✨ Features

✅ Area and perimeter calculation for:  
- Rectangle  
- Square  
- Triangle  
- Circle  
- Regular Hexagon  

✅ Shape comparison based on area (`==`, `<`, `>`, etc.)  
✅ Area multiplication between shapes and numbers using `*`  
✅ Magic methods like `__str__`, `__repr__`, `__eq__`, `__lt__`, `__add__`, `__mul__`  
✅ Full input validation with exceptions for invalid parameters  

---

## 🛠️ How to Run

Make sure you are inside the project folder and run:

```bash
python main.py
```

---

## 🧮 Example Output

```
Rectangle(width=3, height=4)
Rectangle with area 12.00 and perimeter 14.00

Square(side=2)
Square with area 4.00 and perimeter 8.00

...

=== Comparisons ===
Rectangle(width=3, height=4) == Square(side=2)?  False
Rectangle(width=3, height=4) < Square(side=2)?  False
Rectangle(width=3, height=4) > Square(side=2)?  True

=== Multiplication of areas ===
Rectangle(width=3, height=4) * Square(side=2) = 48.00
...
```

---

## 📚 Concepts Demonstrated

- Object-Oriented Programming (OOP)  
- Inheritance & Polymorphism  
- Method overriding  
- Operator overloading  
- Magic (dunder) methods  
- Error handling with exceptions  

---

## 🚀 Future Improvements (optional)

- Add support for more geometric shapes  
- Graphical User Interface (GUI)  
- Save shape data to files  
- Unit tests with `unittest` or `pytest`  

---

## 📂 Version Control

This project is managed with **Git**, allowing clean version control and collaboration.

---

## 📝 Author

Yakov Matan  
GitHub: [https://github.com/yakovmatan/Calculator](https://github.com/yakovmatan/Calculator)

---

## 🛡️ License

This project is provided for educational purposes. Feel free to use, modify, or extend it.
