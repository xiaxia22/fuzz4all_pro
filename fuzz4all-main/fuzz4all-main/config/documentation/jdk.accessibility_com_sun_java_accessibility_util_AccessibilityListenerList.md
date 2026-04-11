# Class AccessibilityListenerList

**Source:** `jdk.accessibility\com\sun\java\accessibility\util\AccessibilityListenerList.html`

### Class Description

```java
public class
AccessibilityListenerList

extends
Object
```

The

AccessibilityListenerList

is a copy of the Swing

EventListerList

class.

---

### Field Details

#### protected transient
Object
[] listenerList

The list of listener type, listener pairs

---

### Constructor Details

#### public AccessibilityListenerList()

*No description found.*

---

### Method Details

#### public
Object
[] getListenerList()

Passes back the event listener list as an array of listener type, listener pairs.
Note that for performance reasons, this implementation passes back the actual
data structure in which the listener data is stored internally. This method
is guaranteed to pass back a non-null array, so that no null-checking
is required in fire methods. A zero-length array of Object is returned if
there are currently no listeners.

Absolutely no modification of the data contained in this array should be
made. If any such manipulation is necessary, it should be done on a copy
of the array returned rather than the array itself.

**Returns:**
- an array of listener type, listener pairs.

---

#### public int getListenerCount()

Returns the total number of listeners for this listener list.

**Returns:**
- the total number of listeners for this listener list.

---

#### public int getListenerCount​(
Class
<? extends
EventListener
> t)

Return the total number of listeners of the supplied type
for this listener list.

**Parameters:**
- t

- the type of the listener to be counted

**Returns:**
- the number of listeners found

---

#### public void add​(
Class
<? extends
EventListener
> t,

EventListener
l)

Add the listener as a listener of the specified type.

**Parameters:**
- t

- the type of the listener to be added
- l

- the listener to be added

---

#### public void remove​(
Class
<? extends
EventListener
> t,

EventListener
l)

Remove the listener as a listener of the specified type.

**Parameters:**
- t

- the type of the listener to be removed
- l

- the listener to be removed

---

#### public
String
toString()

Return a string representation of the

AccessibilityListenerList

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the

AccessibilityListenerList

.

---

### Additional Sections

#### Class AccessibilityListenerList

java.lang.Object

- com.sun.java.accessibility.util.AccessibilityListenerList

com.sun.java.accessibility.util.AccessibilityListenerList

```java
public class
AccessibilityListenerList

extends
Object
```

The

AccessibilityListenerList

is a copy of the Swing

EventListerList

class.

public class

AccessibilityListenerList

extends

Object

The

AccessibilityListenerList

is a copy of the Swing

EventListerList

class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Object

[]

listenerList

The list of listener type, listener pairs

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccessibilityListenerList

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(

Class

<? extends

EventListener

> t,

EventListener

l)

Add the listener as a listener of the specified type.

int

getListenerCount

()

Returns the total number of listeners for this listener list.

int

getListenerCount

​(

Class

<? extends

EventListener

> t)

Return the total number of listeners of the supplied type
for this listener list.

Object

[]

getListenerList

()

Passes back the event listener list as an array of listener type, listener pairs.

void

remove

​(

Class

<? extends

EventListener

> t,

EventListener

l)

Remove the listener as a listener of the specified type.

String

toString

()

Return a string representation of the

AccessibilityListenerList

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

[]

listenerList

The list of listener type, listener pairs

---

#### Field Summary

The list of listener type, listener pairs

Constructor Summary

Constructors

Constructor

Description

AccessibilityListenerList

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(

Class

<? extends

EventListener

> t,

EventListener

l)

Add the listener as a listener of the specified type.

int

getListenerCount

()

Returns the total number of listeners for this listener list.

int

getListenerCount

​(

Class

<? extends

EventListener

> t)

Return the total number of listeners of the supplied type
for this listener list.

Object

[]

getListenerList

()

Passes back the event listener list as an array of listener type, listener pairs.

void

remove

​(

Class

<? extends

EventListener

> t,

EventListener

l)

Remove the listener as a listener of the specified type.

String

toString

()

Return a string representation of the

AccessibilityListenerList

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

wait

,

wait

,

wait

---

#### Method Summary

Add the listener as a listener of the specified type.

Returns the total number of listeners for this listener list.

Return the total number of listeners of the supplied type
for this listener list.

Passes back the event listener list as an array of listener type, listener pairs.

Remove the listener as a listener of the specified type.

Return a string representation of the

