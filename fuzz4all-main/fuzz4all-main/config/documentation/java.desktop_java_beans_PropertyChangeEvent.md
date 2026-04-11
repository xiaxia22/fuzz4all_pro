# Class PropertyChangeEvent

**Source:** `java.desktop\java\beans\PropertyChangeEvent.html`

### Class Description

```java
public class
PropertyChangeEvent

extends
EventObject
```

A "PropertyChange" event gets delivered whenever a bean changes a "bound"
or "constrained" property. A PropertyChangeEvent object is sent as an
argument to the PropertyChangeListener and VetoableChangeListener methods.

Normally PropertyChangeEvents are accompanied by the name and the old
and new value of the changed property. If the new value is a primitive
type (such as int or boolean) it must be wrapped as the
corresponding java.lang.* Object type (such as Integer or Boolean).

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

#### public PropertyChangeEvent​(
Object
source,

String
propertyName,

Object
oldValue,

Object
newValue)

Constructs a new

PropertyChangeEvent

.

**Parameters:**
- source

- the bean that fired the event
- propertyName

- the programmatic name of the property that was changed
- oldValue

- the old value of the property
- newValue

- the new value of the property

**Throws:**
- IllegalArgumentException

- if

source

is

null

---

### Method Details

#### public
String
getPropertyName()

Gets the programmatic name of the property that was changed.

**Returns:**
- The programmatic name of the property that was changed.
May be null if multiple properties have changed.

---

#### public
Object
getNewValue()

Gets the new value for the property, expressed as an Object.

**Returns:**
- The new value for the property, expressed as an Object.
May be null if multiple properties have changed.

---

#### public
Object
getOldValue()

Gets the old value for the property, expressed as an Object.

**Returns:**
- The old value for the property, expressed as an Object.
May be null if multiple properties have changed.

---

#### public void setPropagationId​(
Object
propagationId)

Sets the propagationId object for the event.

**Parameters:**
- propagationId

- The propagationId object for the event.

---

#### public
Object
getPropagationId()

The "propagationId" field is reserved for future use. In Beans 1.0
the sole requirement is that if a listener catches a PropertyChangeEvent
and then fires a PropertyChangeEvent of its own, then it should
make sure that it propagates the propagationId field from its
incoming event to its outgoing event.

**Returns:**
- the propagationId object associated with a bound/constrained
property update.

---

#### public
String
toString()

Returns a string representation of the object.

**Overrides:**
- toString

in class

EventObject

**Returns:**
- a string representation of the object

**Since:**
- 1.7

---

### Additional Sections

#### Class PropertyChangeEvent

java.lang.Object

- java.util.EventObject
- - java.beans.PropertyChangeEvent

java.util.EventObject

- java.beans.PropertyChangeEvent

java.beans.PropertyChangeEvent

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** IndexedPropertyChangeEvent

```java
public class
PropertyChangeEvent

extends
EventObject
```

A "PropertyChange" event gets delivered whenever a bean changes a "bound"
or "constrained" property. A PropertyChangeEvent object is sent as an
argument to the PropertyChangeListener and VetoableChangeListener methods.

Normally PropertyChangeEvents are accompanied by the name and the old
and new value of the changed property. If the new value is a primitive
type (such as int or boolean) it must be wrapped as the
corresponding java.lang.* Object type (such as Integer or Boolean).

Null values may be provided for the old and the new values if their
true values are not known.

An event source may send a null object as the name to indicate that an
arbitrary set of if its properties have changed. In this case the
old and new values should also be null.

**Since:** 1.1
**See Also:** Serialized Form

public class

PropertyChangeEvent

extends

EventObject

A "PropertyChange" event gets delivered whenever a bean changes a "bound"
or "constrained" property. A PropertyChangeEvent object is sent as an
argument to the PropertyChangeListener and VetoableChangeListener methods.

Normally PropertyChangeEvents are accompanied by the name and the old
and new value of the changed property. If the new value is a primitive
type (such as int or boolean) it must be wrapped as the
corresponding java.lang.* Object type (such as Integer or Boolean).

Null values may be provided for the old and the new values if their
true values are not known.

