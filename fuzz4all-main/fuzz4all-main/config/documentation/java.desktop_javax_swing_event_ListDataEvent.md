# Class ListDataEvent

**Source:** `java.desktop\javax\swing\event\ListDataEvent.html`

### Class Description

```java
public class
ListDataEvent

extends
EventObject
```

Defines an event that encapsulates changes to a list.

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

#### public static final int CONTENTS_CHANGED

Identifies one or more changes in the lists contents.

**See Also:**
- Constant Field Values

---

#### public static final int INTERVAL_ADDED

Identifies the addition of one or more contiguous items to the list

**See Also:**
- Constant Field Values

---

#### public static final int INTERVAL_REMOVED

Identifies the removal of one or more contiguous items from the list

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ListDataEvent​(
Object
source,
int type,
int index0,
int index1)

Constructs a ListDataEvent object. If index0 is >
index1, index0 and index1 will be swapped such that
index0 will always be <= index1.

**Parameters:**
- source

- the source Object (typically

this

)
- type

- an int specifying

CONTENTS_CHANGED

,

INTERVAL_ADDED

, or

INTERVAL_REMOVED
- index0

- one end of the new interval
- index1

- the other end of the new interval

---

### Method Details

#### public int getType()

Returns the event type. The possible values are:

- CONTENTS_CHANGED

INTERVAL_ADDED

INTERVAL_REMOVED

**Returns:**
- an int representing the type value

---

#### public int getIndex0()

Returns the lower index of the range. For a single
element, this value is the same as that returned by

getIndex1()

.

**Returns:**
- an int representing the lower index value

---

#### public int getIndex1()

Returns the upper index of the range. For a single
element, this value is the same as that returned by

getIndex0()

.

**Returns:**
- an int representing the upper index value

---

#### public
String
toString()

Returns a string representation of this ListDataEvent. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- toString

in class

EventObject

**Returns:**
- a string representation of this ListDataEvent.

**Since:**
- 1.4

---

### Additional Sections

#### Class ListDataEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.ListDataEvent

java.util.EventObject

- javax.swing.event.ListDataEvent

javax.swing.event.ListDataEvent

**All Implemented Interfaces:** Serializable

```java
public class
ListDataEvent

extends
EventObject
```

Defines an event that encapsulates changes to a list.

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

ListDataEvent

extends

EventObject

Defines an event that encapsulates changes to a list.

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

CONTENTS_CHANGED

Identifies one or more changes in the lists contents.

static int

INTERVAL_ADDED

Identifies the addition of one or more contiguous items to the list

static int

INTERVAL_REMOVED

Identifies the removal of one or more contiguous items from the list

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ListDataEvent

​(

Object

source,
int type,
int index0,
int index1)

Constructs a ListDataEvent object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getIndex0

()

Returns the lower index of the range.

int

getIndex1

()

Returns the upper index of the range.

int

getType

()

Returns the event type.

String

toString

()

Returns a string representation of this ListDataEvent.

- Methods declared in class java.util.

EventObject

getSource

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

static int

CONTENTS_CHANGED

Identifies one or more changes in the lists contents.

static int

INTERVAL_ADDED

Identifies the addition of one or more contiguous items to the list

static int

INTERVAL_REMOVED

Identifies the removal of one or more contiguous items from the list

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Identifies one or more changes in the lists contents.

Identifies the addition of one or more contiguous items to the list

Identifies the removal of one or more contiguous items from the list

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

ListDataEvent

​(

Object

source,
int type,
int index0,
int index1)

Constructs a ListDataEvent object.

---

#### Constructor Summary

Constructs a ListDataEvent object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getIndex0

()

Returns the lower index of the range.

int

getIndex1

()

Returns the upper index of the range.

int

getType

()

Returns the event type.

String

toString

()

Returns a string representation of this ListDataEvent.

- Methods declared in class java.util.

EventObject

getSource

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

Returns the lower index of the range.

Returns the upper index of the range.

Returns the event type.

Returns a string representation of this ListDataEvent.

Methods declared in class java.util.

EventObject

getSource

---

#### Methods declared in class java.util. EventObject

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

- CONTENTS_CHANGED

```java
public static final int CONTENTS_CHANGED
```

Identifies one or more changes in the lists contents.

**See Also:** Constant Field Values

- INTERVAL_ADDED

```java
public static final int INTERVAL_ADDED
```

Identifies the addition of one or more contiguous items to the list

**See Also:** Constant Field Values

- INTERVAL_REMOVED

```java
public static final int INTERVAL_REMOVED
```

Identifies the removal of one or more contiguous items from the list

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ListDataEvent

```java
public ListDataEvent​(
Object
source,
int type,
int index0,
int index1)
```

Constructs a ListDataEvent object. If index0 is >
index1, index0 and index1 will be swapped such that
index0 will always be <= index1.

**Parameters:** source

- the source Object (typically

this

)
**Parameters:** type

- an int specifying

CONTENTS_CHANGED

,

INTERVAL_ADDED

, or

INTERVAL_REMOVED
**Parameters:** index0

- one end of the new interval
**Parameters:** index1

