# Interface LayoutManager2

**Source:** `java.desktop\java\awt\LayoutManager2.html`

### Class Description

```java
public interface
LayoutManager2

extends
LayoutManager
```

Defines an interface for classes that know how to layout Containers
based on a layout constraints object.

This interface extends the LayoutManager interface to deal with layouts
explicitly in terms of constraint objects that specify how and where
components should be added to the layout.

This minimal extension to LayoutManager is intended for tool
providers who wish to the creation of constraint-based layouts.
It does not yet provide full, general support for custom
constraint-based layout managers.

**All Superinterfaces:** LayoutManager

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void addLayoutComponent​(
Component
comp,

Object
constraints)

Adds the specified component to the layout, using the specified
constraint object.

**Parameters:**
- comp

- the component to be added
- constraints

- where/how the component is added to the layout.

---

#### Dimension
maximumLayoutSize​(
Container
target)

Calculates the maximum size dimensions for the specified container,
given the components it contains.

**Parameters:**
- target

- the target container

**Returns:**
- the maximum size of the container

**See Also:**
- Component.getMaximumSize()

,

LayoutManager

---

#### float getLayoutAlignmentX​(
Container
target)

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Parameters:**
- target

- the target container

**Returns:**
- the x-axis alignment preference

---

#### float getLayoutAlignmentY​(
Container
target)

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Parameters:**
- target

- the target container

**Returns:**
- the y-axis alignment preference

---

#### void invalidateLayout​(
Container
target)

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

**Parameters:**
- target

- the target container

---

### Additional Sections

#### Interface LayoutManager2

**All Superinterfaces:** LayoutManager

**All Known Implementing Classes:** BasicSplitPaneUI.BasicHorizontalLayoutManager

,

BasicSplitPaneUI.BasicVerticalLayoutManager

,

BorderLayout

,

BoxLayout

,

CardLayout

,

DefaultMenuLayout

,

GridBagLayout

,

GroupLayout

,

JRootPane.RootLayout

,

OverlayLayout

,

SpringLayout

```java
public interface
LayoutManager2

extends
LayoutManager
```

Defines an interface for classes that know how to layout Containers
based on a layout constraints object.

This interface extends the LayoutManager interface to deal with layouts
explicitly in terms of constraint objects that specify how and where
components should be added to the layout.

This minimal extension to LayoutManager is intended for tool
providers who wish to the creation of constraint-based layouts.
It does not yet provide full, general support for custom
constraint-based layout managers.

**See Also:** LayoutManager

,

Container

public interface

LayoutManager2

extends

LayoutManager

Defines an interface for classes that know how to layout Containers
based on a layout constraints object.

This interface extends the LayoutManager interface to deal with layouts
explicitly in terms of constraint objects that specify how and where
components should be added to the layout.

This minimal extension to LayoutManager is intended for tool
providers who wish to the creation of constraint-based layouts.
It does not yet provide full, general support for custom
constraint-based layout managers.

This minimal extension to LayoutManager is intended for tool
providers who wish to the creation of constraint-based layouts.
It does not yet provide full, general support for custom
constraint-based layout managers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addLayoutComponent

​(

Component

comp,

Object

constraints)

Adds the specified component to the layout, using the specified
constraint object.

float

getLayoutAlignmentX

​(

Container

target)

Returns the alignment along the x axis.

float

getLayoutAlignmentY

​(

Container

target)

Returns the alignment along the y axis.

void

invalidateLayout

​(

Container

target)

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

Dimension

maximumLayoutSize

​(

Container

target)

Calculates the maximum size dimensions for the specified container,
given the components it contains.

- Methods declared in interface java.awt.

LayoutManager

addLayoutComponent

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

removeLayoutComponent

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addLayoutComponent

​(

Component

comp,

Object

constraints)

Adds the specified component to the layout, using the specified
constraint object.

float

getLayoutAlignmentX

​(

Container

target)

Returns the alignment along the x axis.

float

getLayoutAlignmentY

​(

Container

target)

Returns the alignment along the y axis.

void

invalidateLayout

​(

Container

target)

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

Dimension

maximumLayoutSize

