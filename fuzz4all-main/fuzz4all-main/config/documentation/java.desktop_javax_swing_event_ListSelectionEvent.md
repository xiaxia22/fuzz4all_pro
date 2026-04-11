# Class ListSelectionEvent

**Source:** `java.desktop\javax\swing\event\ListSelectionEvent.html`

### Class Description

```java
public class
ListSelectionEvent

extends
EventObject
```

An event that characterizes a change in selection. The change is limited to a
a single inclusive interval. The selection of at least one index within the
range will have changed. A decent

ListSelectionModel

implementation
will keep the range as small as possible.

ListSelectionListeners

will
generally query the source of the event for the new selected status of each
potentially changed row.

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

*No entries found.*

### Constructor Details

#### public ListSelectionEvent​(
Object
source,
int firstIndex,
int lastIndex,
boolean isAdjusting)

Represents a change in selection status between

firstIndex

and

lastIndex

, inclusive.

firstIndex

is less than or equal to

lastIndex

. The selection of at least one index within the range will
have changed.

**Parameters:**
- source

- the

Object

on which the event initially occurred
- firstIndex

- the first index in the range, <= lastIndex
- lastIndex

- the last index in the range, >= firstIndex
- isAdjusting

- whether or not this is one in a series of
multiple events, where changes are still being made

---

### Method Details

#### public int getFirstIndex()

Returns the index of the first row whose selection may have changed.

getFirstIndex() <= getLastIndex()

**Returns:**
- the first row whose selection value may have changed,
where zero is the first row

---

#### public int getLastIndex()

Returns the index of the last row whose selection may have changed.

getLastIndex() >= getFirstIndex()

**Returns:**
- the last row whose selection value may have changed,
where zero is the first row

---

#### public boolean getValueIsAdjusting()

Returns whether or not this is one in a series of multiple events,
where changes are still being made. See the documentation for

ListSelectionModel.setValueIsAdjusting(boolean)

for
more details on how this is used.

**Returns:**
- true

if this is one in a series of multiple events,
where changes are still being made

---

#### public
String
toString()

Returns a

String

that displays and identifies this
object's properties.

**Overrides:**
- toString

in class

EventObject

**Returns:**
- a String representation of this object

---

### Additional Sections

#### Class ListSelectionEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.ListSelectionEvent

java.util.EventObject

- javax.swing.event.ListSelectionEvent

javax.swing.event.ListSelectionEvent

**All Implemented Interfaces:** Serializable

```java
public class
ListSelectionEvent

extends
EventObject
```

An event that characterizes a change in selection. The change is limited to a
a single inclusive interval. The selection of at least one index within the
range will have changed. A decent

ListSelectionModel

implementation
will keep the range as small as possible.

ListSelectionListeners

will
generally query the source of the event for the new selected status of each
potentially changed row.

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

**See Also:** ListSelectionModel

,

Serialized Form

public class

ListSelectionEvent

extends

EventObject

An event that characterizes a change in selection. The change is limited to a
a single inclusive interval. The selection of at least one index within the
range will have changed. A decent

ListSelectionModel

implementation
will keep the range as small as possible.

ListSelectionListeners

will
generally query the source of the event for the new selected status of each
potentially changed row.

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

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ListSelectionEvent

​(

Object

source,
int firstIndex,
int lastIndex,
boolean isAdjusting)

Represents a change in selection status between

firstIndex

and

lastIndex

, inclusive.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getFirstIndex

()

Returns the index of the first row whose selection may have changed.

int

getLastIndex

()

Returns the index of the last row whose selection may have changed.

boolean

getValueIsAdjusting

()

Returns whether or not this is one in a series of multiple events,
where changes are still being made.

String

toString

()

Returns a

String

that displays and identifies this
object's properties.

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

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

ListSelectionEvent

​(

Object

source,
int firstIndex,
int lastIndex,
boolean isAdjusting)

Represents a change in selection status between

firstIndex

and

lastIndex

, inclusive.

---

#### Constructor Summary

Represents a change in selection status between

firstIndex

and

lastIndex

, inclusive.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getFirstIndex

()

Returns the index of the first row whose selection may have changed.

int

getLastIndex

()

Returns the index of the last row whose selection may have changed.

boolean

getValueIsAdjusting

()

Returns whether or not this is one in a series of multiple events,
where changes are still being made.

String

toString

()

Returns a

String

that displays and identifies this
object's properties.

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

Returns the index of the first row whose selection may have changed.

Returns the index of the last row whose selection may have changed.

Returns whether or not this is one in a series of multiple events,
where changes are still being made.

Returns a

String

that displays and identifies this
object's properties.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ListSelectionEvent

```java
public ListSelectionEvent​(
Object
source,
int firstIndex,
int lastIndex,
boolean isAdjusting)
```

Represents a change in selection status between

firstIndex

and

lastIndex

, inclusive.

firstIndex

is less than or equal to

lastIndex

. The selection of at least one index within the range will
have changed.

**Parameters:** source

- the

Object

on which the event initially occurred
**Parameters:** firstIndex

- the first index in the range, <= lastIndex
**Parameters:** lastIndex