An event source may send a null object as the name to indicate that an
arbitrary set of if its properties have changed. In this case the
old and new values should also be null.

Normally PropertyChangeEvents are accompanied by the name and the old
and new value of the changed property. If the new value is a primitive
type (such as int or boolean) it must be wrapped as the
corresponding java.lang.* Object type (such as Integer or Boolean).

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

PropertyChangeEvent

​(

Object

source,

String

propertyName,

Object

oldValue,

Object

newValue)

Constructs a new

PropertyChangeEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getNewValue

()

Gets the new value for the property, expressed as an Object.

Object

getOldValue

()

Gets the old value for the property, expressed as an Object.

Object

getPropagationId

()

The "propagationId" field is reserved for future use.

String

getPropertyName

()

Gets the programmatic name of the property that was changed.

void

setPropagationId

​(

Object

propagationId)

Sets the propagationId object for the event.

String

toString

()

Returns a string representation of the object.

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

PropertyChangeEvent

​(

Object

source,

String

propertyName,

Object

oldValue,

Object

newValue)

Constructs a new

PropertyChangeEvent

.

---

#### Constructor Summary

Constructs a new

PropertyChangeEvent

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getNewValue

()

Gets the new value for the property, expressed as an Object.

Object

getOldValue

()

Gets the old value for the property, expressed as an Object.

Object

getPropagationId

()

The "propagationId" field is reserved for future use.

String

getPropertyName

()

Gets the programmatic name of the property that was changed.

void

setPropagationId

​(

Object

propagationId)

Sets the propagationId object for the event.

String

toString

()

Returns a string representation of the object.

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

Gets the new value for the property, expressed as an Object.

Gets the old value for the property, expressed as an Object.

The "propagationId" field is reserved for future use.

Gets the programmatic name of the property that was changed.

Sets the propagationId object for the event.

Returns a string representation of the object.

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

- PropertyChangeEvent

```java
public PropertyChangeEvent​(
Object
source,

String
propertyName,

Object
oldValue,

Object
newValue)
```

Constructs a new

PropertyChangeEvent

.

**Parameters:** source

- the bean that fired the event
**Parameters:** propertyName

- the programmatic name of the property that was changed
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** IllegalArgumentException

- if

source

is

null

============ METHOD DETAIL ==========

- Method Detail

- getPropertyName

```java
public
String
getPropertyName()
```

Gets the programmatic name of the property that was changed.

**Returns:** The programmatic name of the property that was changed.
May be null if multiple properties have changed.

- getNewValue

```java
public
Object
getNewValue()
```

Gets the new value for the property, expressed as an Object.

**Returns:** The new value for the property, expressed as an Object.
May be null if multiple properties have changed.

- getOldValue

```java
public
Object
getOldValue()
```

Gets the old value for the property, expressed as an Object.

**Returns:** The old value for the property, expressed as an Object.
May be null if multiple properties have changed.

- setPropagationId

```java
public void setPropagationId​(
Object
propagationId)
```

Sets the propagationId object for the event.

**Parameters:** propagationId

- The propagationId object for the event.

- getPropagationId

```java
public
Object
getPropagationId()
```

The "propagationId" field is reserved for future use. In Beans 1.0
the sole requirement is that if a listener catches a PropertyChangeEvent
and then fires a PropertyChangeEvent of its own, then it should
make sure that it propagates the propagationId field from its
incoming event to its outgoing event.

**Returns:** the propagationId object associated with a bound/constrained
property update.

- toString

```java
public
String
toString()
```

Returns a string representation of the object.

**Overrides:** toString

in class

EventObject
**Returns:** a string representation of the object
**Since:** 1.7

Constructor Detail

- PropertyChangeEvent

```java
public PropertyChangeEvent​(
Object
source,

String
propertyName,

Object
oldValue,

Object
newValue)
```

Constructs a new

PropertyChangeEvent

.

**Parameters:** source

- the bean that fired the event
**Parameters:** propertyName

- the programmatic name of the property that was changed
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** IllegalArgumentException

- if

source

is

null

---

#### Constructor Detail

PropertyChangeEvent

