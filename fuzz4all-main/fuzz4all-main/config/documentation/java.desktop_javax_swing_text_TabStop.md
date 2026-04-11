# Class TabStop

**Source:** `java.desktop\javax\swing\text\TabStop.html`

### Class Description

```java
public class
TabStop

extends
Object

implements
Serializable
```

This class encapsulates a single tab stop (basically as tab stops
are thought of by RTF). A tab stop is at a specified distance from the
left margin, aligns text in a specified way, and has a specified leader.
TabStops are immutable, and usually contained in TabSets.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int ALIGN_LEFT

Character following tab is positioned at location.

**See Also:**
- Constant Field Values

---

#### public static final int ALIGN_RIGHT

Characters following tab are positioned such that all following
characters up to next tab/newline end at location.

**See Also:**
- Constant Field Values

---

#### public static final int ALIGN_CENTER

Characters following tab are positioned such that all following
characters up to next tab/newline are centered around the tabs
location.

**See Also:**
- Constant Field Values

---

#### public static final int ALIGN_DECIMAL

Characters following tab are aligned such that next
decimal/tab/newline is at the tab location, very similar to
RIGHT_TAB, just includes decimal as additional character to look for.

**See Also:**
- Constant Field Values

---

#### public static final int ALIGN_BAR

Align bar

**See Also:**
- Constant Field Values

---

#### public static final int LEAD_NONE

Lead none

**See Also:**
- Constant Field Values

---

#### public static final int LEAD_DOTS

Lead dots

**See Also:**
- Constant Field Values

---

#### public static final int LEAD_HYPHENS

Lead hyphens

**See Also:**
- Constant Field Values

---

#### public static final int LEAD_UNDERLINE

Lead underline

**See Also:**
- Constant Field Values

---

#### public static final int LEAD_THICKLINE

Lead thickline

**See Also:**
- Constant Field Values

---

#### public static final int LEAD_EQUALS

Lead equals

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public TabStop​(float pos)

Creates a tab at position

pos

with a default alignment
and default leader.

**Parameters:**
- pos

- position of the tab

---

#### public TabStop​(float pos,
int align,
int leader)

Creates a tab with the specified position

pos

,
alignment

align

and leader

leader

.

**Parameters:**
- pos

- position of the tab
- align

- alignment of the tab
- leader

- leader of the tab

---

### Method Details

#### public float getPosition()

Returns the position, as a float, of the tab.

**Returns:**
- the position of the tab

---

#### public int getAlignment()

Returns the alignment, as an integer, of the tab.

**Returns:**
- the alignment of the tab

---

#### public int getLeader()

Returns the leader of the tab.

**Returns:**
- the leader of the tab

---

#### public boolean equals​(
Object
other)

Returns true if the tabs are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- other

- the reference object with which to compare.

**Returns:**
- true if the tabs are equal, otherwise false

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hashCode for the object. This must be defined
here to ensure 100% pure.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hashCode for the object

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class TabStop

java.lang.Object

- javax.swing.text.TabStop

javax.swing.text.TabStop

**All Implemented Interfaces:** Serializable

```java
public class
TabStop

extends
Object

implements
Serializable
```

This class encapsulates a single tab stop (basically as tab stops
are thought of by RTF). A tab stop is at a specified distance from the
left margin, aligns text in a specified way, and has a specified leader.
TabStops are immutable, and usually contained in TabSets.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Serialized Form

public class

TabStop

extends

Object

implements

Serializable

This class encapsulates a single tab stop (basically as tab stops
are thought of by RTF). A tab stop is at a specified distance from the
left margin, aligns text in a specified way, and has a specified leader.
TabStops are immutable, and usually contained in TabSets.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ALIGN_BAR

Align bar

static int

ALIGN_CENTER

Characters following tab are positioned such that all following
characters up to next tab/newline are centered around the tabs
location.

static int

ALIGN_DECIMAL

Characters following tab are aligned such that next
decimal/tab/newline is at the tab location, very similar to
RIGHT_TAB, just includes decimal as additional character to look for.

static int

ALIGN_LEFT

Character following tab is positioned at location.

static int

ALIGN_RIGHT

Characters following tab are positioned such that all following
characters up to next tab/newline end at location.

static int

LEAD_DOTS

Lead dots

static int

LEAD_EQUALS

Lead equals

static int

LEAD_HYPHENS

Lead hyphens

static int

LEAD_NONE

Lead none

static int

LEAD_THICKLINE

Lead thickline

static int

LEAD_UNDERLINE

Lead underline

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TabStop

​(float pos)

Creates a tab at position

pos

