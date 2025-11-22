# 🔀 Flowchart Diagrams

A **flowchart** is a visual representation of a process or workflow using connected shapes and arrows. It shows the step-by-step flow of logic, decisions, and actions.

A simplest flowchart can be represented in **mermaid** using:
~~~
```mermaid
flowchart
flowchart
    NODE_ID1[NODE 1] --LINK TEXT--> NODE_ID2[NODE 2]
```
~~~

And its visual diagram looks like:
```mermaid
flowchart
    NODE_ID1[NODE 1] --LINK TEXT--> NODE_ID2[NODE 2]
```

It contains:
1. Node
2. Link
3. Link text

## 📐 Node Shapes Supported by `flowchart`

Mermaid supports many different node shapes. Some common examples are shown below:

### Example: Multiple Shapes

~~~
```mermaid
flowchart
    A1[Rt]
    A2(Rr)
    A3([St])
    A4[[Sr]]
    A5[(Cy)]
    A6((Cr))
    A7{Dm}
    A8{{Hx}}
    A9[/Pl/]
    A10[\Pl\]
```
~~~
And the output is given below:
```mermaid
flowchart
    A1[Rt]
    A2(Rr)
    A3([St])
    A4[[Sr]]
    A5[(Cy)]
    A6((Cr))
    A7{Dm}
    A8{{Hx}}
    A9[/Pl/]
    A10[\Pl\]
```

## 🧭 Flowchart Links

Nodes are connected using links.

### 1. Link labels:

Links can include descriptive text labels:

~~~
```mermaid
flowchart
    N1[N1] --I am Link Label--> N2[N2]
    N3[N3] -->|Another way to insert Label| N4[N4]
    N5[N5] -->|You can <b>bold</b><br/>and break| N6[N6]
```
~~~

And the corresponding diagram looks like:

```mermaid
flowchart
    N1[N1] --I am Link Label--> N2[N2]
    N3[N3] -->|Another way to insert Label| N4[N4]
    N5[N5] -->|You can <b>bold</b><br/>and break| N6[N6]
```

### 2. Link Arrows

~~~
```mermaid
flowchart
    N1[N1] --1-- N2[N2]
    N3[N3] --2--> N4[N4]
    N5[N5] <--3--> N6[N6]
```
~~~

```mermaid
flowchart
    N1[N1] --No Arrow--- N2[N2]
    N3[N3] --One Side--> N4[N4]
    N5[N5] <--Two Side--> N6[N6]
```

### 2. Link Length

~~~
```mermaid
flowchart
    N1[N1] --Small-- N2[N2]
    N3[N3] --Big--- N4[N4]
```
~~~

```mermaid
flowchart
    N1[N1] --Small--- N2[N2]
    N3[N3] --Biggg---- N4[N4]
    N5[N5] --Bigst----- N6[N6]
```

> [!TIP]
> - Adding more than 2 dashes on **left side** is an error: `---Text-->` Error.
> - But adding dashes on right side increases the length of the link: `--Text--->` Increase the length.


## 🧭 Flowchart Directions

Control the layout direction of your flowchart:

| Direction | Code | Description |
|-----------|------|-------------|
| Top-Down | `flowchart TD` | Vertical flow (default) |
| Top-Down | `flowchart TB` | Same as `TD` |
| Bottom-Top | `flowchart BT` | Vertical flow reversed |
| Left-Right | `flowchart LR` | Horizontal flow |
| Right-Left | `flowchart RL` | Horizontal flow reversed |

### Direction Examples

```mermaid
flowchart LR
    A[Start] --> B[Process] --> C[End]
```

---

## 🔗 Links Between Nodes

Different link types connect nodes:

| Syntax | Type | Example |
|--------|------|---------|
| `A --> B` | Arrow | Directed link with arrowhead |
| `A --- B` | Open link | Line without arrowhead |
| `A -->&#124;text&#124;B` | Labeled arrow | Arrow with text label |
| `A -.- B` | Dotted link | Dashed line with arrow |
| `A == B` | Thick link | Bold line |
| `A ~~~ B` | Invisible link | Invisible (for positioning) |

### Link Examples

```mermaid
flowchart TD
    A[Start] --> B[Process]
    B -->|Yes| C[Success]
    B -->|No| D[Retry]
    D -.-> B
    B ==> E[End]
```

### Chaining Links

Connect multiple nodes in one statement:

```mermaid
flowchart TD
    A --> B & C --> D
```

This is equivalent to:
```
A --> B
A --> C
B --> D
C --> D
```

