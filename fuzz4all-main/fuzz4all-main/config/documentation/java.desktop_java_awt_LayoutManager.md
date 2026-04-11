# Interface LayoutManager

**Source:** `java.desktop\java\awt\LayoutManager.html`

### Class Description

```java
public interface
LayoutManager
```

Defines the interface for classes that know how to lay out

Container

s.

Swing's painting architecture assumes the children of a

JComponent

do not overlap. If a

JComponent

's

LayoutManager

allows
children to overlap, the

JComponent

must override

isOptimizedDrawingEnabled

to return false.

**All Known Subinterfaces:** LayoutManager2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void addLayoutComponent​(
String
name,

Component
comp)

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

**Parameters:**
- name

- the string to be associated with the component
- comp

- the component to be added

---

#### void removeLayoutComponent​(
Component
comp)

Removes the specified component from the layout.

**Parameters:**
- comp

- the component to be removed

---

#### Dimension
preferredLayoutSize​(
Container
parent)

Calculates the preferred size dimensions for the specified
container, given the components it contains.

**Parameters:**
- parent

- the container to be laid out

**Returns:**
- the preferred dimension for the container

**See Also:**
- minimumLayoutSize(java.awt.Container)

---

#### Dimension
minimumLayoutSize​(
Container
parent)

Calculates the minimum size dimensions for the specified
container, given the components it contains.

**Parameters:**
- parent

- the component to be laid out

**Returns:**
- the minimum dimension for the container

**See Also:**
- preferredLayoutSize(java.awt.Container)

---

#### void layoutContainer​(
Container
parent)

Lays out the specified container.

**Parameters:**
- parent

- the container to be laid out

---

### Additional Sections

#### Interface LayoutManager

**All Known Subinterfaces:** LayoutManager2

**All Known Implementing Classes:** BasicComboBoxUI.ComboBoxLayoutManager

,

BasicInternalFrameTitlePane.TitlePaneLayout

,

BasicInternalFrameUI.InternalFrameLayout

,

BasicOptionPaneUI.ButtonAreaLayout

,

BasicScrollBarUI

,

BasicSplitPaneDivider.DividerLayout

,

BasicSplitPaneUI.BasicHorizontalLayoutManager

,

BasicSplitPaneUI.BasicVerticalLayoutManager

,

BasicTabbedPaneUI.TabbedPaneLayout

,

BorderLayout

,

BoxLayout

,

CardLayout

,

DefaultMenuLayout

,

FlowLayout

,

GridBagLayout

,

GridLayout

,

GroupLayout

,

JRootPane.RootLayout

,

JSpinner.DateEditor

,

JSpinner.DefaultEditor

,

JSpinner.ListEditor

,

JSpinner.NumberEditor

,

MetalComboBoxUI.MetalComboBoxLayoutManager

,

MetalScrollBarUI

,

MetalTabbedPaneUI.TabbedPaneLayout

,

OverlayLayout

,

ScrollPaneLayout

,

ScrollPaneLayout.UIResource

,

SpringLayout

,

SynthScrollBarUI

,

ViewportLayout

```java
public interface
LayoutManager
```

Defines the interface for classes that know how to lay out

Container

s.

Swing's painting architecture assumes the children of a

JComponent

do not overlap. If a

JComponent

's

LayoutManager

allows
children to overlap, the

JComponent

must override

isOptimizedDrawingEnabled

to return false.

**See Also:** Container

,

JComponent.isOptimizedDrawingEnabled()

public interface

LayoutManager

Defines the interface for classes that know how to lay out

Container

s.

Swing's painting architecture assumes the children of a

JComponent

do not overlap. If a

JComponent

's

LayoutManager

allows
children to overlap, the

JComponent

must override

isOptimizedDrawingEnabled

to return false.

Swing's painting architecture assumes the children of a

JComponent

do not overlap. If a

JComponent

's

LayoutManager

allows
children to overlap, the

JComponent

must override

isOptimizedDrawingEnabled

to return false.

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

String

name,

Component

comp)

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

void

layoutContainer

​(

Container

parent)

Lays out the specified container.

Dimension

minimumLayoutSize

​(

Container

parent)

Calculates the minimum size dimensions for the specified
container, given the components it contains.

Dimension

preferredLayoutSize

​(

Container

parent)

Calculates the preferred size dimensions for the specified
container, given the components it contains.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from the layout.

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

String

name,

Component

comp)

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

void

layoutContainer

​(

Container

parent)

Lays out the specified container.

Dimension

minimumLayoutSize

​(

Container

parent)

