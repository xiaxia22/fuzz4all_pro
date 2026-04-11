# Class ColorType

**Source:** `java.desktop\javax\swing\plaf\synth\ColorType.html`

### Class Description

```java
public class
ColorType

extends
Object
```

A typesafe enumeration of colors that can be fetched from a style.

Each

SynthStyle

has a set of

ColorType

s that
are accessed by way of the

SynthStyle.getColor(SynthContext, ColorType)

method.

SynthStyle

's

installDefaults

will install
the

FOREGROUND

color
as the foreground of
the Component, and the

BACKGROUND

color to the background of
the component (assuming that you have not explicitly specified a
foreground and background color). Some components
support more color based properties, for
example

JList

has the property

selectionForeground

which will be mapped to

FOREGROUND

with a component state of

SynthConstants.SELECTED

.

The following example shows a custom

SynthStyle

that returns
a red Color for the

DISABLED

state, otherwise a black color.

```java
class MyStyle extends SynthStyle {
private Color disabledColor = new ColorUIResource(Color.RED);
private Color color = new ColorUIResource(Color.BLACK);
protected Color getColorForState(SynthContext context, ColorType type){
if (context.getComponentState() == SynthConstants.DISABLED) {
return disabledColor;
}
return color;
}
}
```

**Since:** 1.5

---

### Field Details

#### public static final
ColorType
FOREGROUND

ColorType for the foreground of a region.

---

#### public static final
ColorType
BACKGROUND

ColorType for the background of a region.

---

#### public static final
ColorType
TEXT_FOREGROUND

ColorType for the foreground of a region.

---

#### public static final
ColorType
TEXT_BACKGROUND

ColorType for the background of a region.

---

#### public static final
ColorType
FOCUS

ColorType for the focus.

---

#### public static final int MAX_COUNT

Maximum number of

ColorType

s.

---

### Constructor Details

#### protected ColorType​(
String
description)

Creates a new ColorType with the specified description.

**Parameters:**
- description

- String description of the ColorType.

---

### Method Details

#### public final int getID()

Returns a unique id, as an integer, for this ColorType.

**Returns:**
- a unique id, as an integer, for this ColorType.

---

#### public
String
toString()

Returns the textual description of this

ColorType

.
This is the same value that the

ColorType

was created
with.

**Overrides:**
- toString

in class

Object

**Returns:**
- the description of the string

---

### Additional Sections

#### Class ColorType

java.lang.Object

- javax.swing.plaf.synth.ColorType

javax.swing.plaf.synth.ColorType

```java
public class
ColorType

extends
Object
```

A typesafe enumeration of colors that can be fetched from a style.

Each

SynthStyle

has a set of

ColorType

s that
are accessed by way of the

SynthStyle.getColor(SynthContext, ColorType)

method.

SynthStyle

's

installDefaults

will install
the

FOREGROUND

color
as the foreground of
the Component, and the

BACKGROUND

color to the background of
the component (assuming that you have not explicitly specified a
foreground and background color). Some components
support more color based properties, for
example

JList

has the property

selectionForeground

which will be mapped to

FOREGROUND

with a component state of

SynthConstants.SELECTED

.

The following example shows a custom

SynthStyle

that returns
a red Color for the

DISABLED

state, otherwise a black color.

```java
class MyStyle extends SynthStyle {
private Color disabledColor = new ColorUIResource(Color.RED);
private Color color = new ColorUIResource(Color.BLACK);
protected Color getColorForState(SynthContext context, ColorType type){
if (context.getComponentState() == SynthConstants.DISABLED) {
return disabledColor;
}
return color;
}
}
```

**Since:** 1.5

public class

ColorType

extends

Object

A typesafe enumeration of colors that can be fetched from a style.

Each

SynthStyle

has a set of

ColorType

s that
are accessed by way of the

SynthStyle.getColor(SynthContext, ColorType)

method.

SynthStyle

's

installDefaults

will install
the

FOREGROUND

color
as the foreground of
the Component, and the

BACKGROUND

color to the background of
the component (assuming that you have not explicitly specified a
foreground and background color). Some components
support more color based properties, for
example

JList

has the property

selectionForeground

which will be mapped to

FOREGROUND

with a component state of

SynthConstants.SELECTED

.

The following example shows a custom

