# ⚙️ Mermaid Configuration Tutorial

Mermaid diagrams are highly customizable. This tutorial explores the different configurations methods available.

## 📝 Adding Comments in Mermaid Diagrams

Mermaid does not provide its own dedicated comment syntax.  
Because Mermaid is usually embedded inside another language (such as Markdown), you can rely on the **host language’s comment style** instead.  

Since this page is written in **Markdown**, we can simply use Markdown comments here.

 
 ~~~
```mermaid
%% An example comment
flowchart LR
    A
    B

    %% Another example comment
    A --> B
```
~~~

```mermaid
%% An example comment
flowchart LR
    A
    B

    %% A To B LEFT TO RIGHT
    A --> B
```


## 🏷️ Title of Mermaid Diagram

~~~
```mermaid
---
title: Node Title  Here
---
flowchart LR
    A
```
~~~


```mermaid
---
title: Node Title  Here
---
flowchart LR
    A
```

<br/>

# 🛠️ Mermaid Configurations

## 🌐 1. Global Configuration

Mermaid allows you to set **global defaults** that apply to all diagrams.

~~~
```mermaid
%%{init: {'theme':'forest', 'logLevel':'debug'}}%%
flowchart LR
    A[Start] --> B[Configured Node]
~~~

```mermaid
%%{init: {'theme':'forest', 'logLevel':'debug'}}%%
flowchart LR
    A[Start] --> B[Configured Node]
```

<br/>

- `%%{init: {...}}%%` → is the configuration directive at the top of the diagram.

<br/>


## 🎨 2. Themes & Styling

Mermaid comes with built-in themes, but you can override styles.

### Built-in Themes
- `default`
- `forest`
- `dark`
- `neutral`
- `base`

This is explained above.

~~~
```mermaid
%%{init: {'theme':'dark'}}%%
flowchart LR
    A --> B
~~~

```mermaid
%%{init: {'theme':'dark'}}%%
flowchart LR
    A --> B
```

### Using CSS: Apply CSS styles using IDs

~~~
```mermaid
flowchart TD
    id1[Start] --> id2[Stop]

    style id1 fill:#f9f,stroke:#333,stroke-width:4px
    style id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff
```
~~~

```mermaid
flowchart TD
    id1[Start] --> id2[Stop]

    style id1 fill:#f9f,stroke:#333,stroke-width:4px
    style id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff
```

<br/>

### Define reusable style classes using `classDef` and apply using `:::`

~~~
```mermaid
flowchart TD
    A[Start]:::success --> B[Process]:::info --> C[End]:::success
    
    classDef success fill:#90EE90,stroke:#2d5016,stroke-width:2px
    classDef info fill:#87CEEB,stroke:#1a3a52,stroke-width:2px
```
~~~
```mermaid
flowchart TD
    A[Start]:::success --> B[Process]:::info
    
    classDef success fill:#90EE90,stroke:#2d5016,stroke-width:2px
    classDef info fill:#87CEEB,stroke:#1a3a52,stroke-width:2px
```

<br/>

### Apply a calss to an ID

```
```mermaid
flowchart TD
    A[Start] --> B[Process]
    
    classDef success fill:yellow,stroke:black,stroke-width:2px
    classDef info fill:cyan,stroke:red,stroke-width:2px

    class A success
    class B info
```

```mermaid
flowchart TD
    A[Start] --> B[Process]
    
    classDef success fill:yellow,stroke:black,stroke-width:2px
    classDef info fill:cyan,stroke:red,stroke-width:2px

    class A success
    class B info
```

<br/>

### Default Class

~~~
```mermaid
flowchart TD
    A[Node 1] --> B[Node 2]

    classDef default fill:#f9f,stroke:#333,stroke-width:2px
```
~~~

```mermaid
flowchart TD
    A[Node 1] --> B[Node 2]

    classDef default fill:#f9f,stroke:#333,stroke-width:2px
```

<br/>

## 🔄 3. Layout Configuration

### Control diagram direction and spacing.

~~~
```mermaid
flowchart RL
    A[Left] --> B[Right]
