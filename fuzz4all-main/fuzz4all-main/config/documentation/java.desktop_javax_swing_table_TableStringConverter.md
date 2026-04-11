# Class TableStringConverter

**Source:** `java.desktop\javax\swing\table\TableStringConverter.html`

### Class Description

```java
public abstract class
TableStringConverter

extends
Object
```

TableStringConverter is used to convert objects from the model into
strings. This is useful in filtering and searching when the model returns
objects that do not have meaningful

toString

implementations.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### public TableStringConverter()

*No description found.*

---

### Method Details

#### public abstract
String
toString​(
TableModel
model,
int row,
int column)

Returns the string representation of the value at the specified
location.

**Parameters:**
- model

- the

TableModel

to fetch the value from
- row

- the row the string is being requested for
- column

- the column the string is being requested for

**Returns:**
- the string representation. This should never return null.

**Throws:**
- NullPointerException

- if

model

is null
- IndexOutOfBoundsException

- if the arguments are outside the
bounds of the model

---

### Additional Sections

#### Class TableStringConverter

java.lang.Object

- javax.swing.table.TableStringConverter

javax.swing.table.TableStringConverter

```java
public abstract class
TableStringConverter

extends
Object
```

TableStringConverter is used to convert objects from the model into
strings. This is useful in filtering and searching when the model returns
objects that do not have meaningful

toString

implementations.

**Since:** 1.6

public abstract class

TableStringConverter

extends

Object

TableStringConverter is used to convert objects from the model into
strings. This is useful in filtering and searching when the model returns
objects that do not have meaningful

toString

implementations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TableStringConverter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

toString

​(

TableModel

model,
int row,
int column)

Returns the string representation of the value at the specified
location.

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

Constructor Summary

Constructors

Constructor

Description

TableStringConverter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

toString

​(

TableModel

model,
int row,
int column)

Returns the string representation of the value at the specified
location.

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

Returns the string representation of the value at the specified
location.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TableStringConverter

```java
public TableStringConverter()
```

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public abstract
String
toString​(
TableModel
model,
int row,
int column)
```

Returns the string representation of the value at the specified
location.

**Parameters:** model

- the

TableModel

to fetch the value from
**Parameters:** row

- the row the string is being requested for
**Parameters:** column

- the column the string is being requested for
**Returns:** the string representation. This should never return null.
**Throws:** NullPointerException

- if

model

is null
**Throws:** IndexOutOfBoundsException

- if the arguments are outside the
bounds of the model

Constructor Detail

- TableStringConverter

```java
public TableStringConverter()
```

---

#### Constructor Detail

TableStringConverter

```java
public TableStringConverter()
```

---

#### TableStringConverter

public TableStringConverter()

Method Detail

- toString

```java
public abstract
String
toString​(
TableModel
model,
int row,
int column)
```

Returns the string representation of the value at the specified
location.

**Parameters:** model

- the

TableModel

to fetch the value from
**Parameters:** row

- the row the string is being requested for
**Parameters:** column

- the column the string is being requested for
**Returns:** the string representation. This should never return null.
**Throws:** NullPointerException

- if

model

is null
**Throws:** IndexOutOfBoundsException

- if the arguments are outside the
bounds of the model

---

#### Method Detail

toString

```java
public abstract
String
toString​(
TableModel
model,
int row,
int column)
```

Returns the string representation of the value at the specified
location.

**Parameters:** model

- the

TableModel

to fetch the value from
**Parameters:** row

- the row the string is being requested for
**Parameters:** column

- the column the string is being requested for
**Returns:** the string representation. This should never return null.
**Throws:** NullPointerException

- if

model

is null
**Throws:** IndexOutOfBoundsException

- if the arguments are outside the
bounds of the model

---

#### toString

public abstract

String

toString​(

TableModel

model,
int row,
int column)

Returns the string representation of the value at the specified
location.

---

