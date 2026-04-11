# Interface Border

**Source:** `java.desktop\javax\swing\border\Border.html`

### Class Description

```java
public interface
Border
```

Interface describing an object capable of rendering a border
around the edges of a swing component.
For examples of using borders see

How to Use Borders

,
a section in

The Java Tutorial.

In the Swing component set, borders supercede Insets as the
mechanism for creating a (decorated or plain) area around the
edge of a component.

Usage Notes:

- Use EmptyBorder to create a plain border (this mechanism
replaces its predecessor,

setInsets

).

Use CompoundBorder to nest multiple border objects, creating
a single, combined border.

Border instances are designed to be shared. Rather than creating
a new border object using one of border classes, use the
BorderFactory methods, which produces a shared instance of the
common border types.

Additional border styles include BevelBorder, SoftBevelBorder,
EtchedBorder, LineBorder, TitledBorder, and MatteBorder.

To create a new border class, subclass AbstractBorder.

**All Known Implementing Classes:** AbstractBorder

,

BasicBorders.ButtonBorder

,

BasicBorders.FieldBorder

,

BasicBorders.MarginBorder

,

BasicBorders.MenuBarBorder

,

BasicBorders.RadioButtonBorder

,

BasicBorders.RolloverButtonBorder

,

BasicBorders.SplitPaneBorder

,

BasicBorders.ToggleButtonBorder

,

BevelBorder

,

BorderUIResource

,

BorderUIResource.BevelBorderUIResource

,

BorderUIResource.CompoundBorderUIResource

,

BorderUIResource.EmptyBorderUIResource

,

BorderUIResource.EtchedBorderUIResource

,

BorderUIResource.LineBorderUIResource

,

BorderUIResource.MatteBorderUIResource

,

BorderUIResource.TitledBorderUIResource

,

CompoundBorder

,

EmptyBorder

,

EtchedBorder

,

LineBorder

,

MatteBorder

,

MetalBorders.ButtonBorder

,

MetalBorders.Flush3DBorder

,

MetalBorders.InternalFrameBorder

,

MetalBorders.MenuBarBorder

,

MetalBorders.MenuItemBorder

,

MetalBorders.OptionDialogBorder

,

MetalBorders.PaletteBorder

,

MetalBorders.PopupMenuBorder

,

MetalBorders.RolloverButtonBorder

,

MetalBorders.ScrollPaneBorder

,

MetalBorders.TableHeaderBorder

,

MetalBorders.TextFieldBorder

,

MetalBorders.ToggleButtonBorder

,

MetalBorders.ToolBarBorder

,

SoftBevelBorder

,

StrokeBorder

,

TitledBorder

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the specified
position and size.

**Parameters:**
- c

- the component for which this border is being painted
- g

- the paint graphics
- x

- the x position of the painted border
- y

- the y position of the painted border
- width

- the width of the painted border
- height

- the height of the painted border

---

#### Insets
getBorderInsets​(
Component
c)

Returns the insets of the border.

**Parameters:**
- c

- the component for which this border insets value applies

**Returns:**
- an

Insets

object containing the insets from top, left,
bottom and right of this

Border

---

#### boolean isBorderOpaque()

Returns whether or not the border is opaque. If the border
is opaque, it is responsible for filling in it's own
background when painting.

**Returns:**
- true if this

Border

is opaque

---

### Additional Sections

#### Interface Border

**All Known Implementing Classes:** AbstractBorder

,

BasicBorders.ButtonBorder

,

BasicBorders.FieldBorder

,

BasicBorders.MarginBorder

,

BasicBorders.MenuBarBorder

,

BasicBorders.RadioButtonBorder

,

BasicBorders.RolloverButtonBorder

,

BasicBorders.SplitPaneBorder

,

BasicBorders.ToggleButtonBorder

,

BevelBorder

,

BorderUIResource

,

BorderUIResource.BevelBorderUIResource

,

BorderUIResource.CompoundBorderUIResource

,

BorderUIResource.EmptyBorderUIResource

,

BorderUIResource.EtchedBorderUIResource

,

BorderUIResource.LineBorderUIResource

,

BorderUIResource.MatteBorderUIResource

,

BorderUIResource.TitledBorderUIResource

,

CompoundBorder

,

EmptyBorder

,

EtchedBorder

,

LineBorder

,

MatteBorder

,

MetalBorders.ButtonBorder

,

MetalBorders.Flush3DBorder

,

MetalBorders.InternalFrameBorder

,

MetalBorders.MenuBarBorder

,

MetalBorders.MenuItemBorder

,

MetalBorders.OptionDialogBorder

,

MetalBorders.PaletteBorder

,

MetalBorders.PopupMenuBorder

,

MetalBorders.RolloverButtonBorder

,

MetalBorders.ScrollPaneBorder

,

MetalBorders.TableHeaderBorder

,

MetalBorders.TextFieldBorder

,

MetalBorders.ToggleButtonBorder

,

MetalBorders.ToolBarBorder

,

SoftBevelBorder

,

StrokeBorder

,

TitledBorder

```java
public interface
Border
```

Interface describing an object capable of rendering a border
around the edges of a swing component.
For examples of using borders see

How to Use Borders

,
a section in

The Java Tutorial.

In the Swing component set, borders supercede Insets as the
mechanism for creating a (decorated or plain) area around the
edge of a component.

Usage Notes:

- Use EmptyBorder to create a plain border (this mechanism
replaces its predecessor,

setInsets

).

Use CompoundBorder to nest multiple border objects, creating
a single, combined border.

