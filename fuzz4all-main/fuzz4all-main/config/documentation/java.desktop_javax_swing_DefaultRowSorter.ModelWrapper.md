# Class DefaultRowSorter.ModelWrapper<M,​I>

**Source:** `java.desktop\javax\swing\DefaultRowSorter.ModelWrapper.html`

### Class Description

```java
protected abstract static class
DefaultRowSorter.ModelWrapper<M,​I>

extends
Object
```

DefaultRowSorter.ModelWrapper

is responsible for providing
the data that gets sorted by

DefaultRowSorter

. You
normally do not interact directly with

ModelWrapper

.
Subclasses of

DefaultRowSorter

provide an
implementation of

ModelWrapper

wrapping another model.
For example,

TableRowSorter

provides a

ModelWrapper

that
wraps a

TableModel

.

ModelWrapper

makes a distinction between values as

Object

s and

String

s. This allows
implementations to provide a custom string
converter to be used instead of invoking

toString

on the
object.

**Type Parameters:** M

- the type of the underlying model
**Type Parameters:** I

- the identifier supplied to the filter

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ModelWrapper()

Creates a new

ModelWrapper

.

---

### Method Details

#### public abstract
M
getModel()

Returns the underlying model that this

Model

is
wrapping.

**Returns:**
- the underlying model

---

#### public abstract int getColumnCount()

Returns the number of columns in the model.

**Returns:**
- the number of columns in the model

---

#### public abstract int getRowCount()

Returns the number of rows in the model.

**Returns:**
- the number of rows in the model

---

#### public abstract
Object
getValueAt​(int row,
int column)

Returns the value at the specified index.

**Parameters:**
- row

- the row index
- column

- the column index

**Returns:**
- the value at the specified index

**Throws:**
- IndexOutOfBoundsException

- if the indices are outside
the range of the model

---

#### public
String
getStringValueAt​(int row,
int column)

Returns the value as a

String

at the specified
index. This implementation uses

toString

on
the result from

getValueAt

(making sure
to return an empty string for null values). Subclasses that
override this method should never return null.

**Parameters:**
- row

- the row index
- column

- the column index

**Returns:**
- the value at the specified index as a

String

**Throws:**
- IndexOutOfBoundsException

- if the indices are outside
the range of the model

---

#### public abstract
I
getIdentifier​(int row)

Returns the identifier for the specified row. The return value
of this is used as the identifier for the

RowFilter.Entry

that is passed to the

RowFilter

.

**Parameters:**
- row

- the row to return the identifier for, in terms of
the underlying model

**Returns:**
- the identifier

**See Also:**
- RowFilter.Entry.getIdentifier()

---

### Additional Sections

#### Class DefaultRowSorter.ModelWrapper<M,​I>

java.lang.Object

- javax.swing.DefaultRowSorter.ModelWrapper<M,​I>

javax.swing.DefaultRowSorter.ModelWrapper<M,​I>

**Type Parameters:** M

- the type of the underlying model
**Type Parameters:** I

- the identifier supplied to the filter

**Enclosing class:** DefaultRowSorter

<

M

,​

I

>

```java
protected abstract static class
DefaultRowSorter.ModelWrapper<M,​I>

extends
Object
```

DefaultRowSorter.ModelWrapper

is responsible for providing
the data that gets sorted by

DefaultRowSorter

. You
normally do not interact directly with

ModelWrapper

.
Subclasses of

DefaultRowSorter

provide an
implementation of

ModelWrapper

wrapping another model.
For example,

TableRowSorter

provides a

ModelWrapper

that
wraps a

TableModel

.

ModelWrapper

makes a distinction between values as

Object

s and

String

s. This allows
implementations to provide a custom string
converter to be used instead of invoking

toString

on the
object.

**Since:** 1.6
**See Also:** RowFilter

,

RowFilter.Entry

protected abstract static class

DefaultRowSorter.ModelWrapper<M,​I>

extends

Object

DefaultRowSorter.ModelWrapper

is responsible for providing
the data that gets sorted by

DefaultRowSorter

. You
normally do not interact directly with

