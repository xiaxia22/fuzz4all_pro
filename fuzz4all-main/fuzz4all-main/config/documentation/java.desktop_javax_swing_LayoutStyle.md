# Class LayoutStyle

**Source:** `java.desktop\javax\swing\LayoutStyle.html`

### Class Description

```java
public abstract class
LayoutStyle

extends
Object
```

LayoutStyle

provides information about how to position
components. This class is primarily useful for visual tools and
layout managers. Most developers will not need to use this class.

You typically don't set or create a

LayoutStyle

. Instead use the static method

getInstance

to obtain the current instance.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### public LayoutStyle()

Creates a new

LayoutStyle

. You generally don't
create a

LayoutStyle

. Instead use the method

getInstance

to obtain the current

LayoutStyle

.

---

### Method Details

#### public static void setInstance​(
LayoutStyle
style)

Sets the shared instance of

LayoutStyle

. Specifying

null

results in using the

LayoutStyle

from
the current

LookAndFeel

.

**Parameters:**
- style

- the

LayoutStyle

, or

null

**See Also:**
- getInstance()

---

#### public static
LayoutStyle
getInstance()

Returns the shared instance of

LayoutStyle

. If an instance
has not been specified in

setInstance

, this will return
the

LayoutStyle

from the current

LookAndFeel

.

**Returns:**
- the shared instance of

LayoutStyle

**See Also:**
- LookAndFeel.getLayoutStyle()

---

#### public abstract int getPreferredGap​(
JComponent
component1,

JComponent
component2,

LayoutStyle.ComponentPlacement
type,
int position,

Container
parent)

Returns the amount of space to use between two components.
The return value indicates the distance to place

component2

relative to

component1

.
For example, the following returns the amount of space to place
between

component2

and

component1

when

component2

is placed vertically above

component1

:

```java
int gap = getPreferredGap(component1, component2,
ComponentPlacement.RELATED,
SwingConstants.NORTH, parent);
```

The

type

parameter indicates the relation between
the two components. If the two components will be contained in
the same parent and are showing similar logically related
items, use

RELATED

. If the two components will be
contained in the same parent but show logically unrelated items
use

UNRELATED

. Some look and feels may not
distinguish between the

RELATED

and

UNRELATED

types.

The return value is not intended to take into account the
current size and position of

component2

or

component1

. The return value may take into
consideration various properties of the components. For
example, the space may vary based on font size, or the preferred
size of the component.

**Parameters:**
- component1

- the

JComponent

component2

is being placed relative to
- component2

- the

JComponent

being placed
- position

- the position

component2

is being placed
relative to

component1

; one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST
- type

- how the two components are being placed
- parent

- the parent of

component2

; this may differ
from the actual parent and it may be

null

**Returns:**
- the amount of space to place between the two components

**Throws:**
- NullPointerException

- if

component1

,

component2

or

type

is

null
- IllegalArgumentException

- if

position

is not
one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST

**See Also:**
- LookAndFeel.getLayoutStyle()

**Since:**
- 1.6

---

#### public abstract int getContainerGap​(
JComponent
component,
int position,

Container
parent)

Returns the amount of space to place between the component and specified
edge of its parent.

**Parameters:**
- component

- the

JComponent

being positioned
- position

- the position

component

is being placed
relative to its parent; one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST
- parent

- the parent of

component

; this may differ
from the actual parent and may be

null

**Returns:**
- the amount of space to place between the component and specified
edge

**Throws:**
- IllegalArgumentException

- if

position

is not
one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST

---

### Additional Sections

#### Class LayoutStyle

java.lang.Object

- javax.swing.LayoutStyle

javax.swing.LayoutStyle

```java
public abstract class
LayoutStyle

extends
Object
```

LayoutStyle

provides information about how to position
components. This class is primarily useful for visual tools and
layout managers. Most developers will not need to use this class.

You typically don't set or create a

LayoutStyle

. Instead use the static method

getInstance

to obtain the current instance.

**Since:** 1.6

public abstract class

LayoutStyle

extends

Object

LayoutStyle

provides information about how to position
components. This class is primarily useful for visual tools and
layout managers. Most developers will not need to use this class.

You typically don't set or create a

LayoutStyle

. Instead use the static method

getInstance

to obtain the current instance.

You typically don't set or create a

LayoutStyle

. Instead use the static method

getInstance

to obtain the current instance.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

LayoutStyle.ComponentPlacement

ComponentPlacement

