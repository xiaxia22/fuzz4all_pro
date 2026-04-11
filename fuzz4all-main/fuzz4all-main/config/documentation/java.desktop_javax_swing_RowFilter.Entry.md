# Class RowFilter.Entry<M,​I>

**Source:** `java.desktop\javax\swing\RowFilter.Entry.html`

### Class Description

```java
public abstract static class
RowFilter.Entry<M,​I>

extends
Object
```

An

Entry

object is passed to instances of

RowFilter

, allowing the filter to get the value of the
entry's data, and thus to determine whether the entry should be shown.
An

Entry

object contains information about the model
as well as methods for getting the underlying values from the model.

**Type Parameters:** M

- the type of the model; for example

PersonModel
**Type Parameters:** I

- the type of the identifier; when using

TableRowSorter

this will be

Integer

---

### Field Details

*No entries found.*

### Constructor Details

#### public Entry()

Creates an

Entry

.

---

### Method Details

#### public abstract
M
getModel()

Returns the underlying model.

**Returns:**
- the model containing the data that this entry represents

---

#### public abstract int getValueCount()

Returns the number of values in the entry. For
example, when used with a table this corresponds to the
number of columns.

**Returns:**
- number of values in the object being filtered

---

#### public abstract
Object
getValue​(int index)

Returns the value at the specified index. This may return

null

. When used with a table, index
corresponds to the column number in the model.

**Parameters:**
- index

- the index of the value to get

**Returns:**
- value at the specified index

**Throws:**
- IndexOutOfBoundsException

- if index < 0 or
>= getValueCount

---

#### public
String
getStringValue​(int index)

Returns the string value at the specified index. If
filtering is being done based on

String

values
this method is preferred to that of

getValue

as

getValue(index).toString()

may return a
different result than

getStringValue(index)

.

This implementation calls

getValue(index).toString()

after checking for

null

. Subclasses that provide
different string conversion should override this method if
necessary.

**Parameters:**
- index

- the index of the value to get

**Returns:**
- non-null

string at the specified index

**Throws:**
- IndexOutOfBoundsException

- if index < 0 ||
>= getValueCount

---

#### public abstract
I
getIdentifier()

Returns the identifer (in the model) of the entry.
For a table this corresponds to the index of the row in the model,
expressed as an

Integer

.

**Returns:**
- a model-based (not view-based) identifier for
this entry

---

### Additional Sections

#### Class RowFilter.Entry<M,​I>

java.lang.Object

- javax.swing.RowFilter.Entry<M,​I>

javax.swing.RowFilter.Entry<M,​I>

**Type Parameters:** M

- the type of the model; for example

PersonModel
**Type Parameters:** I

- the type of the identifier; when using

TableRowSorter

this will be

Integer

**Enclosing class:** RowFilter

<

M

,​

I

>

```java
public abstract static class
RowFilter.Entry<M,​I>

extends
Object
```

An

Entry

object is passed to instances of

RowFilter

, allowing the filter to get the value of the
entry's data, and thus to determine whether the entry should be shown.
An

Entry

object contains information about the model
as well as methods for getting the underlying values from the model.

**Since:** 1.6
**See Also:** RowFilter

,

DefaultRowSorter.setRowFilter(javax.swing.RowFilter)

public abstract static class

RowFilter.Entry<M,​I>

extends

Object

An

Entry

object is passed to instances of

RowFilter

, allowing the filter to get the value of the
entry's data, and thus to determine whether the entry should be shown.
An

Entry

object contains information about the model
as well as methods for getting the underlying values from the model.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Entry

()

Creates an

Entry

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

I

getIdentifier

()

Returns the identifer (in the model) of the entry.

abstract

M

getModel

()

Returns the underlying model.

String

getStringValue

​(int index)

Returns the string value at the specified index.

abstract

Object

getValue

​(int index)

Returns the value at the specified index.

abstract int

getValueCount

()

Returns the number of values in the entry.

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

Entry

()

Creates an

Entry

.

---

#### Constructor Summary

Creates an

Entry

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

I

getIdentifier

()

Returns the identifer (in the model) of the entry.

abstract

M

getModel

()

Returns the underlying model.

String

getStringValue

​(int index)

Returns the string value at the specified index.

abstract

Object

getValue

​(int index)

Returns the value at the specified index.

abstract int

getValueCount

()

Returns the number of values in the entry.

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

Returns the identifer (in the model) of the entry.

Returns the underlying model.

Returns the string value at the specified index.

Returns the value at the specified index.

Returns the number of values in the entry.

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

- Entry

```java
public Entry()
```

Creates an

Entry

.

============ METHOD DETAIL ==========

- Method Detail

- getModel

```java
public abstract
M
getModel()
```

Returns the underlying model.

**Returns:** the model containing the data that this entry represents

- getValueCount

```java
public abstract int getValueCount()
```

Returns the number of values in the entry. For
example, when used with a table this corresponds to the
number of columns.

**Returns:** number of values in the object being filtered

- getValue

```java
public abstract
Object
getValue​(int index)
```

Returns the value at the specified index. This may return

null

. When used with a table, index
corresponds to the column number in the model.

**Parameters:** index

