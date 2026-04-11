# Class SynthContext

**Source:** `java.desktop\javax\swing\plaf\synth\SynthContext.html`

### Class Description

```java
public class
SynthContext

extends
Object
```

An immutable transient object containing contextual information about
a

Region

. A

SynthContext

should only be
considered valid for the duration
of the method it is passed to. In other words you should not cache
a

SynthContext

that is passed to you and expect it to
remain valid.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthContext​(
JComponent
component,

Region
region,

SynthStyle
style,
int state)

Creates a SynthContext with the specified values. This is meant
for subclasses and custom UI implementors. You very rarely need to
construct a SynthContext, though some methods will take one.

**Parameters:**
- component

- JComponent
- region

- Identifies the portion of the JComponent
- style

- Style associated with the component
- state

- State of the component as defined in SynthConstants.

**Throws:**
- NullPointerException

- if component, region of style is null.

---

### Method Details

#### public
JComponent
getComponent()

Returns the hosting component containing the region.

**Returns:**
- Hosting Component

---

#### public
Region
getRegion()

Returns the Region identifying this state.

**Returns:**
- Region of the hosting component

---

#### public
SynthStyle
getStyle()

Returns the style associated with this Region.

**Returns:**
- SynthStyle associated with the region.

---

#### public int getComponentState()

Returns the state of the widget, which is a bitmask of the
values defined in

SynthConstants

. A region will at least
be in one of

ENABLED

,

MOUSE_OVER

,

PRESSED

or

DISABLED

.

**Returns:**
- State of Component

**See Also:**
- SynthConstants

---

### Additional Sections

#### Class SynthContext

java.lang.Object

- javax.swing.plaf.synth.SynthContext

javax.swing.plaf.synth.SynthContext

```java
public class
SynthContext

extends
Object
```

An immutable transient object containing contextual information about
a

Region

. A

SynthContext

should only be
considered valid for the duration
of the method it is passed to. In other words you should not cache
a

SynthContext

that is passed to you and expect it to
remain valid.

**Since:** 1.5

public class

SynthContext

extends

Object

An immutable transient object containing contextual information about
a

Region

. A

SynthContext

should only be
considered valid for the duration
of the method it is passed to. In other words you should not cache
a

SynthContext

that is passed to you and expect it to
remain valid.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SynthContext

​(

JComponent

component,

Region

region,

SynthStyle

style,
int state)

Creates a SynthContext with the specified values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JComponent

getComponent

()

Returns the hosting component containing the region.

int

getComponentState

()

Returns the state of the widget, which is a bitmask of the
values defined in

SynthConstants

.

Region

getRegion

()

Returns the Region identifying this state.

SynthStyle

getStyle

()

Returns the style associated with this Region.

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

Constructor Summary

Constructors

Constructor

Description

SynthContext

​(

JComponent

component,

Region

region,

SynthStyle

style,
int state)

Creates a SynthContext with the specified values.

---

#### Constructor Summary

Creates a SynthContext with the specified values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JComponent

getComponent

()

Returns the hosting component containing the region.

int

getComponentState

()

Returns the state of the widget, which is a bitmask of the
values defined in

SynthConstants

.

Region

getRegion

()

Returns the Region identifying this state.

SynthStyle

getStyle

()

Returns the style associated with this Region.

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

Returns the hosting component containing the region.

Returns the state of the widget, which is a bitmask of the
values defined in

SynthConstants

.

Returns the Region identifying this state.

Returns the style associated with this Region.

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

- SynthContext

```java
public SynthContext​(
JComponent
component,

Region
region,

SynthStyle
style,
int state)
```

Creates a SynthContext with the specified values. This is meant
for subclasses and custom UI implementors. You very rarely need to
construct a SynthContext, though some methods will take one.

**Parameters:** component

- JComponent
**Parameters:** region

- Identifies the portion of the JComponent
**Parameters:** style

- Style associated with the component
**Parameters:** state

- State of the component as defined in SynthConstants.
**Throws:** NullPointerException

- if component, region of style is null.

============ METHOD DETAIL ==========

- Method Detail

- getComponent

