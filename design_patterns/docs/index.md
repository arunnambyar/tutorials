# Different types of Design Patterns

Here onwards, as I previously stated, lets call it as `Design Patterns From Different Point Of View` (or POV) instead of **Different Types of Design Patterns**

<p align="center">
    <img src="../static/images/index/pov1.png" width=40% height=40%>
</p>


## 🔧 1. Creational POV  
**_"How the car is built"_**  
These patterns deal with object creation mechanisms, aiming to make the process more flexible and reusable.

| Pattern             | Car Analogy                                                                 |
|---------------------|------------------------------------------------------------------------------|
| [**Singleton**](1000_singleton.md)           | Only one engine control unit (ECU) exists—shared across the system.         |
| [**Prototype**](1100_prototype.md)           | Clone and update an existing car design to make a new car design.           |
| [**Factory Method**](1200_factory_method.md)      | A car factory decides which model to produce based on order type.           |
| [**Abstract Factory**](1300_abstract_factory.md)    | A manufacturer decides which factory to use based on a bulk order.          |
| [**Builder**](1400_builder.md)             | Build a car step-by-step: chassis fitting, engine fitting, electric work, paint. |



## 🧩 2. Structural POV  
**_"How the spare parts are organized"_**  
These patterns focus on how classes and objects are composed to form larger structures.

| Pattern             | Car Analogy                                                                 |
|---------------------|------------------------------------------------------------------------------|
| [**Adapter**](1500_adapter.md)            | Like an adapter between an Indian plug and a European socket.             |
| [**Composite**](1600_composite.md)          | Repeating object structure like a tree (e.g., folder/file structure).     |
| [**Proxy**](1700_proxy.md)              | A remote system that simulates interaction with the real system.          |
| [**Facade**](1800_facade.md)             | Auto-park feature encapsulates complex subsystems into one interface.     |
| [**Bridge**](1900_bridge.md)             | Decouples engine from chassis so they can vary independently.             |
| [**Decorator**](2000_decorator.md)          | Wraps a real object to change "access behavior" without altering the object.|



## 🏁 3. Behavioral POV  
**_"How the car behaves while driving and what changes its behaviour"_**  
These patterns manage algorithms, relationships, and responsibilities between objects.

| Pattern                   | Car Analogy                                                                 |
|---------------------------|------------------------------------------------------------------------------|
| [**Template Method**](2100_template_method.md)         | Think of a car's overall design as a template—its 'rear design' is a customizable template method. Hatchbacks and sedans implement this method differently, altering the car's behavior. |
| [**Observer**](2200_observer.md)                | Sensors notify the dashboard when engine temperature increases.         |
| [**Strategy**](2300_strategy.md)                | Choose between eco, sport, or comfort driving modes while driving.      |
| [**Command**](2400_command.md)                 | Pressing a (solid) button sends a command to start the engine.          |
| [**State**](2500_state.md)                   | Auto gear vehicles shifts gear based on the vehicle’s current state.    |
| [**Iterator**](2600_iterator.md)                | Cycle through music tracks or navigation waypoints.                     |
| [**Interpreter**](2700_interpreter.md)             | Voice assistant interprets “Navigate to home” into GPS instructions.    |
| [**Chain of Responsibility**](2800_chain_of_responsibility.md) | A service request passes through different service counters until one (or more) handles it. |

<p align="right">
    <a href="1000_singleton.md">Start with Singleton</a>
</p>
