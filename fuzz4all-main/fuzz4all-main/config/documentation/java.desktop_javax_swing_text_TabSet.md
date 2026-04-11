# Class TabSet

**Source:** `java.desktop\javax\swing\text\TabSet.html`

### Class Description

```java
public class
TabSet

extends
Object

implements
Serializable
```

A TabSet is comprised of many TabStops. It offers methods for locating the
closest TabStop to a given position and finding all the potential TabStops.
It is also immutable.

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

#### public TabSet​(
TabStop
[] tabs)

Creates and returns an instance of TabSet. The array of Tabs
passed in must be sorted in ascending order.

**Parameters:**
- tabs

- the TabStops to initialize the TabSet

---

### Method Details

#### public int getTabCount()

Returns the number of Tab instances the receiver contains.

**Returns:**
- the number of Tab instances the receiver contains

---

#### public
TabStop
getTab​(int index)

Returns the TabStop at index

index

. This will throw an
IllegalArgumentException if

index

is outside the range
of tabs.

**Parameters:**
- index

- which TapStop to return

**Returns:**
- the TabStop at index

index

---

#### public
TabStop
getTabAfter​(float location)

Returns the Tab instance after

location

. This will
return null if there are no tabs after

location

.

**Parameters:**
- location

- location to find a Tab after

**Returns:**
- the Tab instance after

location

---

#### public int getTabIndex​(
TabStop
tab)

Returns the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

**Parameters:**
- tab

- the TabStop to find

**Returns:**
- the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

---

#### public int getTabIndexAfter​(float location)

Returns the index of the Tab to be used after

location

.
This will return -1 if there are no tabs after

location

.

**Parameters:**
- location

- location to find a Tab after

**Returns:**
- the index of the Tab to be used after

location

---

#### public boolean equals​(
Object
o)

Indicates whether this

TabSet

is equal to another one.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the

TabSet

instance which this instance
should be compared to.

**Returns:**
- true

if

o

is the instance of

TabSet

, has the same number of

TabStop

s
and they are all equal,

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

**Since:**
- 1.5

---

#### public int hashCode()

Returns a hashcode for this set of TabStops.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hashcode value for this set of TabStops.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

**Since:**
- 1.5

---

#### public
String
toString()

Returns the string representation of the set of tabs.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class TabSet

java.lang.Object

- javax.swing.text.TabSet

javax.swing.text.TabSet

**All Implemented Interfaces:** Serializable

```java
public class
TabSet

extends
Object

implements
Serializable
```

A TabSet is comprised of many TabStops. It offers methods for locating the
closest TabStop to a given position and finding all the potential TabStops.
It is also immutable.

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

TabSet

extends

Object

implements

Serializable

A TabSet is comprised of many TabStops. It offers methods for locating the
closest TabStop to a given position and finding all the potential TabStops.
It is also immutable.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TabSet

​(

TabStop

[] tabs)

Creates and returns an instance of TabSet.

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

o)

Indicates whether this

TabSet

is equal to another one.

TabStop

getTab

​(int index)

Returns the TabStop at index

index

.

TabStop

getTabAfter

​(float location)

Returns the Tab instance after

location

.

int

getTabCount

()

Returns the number of Tab instances the receiver contains.

int

getTabIndex

​(

TabStop

tab)

Returns the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

int

getTabIndexAfter

​(float location)

Returns the index of the Tab to be used after

location

.

int

hashCode

()

Returns a hashcode for this set of TabStops.

String

toString

()

Returns the string representation of the set of tabs.

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

TabSet

​(

TabStop

[] tabs)

Creates and returns an instance of TabSet.

---

#### Constructor Summary

Creates and returns an instance of TabSet.

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

o)

Indicates whether this

TabSet

is equal to another one.

TabStop

getTab

​(int index)

Returns the TabStop at index

index

.

TabStop

getTabAfter

​(float location)

Returns the Tab instance after

location

.

int

getTabCount

()

Returns the number of Tab instances the receiver contains.

int

getTabIndex

​(

TabStop

tab)

Returns the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

int

getTabIndexAfter

​(float location)

Returns the index of the Tab to be used after

location

.

int

hashCode

()

Returns a hashcode for this set of TabStops.

String

toString

()

Returns the string representation of the set of tabs.

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

wait

,

wait

,

wait

---

#### Method Summary

Indicates whether this

TabSet

is equal to another one.

Returns the TabStop at index

index

.

Returns the Tab instance after

location

.

Returns the number of Tab instances the receiver contains.

Returns the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

Returns the index of the Tab to be used after

location

.

Returns a hashcode for this set of TabStops.

Returns the string representation of the set of tabs.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TabSet

```java
public TabSet​(
TabStop
[] tabs)
```

Creates and returns an instance of TabSet. The array of Tabs
passed in must be sorted in ascending order.

**Parameters:** tabs

- the TabStops to initialize the TabSet

============ METHOD DETAIL ==========

- Method Detail

- getTabCount

```java
public int getTabCount()
```

Returns the number of Tab instances the receiver contains.

**Returns:** the number of Tab instances the receiver contains

- getTab

```java
public
TabStop
getTab​(int index)
```

Returns the TabStop at index

index

. This will throw an
IllegalArgumentException if

index

is outside the range
of tabs.

**Parameters:** index

- which TapStop to return
**Returns:** the TabStop at index

index

- getTabAfter

```java
public
TabStop
getTabAfter​(float location)
```

Returns the Tab instance after

location

. This will
return null if there are no tabs after

location

.

**Parameters:** location

- location to find a Tab after
**Returns:** the Tab instance after

location

- getTabIndex

```java
public int getTabIndex​(
TabStop
tab)
```

Returns the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

**Parameters:** tab