```java
public
JComponent
getComponent()
```

Returns the hosting component containing the region.

**Returns:** Hosting Component

- getRegion

```java
public
Region
getRegion()
```

Returns the Region identifying this state.

**Returns:** Region of the hosting component

- getStyle

```java
public
SynthStyle
getStyle()
```

Returns the style associated with this Region.

**Returns:** SynthStyle associated with the region.

- getComponentState

```java
public int getComponentState()
```

Returns the state of the widget, which is a bitmask of the
values defined in

SynthConstants

. A region will at least
be in one of

ENABLED

,

MOUSE_OVER

,

PRESSED

or

DISABLED

.

**Returns:** State of Component
**See Also:** SynthConstants

Constructor Detail

- SynthContext

```java
public SynthContext​(
JComponent
component,

Region
region,

SynthStyle
style,
int state)
```

Creates a SynthContext with the specified values. This is meant
for subclasses and custom UI implementors. You very rarely need to
construct a SynthContext, though some methods will take one.

**Parameters:** component

- JComponent
**Parameters:** region

- Identifies the portion of the JComponent
**Parameters:** style

- Style associated with the component
**Parameters:** state

- State of the component as defined in SynthConstants.
**Throws:** NullPointerException

- if component, region of style is null.

---

#### Constructor Detail

SynthContext

```java
public SynthContext​(
JComponent
component,

Region
region,

SynthStyle
style,
int state)
```

Creates a SynthContext with the specified values. This is meant
for subclasses and custom UI implementors. You very rarely need to
construct a SynthContext, though some methods will take one.

**Parameters:** component

- JComponent
**Parameters:** region

- Identifies the portion of the JComponent
**Parameters:** style

- Style associated with the component
**Parameters:** state

- State of the component as defined in SynthConstants.
**Throws:** NullPointerException

- if component, region of style is null.

---

#### SynthContext

public SynthContext​(

JComponent

component,

Region

region,

SynthStyle

style,
int state)

Creates a SynthContext with the specified values. This is meant
for subclasses and custom UI implementors. You very rarely need to
construct a SynthContext, though some methods will take one.

Method Detail

- getComponent

```java
public
JComponent
getComponent()
```

Returns the hosting component containing the region.

**Returns:** Hosting Component

- getRegion

```java
public
Region
getRegion()
```

Returns the Region identifying this state.

**Returns:** Region of the hosting component

- getStyle

```java
public
SynthStyle
getStyle()
```

Returns the style associated with this Region.

**Returns:** SynthStyle associated with the region.

- getComponentState

```java
public int getComponentState()
```

Returns the state of the widget, which is a bitmask of the
values defined in

SynthConstants

. A region will at least
be in one of

ENABLED

,

MOUSE_OVER

,

PRESSED

or

DISABLED

.

**Returns:** State of Component
**See Also:** SynthConstants

---

#### Method Detail

getComponent

```java
public
JComponent
getComponent()
```

Returns the hosting component containing the region.

**Returns:** Hosting Component

---

#### getComponent

public

JComponent

getComponent()

Returns the hosting component containing the region.

getRegion

```java
public
Region
getRegion()
```

Returns the Region identifying this state.

**Returns:** Region of the hosting component

---

#### getRegion

public

Region

getRegion()

Returns the Region identifying this state.

getStyle

```java
public
SynthStyle
getStyle()
```

Returns the style associated with this Region.

**Returns:** SynthStyle associated with the region.

---

#### getStyle

public

SynthStyle

getStyle()

Returns the style associated with this Region.

getComponentState

```java
public int getComponentState()
```

Returns the state of the widget, which is a bitmask of the
values defined in

SynthConstants

. A region will at least
be in one of

ENABLED

,

MOUSE_OVER

,

PRESSED

or

DISABLED

.

**Returns:** State of Component
**See Also:** SynthConstants

---

#### getComponentState

public int getComponentState()

Returns the state of the widget, which is a bitmask of the
values defined in

SynthConstants

. A region will at least
be in one of

ENABLED

,

MOUSE_OVER

,

PRESSED

or

DISABLED

.

---