​(

Container

target)

Calculates the maximum size dimensions for the specified container,
given the components it contains.

- Methods declared in interface java.awt.

LayoutManager

addLayoutComponent

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

removeLayoutComponent

---

#### Method Summary

Adds the specified component to the layout, using the specified
constraint object.

Returns the alignment along the x axis.

Returns the alignment along the y axis.

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

Calculates the maximum size dimensions for the specified container,
given the components it contains.

Methods declared in interface java.awt.

LayoutManager

addLayoutComponent

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

removeLayoutComponent

---

#### Methods declared in interface java.awt. LayoutManager

============ METHOD DETAIL ==========

- Method Detail

- addLayoutComponent

```java
void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to the layout, using the specified
constraint object.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- where/how the component is added to the layout.

- maximumLayoutSize

```java
Dimension
maximumLayoutSize​(
Container
target)
```

Calculates the maximum size dimensions for the specified container,
given the components it contains.

**Parameters:** target

- the target container
**Returns:** the maximum size of the container
**See Also:** Component.getMaximumSize()

,

LayoutManager

- getLayoutAlignmentX

```java
float getLayoutAlignmentX​(
Container
target)
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Parameters:** target

- the target container
**Returns:** the x-axis alignment preference

- getLayoutAlignmentY

```java
float getLayoutAlignmentY​(
Container
target)
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Parameters:** target

- the target container
**Returns:** the y-axis alignment preference

- invalidateLayout

```java
void invalidateLayout​(
Container
target)
```

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

**Parameters:** target

- the target container

Method Detail

- addLayoutComponent

```java
void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to the layout, using the specified
constraint object.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- where/how the component is added to the layout.

- maximumLayoutSize

```java
Dimension
maximumLayoutSize​(
Container
target)
```

Calculates the maximum size dimensions for the specified container,
given the components it contains.

**Parameters:** target

- the target container
**Returns:** the maximum size of the container
**See Also:** Component.getMaximumSize()

,

LayoutManager

- getLayoutAlignmentX

```java
float getLayoutAlignmentX​(
Container
target)
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Parameters:** target

- the target container
**Returns:** the x-axis alignment preference

- getLayoutAlignmentY

```java
float getLayoutAlignmentY​(
Container
target)
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Parameters:** target

- the target container
**Returns:** the y-axis alignment preference

- invalidateLayout

```java
void invalidateLayout​(
Container
target)
```

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

**Parameters:** target

- the target container

---

#### Method Detail

addLayoutComponent

```java
void addLayoutComponent​(
Component
comp,

Object
constraints)
```

Adds the specified component to the layout, using the specified
constraint object.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- where/how the component is added to the layout.

---

#### addLayoutComponent

void addLayoutComponent​(

Component

comp,

Object

constraints)

Adds the specified component to the layout, using the specified
constraint object.

maximumLayoutSize

```java
Dimension
maximumLayoutSize​(
Container
target)
```

Calculates the maximum size dimensions for the specified container,
given the components it contains.

**Parameters:** target

- the target container
**Returns:** the maximum size of the container
**See Also:** Component.getMaximumSize()

,

LayoutManager

---

#### maximumLayoutSize

Dimension

maximumLayoutSize​(

Container

target)

Calculates the maximum size dimensions for the specified container,
given the components it contains.

getLayoutAlignmentX

```java
float getLayoutAlignmentX​(
Container
target)
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Parameters:** target

- the target container
**Returns:** the x-axis alignment preference

---

#### getLayoutAlignmentX

float getLayoutAlignmentX​(

Container

target)

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

getLayoutAlignmentY

```java
float getLayoutAlignmentY​(
Container
target)
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Parameters:** target

- the target container
**Returns:** the y-axis alignment preference

---

#### getLayoutAlignmentY

float getLayoutAlignmentY​(

Container

target)

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

invalidateLayout

```java
void invalidateLayout​(
Container
target)
```

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

**Parameters:** target

- the target container

---

#### invalidateLayout

void invalidateLayout​(

Container

target)

Invalidates the layout, indicating that if the layout manager
has cached information it should be discarded.

---

