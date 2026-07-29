# Factory Method Design Pattern

## On this page

- [What is the Factory Method pattern?](#what-is-the-factory-method-pattern)
- [Car analogy](#car-analogy)
- [When should you use it?](#when-should-you-use-it)
- [Two ways to implement it](#two-ways-to-implement-it)

## What is the Factory Method pattern?

Factory Method lets _a method_ decide which object to create. Usually, object creation logic is placed inside a method (of a class in OOPs). Though, that method can be a standalone function or a member of a class. Based on the arguments passed to it, the method selects one class from a group of classes and creates and returns an instance of it.

**Category:** Creational POV

## Car analogy

A car factory decides which model to produce based on order type.

## When should you use it?

Use it when object creation depends on input type but the creation steps should stay in one place.

## Two ways to implement it

- [**Parameterized / Simple Factory**](1210_simple_factory.md) — One factory class takes a type parameter (for example `"sedan"` or `"suv"`) and returns the matching product. Quick to add, easy to read, best when the product list is small and stable.

- [**Classic GoF Factory Method**](1220_factory_method_gof.md) — Each product line gets its own factory subclass that overrides a creation method. Better when you need to extend factories without editing a central `if/elif` block.

<br/>
<p>
    <span style="float: left;">
        <a href="1100_prototype.md">Previous: Prototype</a>
        &nbsp;
        <a href="1210_simple_factory.md">Next: Simple Factory</a>
    </span>
    <span style="float: right;">
        <a href="../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="index.md">Back to Design Patterns Index</a>
    </span>
</p>
