# Interface Renderer

**Source:** `java.desktop\javax\swing\Renderer.html`

### Class Description

```java
public interface
Renderer
```

Defines the requirements for an object responsible for
"rendering" (displaying) a value.

**Since:** 1.2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setValue​(
Object
aValue,
boolean isSelected)

Specifies the value to display and whether or not the
value should be portrayed as "currently selected".

**Parameters:**
- aValue

- an Object object
- isSelected

- a boolean

---

#### Component
getComponent()

Returns the component used to render the value.

**Returns:**
- the Component responsible for displaying the value

---

### Additional Sections

#### Interface Renderer

```java
public interface
Renderer
```

Defines the requirements for an object responsible for
"rendering" (displaying) a value.

**Since:** 1.2

public interface

Renderer

Defines the requirements for an object responsible for
"rendering" (displaying) a value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Component

getComponent

()

Returns the component used to render the value.

void

setValue

​(

Object

aValue,
boolean isSelected)

Specifies the value to display and whether or not the
value should be portrayed as "currently selected".

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Component

getComponent

()

Returns the component used to render the value.

void

setValue

​(

Object

aValue,
boolean isSelected)

Specifies the value to display and whether or not the
value should be portrayed as "currently selected".

---

#### Method Summary

Returns the component used to render the value.

Specifies the value to display and whether or not the
value should be portrayed as "currently selected".

============ METHOD DETAIL ==========

- Method Detail

- setValue

```java
void setValue​(
Object
aValue,
boolean isSelected)
```

Specifies the value to display and whether or not the
value should be portrayed as "currently selected".

**Parameters:** aValue

- an Object object
**Parameters:** isSelected

- a boolean

- getComponent

```java
Component
getComponent()
```

Returns the component used to render the value.

**Returns:** the Component responsible for displaying the value

Method Detail

- setValue

```java
void setValue​(
Object
aValue,
boolean isSelected)
```

Specifies the value to display and whether or not the
value should be portrayed as "currently selected".

**Parameters:** aValue

- an Object object
**Parameters:** isSelected

- a boolean

- getComponent

```java
Component
getComponent()
```

Returns the component used to render the value.

**Returns:** the Component responsible for displaying the value

---

#### Method Detail

setValue

```java
void setValue​(
Object
aValue,
boolean isSelected)
```

Specifies the value to display and whether or not the
value should be portrayed as "currently selected".

**Parameters:** aValue

- an Object object
**Parameters:** isSelected

- a boolean

---

#### setValue

void setValue​(

Object

aValue,
boolean isSelected)

Specifies the value to display and whether or not the
value should be portrayed as "currently selected".

getComponent

```java
Component
getComponent()
```

Returns the component used to render the value.

**Returns:** the Component responsible for displaying the value

---

#### getComponent

Component

getComponent()

Returns the component used to render the value.

---