Border instances are designed to be shared. Rather than creating
a new border object using one of border classes, use the
BorderFactory methods, which produces a shared instance of the
common border types.

Additional border styles include BevelBorder, SoftBevelBorder,
EtchedBorder, LineBorder, TitledBorder, and MatteBorder.

To create a new border class, subclass AbstractBorder.

**See Also:** BorderFactory

,

EmptyBorder

,

CompoundBorder

public interface

Border

Interface describing an object capable of rendering a border
around the edges of a swing component.
For examples of using borders see

How to Use Borders

,
a section in

The Java Tutorial.

In the Swing component set, borders supercede Insets as the
mechanism for creating a (decorated or plain) area around the
edge of a component.

Usage Notes:

- Use EmptyBorder to create a plain border (this mechanism
replaces its predecessor,

setInsets

).

Use CompoundBorder to nest multiple border objects, creating
a single, combined border.

Border instances are designed to be shared. Rather than creating
a new border object using one of border classes, use the
BorderFactory methods, which produces a shared instance of the
common border types.

Additional border styles include BevelBorder, SoftBevelBorder,
EtchedBorder, LineBorder, TitledBorder, and MatteBorder.

To create a new border class, subclass AbstractBorder.

In the Swing component set, borders supercede Insets as the
mechanism for creating a (decorated or plain) area around the
edge of a component.

Usage Notes:

- Use EmptyBorder to create a plain border (this mechanism
replaces its predecessor,

setInsets

).

Use CompoundBorder to nest multiple border objects, creating
a single, combined border.

Border instances are designed to be shared. Rather than creating
a new border object using one of border classes, use the
BorderFactory methods, which produces a shared instance of the
common border types.

Additional border styles include BevelBorder, SoftBevelBorder,
EtchedBorder, LineBorder, TitledBorder, and MatteBorder.

To create a new border class, subclass AbstractBorder.

Usage Notes:

- Use EmptyBorder to create a plain border (this mechanism
replaces its predecessor,

setInsets

).

Use CompoundBorder to nest multiple border objects, creating
a single, combined border.

Border instances are designed to be shared. Rather than creating
a new border object using one of border classes, use the
BorderFactory methods, which produces a shared instance of the
common border types.

Additional border styles include BevelBorder, SoftBevelBorder,
EtchedBorder, LineBorder, TitledBorder, and MatteBorder.

To create a new border class, subclass AbstractBorder.

Use EmptyBorder to create a plain border (this mechanism
replaces its predecessor,

setInsets

).

Use CompoundBorder to nest multiple border objects, creating
a single, combined border.

Border instances are designed to be shared. Rather than creating
a new border object using one of border classes, use the
BorderFactory methods, which produces a shared instance of the
common border types.

Additional border styles include BevelBorder, SoftBevelBorder,
EtchedBorder, LineBorder, TitledBorder, and MatteBorder.

To create a new border class, subclass AbstractBorder.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Insets

getBorderInsets

​(

Component

c)

Returns the insets of the border.

boolean

isBorderOpaque

()

Returns whether or not the border is opaque.

void

paintBorder

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the specified
position and size.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Insets

getBorderInsets

​(

Component

c)

Returns the insets of the border.

boolean

isBorderOpaque

()

Returns whether or not the border is opaque.

void

paintBorder

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the specified
position and size.

---

#### Method Summary

Returns the insets of the border.

Returns whether or not the border is opaque.

Paints the border for the specified component with the specified
position and size.

============ METHOD DETAIL ==========

- Method Detail

- paintBorder

```java
void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the border for the specified component with the specified
position and size.

**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

- getBorderInsets

```java
Insets
getBorderInsets​(
Component
c)
```

Returns the insets of the border.

**Parameters:** c

- the component for which this border insets value applies
**Returns:** an

Insets

object containing the insets from top, left,
bottom and right of this

Border

- isBorderOpaque

```java
boolean isBorderOpaque()
```

Returns whether or not the border is opaque. If the border
is opaque, it is responsible for filling in it's own
background when painting.

**Returns:** true if this

Border

is opaque

Method Detail

- paintBorder

```java
void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the border for the specified component with the specified
position and size.

**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

- getBorderInsets

```java
Insets
getBorderInsets​(
Component
c)
```

Returns the insets of the border.

**Parameters:** c

- the component for which this border insets value applies
**Returns:** an

Insets

object containing the insets from top, left,
bottom and right of this

Border

- isBorderOpaque

```java
boolean isBorderOpaque()
```

Returns whether or not the border is opaque. If the border
is opaque, it is responsible for filling in it's own
background when painting.

**Returns:** true if this

Border

is opaque

---

#### Method Detail

paintBorder

```java
void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the border for the specified component with the specified
position and size.

**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

---

#### paintBorder

void paintBorder​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the specified
position and size.

getBorderInsets

```java
Insets
getBorderInsets​(
Component
c)
```

Returns the insets of the border.

**Parameters:** c

- the component for which this border insets value applies
**Returns:** an

Insets

object containing the insets from top, left,
bottom and right of this

Border

---

#### getBorderInsets

Insets

getBorderInsets​(

Component

c)

Returns the insets of the border.

isBorderOpaque

```java
boolean isBorderOpaque()
```

Returns whether or not the border is opaque. If the border
is opaque, it is responsible for filling in it's own
background when painting.

**Returns:** true if this

Border

is opaque

---

#### isBorderOpaque

boolean isBorderOpaque()

Returns whether or not the border is opaque. If the border
is opaque, it is responsible for filling in it's own
background when painting.

---