SynthStyle

that returns
a red Color for the

DISABLED

state, otherwise a black color.

```java
class MyStyle extends SynthStyle {
private Color disabledColor = new ColorUIResource(Color.RED);
private Color color = new ColorUIResource(Color.BLACK);
protected Color getColorForState(SynthContext context, ColorType type){
if (context.getComponentState() == SynthConstants.DISABLED) {
return disabledColor;
}
return color;
}
}
```

Each

SynthStyle

has a set of

ColorType

s that
are accessed by way of the

SynthStyle.getColor(SynthContext, ColorType)

method.

SynthStyle

's

installDefaults

will install
the

FOREGROUND

color
as the foreground of
the Component, and the

BACKGROUND

color to the background of
the component (assuming that you have not explicitly specified a
foreground and background color). Some components
support more color based properties, for
example

JList

has the property

selectionForeground

which will be mapped to

FOREGROUND

with a component state of

SynthConstants.SELECTED

.

The following example shows a custom

SynthStyle

that returns
a red Color for the

DISABLED

state, otherwise a black color.

```java
class MyStyle extends SynthStyle {
private Color disabledColor = new ColorUIResource(Color.RED);
private Color color = new ColorUIResource(Color.BLACK);
protected Color getColorForState(SynthContext context, ColorType type){
if (context.getComponentState() == SynthConstants.DISABLED) {
return disabledColor;
}
return color;
}
}
```

The following example shows a custom

SynthStyle

that returns
a red Color for the

DISABLED

state, otherwise a black color.

```java
class MyStyle extends SynthStyle {
private Color disabledColor = new ColorUIResource(Color.RED);
private Color color = new ColorUIResource(Color.BLACK);
protected Color getColorForState(SynthContext context, ColorType type){
if (context.getComponentState() == SynthConstants.DISABLED) {
return disabledColor;
}
return color;
}
}
```

class MyStyle extends SynthStyle {
private Color disabledColor = new ColorUIResource(Color.RED);
private Color color = new ColorUIResource(Color.BLACK);
protected Color getColorForState(SynthContext context, ColorType type){
if (context.getComponentState() == SynthConstants.DISABLED) {
return disabledColor;
}
return color;
}
}

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ColorType

BACKGROUND

ColorType for the background of a region.

static

ColorType

FOCUS

ColorType for the focus.

static

ColorType

FOREGROUND

ColorType for the foreground of a region.

static int

MAX_COUNT

Maximum number of

ColorType

s.

static

ColorType

TEXT_BACKGROUND

ColorType for the background of a region.

static

ColorType

TEXT_FOREGROUND

ColorType for the foreground of a region.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ColorType

​(

String

description)

Creates a new ColorType with the specified description.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getID

()

Returns a unique id, as an integer, for this ColorType.

String

toString

()

Returns the textual description of this

ColorType

.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static

ColorType

BACKGROUND

ColorType for the background of a region.

static

ColorType

FOCUS

ColorType for the focus.

static

ColorType

FOREGROUND

ColorType for the foreground of a region.

static int

MAX_COUNT

Maximum number of

ColorType

s.

static

ColorType

TEXT_BACKGROUND

ColorType for the background of a region.

static

ColorType

TEXT_FOREGROUND

ColorType for the foreground of a region.

---

#### Field Summary

ColorType for the background of a region.

ColorType for the focus.

ColorType for the foreground of a region.

Maximum number of

ColorType

s.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ColorType

​(

String

description)

Creates a new ColorType with the specified description.

---

#### Constructor Summary

Creates a new ColorType with the specified description.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getID

()

Returns a unique id, as an integer, for this ColorType.

String

toString

()

Returns the textual description of this

ColorType

.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a unique id, as an integer, for this ColorType.

Returns the textual description of this

ColorType

.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- FOREGROUND

```java
public static final
ColorType
FOREGROUND
```

ColorType for the foreground of a region.

- BACKGROUND

```java
public static final
ColorType
BACKGROUND
```

ColorType for the background of a region.

- TEXT_FOREGROUND

```java
public static final
ColorType
TEXT_FOREGROUND
```

ColorType for the foreground of a region.

- TEXT_BACKGROUND

```java
public static final
ColorType
TEXT_BACKGROUND
```

ColorType for the background of a region.