```java
public PropertyChangeEvent​(
Object
source,

String
propertyName,

Object
oldValue,

Object
newValue)
```

Constructs a new

PropertyChangeEvent

.

**Parameters:** source

- the bean that fired the event
**Parameters:** propertyName

- the programmatic name of the property that was changed
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property
**Throws:** IllegalArgumentException

- if

source

is

null

---

#### PropertyChangeEvent

public PropertyChangeEvent​(

Object

source,

String

propertyName,

Object

oldValue,

Object

newValue)

Constructs a new

PropertyChangeEvent

.

Method Detail

- getPropertyName

```java
public
String
getPropertyName()
```

Gets the programmatic name of the property that was changed.

**Returns:** The programmatic name of the property that was changed.
May be null if multiple properties have changed.

- getNewValue

```java
public
Object
getNewValue()
```

Gets the new value for the property, expressed as an Object.

**Returns:** The new value for the property, expressed as an Object.
May be null if multiple properties have changed.

- getOldValue

```java
public
Object
getOldValue()
```

Gets the old value for the property, expressed as an Object.

**Returns:** The old value for the property, expressed as an Object.
May be null if multiple properties have changed.

- setPropagationId

```java
public void setPropagationId​(
Object
propagationId)
```

Sets the propagationId object for the event.

**Parameters:** propagationId

- The propagationId object for the event.

- getPropagationId

```java
public
Object
getPropagationId()
```

The "propagationId" field is reserved for future use. In Beans 1.0
the sole requirement is that if a listener catches a PropertyChangeEvent
and then fires a PropertyChangeEvent of its own, then it should
make sure that it propagates the propagationId field from its
incoming event to its outgoing event.

**Returns:** the propagationId object associated with a bound/constrained
property update.

- toString

```java
public
String
toString()
```

Returns a string representation of the object.

**Overrides:** toString

in class

EventObject
**Returns:** a string representation of the object
**Since:** 1.7

---

#### Method Detail

getPropertyName

```java
public
String
getPropertyName()
```

Gets the programmatic name of the property that was changed.

**Returns:** The programmatic name of the property that was changed.
May be null if multiple properties have changed.

---

#### getPropertyName

public

String

getPropertyName()

Gets the programmatic name of the property that was changed.

getNewValue

```java
public
Object
getNewValue()
```

Gets the new value for the property, expressed as an Object.

**Returns:** The new value for the property, expressed as an Object.
May be null if multiple properties have changed.

---

#### getNewValue

public

Object

getNewValue()

Gets the new value for the property, expressed as an Object.

getOldValue

```java
public
Object
getOldValue()
```

Gets the old value for the property, expressed as an Object.

**Returns:** The old value for the property, expressed as an Object.
May be null if multiple properties have changed.

---

#### getOldValue

public

Object

getOldValue()

Gets the old value for the property, expressed as an Object.

setPropagationId

```java
public void setPropagationId​(
Object
propagationId)
```

Sets the propagationId object for the event.

**Parameters:** propagationId

- The propagationId object for the event.

---

#### setPropagationId

public void setPropagationId​(

Object

propagationId)

Sets the propagationId object for the event.

getPropagationId

```java
public
Object
getPropagationId()
```

The "propagationId" field is reserved for future use. In Beans 1.0
the sole requirement is that if a listener catches a PropertyChangeEvent
and then fires a PropertyChangeEvent of its own, then it should
make sure that it propagates the propagationId field from its
incoming event to its outgoing event.

**Returns:** the propagationId object associated with a bound/constrained
property update.

---

#### getPropagationId

public

Object

getPropagationId()

The "propagationId" field is reserved for future use. In Beans 1.0
the sole requirement is that if a listener catches a PropertyChangeEvent
and then fires a PropertyChangeEvent of its own, then it should
make sure that it propagates the propagationId field from its
incoming event to its outgoing event.

toString

```java
public
String
toString()
```

Returns a string representation of the object.

**Overrides:** toString

in class

EventObject
**Returns:** a string representation of the object
**Since:** 1.7

---

#### toString

public

String

toString()

Returns a string representation of the object.

---