ModelWrapper

.
Subclasses of

DefaultRowSorter

provide an
implementation of

ModelWrapper

wrapping another model.
For example,

TableRowSorter

provides a

ModelWrapper

that
wraps a

TableModel

.

ModelWrapper

makes a distinction between values as

Object

s and

String

s. This allows
implementations to provide a custom string
converter to be used instead of invoking

toString

on the
object.

ModelWrapper

makes a distinction between values as

Object

s and

String

s. This allows
implementations to provide a custom string
converter to be used instead of invoking

toString

on the
object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ModelWrapper

()

Creates a new

ModelWrapper

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

abstract int

getColumnCount

()

Returns the number of columns in the model.

abstract

I

getIdentifier

​(int row)

Returns the identifier for the specified row.

abstract

M

getModel

()

Returns the underlying model that this

Model

is
wrapping.

abstract int

getRowCount

()

Returns the number of rows in the model.

String

getStringValueAt

​(int row,
int column)

Returns the value as a

String

at the specified
index.

abstract

Object

getValueAt

​(int row,
int column)

Returns the value at the specified index.

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

Modifier

Constructor

Description

protected

ModelWrapper

()

Creates a new

ModelWrapper

.

---

#### Constructor Summary

Creates a new

ModelWrapper

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract int

getColumnCount

()

Returns the number of columns in the model.

abstract

I

getIdentifier

​(int row)

Returns the identifier for the specified row.

abstract

M

getModel

()

Returns the underlying model that this

Model

is
wrapping.

abstract int

getRowCount

()

Returns the number of rows in the model.

String

getStringValueAt

​(int row,
int column)

Returns the value as a

String

at the specified
index.

abstract

Object

getValueAt

​(int row,
int column)

Returns the value at the specified index.

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

Returns the number of columns in the model.

Returns the identifier for the specified row.

Returns the underlying model that this

Model

is
wrapping.

Returns the number of rows in the model.

Returns the value as a

String

at the specified
index.

Returns the value at the specified index.

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

- ModelWrapper

```java
protected ModelWrapper()
```

Creates a new

ModelWrapper

.

============ METHOD DETAIL ==========

- Method Detail

- getModel

```java
public abstract
M
getModel()
```

Returns the underlying model that this

Model

is
wrapping.

**Returns:** the underlying model

- getColumnCount

```java
public abstract int getColumnCount()
```

Returns the number of columns in the model.

**Returns:** the number of columns in the model

- getRowCount

```java
public abstract int getRowCount()
```

Returns the number of rows in the model.

**Returns:** the number of rows in the model

- getValueAt

```java
public abstract
Object
getValueAt​(int row,
int column)
```

Returns the value at the specified index.

**Parameters:** row

- the row index
**Parameters:** column

- the column index
**Returns:** the value at the specified index
**Throws:** IndexOutOfBoundsException

- if the indices are outside
the range of the model

- getStringValueAt

```java
public
String
getStringValueAt​(int row,
int column)
```

Returns the value as a

String

at the specified
index. This implementation uses

toString

on
the result from

getValueAt

(making sure
to return an empty string for null values). Subclasses that
override this method should never return null.

**Parameters:** row

- the row index
**Parameters:** column

- the column index
**Returns:** the value at the specified index as a

String
**Throws:** IndexOutOfBoundsException

- if the indices are outside
the range of the model

- getIdentifier

```java
public abstract
I
getIdentifier​(int row)
```

Returns the identifier for the specified row. The return value
of this is used as the identifier for the

RowFilter.Entry

that is passed to the

RowFilter

.

**Parameters:** row

- the row to return the identifier for, in terms of
the underlying model
**Returns:** the identifier
**See Also:** RowFilter.Entry.getIdentifier()

Constructor Detail

- ModelWrapper

```java
protected ModelWrapper()
```

Creates a new

ModelWrapper

.

---

#### Constructor Detail

ModelWrapper

```java
protected ModelWrapper()
```

Creates a new

ModelWrapper

.

---

#### ModelWrapper

protected ModelWrapper()

Creates a new