with a default alignment
and default leader.

TabStop

​(float pos,
int align,
int leader)

Creates a tab with the specified position

pos

,
alignment

align

and leader

leader

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Returns true if the tabs are equal.

int

getAlignment

()

Returns the alignment, as an integer, of the tab.

int

getLeader

()

Returns the leader of the tab.

float

getPosition

()

Returns the position, as a float, of the tab.

int

hashCode

()

Returns the hashCode for the object.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

ALIGN_BAR

Align bar

static int

ALIGN_CENTER

Characters following tab are positioned such that all following
characters up to next tab/newline are centered around the tabs
location.

static int

ALIGN_DECIMAL

Characters following tab are aligned such that next
decimal/tab/newline is at the tab location, very similar to
RIGHT_TAB, just includes decimal as additional character to look for.

static int

ALIGN_LEFT

Character following tab is positioned at location.

static int

ALIGN_RIGHT

Characters following tab are positioned such that all following
characters up to next tab/newline end at location.

static int

LEAD_DOTS

Lead dots

static int

LEAD_EQUALS

Lead equals

static int

LEAD_HYPHENS

Lead hyphens

static int

LEAD_NONE

Lead none

static int

LEAD_THICKLINE

Lead thickline

static int

LEAD_UNDERLINE

Lead underline

---

#### Field Summary

Align bar

Characters following tab are positioned such that all following
characters up to next tab/newline are centered around the tabs
location.

Characters following tab are aligned such that next
decimal/tab/newline is at the tab location, very similar to
RIGHT_TAB, just includes decimal as additional character to look for.

Character following tab is positioned at location.

Characters following tab are positioned such that all following
characters up to next tab/newline end at location.

Lead dots

Lead equals

Lead hyphens

Lead none

Lead thickline

Lead underline

Constructor Summary

Constructors

Constructor

Description

TabStop

​(float pos)

Creates a tab at position

pos

with a default alignment
and default leader.

TabStop

​(float pos,
int align,
int leader)

Creates a tab with the specified position

pos

,
alignment

align

and leader

leader

.

---

#### Constructor Summary

Creates a tab at position

pos

with a default alignment
and default leader.

Creates a tab with the specified position

pos

,
alignment

align

and leader

leader

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Returns true if the tabs are equal.

int

getAlignment

()

Returns the alignment, as an integer, of the tab.

int

getLeader

()

Returns the leader of the tab.

float

getPosition

()

Returns the position, as a float, of the tab.

int

hashCode

()

Returns the hashCode for the object.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Returns true if the tabs are equal.

Returns the alignment, as an integer, of the tab.

Returns the leader of the tab.

Returns the position, as a float, of the tab.

Returns the hashCode for the object.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

============ FIELD DETAIL ===========

- Field Detail

- ALIGN_LEFT

```java
public static final int ALIGN_LEFT
```

Character following tab is positioned at location.

**See Also:** Constant Field Values

- ALIGN_RIGHT

```java
public static final int ALIGN_RIGHT
```

Characters following tab are positioned such that all following
characters up to next tab/newline end at location.

**See Also:** Constant Field Values

- ALIGN_CENTER

```java
public static final int ALIGN_CENTER
```

Characters following tab are positioned such that all following
characters up to next tab/newline are centered around the tabs
location.

**See Also:** Constant Field Values

- ALIGN_DECIMAL

```java
public static final int ALIGN_DECIMAL
```

Characters following tab are aligned such that next
decimal/tab/newline is at the tab location, very similar to
RIGHT_TAB, just includes decimal as additional character to look for.

**See Also:** Constant Field Values

- ALIGN_BAR

```java
public static final int ALIGN_BAR
```

Align bar

**See Also:** Constant Field Values

- LEAD_NONE

```java
public static final int LEAD_NONE
```

Lead none

**See Also:** Constant Field Values

- LEAD_DOTS

```java
public static final int LEAD_DOTS
```

Lead dots

**See Also:** Constant Field Values

- LEAD_HYPHENS

```java
public static final int LEAD_HYPHENS
```

Lead hyphens

**See Also:** Constant Field Values

- LEAD_UNDERLINE

```java
public static final int LEAD_UNDERLINE
```

Lead underline

**See Also:** Constant Field Values

- LEAD_THICKLINE

```java
public static final int LEAD_THICKLINE
```

Lead thickline

**See Also:** Constant Field Values

- LEAD_EQUALS

```java
public static final int LEAD_EQUALS
```

Lead equals

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TabStop

```java
public TabStop​(float pos)
```

Creates a tab at position

pos

with a default alignment
and default leader.