Calculates the minimum size dimensions for the specified
container, given the components it contains.

Dimension

preferredLayoutSize

​(

Container

parent)

Calculates the preferred size dimensions for the specified
container, given the components it contains.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from the layout.

---

#### Method Summary

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

Lays out the specified container.

Calculates the minimum size dimensions for the specified
container, given the components it contains.

Calculates the preferred size dimensions for the specified
container, given the components it contains.

Removes the specified component from the layout.

============ METHOD DETAIL ==========

- Method Detail

- addLayoutComponent

```java
void addLayoutComponent​(
String
name,

Component
comp)
```

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

**Parameters:** name

- the string to be associated with the component
**Parameters:** comp

- the component to be added

- removeLayoutComponent

```java
void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout.

**Parameters:** comp

- the component to be removed

- preferredLayoutSize

```java
Dimension
preferredLayoutSize​(
Container
parent)
```

Calculates the preferred size dimensions for the specified
container, given the components it contains.

**Parameters:** parent

- the container to be laid out
**Returns:** the preferred dimension for the container
**See Also:** minimumLayoutSize(java.awt.Container)

- minimumLayoutSize

```java
Dimension
minimumLayoutSize​(
Container
parent)
```

Calculates the minimum size dimensions for the specified
container, given the components it contains.

**Parameters:** parent

- the component to be laid out
**Returns:** the minimum dimension for the container
**See Also:** preferredLayoutSize(java.awt.Container)

- layoutContainer

```java
void layoutContainer​(
Container
parent)
```

Lays out the specified container.

**Parameters:** parent

- the container to be laid out

Method Detail

- addLayoutComponent

```java
void addLayoutComponent​(
String
name,

Component
comp)
```

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

**Parameters:** name

- the string to be associated with the component
**Parameters:** comp

- the component to be added

- removeLayoutComponent

```java
void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout.

**Parameters:** comp

- the component to be removed

- preferredLayoutSize

```java
Dimension
preferredLayoutSize​(
Container
parent)
```

Calculates the preferred size dimensions for the specified
container, given the components it contains.

**Parameters:** parent

- the container to be laid out
**Returns:** the preferred dimension for the container
**See Also:** minimumLayoutSize(java.awt.Container)

- minimumLayoutSize

```java
Dimension
minimumLayoutSize​(
Container
parent)
```

Calculates the minimum size dimensions for the specified
container, given the components it contains.

**Parameters:** parent

- the component to be laid out
**Returns:** the minimum dimension for the container
**See Also:** preferredLayoutSize(java.awt.Container)

- layoutContainer

```java
void layoutContainer​(
Container
parent)
```

Lays out the specified container.

**Parameters:** parent

- the container to be laid out

---

#### Method Detail

addLayoutComponent

```java
void addLayoutComponent​(
String
name,

Component
comp)
```

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

**Parameters:** name

- the string to be associated with the component
**Parameters:** comp

- the component to be added

---

#### addLayoutComponent

void addLayoutComponent​(

String

name,

Component

comp)

If the layout manager uses a per-component string,
adds the component

comp

to the layout,
associating it
with the string specified by

name

.

removeLayoutComponent

```java
void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout.

**Parameters:** comp

- the component to be removed

---

#### removeLayoutComponent

void removeLayoutComponent​(

Component

comp)

Removes the specified component from the layout.

preferredLayoutSize

```java
Dimension
preferredLayoutSize​(
Container
parent)
```

Calculates the preferred size dimensions for the specified
container, given the components it contains.

**Parameters:** parent

- the container to be laid out
**Returns:** the preferred dimension for the container
**See Also:** minimumLayoutSize(java.awt.Container)

---

#### preferredLayoutSize

Dimension

preferredLayoutSize​(

Container

parent)

Calculates the preferred size dimensions for the specified
container, given the components it contains.

minimumLayoutSize

```java
Dimension
minimumLayoutSize​(
Container
parent)
```

Calculates the minimum size dimensions for the specified
container, given the components it contains.

**Parameters:** parent

- the component to be laid out
**Returns:** the minimum dimension for the container
**See Also:** preferredLayoutSize(java.awt.Container)

---

#### minimumLayoutSize

Dimension

minimumLayoutSize​(

Container

parent)

Calculates the minimum size dimensions for the specified
container, given the components it contains.

layoutContainer

```java
void layoutContainer​(
Container
parent)
```

Lays out the specified container.

**Parameters:** parent

- the container to be laid out

---

#### layoutContainer

void layoutContainer​(

Container

parent)

Lays out the specified container.

---