is an enumeration of the
possible ways two components can be placed relative to each
other.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LayoutStyle

()

Creates a new

LayoutStyle

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract int

getContainerGap

​(

JComponent

component,
int position,

Container

parent)

Returns the amount of space to place between the component and specified
edge of its parent.

static

LayoutStyle

getInstance

()

Returns the shared instance of

LayoutStyle

.

abstract int

getPreferredGap

​(

JComponent

component1,

JComponent

component2,

LayoutStyle.ComponentPlacement

type,
int position,

Container

parent)

Returns the amount of space to use between two components.

static void

setInstance

​(

LayoutStyle

style)

Sets the shared instance of

LayoutStyle

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

toString

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

LayoutStyle.ComponentPlacement

ComponentPlacement

is an enumeration of the
possible ways two components can be placed relative to each
other.

---

#### Nested Class Summary

ComponentPlacement

is an enumeration of the
possible ways two components can be placed relative to each
other.

Constructor Summary

Constructors

Constructor

Description

LayoutStyle

()

Creates a new

LayoutStyle

.

---

#### Constructor Summary

Creates a new

LayoutStyle

.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract int

getContainerGap

​(

JComponent

component,
int position,

Container

parent)

Returns the amount of space to place between the component and specified
edge of its parent.

static

LayoutStyle

getInstance

()

Returns the shared instance of

LayoutStyle

.

abstract int

getPreferredGap

​(

JComponent

component1,

JComponent

component2,

LayoutStyle.ComponentPlacement

type,
int position,

Container

parent)

Returns the amount of space to use between two components.

static void

setInstance

​(

LayoutStyle

style)

Sets the shared instance of

LayoutStyle

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the amount of space to place between the component and specified
edge of its parent.

Returns the shared instance of

LayoutStyle

.

Returns the amount of space to use between two components.

Sets the shared instance of

LayoutStyle

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LayoutStyle

```java
public LayoutStyle()
```

Creates a new

LayoutStyle

. You generally don't
create a

LayoutStyle

. Instead use the method

getInstance

to obtain the current

LayoutStyle

.

============ METHOD DETAIL ==========

- Method Detail

- setInstance

```java
public static void setInstance​(
LayoutStyle
style)
```

Sets the shared instance of

LayoutStyle

. Specifying

null

results in using the

LayoutStyle

from
the current

LookAndFeel

.

**Parameters:** style

- the

LayoutStyle

, or

null
**See Also:** getInstance()

- getInstance

```java
public static
LayoutStyle
getInstance()
```

Returns the shared instance of

LayoutStyle

. If an instance
has not been specified in

setInstance

, this will return
the

LayoutStyle

from the current

LookAndFeel

.

**Returns:** the shared instance of

LayoutStyle
**See Also:** LookAndFeel.getLayoutStyle()

- getPreferredGap

```java
public abstract int getPreferredGap​(
JComponent
component1,

JComponent
component2,

LayoutStyle.ComponentPlacement
type,
int position,

Container
parent)
```

Returns the amount of space to use between two components.
The return value indicates the distance to place

component2

relative to

component1

.
For example, the following returns the amount of space to place
between

component2

and

component1

when

component2

is placed vertically above

component1

:

```java
int gap = getPreferredGap(component1, component2,
ComponentPlacement.RELATED,
SwingConstants.NORTH, parent);
```

The

type

parameter indicates the relation between
the two components. If the two components will be contained in
the same parent and are showing similar logically related
items, use

RELATED

. If the two components will be
contained in the same parent but show logically unrelated items
use

UNRELATED

. Some look and feels may not
distinguish between the

RELATED

and

UNRELATED

types.

The return value is not intended to take into account the
current size and position of

component2

or

component1

. The return value may take into
consideration various properties of the components. For
example, the space may vary based on font size, or the preferred
size of the component.

**Parameters:** component1

- the

JComponent

component2

is being placed relative to
**Parameters:** component2

- the

JComponent

being placed
**Parameters:** position

- the position

component2

is being placed
relative to

component1

; one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST
**Parameters:** type

- how the two components are being placed
**Parameters:** parent

- the parent of

component2

; this may differ
from the actual parent and it may be

null
**Returns:** the amount of space to place between the two components
**Throws:** NullPointerException

- if

component1

,

component2

or

type

is

null
**Throws:** IllegalArgumentException

- if

position

is not
one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST
**Since:** 1.6
**See Also:** LookAndFeel.getLayoutStyle()

- getContainerGap

```java
public abstract int getContainerGap​(
JComponent
component,
int position,

Container
parent)
```