**Parameters:** pos

- position of the tab

- TabStop

```java
public TabStop​(float pos,
int align,
int leader)
```

Creates a tab with the specified position

pos

,
alignment

align

and leader

leader

.

**Parameters:** pos

- position of the tab
**Parameters:** align

- alignment of the tab
**Parameters:** leader

- leader of the tab

============ METHOD DETAIL ==========

- Method Detail

- getPosition

```java
public float getPosition()
```

Returns the position, as a float, of the tab.

**Returns:** the position of the tab

- getAlignment

```java
public int getAlignment()
```

Returns the alignment, as an integer, of the tab.

**Returns:** the alignment of the tab

- getLeader

```java
public int getLeader()
```

Returns the leader of the tab.

**Returns:** the leader of the tab

- equals

```java
public boolean equals​(
Object
other)
```

Returns true if the tabs are equal.

**Overrides:** equals

in class

Object
**Parameters:** other

- the reference object with which to compare.
**Returns:** true if the tabs are equal, otherwise false
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hashCode for the object. This must be defined
here to ensure 100% pure.

**Overrides:** hashCode

in class

Object
**Returns:** the hashCode for the object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Field Detail

- ALIGN_LEFT

```java
public static final int ALIGN_LEFT
```

Character following tab is positioned at location.

**See Also:** Constant Field Values

- ALIGN_RIGHT

```java
public static final int ALIGN_RIGHT
```

Characters following tab are positioned such that all following
characters up to next tab/newline end at location.

**See Also:** Constant Field Values

- ALIGN_CENTER

```java
public static final int ALIGN_CENTER
```

Characters following tab are positioned such that all following
characters up to next tab/newline are centered around the tabs
location.

**See Also:** Constant Field Values

- ALIGN_DECIMAL

```java
public static final int ALIGN_DECIMAL
```

Characters following tab are aligned such that next
decimal/tab/newline is at the tab location, very similar to
RIGHT_TAB, just includes decimal as additional character to look for.

**See Also:** Constant Field Values

- ALIGN_BAR

```java
public static final int ALIGN_BAR
```

Align bar

**See Also:** Constant Field Values

- LEAD_NONE

```java
public static final int LEAD_NONE
```

Lead none

**See Also:** Constant Field Values

- LEAD_DOTS

```java
public static final int LEAD_DOTS
```

Lead dots

**See Also:** Constant Field Values

- LEAD_HYPHENS

```java
public static final int LEAD_HYPHENS
```

Lead hyphens

**See Also:** Constant Field Values

- LEAD_UNDERLINE

```java
public static final int LEAD_UNDERLINE
```

Lead underline

**See Also:** Constant Field Values

- LEAD_THICKLINE

```java
public static final int LEAD_THICKLINE
```

Lead thickline

**See Also:** Constant Field Values

- LEAD_EQUALS

```java
public static final int LEAD_EQUALS
```

Lead equals

**See Also:** Constant Field Values

---

#### Field Detail

ALIGN_LEFT

```java
public static final int ALIGN_LEFT
```

Character following tab is positioned at location.

**See Also:** Constant Field Values

---

#### ALIGN_LEFT

public static final int ALIGN_LEFT

Character following tab is positioned at location.

ALIGN_RIGHT

```java
public static final int ALIGN_RIGHT
```

Characters following tab are positioned such that all following
characters up to next tab/newline end at location.

**See Also:** Constant Field Values

---

#### ALIGN_RIGHT

public static final int ALIGN_RIGHT

Characters following tab are positioned such that all following
characters up to next tab/newline end at location.

ALIGN_CENTER

```java
public static final int ALIGN_CENTER
```

Characters following tab are positioned such that all following
characters up to next tab/newline are centered around the tabs
location.

**See Also:** Constant Field Values

---

#### ALIGN_CENTER

public static final int ALIGN_CENTER

Characters following tab are positioned such that all following
characters up to next tab/newline are centered around the tabs
location.

ALIGN_DECIMAL

```java
public static final int ALIGN_DECIMAL
```

Characters following tab are aligned such that next
decimal/tab/newline is at the tab location, very similar to
RIGHT_TAB, just includes decimal as additional character to look for.

**See Also:** Constant Field Values

---

#### ALIGN_DECIMAL

public static final int ALIGN_DECIMAL

Characters following tab are aligned such that next
decimal/tab/newline is at the tab location, very similar to
RIGHT_TAB, just includes decimal as additional character to look for.

ALIGN_BAR

```java
public static final int ALIGN_BAR
```

Align bar

**See Also:** Constant Field Values

---