ModelWrapper

.

Method Detail

- getModel

```java
public abstract
M
getModel()
```

Returns the underlying model that this

Model

is
wrapping.

**Returns:** the underlying model

- getColumnCount

```java
public abstract int getColumnCount()
```

Returns the number of columns in the model.

**Returns:** the number of columns in the model

- getRowCount

```java
public abstract int getRowCount()
```

Returns the number of rows in the model.

**Returns:** the number of rows in the model

- getValueAt

```java
public abstract
Object
getValueAt​(int row,
int column)
```

Returns the value at the specified index.

**Parameters:** row

- the row index
**Parameters:** column

- the column index
**Returns:** the value at the specified index
**Throws:** IndexOutOfBoundsException

- if the indices are outside
the range of the model

- getStringValueAt

```java
public
String
getStringValueAt​(int row,
int column)
```

Returns the value as a

String

at the specified
index. This implementation uses

toString

on
the result from

getValueAt

(making sure
to return an empty string for null values). Subclasses that
override this method should never return null.

**Parameters:** row

- the row index
**Parameters:** column

- the column index
**Returns:** the value at the specified index as a

String
**Throws:** IndexOutOfBoundsException

- if the indices are outside
the range of the model

- getIdentifier

```java
public abstract
I
getIdentifier​(int row)
```

Returns the identifier for the specified row. The return value
of this is used as the identifier for the

RowFilter.Entry

that is passed to the

RowFilter

.

**Parameters:** row

- the row to return the identifier for, in terms of
the underlying model
**Returns:** the identifier
**See Also:** RowFilter.Entry.getIdentifier()

---

#### Method Detail

getModel

```java
public abstract
M
getModel()
```

Returns the underlying model that this

Model

is
wrapping.

**Returns:** the underlying model

---

#### getModel

public abstract

M

getModel()

Returns the underlying model that this

Model

is
wrapping.

getColumnCount

```java
public abstract int getColumnCount()
```

Returns the number of columns in the model.

**Returns:** the number of columns in the model

---

#### getColumnCount

public abstract int getColumnCount()

Returns the number of columns in the model.

getRowCount

```java
public abstract int getRowCount()
```

Returns the number of rows in the model.

**Returns:** the number of rows in the model

---

#### getRowCount

public abstract int getRowCount()

Returns the number of rows in the model.

getValueAt

```java
public abstract
Object
getValueAt​(int row,
int column)
```

Returns the value at the specified index.

**Parameters:** row

- the row index
**Parameters:** column

- the column index
**Returns:** the value at the specified index
**Throws:** IndexOutOfBoundsException

- if the indices are outside
the range of the model

---

#### getValueAt

public abstract

Object

getValueAt​(int row,
int column)

Returns the value at the specified index.

getStringValueAt

```java
public
String
getStringValueAt​(int row,
int column)
```

Returns the value as a

String

at the specified
index. This implementation uses

toString

on
the result from

getValueAt

(making sure
to return an empty string for null values). Subclasses that
override this method should never return null.

**Parameters:** row

- the row index
**Parameters:** column

- the column index
**Returns:** the value at the specified index as a

String
**Throws:** IndexOutOfBoundsException

- if the indices are outside
the range of the model

---

#### getStringValueAt

public

String

getStringValueAt​(int row,
int column)

Returns the value as a

String

at the specified
index. This implementation uses

toString

on
the result from

getValueAt

(making sure
to return an empty string for null values). Subclasses that
override this method should never return null.

getIdentifier

```java
public abstract
I
getIdentifier​(int row)
```

Returns the identifier for the specified row. The return value
of this is used as the identifier for the

RowFilter.Entry

that is passed to the

RowFilter

.

**Parameters:** row

- the row to return the identifier for, in terms of
the underlying model
**Returns:** the identifier
**See Also:** RowFilter.Entry.getIdentifier()

---

#### getIdentifier

public abstract

I

getIdentifier​(int row)

Returns the identifier for the specified row. The return value
of this is used as the identifier for the

RowFilter.Entry

that is passed to the

RowFilter

.

---

