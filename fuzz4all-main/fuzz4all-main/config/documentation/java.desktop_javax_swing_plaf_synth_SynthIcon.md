# Interface SynthIcon

**Source:** `java.desktop\javax\swing\plaf\synth\SynthIcon.html`

### Class Description

```java
public interface
SynthIcon

extends
Icon
```

An icon that is passed a

SynthContext

. Subclasses need only implement
the variants that take a

SynthContext

, but must be prepared for the

SynthContext

to be null.

**All Superinterfaces:** Icon

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void paintIcon​(
SynthContext
context,

Graphics
g,
int x,
int y,
int width,
int height)

Paints the icon at the specified location for the given synth context.

**Parameters:**
- context

- identifies hosting region, may be null.
- g

- the graphics context
- x

- the x location to paint to
- y

- the y location to paint to
- width

- the width of the region to paint to, may be 0
- height

- the height of the region to paint to, may be 0

---

#### int getIconWidth​(
SynthContext
context)

Returns the icon's width for the given synth context.

**Parameters:**
- context

-

SynthContext

requesting the Icon, may be null.

**Returns:**
- an int specifying the width of the icon.

---

#### int getIconHeight​(
SynthContext
context)

Returns the icon's height for the given synth context.

**Parameters:**
- context

-

SynthContext

requesting the Icon, may be null.

**Returns:**
- an int specifying the height of the icon.

---

### Additional Sections

#### Interface SynthIcon

**All Superinterfaces:** Icon

```java
public interface
SynthIcon

extends
Icon
```

An icon that is passed a

SynthContext

. Subclasses need only implement
the variants that take a

SynthContext

, but must be prepared for the

SynthContext

to be null.

public interface

SynthIcon

extends

Icon

An icon that is passed a

SynthContext

. Subclasses need only implement
the variants that take a

SynthContext

, but must be prepared for the

SynthContext

to be null.

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

​(

SynthContext

context)

Returns the icon's height for the given synth context.

int

getIconWidth

​(

SynthContext

context)

Returns the icon's width for the given synth context.

void

paintIcon

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the icon at the specified location for the given synth context.

- Methods declared in interface javax.swing.

Icon

getIconHeight

,

getIconWidth

,

paintIcon

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getIconHeight

​(

SynthContext

context)

Returns the icon's height for the given synth context.

int

getIconWidth

​(

SynthContext

context)

Returns the icon's width for the given synth context.

void

paintIcon

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the icon at the specified location for the given synth context.

- Methods declared in interface javax.swing.

Icon

getIconHeight

,

getIconWidth

,

paintIcon

---

#### Method Summary

Returns the icon's height for the given synth context.

Returns the icon's width for the given synth context.

Paints the icon at the specified location for the given synth context.

Methods declared in interface javax.swing.

Icon

getIconHeight

,

getIconWidth

,

paintIcon

---

#### Methods declared in interface javax.swing. Icon

============ METHOD DETAIL ==========

- Method Detail

- paintIcon

```java
void paintIcon​(
SynthContext
context,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the icon at the specified location for the given synth context.

**Parameters:** context

- identifies hosting region, may be null.
**Parameters:** g

- the graphics context
**Parameters:** x

- the x location to paint to
**Parameters:** y

- the y location to paint to
**Parameters:** width

- the width of the region to paint to, may be 0
**Parameters:** height

- the height of the region to paint to, may be 0

- getIconWidth

```java
int getIconWidth​(
SynthContext
context)
```

Returns the icon's width for the given synth context.

**Parameters:** context

-

SynthContext

requesting the Icon, may be null.
**Returns:** an int specifying the width of the icon.

- getIconHeight

```java
int getIconHeight​(
SynthContext
context)
```

Returns the icon's height for the given synth context.

**Parameters:** context

-

SynthContext

requesting the Icon, may be null.
**Returns:** an int specifying the height of the icon.

Method Detail

- paintIcon

```java
void paintIcon​(
SynthContext
context,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the icon at the specified location for the given synth context.

**Parameters:** context

- identifies hosting region, may be null.
**Parameters:** g

- the graphics context
**Parameters:** x

- the x location to paint to
**Parameters:** y

- the y location to paint to
**Parameters:** width

- the width of the region to paint to, may be 0
**Parameters:** height

- the height of the region to paint to, may be 0

- getIconWidth

```java
int getIconWidth​(
SynthContext
context)
```

Returns the icon's width for the given synth context.

**Parameters:** context

-

SynthContext

requesting the Icon, may be null.
**Returns:** an int specifying the width of the icon.

- getIconHeight

```java
int getIconHeight​(
SynthContext
context)
```

Returns the icon's height for the given synth context.

**Parameters:** context

-

SynthContext

requesting the Icon, may be null.
**Returns:** an int specifying the height of the icon.

---

#### Method Detail

paintIcon

```java
void paintIcon​(
SynthContext
context,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the icon at the specified location for the given synth context.

**Parameters:** context

- identifies hosting region, may be null.
**Parameters:** g

- the graphics context
**Parameters:** x

- the x location to paint to
**Parameters:** y

- the y location to paint to
**Parameters:** width

- the width of the region to paint to, may be 0
**Parameters:** height

- the height of the region to paint to, may be 0

---

#### paintIcon

void paintIcon​(

SynthContext

context,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the icon at the specified location for the given synth context.

getIconWidth

```java
int getIconWidth​(
SynthContext
context)
```

Returns the icon's width for the given synth context.

**Parameters:** context

-

SynthContext

requesting the Icon, may be null.
**Returns:** an int specifying the width of the icon.

---

#### getIconWidth

int getIconWidth​(

SynthContext

context)

Returns the icon's width for the given synth context.

getIconHeight

```java
int getIconHeight​(
SynthContext
context)
```

Returns the icon's height for the given synth context.

**Parameters:** context

-

SynthContext

requesting the Icon, may be null.
**Returns:** an int specifying the height of the icon.

---

#### getIconHeight

int getIconHeight​(

SynthContext

context)

Returns the icon's height for the given synth context.

---

