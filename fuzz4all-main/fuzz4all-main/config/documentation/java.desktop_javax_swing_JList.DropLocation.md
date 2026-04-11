# Class JList.DropLocation

**Source:** `java.desktop\javax\swing\JList.DropLocation.html`

### Class Description

```java
public static final class
JList.DropLocation

extends
TransferHandler.DropLocation
```

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JList

.

**Enclosing class:** JList

<

E

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public int getIndex()

Returns the index where dropped data should be placed in the
list. Interpretation of the value depends on the drop mode set on
the associated component. If the drop mode is either

DropMode.USE_SELECTION

or

DropMode.ON

,
the return value is an index of a row in the list. If the drop mode is

DropMode.INSERT

, the return value refers to the index
where the data should be inserted. If the drop mode is

DropMode.ON_OR_INSERT

, the value of

isInsert()

indicates whether the index is an index
of a row, or an insert index.

-1

indicates that the drop occurred over empty space,
and no index could be calculated.

**Returns:**
- the drop index

---

#### public boolean isInsert()

Returns whether or not this location represents an insert
location.

**Returns:**
- whether or not this is an insert location

---

#### public
String
toString()

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:**
- toString

in class

TransferHandler.DropLocation

**Returns:**
- a string representation of this drop location

---

### Additional Sections

#### Class JList.DropLocation

java.lang.Object

- javax.swing.TransferHandler.DropLocation
- - javax.swing.JList.DropLocation

javax.swing.TransferHandler.DropLocation

- javax.swing.JList.DropLocation

javax.swing.JList.DropLocation

**Enclosing class:** JList

<

E

>

```java
public static final class
JList.DropLocation

extends
TransferHandler.DropLocation
```

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JList

.

**Since:** 1.6
**See Also:** JList.getDropLocation()

public static final class

JList.DropLocation

extends

TransferHandler.DropLocation

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JList

.

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

Returns the index where dropped data should be placed in the
list.

boolean

isInsert

()

Returns whether or not this location represents an insert
location.

String

toString

()

Returns a string representation of this drop location.

- Methods declared in class javax.swing.

TransferHandler.DropLocation

getDropPoint

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

Returns the index where dropped data should be placed in the
list.

boolean

isInsert

()

Returns whether or not this location represents an insert
location.

String

toString

()

Returns a string representation of this drop location.

- Methods declared in class javax.swing.

TransferHandler.DropLocation

getDropPoint

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

Returns the index where dropped data should be placed in the
list.

Returns whether or not this location represents an insert
location.

Returns a string representation of this drop location.

Methods declared in class javax.swing.

TransferHandler.DropLocation

getDropPoint

---

#### Methods declared in class javax.swing. TransferHandler.DropLocation

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

============ METHOD DETAIL ==========

- Method Detail

- getIndex

```java
public int getIndex()
```

Returns the index where dropped data should be placed in the
list. Interpretation of the value depends on the drop mode set on
the associated component. If the drop mode is either

DropMode.USE_SELECTION

or

DropMode.ON

,
the return value is an index of a row in the list. If the drop mode is

DropMode.INSERT

, the return value refers to the index
where the data should be inserted. If the drop mode is

DropMode.ON_OR_INSERT

, the value of

isInsert()

indicates whether the index is an index
of a row, or an insert index.

-1

indicates that the drop occurred over empty space,
and no index could be calculated.

**Returns:** the drop index

- isInsert

```java
public boolean isInsert()
```

Returns whether or not this location represents an insert
location.

**Returns:** whether or not this is an insert location

- toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

TransferHandler.DropLocation
**Returns:** a string representation of this drop location

Method Detail

- getIndex

```java
public int getIndex()
```

Returns the index where dropped data should be placed in the
list. Interpretation of the value depends on the drop mode set on
the associated component. If the drop mode is either

DropMode.USE_SELECTION

or

DropMode.ON

,
the return value is an index of a row in the list. If the drop mode is

DropMode.INSERT

, the return value refers to the index
where the data should be inserted. If the drop mode is

DropMode.ON_OR_INSERT

, the value of

isInsert()

indicates whether the index is an index
of a row, or an insert index.

-1

indicates that the drop occurred over empty space,
and no index could be calculated.

**Returns:** the drop index

- isInsert

```java
public boolean isInsert()
```

Returns whether or not this location represents an insert
location.

**Returns:** whether or not this is an insert location

- toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

TransferHandler.DropLocation
**Returns:** a string representation of this drop location

---

#### Method Detail

getIndex

```java
public int getIndex()
```

Returns the index where dropped data should be placed in the
list. Interpretation of the value depends on the drop mode set on
the associated component. If the drop mode is either

DropMode.USE_SELECTION

or

DropMode.ON

,
the return value is an index of a row in the list. If the drop mode is

DropMode.INSERT

, the return value refers to the index
where the data should be inserted. If the drop mode is

DropMode.ON_OR_INSERT

, the value of

isInsert()

indicates whether the index is an index
of a row, or an insert index.

-1

indicates that the drop occurred over empty space,
and no index could be calculated.

**Returns:** the drop index

---

#### getIndex

public int getIndex()

Returns the index where dropped data should be placed in the
list. Interpretation of the value depends on the drop mode set on
the associated component. If the drop mode is either

DropMode.USE_SELECTION

or

DropMode.ON

,
the return value is an index of a row in the list. If the drop mode is

DropMode.INSERT

, the return value refers to the index
where the data should be inserted. If the drop mode is

DropMode.ON_OR_INSERT

, the value of

isInsert()

indicates whether the index is an index
of a row, or an insert index.

-1

indicates that the drop occurred over empty space,
and no index could be calculated.

-1

indicates that the drop occurred over empty space,
and no index could be calculated.

isInsert

```java
public boolean isInsert()
```

Returns whether or not this location represents an insert
location.

**Returns:** whether or not this is an insert location

---

#### isInsert

public boolean isInsert()

Returns whether or not this location represents an insert
location.

toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

TransferHandler.DropLocation
**Returns:** a string representation of this drop location

---

#### toString

public

String

toString()

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

---