```
~~~

```mermaid
flowchart RL
    A[Left] --> B[Right]
```

- Available Directions:
  - `TB` → Top to Bottom
  - `BT` → Bottom to Top
  - `LR` → Left to Right
  - `RL` → Right to Left

<br/><br/>

## 🔒 4. Security Configuration

Mermaid supports different **security levels** using below tag in `%%{init: {...}}%%`

`securityLevel`: `"strict"`, `"loose"`, `"antiscript"`

The **securityLevel** setting controls whether HTML tags are supported.  
For example: `<b>` for bold text.  

Allowing HTML tags can introduce the risk of **HTML injection vulnerabilities**, so this option should be used with caution.

> [!TIP] some renderer like VScode does not support it.

~~~
```mermaid
%%{init: {'securityLevel': 'loose'}}%%
flowchart TD
    A["<b>Bold HTML</b>"] --> B["<i>Italic HTML</i>"]
```
~~~

```mermaid
%%{init: {'securityLevel': 'loose'}}%%
flowchart TD
    A["<b>Bold HTML</b>"] --> B["<i>Italic HTML</i>"]
```

## 🧩 5. Diagram-Specific Configurations

Each diagram type has its own configuration options.

### Sequence Diagram
~~~
```mermaid
%%{init: {'sequence': {'mirrorActors': false, 'rightAngles': true}}}%%
sequenceDiagram
    participant User
    participant System
    User->>System: Request
    System-->>User: Response
```
~~~

```mermaid
%%{init: {'sequence': {'mirrorActors': false, 'rightAngles': true}}}%%
sequenceDiagram
    participant User
    participant System
    User->>System: Request
    System-->>User: Response
```

- `mirrorActors`: duplicates actors on both sides.
- `rightAngles`: forces right-angle connectors.

<br/>

### Gantt Chart
~~~
```mermaid
%%{init: {'gantt': {'titleTopMargin':25, 'barHeight':30}}}%%
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Development
    Task A :a1, 2025-11-01, 5d
    Task B :after a1, 3d
```
~~~

```mermaid
%%{
    init: {
        'gantt': {'titleTopMargin':25, 'barHeight':30},
        'themeVariables': { 'taskColor': '#ffcc00', 'taskTextColor': '#000000'}
    }
}%%
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Development
    Task A :a1, 2025-11-01, 5d
    Task B :after a1, 3d
```

<br/>

### Flowchart

`nodeSpacing` and `rankSpacing` in `init`.

~~~
```mermaid
%%{init: {'flowchart': {'nodeSpacing': 50, 'rankSpacing': 80}}}%%
flowchart LR
    A --> B --> C
~~~

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 50, 'rankSpacing': 80}}}%%
flowchart LR
    A --> B --> C
```

<br/><br/>

## 🚀 7. Advanced Configuration with JSON

You can pass many configurations as a JSON object to `init` as given below:


~~~
```mermaid
---
HEADING
---
%%{init: {
  'theme': 'forest',
  'themeVariables': { 'primaryColor': '#ffcc00', 'fontSize': '35px' },
  'flowchart': { 'curve': 'basis', 'nodeSpacing': 50, 'rankSpacing': 80 },
  'sequence': { 'mirrorActors': true, 'showSequenceNumbers': true },
  'gantt': { 'titleTopMargin': 25, 'barHeight': 30 },
  'class': { 'useMaxWidth': true },
  'state': { 'padding': 15, 'nodeSpacing': 40 }
}}%%
flowchart LR
    A --> B
```
~~~


```mermaid
---
HEADING
---
%%{init: {
  'theme': 'forest',
  'themeVariables': { 'primaryColor': '#ffcc00', 'fontSize': '35px' },
  'flowchart': { 'curve': 'basis', 'nodeSpacing': 50, 'rankSpacing': 80 },
  'sequence': { 'mirrorActors': true, 'showSequenceNumbers': true },
  'gantt': { 'titleTopMargin': 25, 'barHeight': 30 },
  'class': { 'useMaxWidth': true },
  'state': { 'padding': 15, 'nodeSpacing': 40 }
}}%%
flowchart LR
    A --> B
```