- FOCUS

```java
public static final
ColorType
FOCUS
```

ColorType for the focus.

- MAX_COUNT

```java
public static final int MAX_COUNT
```

Maximum number of

ColorType

s.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ColorType

```java
protected ColorType​(
String
description)
```

Creates a new ColorType with the specified description.

**Parameters:** description

- String description of the ColorType.

============ METHOD DETAIL ==========

- Method Detail

- getID

```java
public final int getID()
```

Returns a unique id, as an integer, for this ColorType.

**Returns:** a unique id, as an integer, for this ColorType.

- toString

```java
public
String
toString()
```

Returns the textual description of this

ColorType

.
This is the same value that the

ColorType

was created
with.

**Overrides:** toString

in class

Object
**Returns:** the description of the string

Field Detail

- FOREGROUND

```java
public static final
ColorType
FOREGROUND
```

ColorType for the foreground of a region.

- BACKGROUND

```java
public static final
ColorType
BACKGROUND
```

ColorType for the background of a region.

- TEXT_FOREGROUND

```java
public static final
ColorType
TEXT_FOREGROUND
```

ColorType for the foreground of a region.

- TEXT_BACKGROUND

```java
public static final
ColorType
TEXT_BACKGROUND
```

ColorType for the background of a region.

- FOCUS

```java
public static final
ColorType
FOCUS
```

ColorType for the focus.

- MAX_COUNT

```java
public static final int MAX_COUNT
```

Maximum number of

ColorType

s.

---

#### Field Detail

FOREGROUND

```java
public static final
ColorType
FOREGROUND
```

ColorType for the foreground of a region.

---

#### FOREGROUND

public static final

ColorType

FOREGROUND

ColorType for the foreground of a region.

BACKGROUND

```java
public static final
ColorType
BACKGROUND
```

ColorType for the background of a region.

---

#### BACKGROUND

public static final

ColorType

BACKGROUND

ColorType for the background of a region.

TEXT_FOREGROUND

```java
public static final
ColorType
TEXT_FOREGROUND
```

ColorType for the foreground of a region.

---

#### TEXT_FOREGROUND

public static final

ColorType

TEXT_FOREGROUND

ColorType for the foreground of a region.

TEXT_BACKGROUND

```java
public static final
ColorType
TEXT_BACKGROUND
```

ColorType for the background of a region.

---

#### TEXT_BACKGROUND

public static final

ColorType

TEXT_BACKGROUND

ColorType for the background of a region.

FOCUS

```java
public static final
ColorType
FOCUS
```

ColorType for the focus.

---

#### FOCUS

public static final

ColorType

FOCUS

ColorType for the focus.

MAX_COUNT

```java
public static final int MAX_COUNT
```

Maximum number of

ColorType

s.

---

#### MAX_COUNT

public static final int MAX_COUNT

Maximum number of

ColorType

s.

Constructor Detail

- ColorType

```java
protected ColorType​(
String
description)
```

Creates a new ColorType with the specified description.

**Parameters:** description

- String description of the ColorType.

---

#### Constructor Detail

ColorType

```java
protected ColorType​(
String
description)
```

Creates a new ColorType with the specified description.

**Parameters:** description

- String description of the ColorType.

---

#### ColorType

protected ColorType​(

String

description)

Creates a new ColorType with the specified description.

Method Detail

- getID

```java
public final int getID()
```

Returns a unique id, as an integer, for this ColorType.

**Returns:** a unique id, as an integer, for this ColorType.

- toString

```java
public
String
toString()
```

Returns the textual description of this

ColorType

.
This is the same value that the

ColorType

was created
with.

**Overrides:** toString

in class

Object
**Returns:** the description of the string

---

#### Method Detail

getID

```java
public final int getID()
```

Returns a unique id, as an integer, for this ColorType.

**Returns:** a unique id, as an integer, for this ColorType.

---

#### getID

public final int getID()

Returns a unique id, as an integer, for this ColorType.

toString

```java
public
String
toString()
```

Returns the textual description of this

ColorType

.
This is the same value that the

ColorType

was created
with.

**Overrides:** toString

in class

Object
**Returns:** the description of the string

---

#### toString

public

String

toString()

Returns the textual description of this

ColorType

.
This is the same value that the

ColorType

was created
with.

---

