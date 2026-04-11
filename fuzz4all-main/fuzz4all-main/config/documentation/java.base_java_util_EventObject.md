# Class EventObject

**Source:** `java.base\java\util\EventObject.html`

### Class Description

```java
public class
EventObject

extends
Object

implements
Serializable
```

The root class from which all event state objects shall be derived.

All Events are constructed with a reference to the object, the "source",
that is logically deemed to be the object upon which the Event in question
initially occurred upon.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected transient
Object
source

The object on which the Event initially occurred.

---

### Constructor Details

#### public EventObject​(
Object
source)

Constructs a prototypical Event.

**Parameters:**
- source

- the object on which the Event initially occurred

**Throws:**
- IllegalArgumentException

- if source is null

---

### Method Details

#### public
Object
getSource()

The object on which the Event initially occurred.

**Returns:**
- the object on which the Event initially occurred

---

#### public
String
toString()

Returns a String representation of this EventObject.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this EventObject

---

### Additional Sections

#### Class EventObject

java.lang.Object

- java.util.EventObject

java.util.EventObject

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AppEvent

,

AWTEvent

,

BeanContextEvent

,

CaretEvent

,

ChangeEvent

,

ConnectionEvent

,

DragGestureEvent

,

DragSourceEvent

,

DropTargetEvent

,

FlavorEvent

,

HandshakeCompletedEvent

,

HyperlinkEvent

,

LineEvent

,

ListDataEvent

,

ListSelectionEvent

,

MenuEvent

,

NamingEvent

,

NamingExceptionEvent

,

NodeChangeEvent

,

Notification

,

PopupMenuEvent

,

PreferenceChangeEvent

,

PrintEvent

,

PropertyChangeEvent

,

RowSetEvent

,

RowSorterEvent

,

SSLSessionBindingEvent

,

StatementEvent

,

TableColumnModelEvent

,

TableModelEvent

,

TreeExpansionEvent

,

TreeModelEvent

,

TreeSelectionEvent

,

UndoableEditEvent

,

UnsolicitedNotificationEvent

```java
public class
EventObject

extends
Object

implements
Serializable
```

The root class from which all event state objects shall be derived.

All Events are constructed with a reference to the object, the "source",
that is logically deemed to be the object upon which the Event in question
initially occurred upon.

**Since:** 1.1
**See Also:** Serialized Form

public class

EventObject

extends

Object

implements

Serializable

The root class from which all event state objects shall be derived.

All Events are constructed with a reference to the object, the "source",
that is logically deemed to be the object upon which the Event in question
initially occurred upon.

All Events are constructed with a reference to the object, the "source",
that is logically deemed to be the object upon which the Event in question
initially occurred upon.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Object

source

The object on which the Event initially occurred.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EventObject

​(

Object

source)

Constructs a prototypical Event.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getSource

()

The object on which the Event initially occurred.

String

toString

()

Returns a String representation of this EventObject.

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

protected

Object

source

The object on which the Event initially occurred.

---

#### Field Summary

The object on which the Event initially occurred.

Constructor Summary

Constructors

Constructor

Description

EventObject

​(

Object

source)

Constructs a prototypical Event.

---

#### Constructor Summary

Constructs a prototypical Event.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getSource

()

The object on which the Event initially occurred.

String

toString

()

Returns a String representation of this EventObject.

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

The object on which the Event initially occurred.

Returns a String representation of this EventObject.

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

- source

```java
protected transient
Object
source
```

The object on which the Event initially occurred.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- EventObject

```java
public EventObject​(
Object
source)
```

Constructs a prototypical Event.

**Parameters:** source

- the object on which the Event initially occurred
**Throws:** IllegalArgumentException

- if source is null

============ METHOD DETAIL ==========

- Method Detail

- getSource

```java
public
Object
getSource()
```

The object on which the Event initially occurred.

**Returns:** the object on which the Event initially occurred

- toString

```java
public
String
toString()
```

Returns a String representation of this EventObject.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this EventObject

Field Detail

- source

```java
protected transient
Object
source
```

The object on which the Event initially occurred.

---

#### Field Detail

source

```java
protected transient
Object
source
```

The object on which the Event initially occurred.

---

#### source

protected transient

Object

source

The object on which the Event initially occurred.

Constructor Detail

- EventObject

```java
public EventObject​(
Object
source)
```

Constructs a prototypical Event.

**Parameters:** source

- the object on which the Event initially occurred
**Throws:** IllegalArgumentException

- if source is null

---

#### Constructor Detail

EventObject

```java
public EventObject​(
Object
source)
```

Constructs a prototypical Event.

**Parameters:** source

- the object on which the Event initially occurred
**Throws:** IllegalArgumentException

- if source is null

---

#### EventObject

public EventObject​(

Object

source)

Constructs a prototypical Event.

Method Detail

- getSource

```java
public
Object
getSource()
```

The object on which the Event initially occurred.

**Returns:** the object on which the Event initially occurred

- toString

```java
public
String
toString()
```

Returns a String representation of this EventObject.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this EventObject

---

#### Method Detail

getSource

```java
public
Object
getSource()
```

The object on which the Event initially occurred.

**Returns:** the object on which the Event initially occurred

---

#### getSource

public

Object

getSource()

The object on which the Event initially occurred.

toString

```java
public
String
toString()
```

Returns a String representation of this EventObject.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this EventObject

---

#### toString

public

String

toString()

Returns a String representation of this EventObject.

---

