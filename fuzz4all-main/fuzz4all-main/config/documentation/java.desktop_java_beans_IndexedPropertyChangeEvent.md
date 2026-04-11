# Class IndexedPropertyChangeEvent

**Source:** `java.desktop\java\beans\IndexedPropertyChangeEvent.html`

### Class Description

```java
public class
IndexedPropertyChangeEvent

extends
PropertyChangeEvent
```

An "IndexedPropertyChange" event gets delivered whenever a component that
conforms to the JavaBeans™ specification (a "bean") changes a bound
indexed property. This class is an extension of

PropertyChangeEvent

but contains the index of the property that has changed.

Null values may be provided for the old and the new values if their
true values are not known.

An event source may send a null object as the name to indicate that an
arbitrary set of if its properties have changed. In this case the
old and new values should also be null.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public IndexedPropertyChangeEvent​(
Object
source,

String
propertyName,

Object
oldValue,

Object
newValue,
int index)

Constructs a new

IndexedPropertyChangeEvent

object.

**Parameters:**
- source

- The bean that fired the event.
- propertyName

- The programmatic name of the property that
was changed.
- oldValue

- The old value of the property.
- newValue

- The new value of the property.
- index

- index of the property element that was changed.

---

### Method Details

#### public int getIndex()

Gets the index of the property that was changed.

**Returns:**
- The index specifying the property element that was
changed.

---

### Additional Sections

#### Class IndexedPropertyChangeEvent

java.lang.Object

- java.util.EventObject
- - java.beans.PropertyChangeEvent
- - java.beans.IndexedPropertyChangeEvent

java.util.EventObject

- java.beans.PropertyChangeEvent
- - java.beans.IndexedPropertyChangeEvent

java.beans.PropertyChangeEvent

- java.beans.IndexedPropertyChangeEvent

java.beans.IndexedPropertyChangeEvent

**All Implemented Interfaces:** Serializable

```java
public class
IndexedPropertyChangeEvent

extends
PropertyChangeEvent
```

An "IndexedPropertyChange" event gets delivered whenever a component that
conforms to the JavaBeans™ specification (a "bean") changes a bound
indexed property. This class is an extension of

PropertyChangeEvent

but contains the index of the property that has changed.

Null values may be provided for the old and the new values if their
true values are not known.

An event source may send a null object as the name to indicate that an
arbitrary set of if its properties have changed. In this case the
old and new values should also be null.

**Since:** 1.5
**See Also:** Serialized Form

public class

IndexedPropertyChangeEvent

extends

PropertyChangeEvent

An "IndexedPropertyChange" event gets delivered whenever a component that
conforms to the JavaBeans™ specification (a "bean") changes a bound
indexed property. This class is an extension of

PropertyChangeEvent

but contains the index of the property that has changed.

Null values may be provided for the old and the new values if their
true values are not known.

An event source may send a null object as the name to indicate that an
arbitrary set of if its properties have changed. In this case the
old and new values should also be null.

Null values may be provided for the old and the new values if their
true values are not known.

An event source may send a null object as the name to indicate that an
arbitrary set of if its properties have changed. In this case the
old and new values should also be null.

An event source may send a null object as the name to indicate that an
arbitrary set of if its properties have changed. In this case the
old and new values should also be null.

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

IndexedPropertyChangeEvent

​(

Object

source,

String

propertyName,

Object

oldValue,

Object

newValue,
int index)

Constructs a new

IndexedPropertyChangeEvent

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getIndex

()

Gets the index of the property that was changed.

- Methods declared in class java.beans.

PropertyChangeEvent

getNewValue

,

getOldValue

,

getPropagationId

,

getPropertyName

,

setPropagationId

,

toString

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

IndexedPropertyChangeEvent

​(

Object

source,

String

propertyName,

Object

oldValue,

Object

newValue,
int index)

Constructs a new

IndexedPropertyChangeEvent

object.

---

#### Constructor Summary

Constructs a new

IndexedPropertyChangeEvent

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getIndex

()

Gets the index of the property that was changed.

- Methods declared in class java.beans.

PropertyChangeEvent

getNewValue

,

getOldValue

,

getPropagationId

,

getPropertyName

,

setPropagationId

,

toString

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

Gets the index of the property that was changed.

Methods declared in class java.beans.

PropertyChangeEvent

getNewValue

,

getOldValue

,

getPropagationId

,

getPropertyName

,

setPropagationId

,

toString

---

#### Methods declared in class java.beans. PropertyChangeEvent

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

- IndexedPropertyChangeEvent

```java
public IndexedPropertyChangeEvent​(
Object
source,

String
propertyName,

Object
oldValue,

Object
newValue,
int index)
```

Constructs a new

IndexedPropertyChangeEvent

object.

**Parameters:** source

- The bean that fired the event.
**Parameters:** propertyName

- The programmatic name of the property that
was changed.
**Parameters:** oldValue

- The old value of the property.
**Parameters:** newValue

- The new value of the property.
**Parameters:** index

- index of the property element that was changed.

============ METHOD DETAIL ==========

- Method Detail

- getIndex

```java
public int getIndex()
```

Gets the index of the property that was changed.

**Returns:** The index specifying the property element that was
changed.

Constructor Detail

- IndexedPropertyChangeEvent

```java
public IndexedPropertyChangeEvent​(
Object
source,

String
propertyName,

Object
oldValue,

Object
newValue,
int index)
```

Constructs a new

IndexedPropertyChangeEvent

object.

**Parameters:** source

- The bean that fired the event.
**Parameters:** propertyName

- The programmatic name of the property that
was changed.
**Parameters:** oldValue

- The old value of the property.
**Parameters:** newValue

- The new value of the property.
**Parameters:** index

- index of the property element that was changed.

---

#### Constructor Detail

IndexedPropertyChangeEvent

```java
public IndexedPropertyChangeEvent​(
Object
source,

String
propertyName,

Object
oldValue,

Object
newValue,
int index)
```

Constructs a new

IndexedPropertyChangeEvent

object.

**Parameters:** source

- The bean that fired the event.
**Parameters:** propertyName

- The programmatic name of the property that
was changed.
**Parameters:** oldValue

- The old value of the property.
**Parameters:** newValue

- The new value of the property.
**Parameters:** index

- index of the property element that was changed.

---

#### IndexedPropertyChangeEvent

public IndexedPropertyChangeEvent​(

Object

source,

String

propertyName,

Object

oldValue,

Object

newValue,
int index)

Constructs a new

IndexedPropertyChangeEvent

object.

Method Detail

- getIndex

```java
public int getIndex()
```

Gets the index of the property that was changed.

**Returns:** The index specifying the property element that was
changed.

---

#### Method Detail

getIndex

```java
public int getIndex()
```

Gets the index of the property that was changed.

**Returns:** The index specifying the property element that was
changed.

---

#### getIndex

public int getIndex()

Gets the index of the property that was changed.

---