---

## 🎯 Decision Nodes

Use diamond nodes (`{ }`) for decisions that branch logic:

```mermaid
flowchart TD
    Start(Start) --> Input["Enter Age"]
    Input --> Check{Age >= 18?}
    Check -->|Yes| Adult["Access Granted"]
    Check -->|No| Minor["Access Denied"]
    Adult --> End(End)
    Minor --> End
```

Label the paths with `|Yes|`, `|No|`, etc. to clarify conditions.

---

## 📦 Subgraphs for Grouping

Organize related nodes into logical groups:

```mermaid
flowchart TD
    subgraph Input["User Input"]
        A["Enter Data"]
        B["Validate Format"]
    end
    
    subgraph Process["Processing"]
        C["Transform Data"]
        D["Calculate Results"]
    end
    
    subgraph Output["Results"]
        E["Display Output"]
        F["Save to Database"]
    end
    
    A --> B --> C --> D --> E --> F
```

### Direction Within Subgraphs

Control the flow direction inside subgraphs:

```mermaid
flowchart LR
    subgraph TOP
        direction TB
        subgraph B1
            direction RL
            i1 -->f1
        end
        subgraph B2
            direction BT
            i2 -->f2
        end
    end
    A --> TOP --> B
    B1 --> B2
```

---

## 🎨 Styling & Coloring

### Inline Style

Apply CSS styles directly to nodes:

```mermaid
flowchart TD
    id1[Start] --> id2[Stop]
    style id1 fill:#f9f,stroke:#333,stroke-width:4px
    style id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff
```

### Using Classes

Define reusable style classes:

```mermaid
flowchart TD
    A[Start]:::success --> B[Process]:::info --> C[End]:::success
    
    classDef success fill:#90EE90,stroke:#2d5016,stroke-width:2px
    classDef info fill:#87CEEB,stroke:#1a3a52,stroke-width:2px
```

### Default Class

Apply a style to all nodes without a specific class:

```mermaid
flowchart TD
    A[Node 1] --> B[Node 2]
    classDef default fill:#f9f,stroke:#333,stroke-width:2px
```

### Shorthand with `::`

Attach a class to a node using the `::` operator:

```mermaid
flowchart TD
    A:::success --> B:::warning --> C:::error
    
    classDef success fill:#90EE90
    classDef warning fill:#FFD700
    classDef error fill:#FFB6C1
```

---

## 🎯 Real-World Example: E-Commerce Checkout

```mermaid
flowchart TD
    Start(Customer Visits Shop) --> Browse["Browse Products"]
    Browse --> AddCart{Add to Cart?}
    AddCart -->|No| Browse
    AddCart -->|Yes| Cart["View Cart"]
    Cart --> Checkout{Proceed to Checkout?}
    Checkout -->|No| Browse
    Checkout -->|Yes| Payment["Enter Payment Info"]
    Payment --> Validate{Payment Valid?}
    Validate -->|No| Error["Show Error"]
    Error --> Payment
    Validate -->|Yes| Success["Order Confirmed"]
    Success --> End(End)
    
    style Start fill:#e1f5e1,stroke:#2d5016,stroke-width:2px
    style Success fill:#e1f5e1,stroke:#2d5016,stroke-width:2px
    style End fill:#e1f5e1,stroke:#2d5016,stroke-width:2px
    style Error fill:#ffe1e1,stroke:#5d0016,stroke-width:2px
```

---

## 🧪 Practice Exercise

Create a flowchart for a **login system** that:

1. Prompts the user for username and password
2. Validates credentials against a database
3. Shows an error message if credentials are invalid (loop back to step 1)
4. Redirects to the dashboard if credentials are valid

**Tip:** Use decision nodes for validation and subgraphs to organize input/processing sections.

Try it in the [Mermaid Live Editor](https://mermaid.live) and experiment with different layouts and styles!

---

## 📚 Additional Resources

- **Official Mermaid Docs:** [Flowchart Syntax](https://mermaid.js.org/syntax/flowchart.html)
- **Curve Styles:** `basis`, `bumpX`, `bumpY`, `cardinal`, `catmullRom`, `linear`, `monotoneX`, `monotoneY`, `natural`, `step`, `stepAfter`, `stepBefore`
- **Font Awesome Icons:** Use `fa:fa-icon-name` in node text
- **Markdown Text:** Enable with config `htmlLabels: false` and use backticks for markdown formatting

---

**Next:** Explore [Sequence Diagrams](./sequence-diagram.md) for visualizing interactions between entities over time.