- the TabStop to find
**Returns:** the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

- getTabIndexAfter

```java
public int getTabIndexAfter​(float location)
```

Returns the index of the Tab to be used after

location

.
This will return -1 if there are no tabs after

location

.

**Parameters:** location

- location to find a Tab after
**Returns:** the index of the Tab to be used after

location

- equals

```java
public boolean equals​(
Object
o)
```

Indicates whether this

TabSet

is equal to another one.

**Overrides:** equals

in class

Object
**Parameters:** o

- the

TabSet

instance which this instance
should be compared to.
**Returns:** true

if

o

is the instance of

TabSet

, has the same number of

TabStop

s
and they are all equal,

false

otherwise.
**Since:** 1.5
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this set of TabStops.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this set of TabStops.
**Since:** 1.5
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns the string representation of the set of tabs.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- TabSet

```java
public TabSet​(
TabStop
[] tabs)
```

Creates and returns an instance of TabSet. The array of Tabs
passed in must be sorted in ascending order.

**Parameters:** tabs

- the TabStops to initialize the TabSet

---

#### Constructor Detail

TabSet

```java
public TabSet​(
TabStop
[] tabs)
```

Creates and returns an instance of TabSet. The array of Tabs
passed in must be sorted in ascending order.

**Parameters:** tabs

- the TabStops to initialize the TabSet

---

#### TabSet

public TabSet​(

TabStop

[] tabs)

Creates and returns an instance of TabSet. The array of Tabs
passed in must be sorted in ascending order.

Method Detail

- getTabCount

```java
public int getTabCount()
```

Returns the number of Tab instances the receiver contains.

**Returns:** the number of Tab instances the receiver contains

- getTab

```java
public
TabStop
getTab​(int index)
```

Returns the TabStop at index

index

. This will throw an
IllegalArgumentException if

index

is outside the range
of tabs.

**Parameters:** index

- which TapStop to return
**Returns:** the TabStop at index

index

- getTabAfter

```java
public
TabStop
getTabAfter​(float location)
```

Returns the Tab instance after

location

. This will
return null if there are no tabs after

location

.

**Parameters:** location

- location to find a Tab after
**Returns:** the Tab instance after

location

- getTabIndex

```java
public int getTabIndex​(
TabStop
tab)
```

Returns the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

**Parameters:** tab

- the TabStop to find
**Returns:** the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

- getTabIndexAfter

```java
public int getTabIndexAfter​(float location)
```

Returns the index of the Tab to be used after

location

.
This will return -1 if there are no tabs after

location

.

**Parameters:** location

- location to find a Tab after
**Returns:** the index of the Tab to be used after

location

- equals

```java
public boolean equals​(
Object
o)
```

Indicates whether this

TabSet

is equal to another one.

**Overrides:** equals

in class

Object
**Parameters:** o

- the

TabSet

instance which this instance
should be compared to.
**Returns:** true

if

o

is the instance of

TabSet

, has the same number of

TabStop

s
and they are all equal,

false

otherwise.
**Since:** 1.5
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this set of TabStops.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this set of TabStops.
**Since:** 1.5
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns the string representation of the set of tabs.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getTabCount

```java
public int getTabCount()
```

Returns the number of Tab instances the receiver contains.

**Returns:** the number of Tab instances the receiver contains

---

#### getTabCount

public int getTabCount()

Returns the number of Tab instances the receiver contains.

getTab

```java
public
TabStop
getTab​(int index)
```

Returns the TabStop at index

index

. This will throw an
IllegalArgumentException if

index

is outside the range
of tabs.

**Parameters:** index

- which TapStop to return
**Returns:** the TabStop at index

index

---

#### getTab

public

TabStop

getTab​(int index)

Returns the TabStop at index

index

. This will throw an
IllegalArgumentException if

index

is outside the range
of tabs.

getTabAfter

```java
public
TabStop
getTabAfter​(float location)
```

Returns the Tab instance after

location

. This will
return null if there are no tabs after

location

.

**Parameters:** location

- location to find a Tab after
**Returns:** the Tab instance after

location

---

#### getTabAfter

public

TabStop

getTabAfter​(float location)

Returns the Tab instance after

location

. This will
return null if there are no tabs after

location

.

getTabIndex

```java
public int getTabIndex​(
TabStop
tab)
```

Returns the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

**Parameters:** tab

- the TabStop to find
**Returns:** the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

---

#### getTabIndex

public int getTabIndex​(

TabStop

tab)

Returns the index of the TabStop

tab

, or -1 if

tab

is not contained in the receiver.

getTabIndexAfter

```java
public int getTabIndexAfter​(float location)
```

Returns the index of the Tab to be used after

location

.
This will return -1 if there are no tabs after

location

.

**Parameters:** location

- location to find a Tab after
**Returns:** the index of the Tab to be used after

location

---

#### getTabIndexAfter

public int getTabIndexAfter​(float location)

Returns the index of the Tab to be used after

location

.
This will return -1 if there are no tabs after

location

.

equals

```java
public boolean equals​(
Object
o)
```

Indicates whether this

TabSet

is equal to another one.

**Overrides:** equals

in class

Object
**Parameters:** o

- the

TabSet

instance which this instance
should be compared to.
**Returns:** true

if

o

is the instance of

TabSet

, has the same number of

TabStop

s
and they are all equal,

false

otherwise.
**Since:** 1.5
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Indicates whether this

TabSet

is equal to another one.

hashCode

```java
public int hashCode()
```

Returns a hashcode for this set of TabStops.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this set of TabStops.
**Since:** 1.5
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode for this set of TabStops.

toString

```java
public
String
toString()
```

Returns the string representation of the set of tabs.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns the string representation of the set of tabs.

---