#### ALIGN_BAR

public static final int ALIGN_BAR

Align bar

LEAD_NONE

```java
public static final int LEAD_NONE
```

Lead none

**See Also:** Constant Field Values

---

#### LEAD_NONE

public static final int LEAD_NONE

Lead none

LEAD_DOTS

```java
public static final int LEAD_DOTS
```

Lead dots

**See Also:** Constant Field Values

---

#### LEAD_DOTS

public static final int LEAD_DOTS

Lead dots

LEAD_HYPHENS

```java
public static final int LEAD_HYPHENS
```

Lead hyphens

**See Also:** Constant Field Values

---

#### LEAD_HYPHENS

public static final int LEAD_HYPHENS

Lead hyphens

LEAD_UNDERLINE

```java
public static final int LEAD_UNDERLINE
```

Lead underline

**See Also:** Constant Field Values

---

#### LEAD_UNDERLINE

public static final int LEAD_UNDERLINE

Lead underline

LEAD_THICKLINE

```java
public static final int LEAD_THICKLINE
```

Lead thickline

**See Also:** Constant Field Values

---

#### LEAD_THICKLINE

public static final int LEAD_THICKLINE

Lead thickline

LEAD_EQUALS

```java
public static final int LEAD_EQUALS
```

Lead equals

**See Also:** Constant Field Values

---

#### LEAD_EQUALS

public static final int LEAD_EQUALS

Lead equals

Constructor Detail

- TabStop

```java
public TabStop​(float pos)
```

Creates a tab at position

pos

with a default alignment
and default leader.

**Parameters:** pos

- position of the tab

- TabStop

```java
public TabStop​(float pos,
int align,
int leader)
```

Creates a tab with the specified position

pos

,
alignment

align

and leader

leader

.

**Parameters:** pos

- position of the tab
**Parameters:** align

- alignment of the tab
**Parameters:** leader

- leader of the tab

---

#### Constructor Detail

TabStop

```java
public TabStop​(float pos)
```

Creates a tab at position

pos

with a default alignment
and default leader.

**Parameters:** pos

- position of the tab

---

#### TabStop

public TabStop​(float pos)

Creates a tab at position

pos

with a default alignment
and default leader.

TabStop

```java
public TabStop​(float pos,
int align,
int leader)
```

Creates a tab with the specified position

pos

,
alignment

align

and leader

leader

.

**Parameters:** pos

- position of the tab
**Parameters:** align

- alignment of the tab
**Parameters:** leader

- leader of the tab

---

#### TabStop

public TabStop​(float pos,
int align,
int leader)

Creates a tab with the specified position

pos

,
alignment

align

and leader

leader

.

Method Detail

- getPosition

```java
public float getPosition()
```

Returns the position, as a float, of the tab.

**Returns:** the position of the tab

- getAlignment

```java
public int getAlignment()
```

Returns the alignment, as an integer, of the tab.

**Returns:** the alignment of the tab

- getLeader

```java
public int getLeader()
```

Returns the leader of the tab.

**Returns:** the leader of the tab

- equals

```java
public boolean equals​(
Object
other)
```

Returns true if the tabs are equal.

**Overrides:** equals

in class

Object
**Parameters:** other

- the reference object with which to compare.
**Returns:** true if the tabs are equal, otherwise false
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hashCode for the object. This must be defined
here to ensure 100% pure.

**Overrides:** hashCode

in class

Object
**Returns:** the hashCode for the object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getPosition

```java
public float getPosition()
```

Returns the position, as a float, of the tab.

**Returns:** the position of the tab

---

#### getPosition

public float getPosition()

Returns the position, as a float, of the tab.

getAlignment

```java
public int getAlignment()
```

Returns the alignment, as an integer, of the tab.

**Returns:** the alignment of the tab

---

#### getAlignment

public int getAlignment()

Returns the alignment, as an integer, of the tab.

getLeader

```java
public int getLeader()
```

Returns the leader of the tab.

**Returns:** the leader of the tab

---

#### getLeader

public int getLeader()

Returns the leader of the tab.

equals

```java
public boolean equals​(
Object
other)
```

Returns true if the tabs are equal.

**Overrides:** equals

in class

Object
**Parameters:** other

- the reference object with which to compare.
**Returns:** true if the tabs are equal, otherwise false
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Returns true if the tabs are equal.

hashCode

```java
public int hashCode()
```

Returns the hashCode for the object. This must be defined
here to ensure 100% pure.

**Overrides:** hashCode

in class

Object
**Returns:** the hashCode for the object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hashCode for the object. This must be defined
here to ensure 100% pure.

---