AccessibilityListenerList

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
protected transient
Object
[] listenerList
```

The list of listener type, listener pairs

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AccessibilityListenerList

```java
public AccessibilityListenerList()
```

============ METHOD DETAIL ==========

- Method Detail

- getListenerList

```java
public
Object
[] getListenerList()
```

Passes back the event listener list as an array of listener type, listener pairs.
Note that for performance reasons, this implementation passes back the actual
data structure in which the listener data is stored internally. This method
is guaranteed to pass back a non-null array, so that no null-checking
is required in fire methods. A zero-length array of Object is returned if
there are currently no listeners.

Absolutely no modification of the data contained in this array should be
made. If any such manipulation is necessary, it should be done on a copy
of the array returned rather than the array itself.

**Returns:** an array of listener type, listener pairs.

- getListenerCount

```java
public int getListenerCount()
```

Returns the total number of listeners for this listener list.

**Returns:** the total number of listeners for this listener list.

- getListenerCount

```java
public int getListenerCount​(
Class
<? extends
EventListener
> t)
```

Return the total number of listeners of the supplied type
for this listener list.

**Parameters:** t

- the type of the listener to be counted
**Returns:** the number of listeners found

- add

```java
public void add​(
Class
<? extends
EventListener
> t,

EventListener
l)
```

Add the listener as a listener of the specified type.

**Parameters:** t

- the type of the listener to be added
**Parameters:** l

- the listener to be added

- remove

```java
public void remove​(
Class
<? extends
EventListener
> t,

EventListener
l)
```

Remove the listener as a listener of the specified type.

**Parameters:** t

- the type of the listener to be removed
**Parameters:** l

- the listener to be removed

- toString

```java
public
String
toString()
```

Return a string representation of the

AccessibilityListenerList

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the

AccessibilityListenerList

.

Field Detail

- listenerList

```java
protected transient
Object
[] listenerList
```

The list of listener type, listener pairs

---

#### Field Detail

listenerList

```java
protected transient
Object
[] listenerList
```

The list of listener type, listener pairs

---

#### listenerList

protected transient

Object

[] listenerList

The list of listener type, listener pairs

Constructor Detail

- AccessibilityListenerList

```java
public AccessibilityListenerList()
```

---

#### Constructor Detail

AccessibilityListenerList

```java
public AccessibilityListenerList()
```

---

#### AccessibilityListenerList

public AccessibilityListenerList()

Method Detail

- getListenerList

```java
public
Object
[] getListenerList()
```

Passes back the event listener list as an array of listener type, listener pairs.
Note that for performance reasons, this implementation passes back the actual
data structure in which the listener data is stored internally. This method
is guaranteed to pass back a non-null array, so that no null-checking
is required in fire methods. A zero-length array of Object is returned if
there are currently no listeners.

Absolutely no modification of the data contained in this array should be
made. If any such manipulation is necessary, it should be done on a copy
of the array returned rather than the array itself.

**Returns:** an array of listener type, listener pairs.

- getListenerCount

```java
public int getListenerCount()
```

Returns the total number of listeners for this listener list.

**Returns:** the total number of listeners for this listener list.

- getListenerCount

```java
public int getListenerCount​(
Class
<? extends
EventListener
> t)
```

Return the total number of listeners of the supplied type
for this listener list.

**Parameters:** t

- the type of the listener to be counted
**Returns:** the number of listeners found

- add

```java
public void add​(
Class
<? extends
EventListener
> t,

EventListener
l)
```

Add the listener as a listener of the specified type.

**Parameters:** t

- the type of the listener to be added
**Parameters:** l

- the listener to be added

- remove

```java
public void remove​(
Class
<? extends
EventListener
> t,

EventListener
l)
```

Remove the listener as a listener of the specified type.

**Parameters:** t

- the type of the listener to be removed
**Parameters:** l

- the listener to be removed

- toString

```java
public
String
toString()
```

Return a string representation of the

AccessibilityListenerList

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the

AccessibilityListenerList

.

---

#### Method Detail

getListenerList

```java
public
Object
[] getListenerList()
```

Passes back the event listener list as an array of listener type, listener pairs.
Note that for performance reasons, this implementation passes back the actual
data structure in which the listener data is stored internally. This method
is guaranteed to pass back a non-null array, so that no null-checking
is required in fire methods. A zero-length array of Object is returned if
there are currently no listeners.

Absolutely no modification of the data contained in this array should be
made. If any such manipulation is necessary, it should be done on a copy
of the array returned rather than the array itself.

**Returns:** an array of listener type, listener pairs.

---

#### getListenerList

public

Object

[] getListenerList()

Passes back the event listener list as an array of listener type, listener pairs.
Note that for performance reasons, this implementation passes back the actual
data structure in which the listener data is stored internally. This method
is guaranteed to pass back a non-null array, so that no null-checking
is required in fire methods. A zero-length array of Object is returned if
there are currently no listeners.

Absolutely no modification of the data contained in this array should be
made. If any such manipulation is necessary, it should be done on a copy
of the array returned rather than the array itself.

Absolutely no modification of the data contained in this array should be
made. If any such manipulation is necessary, it should be done on a copy
of the array returned rather than the array itself.

getListenerCount

```java
public int getListenerCount()
```

Returns the total number of listeners for this listener list.

**Returns:** the total number of listeners for this listener list.

---

#### getListenerCount

public int getListenerCount()

Returns the total number of listeners for this listener list.

getListenerCount

```java
public int getListenerCount​(
Class
<? extends
EventListener
> t)
```

Return the total number of listeners of the supplied type
for this listener list.

**Parameters:** t

- the type of the listener to be counted
**Returns:** the number of listeners found

---

#### getListenerCount

public int getListenerCount​(

Class

<? extends

EventListener

> t)

Return the total number of listeners of the supplied type
for this listener list.

add

```java
public void add​(
Class
<? extends
EventListener
> t,

EventListener
l)
```

Add the listener as a listener of the specified type.

**Parameters:** t

- the type of the listener to be added
**Parameters:** l

- the listener to be added

---

#### add

public void add​(

Class

<? extends

EventListener

> t,

EventListener

l)

Add the listener as a listener of the specified type.

remove

```java
public void remove​(
Class
<? extends
EventListener
> t,

EventListener
l)
```

Remove the listener as a listener of the specified type.

**Parameters:** t

- the type of the listener to be removed
**Parameters:** l

- the listener to be removed

---

#### remove

public void remove​(

Class

<? extends

EventListener

> t,

EventListener

l)

Remove the listener as a listener of the specified type.

toString

```java
public
String
toString()
```

Return a string representation of the

AccessibilityListenerList

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the

AccessibilityListenerList

.

---

#### toString

public

String

toString()

Return a string representation of the

AccessibilityListenerList

.

---