- the last index in the range, >= firstIndex
**Parameters:** isAdjusting

- whether or not this is one in a series of
multiple events, where changes are still being made

============ METHOD DETAIL ==========

- Method Detail

- getFirstIndex

```java
public int getFirstIndex()
```

Returns the index of the first row whose selection may have changed.

getFirstIndex() <= getLastIndex()

**Returns:** the first row whose selection value may have changed,
where zero is the first row

- getLastIndex

```java
public int getLastIndex()
```

Returns the index of the last row whose selection may have changed.

getLastIndex() >= getFirstIndex()

**Returns:** the last row whose selection value may have changed,
where zero is the first row

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns whether or not this is one in a series of multiple events,
where changes are still being made. See the documentation for

ListSelectionModel.setValueIsAdjusting(boolean)

for
more details on how this is used.

**Returns:** true

if this is one in a series of multiple events,
where changes are still being made

- toString

```java
public
String
toString()
```

Returns a

String

that displays and identifies this
object's properties.

**Overrides:** toString

in class

EventObject
**Returns:** a String representation of this object

Constructor Detail

- ListSelectionEvent

```java
public ListSelectionEvent​(
Object
source,
int firstIndex,
int lastIndex,
boolean isAdjusting)
```

Represents a change in selection status between

firstIndex

and

lastIndex

, inclusive.

firstIndex

is less than or equal to

lastIndex

. The selection of at least one index within the range will
have changed.

**Parameters:** source

- the

Object

on which the event initially occurred
**Parameters:** firstIndex

- the first index in the range, <= lastIndex
**Parameters:** lastIndex

- the last index in the range, >= firstIndex
**Parameters:** isAdjusting

- whether or not this is one in a series of
multiple events, where changes are still being made

---

#### Constructor Detail

ListSelectionEvent

```java
public ListSelectionEvent​(
Object
source,
int firstIndex,
int lastIndex,
boolean isAdjusting)
```

Represents a change in selection status between

firstIndex

and

lastIndex

, inclusive.

firstIndex

is less than or equal to

lastIndex

. The selection of at least one index within the range will
have changed.

**Parameters:** source

- the

Object

on which the event initially occurred
**Parameters:** firstIndex

- the first index in the range, <= lastIndex
**Parameters:** lastIndex

- the last index in the range, >= firstIndex
**Parameters:** isAdjusting

- whether or not this is one in a series of
multiple events, where changes are still being made

---

#### ListSelectionEvent

public ListSelectionEvent​(

Object

source,
int firstIndex,
int lastIndex,
boolean isAdjusting)

Represents a change in selection status between

firstIndex

and

lastIndex

, inclusive.

firstIndex

is less than or equal to

lastIndex

. The selection of at least one index within the range will
have changed.

Method Detail

- getFirstIndex

```java
public int getFirstIndex()
```

Returns the index of the first row whose selection may have changed.

getFirstIndex() <= getLastIndex()

**Returns:** the first row whose selection value may have changed,
where zero is the first row

- getLastIndex

```java
public int getLastIndex()
```

Returns the index of the last row whose selection may have changed.

getLastIndex() >= getFirstIndex()

**Returns:** the last row whose selection value may have changed,
where zero is the first row

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns whether or not this is one in a series of multiple events,
where changes are still being made. See the documentation for

ListSelectionModel.setValueIsAdjusting(boolean)

for
more details on how this is used.

**Returns:** true

if this is one in a series of multiple events,
where changes are still being made

- toString

```java
public
String
toString()
```

Returns a

String

that displays and identifies this
object's properties.

**Overrides:** toString

in class

EventObject
**Returns:** a String representation of this object

---

#### Method Detail

getFirstIndex

```java
public int getFirstIndex()
```

Returns the index of the first row whose selection may have changed.

getFirstIndex() <= getLastIndex()

**Returns:** the first row whose selection value may have changed,
where zero is the first row

---

#### getFirstIndex

public int getFirstIndex()

Returns the index of the first row whose selection may have changed.

getFirstIndex() <= getLastIndex()

getLastIndex

```java
public int getLastIndex()
```

Returns the index of the last row whose selection may have changed.

getLastIndex() >= getFirstIndex()

**Returns:** the last row whose selection value may have changed,
where zero is the first row

---

#### getLastIndex

public int getLastIndex()

Returns the index of the last row whose selection may have changed.

getLastIndex() >= getFirstIndex()

getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns whether or not this is one in a series of multiple events,
where changes are still being made. See the documentation for

ListSelectionModel.setValueIsAdjusting(boolean)

for
more details on how this is used.

**Returns:** true

if this is one in a series of multiple events,
where changes are still being made

---

#### getValueIsAdjusting

public boolean getValueIsAdjusting()

Returns whether or not this is one in a series of multiple events,
where changes are still being made. See the documentation for

ListSelectionModel.setValueIsAdjusting(boolean)

for
more details on how this is used.

toString

```java
public
String
toString()
```

Returns a

String

that displays and identifies this
object's properties.

**Overrides:** toString

in class

EventObject
**Returns:** a String representation of this object

---

#### toString

public

String

toString()

Returns a

String

that displays and identifies this
object's properties.

---