- the other end of the new interval

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public int getType()
```

Returns the event type. The possible values are:

- CONTENTS_CHANGED

INTERVAL_ADDED

INTERVAL_REMOVED

**Returns:** an int representing the type value

- getIndex0

```java
public int getIndex0()
```

Returns the lower index of the range. For a single
element, this value is the same as that returned by

getIndex1()

.

**Returns:** an int representing the lower index value

- getIndex1

```java
public int getIndex1()
```

Returns the upper index of the range. For a single
element, this value is the same as that returned by

getIndex0()

.

**Returns:** an int representing the upper index value

- toString

```java
public
String
toString()
```

Returns a string representation of this ListDataEvent. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** toString

in class

EventObject
**Returns:** a string representation of this ListDataEvent.
**Since:** 1.4

Field Detail

- CONTENTS_CHANGED

```java
public static final int CONTENTS_CHANGED
```

Identifies one or more changes in the lists contents.

**See Also:** Constant Field Values

- INTERVAL_ADDED

```java
public static final int INTERVAL_ADDED
```

Identifies the addition of one or more contiguous items to the list

**See Also:** Constant Field Values

- INTERVAL_REMOVED

```java
public static final int INTERVAL_REMOVED
```

Identifies the removal of one or more contiguous items from the list

**See Also:** Constant Field Values

---

#### Field Detail

CONTENTS_CHANGED

```java
public static final int CONTENTS_CHANGED
```

Identifies one or more changes in the lists contents.

**See Also:** Constant Field Values

---

#### CONTENTS_CHANGED

public static final int CONTENTS_CHANGED

Identifies one or more changes in the lists contents.

INTERVAL_ADDED

```java
public static final int INTERVAL_ADDED
```

Identifies the addition of one or more contiguous items to the list

**See Also:** Constant Field Values

---

#### INTERVAL_ADDED

public static final int INTERVAL_ADDED

Identifies the addition of one or more contiguous items to the list

INTERVAL_REMOVED

```java
public static final int INTERVAL_REMOVED
```

Identifies the removal of one or more contiguous items from the list

**See Also:** Constant Field Values

---

#### INTERVAL_REMOVED

public static final int INTERVAL_REMOVED

Identifies the removal of one or more contiguous items from the list

Constructor Detail

- ListDataEvent

```java
public ListDataEvent​(
Object
source,
int type,
int index0,
int index1)
```

Constructs a ListDataEvent object. If index0 is >
index1, index0 and index1 will be swapped such that
index0 will always be <= index1.

**Parameters:** source

- the source Object (typically

this

)
**Parameters:** type

- an int specifying

CONTENTS_CHANGED

,

INTERVAL_ADDED

, or

INTERVAL_REMOVED
**Parameters:** index0

- one end of the new interval
**Parameters:** index1

- the other end of the new interval

---

#### Constructor Detail

ListDataEvent

```java
public ListDataEvent​(
Object
source,
int type,
int index0,
int index1)
```

Constructs a ListDataEvent object. If index0 is >
index1, index0 and index1 will be swapped such that
index0 will always be <= index1.

**Parameters:** source

- the source Object (typically

this

)
**Parameters:** type

- an int specifying

CONTENTS_CHANGED

,

INTERVAL_ADDED

, or

INTERVAL_REMOVED
**Parameters:** index0

- one end of the new interval
**Parameters:** index1

- the other end of the new interval

---

#### ListDataEvent

public ListDataEvent​(

Object

source,
int type,
int index0,
int index1)

Constructs a ListDataEvent object. If index0 is >
index1, index0 and index1 will be swapped such that
index0 will always be <= index1.

Method Detail

- getType

```java
public int getType()
```

Returns the event type. The possible values are:

- CONTENTS_CHANGED

INTERVAL_ADDED

INTERVAL_REMOVED

**Returns:** an int representing the type value

- getIndex0

```java
public int getIndex0()
```

Returns the lower index of the range. For a single
element, this value is the same as that returned by

getIndex1()

.

**Returns:** an int representing the lower index value

- getIndex1

```java
public int getIndex1()
```

Returns the upper index of the range. For a single
element, this value is the same as that returned by

getIndex0()

.

**Returns:** an int representing the upper index value

- toString

```java
public
String
toString()
```

Returns a string representation of this ListDataEvent. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** toString

in class

EventObject
**Returns:** a string representation of this ListDataEvent.
**Since:** 1.4

---

#### Method Detail

getType

```java
public int getType()
```

Returns the event type. The possible values are:

- CONTENTS_CHANGED

INTERVAL_ADDED

INTERVAL_REMOVED

**Returns:** an int representing the type value

---

#### getType

public int getType()

Returns the event type. The possible values are:

- CONTENTS_CHANGED

INTERVAL_ADDED

INTERVAL_REMOVED

CONTENTS_CHANGED

INTERVAL_ADDED

INTERVAL_REMOVED

getIndex0

```java
public int getIndex0()
```

Returns the lower index of the range. For a single
element, this value is the same as that returned by

getIndex1()

.

**Returns:** an int representing the lower index value

---

#### getIndex0

public int getIndex0()

Returns the lower index of the range. For a single
element, this value is the same as that returned by

getIndex1()

.

getIndex1

```java
public int getIndex1()
```

Returns the upper index of the range. For a single
element, this value is the same as that returned by

getIndex0()

.

**Returns:** an int representing the upper index value

---

#### getIndex1

public int getIndex1()

Returns the upper index of the range. For a single
element, this value is the same as that returned by

getIndex0()

.

toString

```java
public
String
toString()
```

Returns a string representation of this ListDataEvent. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** toString

in class

EventObject
**Returns:** a string representation of this ListDataEvent.
**Since:** 1.4

---

#### toString

public

String

toString()

Returns a string representation of this ListDataEvent. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

---