Returns the amount of space to place between the component and specified
edge of its parent.

**Parameters:** component

- the

JComponent

being positioned
**Parameters:** position

- the position

component

is being placed
relative to its parent; one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST
**Parameters:** parent

- the parent of

component

; this may differ
from the actual parent and may be

null
**Returns:** the amount of space to place between the component and specified
edge
**Throws:** IllegalArgumentException

- if

position

is not
one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST

Constructor Detail

- LayoutStyle

```java
public LayoutStyle()
```

Creates a new

LayoutStyle

. You generally don't
create a

LayoutStyle

. Instead use the method

getInstance

to obtain the current

LayoutStyle

.

---

#### Constructor Detail

LayoutStyle

```java
public LayoutStyle()
```

Creates a new

LayoutStyle

. You generally don't
create a

LayoutStyle

. Instead use the method

getInstance

to obtain the current

LayoutStyle

.

---

#### LayoutStyle

public LayoutStyle()

Creates a new

LayoutStyle

. You generally don't
create a

LayoutStyle

. Instead use the method

getInstance

to obtain the current

LayoutStyle

.

Method Detail

- setInstance

```java
public static void setInstance​(
LayoutStyle
style)
```

Sets the shared instance of

LayoutStyle

. Specifying

null

results in using the

LayoutStyle

from
the current

LookAndFeel

.

**Parameters:** style

- the

LayoutStyle

, or

null
**See Also:** getInstance()

- getInstance

```java
public static
LayoutStyle
getInstance()
```

Returns the shared instance of

LayoutStyle

. If an instance
has not been specified in

setInstance

, this will return
the

LayoutStyle

from the current

LookAndFeel

.

**Returns:** the shared instance of

LayoutStyle
**See Also:** LookAndFeel.getLayoutStyle()

- getPreferredGap

```java
public abstract int getPreferredGap​(
JComponent
component1,

JComponent
component2,

LayoutStyle.ComponentPlacement
type,
int position,

Container
parent)
```

Returns the amount of space to use between two components.
The return value indicates the distance to place

component2

relative to

component1

.
For example, the following returns the amount of space to place
between

component2

and

component1

when

component2

is placed vertically above

component1

:

```java
int gap = getPreferredGap(component1, component2,
ComponentPlacement.RELATED,
SwingConstants.NORTH, parent);
```

The

type

parameter indicates the relation between
the two components. If the two components will be contained in
the same parent and are showing similar logically related
items, use

RELATED

. If the two components will be
contained in the same parent but show logically unrelated items
use

UNRELATED

. Some look and feels may not
distinguish between the

RELATED

and

UNRELATED

types.

The return value is not intended to take into account the
current size and position of

component2

or

component1

. The return value may take into
consideration various properties of the components. For
example, the space may vary based on font size, or the preferred
size of the component.

**Parameters:** component1

- the

JComponent

component2

is being placed relative to
**Parameters:** component2

- the

JComponent

being placed
**Parameters:** position

- the position

component2

is being placed
relative to

component1

; one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST
**Parameters:** type

- how the two components are being placed
**Parameters:** parent

- the parent of

component2

; this may differ
from the actual parent and it may be

null
**Returns:** the amount of space to place between the two components
**Throws:** NullPointerException

- if

component1

,

component2

or

type

is

null
**Throws:** IllegalArgumentException

- if

position

is not
one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST
**Since:** 1.6
**See Also:** LookAndFeel.getLayoutStyle()

- getContainerGap

```java
public abstract int getContainerGap​(
JComponent
component,
int position,

Container
parent)
```

Returns the amount of space to place between the component and specified
edge of its parent.

**Parameters:** component

- the

JComponent

being positioned
**Parameters:** position

- the position

component

is being placed
relative to its parent; one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST
**Parameters:** parent

- the parent of

component

; this may differ
from the actual parent and may be

null
**Returns:** the amount of space to place between the component and specified
edge
**Throws:** IllegalArgumentException

- if

position

is not
one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST

---

#### Method Detail

setInstance

```java
public static void setInstance​(
LayoutStyle
style)
```

Sets the shared instance of

LayoutStyle

. Specifying

null

results in using the

LayoutStyle

from
the current

LookAndFeel

.

**Parameters:** style

- the

LayoutStyle

, or

null
**See Also:** getInstance()

---

#### setInstance

public static void setInstance​(

LayoutStyle

style)

Sets the shared instance of

LayoutStyle