- the index of the value to get
**Returns:** value at the specified index
**Throws:** IndexOutOfBoundsException

- if index < 0 or
>= getValueCount

- getStringValue

```java
public
String
getStringValue​(int index)
```

Returns the string value at the specified index. If
filtering is being done based on

String

values
this method is preferred to that of

getValue

as

getValue(index).toString()

may return a
different result than

getStringValue(index)

.

This implementation calls

getValue(index).toString()

after checking for

null

. Subclasses that provide
different string conversion should override this method if
necessary.

**Parameters:** index

- the index of the value to get
**Returns:** non-null

string at the specified index
**Throws:** IndexOutOfBoundsException

- if index < 0 ||
>= getValueCount

- getIdentifier

```java
public abstract
I
getIdentifier()
```

Returns the identifer (in the model) of the entry.
For a table this corresponds to the index of the row in the model,
expressed as an

Integer

.

**Returns:** a model-based (not view-based) identifier for
this entry

Constructor Detail

- Entry

```java
public Entry()
```

Creates an

Entry

.

---

#### Constructor Detail

Entry

```java
public Entry()
```

Creates an

Entry

.

---

#### Entry

public Entry()

Creates an

Entry

.

Method Detail

- getModel

```java
public abstract
M
getModel()
```

Returns the underlying model.

**Returns:** the model containing the data that this entry represents

- getValueCount

```java
public abstract int getValueCount()
```

Returns the number of values in the entry. For
example, when used with a table this corresponds to the
number of columns.

**Returns:** number of values in the object being filtered

- getValue

```java
public abstract
Object
getValue​(int index)
```

Returns the value at the specified index. This may return

null

. When used with a table, index
corresponds to the column number in the model.

**Parameters:** index

- the index of the value to get
**Returns:** value at the specified index
**Throws:** IndexOutOfBoundsException

- if index < 0 or
>= getValueCount

- getStringValue

```java
public
String
getStringValue​(int index)
```

Returns the string value at the specified index. If
filtering is being done based on

String

values
this method is preferred to that of

getValue

as

getValue(index).toString()

may return a
different result than

getStringValue(index)

.

This implementation calls

getValue(index).toString()

after checking for

null

. Subclasses that provide
different string conversion should override this method if
necessary.

**Parameters:** index

- the index of the value to get
**Returns:** non-null

string at the specified index
**Throws:** IndexOutOfBoundsException

- if index < 0 ||
>= getValueCount

- getIdentifier

```java
public abstract
I
getIdentifier()
```

Returns the identifer (in the model) of the entry.
For a table this corresponds to the index of the row in the model,
expressed as an

Integer

.

**Returns:** a model-based (not view-based) identifier for
this entry

---

#### Method Detail

getModel

```java
public abstract
M
getModel()
```

Returns the underlying model.

**Returns:** the model containing the data that this entry represents

---

#### getModel

public abstract

M

getModel()

Returns the underlying model.

getValueCount

```java
public abstract int getValueCount()
```

Returns the number of values in the entry. For
example, when used with a table this corresponds to the
number of columns.

**Returns:** number of values in the object being filtered

---

#### getValueCount

public abstract int getValueCount()

Returns the number of values in the entry. For
example, when used with a table this corresponds to the
number of columns.

getValue

```java
public abstract
Object
getValue​(int index)
```

Returns the value at the specified index. This may return

null

. When used with a table, index
corresponds to the column number in the model.

**Parameters:** index

- the index of the value to get
**Returns:** value at the specified index
**Throws:** IndexOutOfBoundsException

- if index < 0 or
>= getValueCount

---

#### getValue

public abstract

Object

getValue​(int index)

Returns the value at the specified index. This may return

null

. When used with a table, index
corresponds to the column number in the model.

getStringValue

```java
public
String
getStringValue​(int index)
```

Returns the string value at the specified index. If
filtering is being done based on

String

values
this method is preferred to that of

getValue

as

getValue(index).toString()

may return a
different result than

getStringValue(index)

.

This implementation calls

getValue(index).toString()

after checking for

null

. Subclasses that provide
different string conversion should override this method if
necessary.

**Parameters:** index

- the index of the value to get
**Returns:** non-null

string at the specified index
**Throws:** IndexOutOfBoundsException

- if index < 0 ||
>= getValueCount

---

#### getStringValue

public

String

getStringValue​(int index)

Returns the string value at the specified index. If
filtering is being done based on

String

values
this method is preferred to that of

getValue

as

getValue(index).toString()

may return a
different result than

getStringValue(index)

.

This implementation calls

getValue(index).toString()

after checking for

null

. Subclasses that provide
different string conversion should override this method if
necessary.

This implementation calls

getValue(index).toString()

after checking for

null

. Subclasses that provide
different string conversion should override this method if
necessary.

getIdentifier

```java
public abstract
I
getIdentifier()
```

Returns the identifer (in the model) of the entry.
For a table this corresponds to the index of the row in the model,
expressed as an

Integer

.

**Returns:** a model-based (not view-based) identifier for
this entry

---

#### getIdentifier

public abstract

I

getIdentifier()

Returns the identifer (in the model) of the entry.
For a table this corresponds to the index of the row in the model,
expressed as an

Integer

.

---

