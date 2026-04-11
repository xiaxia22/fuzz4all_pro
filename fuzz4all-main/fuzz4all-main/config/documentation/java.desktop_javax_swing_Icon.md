# Interface Icon

**Source:** `java.desktop\javax\swing\Icon.html`

### Class Description

```java
public interface
Icon
```

A small fixed size picture, typically used to decorate components.

**All Known Subinterfaces:** SynthIcon

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void paintIcon​(
Component
c,

Graphics
g,
int x,
int y)

Draw the icon at the specified location. Icon implementations
may use the Component argument to get properties useful for
painting, e.g. the foreground or background color.

**Parameters:**
- c

- a

Component

to get properties useful for painting
- g

- the graphics context
- x

- the X coordinate of the icon's top-left corner
- y

- the Y coordinate of the icon's top-left corner

---

#### int getIconWidth()

Returns the icon's width.

**Returns:**
- an int specifying the fixed width of the icon.

---

#### int getIconHeight()

Returns the icon's height.

**Returns:**
- an int specifying the fixed height of the icon.

---

### Additional Sections

#### Interface Icon

**All Known Subinterfaces:** SynthIcon

**All Known Implementing Classes:** IconUIResource

,

ImageIcon

,

MetalCheckBoxIcon

,

MetalComboBoxIcon

,

MetalIconFactory.FileIcon16

,

MetalIconFactory.FolderIcon16

,

MetalIconFactory.PaletteCloseIcon

,

MetalIconFactory.TreeControlIcon

,

MetalIconFactory.TreeFolderIcon

,

MetalIconFactory.TreeLeafIcon

```java
public interface
Icon
```

A small fixed size picture, typically used to decorate components.

**Since:** 1.2
**See Also:** ImageIcon

public interface

Icon

A small fixed size picture, typically used to decorate components.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getIconHeight

()

Returns the icon's height.

int

getIconWidth

()

Returns the icon's width.

void

paintIcon

​(

Component

c,

Graphics

g,
int x,
int y)

Draw the icon at the specified location.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getIconHeight

()

Returns the icon's height.

int

getIconWidth

()

Returns the icon's width.

void

paintIcon

​(

Component

c,

Graphics

g,
int x,
int y)

Draw the icon at the specified location.

---

#### Method Summary

Returns the icon's height.

Returns the icon's width.

Draw the icon at the specified location.

============ METHOD DETAIL ==========

- Method Detail

- paintIcon

```java
void paintIcon​(
Component
c,

Graphics
g,
int x,
int y)
```

Draw the icon at the specified location. Icon implementations
may use the Component argument to get properties useful for
painting, e.g. the foreground or background color.

**Parameters:** c

- a

Component

to get properties useful for painting
**Parameters:** g

- the graphics context
**Parameters:** x

- the X coordinate of the icon's top-left corner
**Parameters:** y

- the Y coordinate of the icon's top-left corner

- getIconWidth

```java
int getIconWidth()
```

Returns the icon's width.

**Returns:** an int specifying the fixed width of the icon.

- getIconHeight

```java
int getIconHeight()
```

Returns the icon's height.

**Returns:** an int specifying the fixed height of the icon.

Method Detail

- paintIcon

```java
void paintIcon​(
Component
c,

Graphics
g,
int x,
int y)
```

Draw the icon at the specified location. Icon implementations
may use the Component argument to get properties useful for
painting, e.g. the foreground or background color.

**Parameters:** c

- a

Component

to get properties useful for painting
**Parameters:** g

- the graphics context
**Parameters:** x

- the X coordinate of the icon's top-left corner
**Parameters:** y

- the Y coordinate of the icon's top-left corner

- getIconWidth

```java
int getIconWidth()
```

Returns the icon's width.

**Returns:** an int specifying the fixed width of the icon.

- getIconHeight

```java
int getIconHeight()
```

Returns the icon's height.

**Returns:** an int specifying the fixed height of the icon.

---

#### Method Detail

paintIcon

```java
void paintIcon​(
Component
c,

Graphics
g,
int x,
int y)
```

Draw the icon at the specified location. Icon implementations
may use the Component argument to get properties useful for
painting, e.g. the foreground or background color.

**Parameters:** c

- a

Component

to get properties useful for painting
**Parameters:** g

- the graphics context
**Parameters:** x

- the X coordinate of the icon's top-left corner
**Parameters:** y

- the Y coordinate of the icon's top-left corner

---

#### paintIcon

void paintIcon​(

Component

c,

Graphics

g,
int x,
int y)

Draw the icon at the specified location. Icon implementations
may use the Component argument to get properties useful for
painting, e.g. the foreground or background color.

getIconWidth

```java
int getIconWidth()
```

Returns the icon's width.

**Returns:** an int specifying the fixed width of the icon.

---

#### getIconWidth

int getIconWidth()

Returns the icon's width.

getIconHeight

```java
int getIconHeight()
```

Returns the icon's height.

**Returns:** an int specifying the fixed height of the icon.

---

#### getIconHeight

int getIconHeight()

Returns the icon's height.

---

