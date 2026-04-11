# Class CaretEvent

**Source:** `java.desktop\javax\swing\event\CaretEvent.html`

### Class Description

```java
public abstract class
CaretEvent

extends
EventObject
```

CaretEvent is used to notify interested parties that
the text caret has changed in the event source.

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

#### public CaretEvent​(
Object
source)

Creates a new CaretEvent object.

**Parameters:**
- source

- the object responsible for the event

---

### Method Details

#### public abstract int getDot()

Fetches the location of the caret.

**Returns:**
- the dot >= 0

---

#### public abstract int getMark()

Fetches the location of other end of a logical
selection. If there is no selection, this
will be the same as dot.

**Returns:**
- the mark >= 0

---

### Additional Sections

#### Class CaretEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.CaretEvent

java.util.EventObject

- javax.swing.event.CaretEvent

javax.swing.event.CaretEvent

**All Implemented Interfaces:** Serializable

```java
public abstract class
CaretEvent

extends
EventObject
```

CaretEvent is used to notify interested parties that
the text caret has changed in the event source.

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

public abstract class

CaretEvent

extends

EventObject

CaretEvent is used to notify interested parties that
the text caret has changed in the event source.

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

CaretEvent

​(

Object

source)

Creates a new CaretEvent object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract int

getDot

()

Fetches the location of the caret.

abstract int

getMark

()

Fetches the location of other end of a logical
selection.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

CaretEvent

​(

Object

source)

Creates a new CaretEvent object.

---

#### Constructor Summary

Creates a new CaretEvent object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract int

getDot

()

Fetches the location of the caret.

abstract int

getMark

()

Fetches the location of other end of a logical
selection.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

Fetches the location of the caret.

Fetches the location of other end of a logical
selection.

Methods declared in class java.util.

EventObject

getSource

,

toString

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

- CaretEvent

```java
public CaretEvent​(
Object
source)
```

Creates a new CaretEvent object.

**Parameters:** source

- the object responsible for the event

============ METHOD DETAIL ==========

- Method Detail

- getDot

```java
public abstract int getDot()
```

Fetches the location of the caret.

**Returns:** the dot >= 0

- getMark

```java
public abstract int getMark()
```

Fetches the location of other end of a logical
selection. If there is no selection, this
will be the same as dot.

**Returns:** the mark >= 0

Constructor Detail

- CaretEvent

```java
public CaretEvent​(
Object
source)
```

Creates a new CaretEvent object.

**Parameters:** source

- the object responsible for the event

---

#### Constructor Detail

CaretEvent

```java
public CaretEvent​(
Object
source)
```

Creates a new CaretEvent object.

**Parameters:** source

- the object responsible for the event

---

#### CaretEvent

public CaretEvent​(

Object

source)

Creates a new CaretEvent object.

Method Detail

- getDot

```java
public abstract int getDot()
```

Fetches the location of the caret.

**Returns:** the dot >= 0

- getMark

```java
public abstract int getMark()
```

Fetches the location of other end of a logical
selection. If there is no selection, this
will be the same as dot.

**Returns:** the mark >= 0

---

#### Method Detail

getDot

```java
public abstract int getDot()
```

Fetches the location of the caret.

**Returns:** the dot >= 0

---

#### getDot

public abstract int getDot()

Fetches the location of the caret.

getMark

```java
public abstract int getMark()
```

Fetches the location of other end of a logical
selection. If there is no selection, this
will be the same as dot.

**Returns:** the mark >= 0

---

#### getMark

public abstract int getMark()

Fetches the location of other end of a logical
selection. If there is no selection, this
will be the same as dot.

---

