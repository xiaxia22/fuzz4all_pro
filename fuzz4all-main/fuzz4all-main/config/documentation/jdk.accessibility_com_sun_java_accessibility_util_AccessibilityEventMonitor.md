# Class AccessibilityEventMonitor

**Source:** `jdk.accessibility\com\sun\java\accessibility\util\AccessibilityEventMonitor.html`

### Class Description

```java
public class
AccessibilityEventMonitor

extends
Object
```

AccessibilityEventMonitor

implements a PropertyChange listener
on every UI object that implements interface

Accessible

in the Java
Virtual Machine. The events captured by these listeners are made available
through listeners supported by

AccessibilityEventMonitor

.
With this, all the individual events on each of the UI object
instances are funneled into one set of PropertyChange listeners.

This class depends upon

EventQueueMonitor

, which provides the base
level support for capturing the top-level containers as they are created.

---

### Field Details

#### protected static final
AccessibilityListenerList
listenerList

The current list of registered

PropertyChangeListener

classes.

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

---

### Constructor Details

#### public AccessibilityEventMonitor()

*No description found.*

---

### Method Details

#### public static void addPropertyChangeListener​(
PropertyChangeListener
l)

Adds the specified listener to receive all PropertyChange events on
each UI object instance in the Java Virtual Machine as they occur.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to UI object instances that support this listener type.

**Parameters:**
- l

- the listener to add

**See Also:**
- removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### public static void removePropertyChangeListener​(
PropertyChangeListener
l)

Removes the specified listener so it no longer receives PropertyChange
events when they occur.

**Parameters:**
- l

- the listener to remove

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

---

### Additional Sections

#### Class AccessibilityEventMonitor

java.lang.Object

- com.sun.java.accessibility.util.AccessibilityEventMonitor

com.sun.java.accessibility.util.AccessibilityEventMonitor

```java
public class
AccessibilityEventMonitor

extends
Object
```

AccessibilityEventMonitor

implements a PropertyChange listener
on every UI object that implements interface

Accessible

in the Java
Virtual Machine. The events captured by these listeners are made available
through listeners supported by

AccessibilityEventMonitor

.
With this, all the individual events on each of the UI object
instances are funneled into one set of PropertyChange listeners.

This class depends upon

EventQueueMonitor

, which provides the base
level support for capturing the top-level containers as they are created.

public class

AccessibilityEventMonitor

extends

Object

AccessibilityEventMonitor

implements a PropertyChange listener
on every UI object that implements interface

Accessible

in the Java
Virtual Machine. The events captured by these listeners are made available
through listeners supported by

AccessibilityEventMonitor

.
With this, all the individual events on each of the UI object
instances are funneled into one set of PropertyChange listeners.

This class depends upon

EventQueueMonitor

, which provides the base
level support for capturing the top-level containers as they are created.

This class depends upon

EventQueueMonitor

, which provides the base
level support for capturing the top-level containers as they are created.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected static

AccessibilityListenerList

listenerList

The current list of registered

PropertyChangeListener

classes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccessibilityEventMonitor

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static void

addPropertyChangeListener

​(

PropertyChangeListener

l)

Adds the specified listener to receive all PropertyChange events on
each UI object instance in the Java Virtual Machine as they occur.

static void

removePropertyChangeListener

​(

PropertyChangeListener

l)

Removes the specified listener so it no longer receives PropertyChange
events when they occur.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected static

AccessibilityListenerList

listenerList

The current list of registered

PropertyChangeListener

classes.

---

#### Field Summary

The current list of registered

PropertyChangeListener

classes.

Constructor Summary

Constructors

Constructor

Description

AccessibilityEventMonitor

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static void

addPropertyChangeListener

​(

PropertyChangeListener

l)

Adds the specified listener to receive all PropertyChange events on
each UI object instance in the Java Virtual Machine as they occur.

static void

removePropertyChangeListener

​(

PropertyChangeListener

l)

Removes the specified listener so it no longer receives PropertyChange
events when they occur.

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

Adds the specified listener to receive all PropertyChange events on
each UI object instance in the Java Virtual Machine as they occur.

Removes the specified listener so it no longer receives PropertyChange
events when they occur.

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

============ FIELD DETAIL ===========

- Field Detail

- listenerList

```java
protected static final
AccessibilityListenerList
listenerList
```

The current list of registered

PropertyChangeListener

classes.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AccessibilityEventMonitor

```java
public AccessibilityEventMonitor()
```

============ METHOD DETAIL ==========

- Method Detail

- addPropertyChangeListener

```java
public static void addPropertyChangeListener​(
PropertyChangeListener
l)
```

Adds the specified listener to receive all PropertyChange events on
each UI object instance in the Java Virtual Machine as they occur.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to UI object instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removePropertyChangeListener(java.beans.PropertyChangeListener)

- removePropertyChangeListener

```java
public static void removePropertyChangeListener​(
PropertyChangeListener
l)
```

Removes the specified listener so it no longer receives PropertyChange
events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

Field Detail

- listenerList

```java
protected static final
AccessibilityListenerList
listenerList
```

The current list of registered

PropertyChangeListener

classes.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### Field Detail

listenerList

```java
protected static final
AccessibilityListenerList
listenerList
```

The current list of registered

PropertyChangeListener

classes.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### listenerList

protected static final

AccessibilityListenerList

listenerList

The current list of registered

PropertyChangeListener

classes.

Constructor Detail

- AccessibilityEventMonitor

```java
public AccessibilityEventMonitor()
```

---

#### Constructor Detail

AccessibilityEventMonitor

```java
public AccessibilityEventMonitor()
```

---

#### AccessibilityEventMonitor

public AccessibilityEventMonitor()

Method Detail

- addPropertyChangeListener

```java
public static void addPropertyChangeListener​(
PropertyChangeListener
l)
```

Adds the specified listener to receive all PropertyChange events on
each UI object instance in the Java Virtual Machine as they occur.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to UI object instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removePropertyChangeListener(java.beans.PropertyChangeListener)

- removePropertyChangeListener

```java
public static void removePropertyChangeListener​(
PropertyChangeListener
l)
```

Removes the specified listener so it no longer receives PropertyChange
events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### Method Detail

addPropertyChangeListener

```java
public static void addPropertyChangeListener​(
PropertyChangeListener
l)
```

Adds the specified listener to receive all PropertyChange events on
each UI object instance in the Java Virtual Machine as they occur.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to UI object instances that support this listener type.

**Parameters:** l

- the listener to add
**See Also:** removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### addPropertyChangeListener

public static void addPropertyChangeListener​(

PropertyChangeListener

l)

Adds the specified listener to receive all PropertyChange events on
each UI object instance in the Java Virtual Machine as they occur.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to UI object instances that support this listener type.

Note: This listener is automatically added to all component
instances created after this method is called. In addition, it
is only added to UI object instances that support this listener type.

removePropertyChangeListener

```java
public static void removePropertyChangeListener​(
PropertyChangeListener
l)
```

Removes the specified listener so it no longer receives PropertyChange
events when they occur.

**Parameters:** l

- the listener to remove
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### removePropertyChangeListener

public static void removePropertyChangeListener​(

PropertyChangeListener

l)

Removes the specified listener so it no longer receives PropertyChange
events when they occur.

---

