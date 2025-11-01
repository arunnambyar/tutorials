# Different types of Design Patterns

Here onwards, as I previously stated, lets call it as `Design Patterns From Different Point Of View` (or POV) instead of **Different Types of Design Patterns**

<p align="center">
    <img src="../static/images/index/pov1.png" width=40% height=40%>
</p>


### 🔧 1. **Creational POV**  
**_"How the car is built ?"_**  
These patterns deal with object creation mechanisms, aiming to make the process more flexible and reusable.

| Pattern             | Car Analogy                                                                              |
|---------------------|------------------------------------------------------------------------------------------|
| **Singleton**       | Only one engine control unit (ECU) exists—shared across the system.                      |
| **Prototype**       | Clone an existing car design to make a new one.                                          |
| **Factory Method**  | A car factory decides which model to produce based on order type.                        |
| **Abstract Factory**| A car manufacture decides which factory to produce an order based on a bulk order.       |
| **Builder**         | Build a car step-by-step: chassis fitting, engine fitting, electric work, paint          |

---

### 🧩 2. **Structural POV**  
**_"How the spare parts are organized ?"_**  
These patterns focus on how classes and objects are composed to form larger structures.

| **Pattern**     | **Car Analogy**                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| **Adapter**     | like an adapter in between an 'Indian plug and a European socket'                         |
| **Composite**   | If some object structure repeats uniformly like a tree (eg:- folder/file structure).      |
| **Proxy**       | A remote (simulater type) system that helps user to interact with the real system         |
| **Facade**      | The auto park fature of a car encapsulates a complex orchestration of steering, gear shifting, camera feeds, obstacle detection, throttle control, braking, etc into a single feature  |
| **Bridge**      | Decouples vehicle engine from chassis, so they can work/vary independently                |
| **Decorator**   | Organizing a wrapper on top of a real object, that change the way you are accessing the real objrct, without physically changing that object |

---

### 🏁 3. **Behavioral POV**  
**_"How the car can be drive ?"_**  
These patterns manage algorithms, relationships, and responsibilities between objects.

| Pattern            | Car Analogy                                      |
|--------------------|--------------------------------------------------|
| **Template Method** | Driving steps: start → accelerate → brake → stop—fixed sequence with customizable steps. |
| **Observer**        | Sensors notify the dashboard when tire pressure drops. |
| **Strategy**        | Choose between eco, sport, or comfort driving modes. |
| **Command**         | Pressing a button sends a command to start the engine. |
| **State**           | Car behaves differently in park, drive, or reverse gear. |
| **Iterator**        | Cycle through music tracks or navigation waypoints. |
| **Interpreter**     | Voice assistant interprets “Navigate to home” into GPS instructions. |
| **Chain of Responsibility**| |

---

## 🗂️ Index

### 🔧 Creational POV
- <a href="#">Singleton</a>
- <a href="#">Prototype</a>
- <a href="#">Factory Method</a>
- <a href="#">Abstract Factory</a>
- <a href="#">Builder</a>

### 🧩 Structural POV
- <a href="#">Adapter</a>
- <a href="#">Composite</a>
- <a href="#">Proxy</a>
- <a href="#">Facade</a>
- <a href="#">Bridge</a>
- <a href="#">Decorator</a>

### 🏁 Behavioral POV
- <a href="#">Template Method</a>
- <a href="#">Observer</a>
- <a href="#">Strategy</a>
- <a href="#">Command</a>
- <a href="#">State</a>
- <a href="#">Iterator</a>
- <a href="#">Interpreter</a>