. Specifying

null

results in using the

LayoutStyle

from
the current

LookAndFeel

.

getInstance

```java
public static
LayoutStyle
getInstance()
```

Returns the shared instance of

LayoutStyle

. If an instance
has not been specified in

setInstance

, this will return
the

LayoutStyle

from the current

LookAndFeel

.

**Returns:** the shared instance of

LayoutStyle
**See Also:** LookAndFeel.getLayoutStyle()

---

#### getInstance

public static

LayoutStyle

getInstance()

Returns the shared instance of

LayoutStyle

. If an instance
has not been specified in

setInstance

, this will return
the

LayoutStyle

from the current

LookAndFeel

.

getPreferredGap

```java
public abstract int getPreferredGap​(
JComponent
component1,

JComponent
component2,

LayoutStyle.ComponentPlacement
type,
int position,

Container
parent)
```

Returns the amount of space to use between two components.
The return value indicates the distance to place

component2

relative to

component1

.
For example, the following returns the amount of space to place
between

component2

and

component1

when

component2

is placed vertically above

component1

:

```java
int gap = getPreferredGap(component1, component2,
ComponentPlacement.RELATED,
SwingConstants.NORTH, parent);
```

The

type

parameter indicates the relation between
the two components. If the two components will be contained in
the same parent and are showing similar logically related
items, use

RELATED

. If the two components will be
contained in the same parent but show logically unrelated items
use

UNRELATED

. Some look and feels may not
distinguish between the

RELATED

and

UNRELATED

types.

The return value is not intended to take into account the
current size and position of

component2

or

component1

. The return value may take into
consideration various properties of the components. For
example, the space may vary based on font size, or the preferred
size of the component.

**Parameters:** component1

- the

JComponent

component2

is being placed relative to
**Parameters:** component2

- the

JComponent

being placed
**Parameters:** position

- the position

component2

is being placed
relative to

component1

; one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST
**Parameters:** type

- how the two components are being placed
**Parameters:** parent

- the parent of

component2

; this may differ
from the actual parent and it may be

null
**Returns:** the amount of space to place between the two components
**Throws:** NullPointerException

- if

component1

,

component2

or

type

is

null
**Throws:** IllegalArgumentException

- if

position

is not
one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST
**Since:** 1.6
**See Also:** LookAndFeel.getLayoutStyle()

---

#### getPreferredGap

public abstract int getPreferredGap​(

JComponent

component1,

JComponent

component2,

LayoutStyle.ComponentPlacement

type,
int position,

Container

parent)

Returns the amount of space to use between two components.
The return value indicates the distance to place

component2

relative to

component1

.
For example, the following returns the amount of space to place
between

component2

and

component1

when

component2

is placed vertically above

component1

:

```java
int gap = getPreferredGap(component1, component2,
ComponentPlacement.RELATED,
SwingConstants.NORTH, parent);
```

The

type

parameter indicates the relation between
the two components. If the two components will be contained in
the same parent and are showing similar logically related
items, use

RELATED

. If the two components will be
contained in the same parent but show logically unrelated items
use

UNRELATED

. Some look and feels may not
distinguish between the

RELATED

and

UNRELATED

types.

The return value is not intended to take into account the
current size and position of

component2

or

component1

. The return value may take into
consideration various properties of the components. For
example, the space may vary based on font size, or the preferred
size of the component.

int gap = getPreferredGap(component1, component2,
ComponentPlacement.RELATED,
SwingConstants.NORTH, parent);

The return value is not intended to take into account the
current size and position of

component2

or

component1

. The return value may take into
consideration various properties of the components. For
example, the space may vary based on font size, or the preferred
size of the component.

getContainerGap

```java
public abstract int getContainerGap​(
JComponent
component,
int position,

Container
parent)
```

Returns the amount of space to place between the component and specified
edge of its parent.

**Parameters:** component

- the

JComponent

being positioned
**Parameters:** position

- the position

component

is being placed
relative to its parent; one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST
**Parameters:** parent

- the parent of

component

; this may differ
from the actual parent and may be

null
**Returns:** the amount of space to place between the component and specified
edge
**Throws:** IllegalArgumentException

- if

position

is not
one of

SwingConstants.NORTH

,

SwingConstants.SOUTH

,

SwingConstants.EAST

or

SwingConstants.WEST

---

#### getContainerGap

public abstract int getContainerGap​(

JComponent

component,
int position,

Container

parent)

Returns the amount of space to place between the component and specified
edge of its parent.

---

