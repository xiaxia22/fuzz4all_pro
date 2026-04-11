# Class JTable.DropLocation

**Source:** `java.desktop\javax\swing\JTable.DropLocation.html`

### Class Description

```java
public static final class
JTable.DropLocation

extends
TransferHandler.DropLocation
```

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JTable

.

**Enclosing class:** JTable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public int getRow()

Returns the row index where a dropped item should be placed in the
table. Interpretation of the value depends on the return of

isInsertRow()

. If that method returns

true

this value indicates the index where a new
row should be inserted. Otherwise, it represents the value
of an existing row on which the data was dropped. This index is
in terms of the view.

-1

indicates that the drop occurred over empty space,
and no row could be calculated.

**Returns:**
- the drop row

---

#### public int getColumn()

Returns the column index where a dropped item should be placed in the
table. Interpretation of the value depends on the return of

isInsertColumn()

. If that method returns

true

this value indicates the index where a new
column should be inserted. Otherwise, it represents the value
of an existing column on which the data was dropped. This index is
in terms of the view.

-1

indicates that the drop occurred over empty space,
and no column could be calculated.

**Returns:**
- the drop row

---

#### public boolean isInsertRow()

Returns whether or not this location represents an insert
of a row.

**Returns:**
- whether or not this is an insert row

---

#### public boolean isInsertColumn()

Returns whether or not this location represents an insert
of a column.

**Returns:**
- whether or not this is an insert column

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

#### Class JTable.DropLocation

java.lang.Object

- javax.swing.TransferHandler.DropLocation
- - javax.swing.JTable.DropLocation

javax.swing.TransferHandler.DropLocation

- javax.swing.JTable.DropLocation

javax.swing.JTable.DropLocation

**Enclosing class:** JTable

```java
public static final class
JTable.DropLocation

extends
TransferHandler.DropLocation
```

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JTable

.

**Since:** 1.6
**See Also:** JTable.getDropLocation()

public static final class

JTable.DropLocation

extends

TransferHandler.DropLocation

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JTable

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

getColumn

()

Returns the column index where a dropped item should be placed in the
table.

int

getRow

()

Returns the row index where a dropped item should be placed in the
table.

boolean

isInsertColumn

()

Returns whether or not this location represents an insert
of a column.

boolean

isInsertRow

()

Returns whether or not this location represents an insert
of a row.

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

getColumn

()

Returns the column index where a dropped item should be placed in the
table.

int

getRow

()

Returns the row index where a dropped item should be placed in the
table.

boolean

isInsertColumn

()

Returns whether or not this location represents an insert
of a column.

boolean

isInsertRow

()

Returns whether or not this location represents an insert
of a row.

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

Returns the column index where a dropped item should be placed in the
table.

Returns the row index where a dropped item should be placed in the
table.

Returns whether or not this location represents an insert
of a column.

Returns whether or not this location represents an insert
of a row.

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

- getRow

```java
public int getRow()
```

Returns the row index where a dropped item should be placed in the
table. Interpretation of the value depends on the return of

isInsertRow()

. If that method returns

true

this value indicates the index where a new
row should be inserted. Otherwise, it represents the value
of an existing row on which the data was dropped. This index is
in terms of the view.

-1

indicates that the drop occurred over empty space,
and no row could be calculated.

**Returns:** the drop row

- getColumn

```java
public int getColumn()
```

Returns the column index where a dropped item should be placed in the
table. Interpretation of the value depends on the return of

isInsertColumn()

. If that method returns

true

this value indicates the index where a new
column should be inserted. Otherwise, it represents the value
of an existing column on which the data was dropped. This index is
in terms of the view.

-1

indicates that the drop occurred over empty space,
and no column could be calculated.

**Returns:** the drop row

- isInsertRow

```java
public boolean isInsertRow()
```

Returns whether or not this location represents an insert
of a row.

**Returns:** whether or not this is an insert row

- isInsertColumn

```java
public boolean isInsertColumn()
```

Returns whether or not this location represents an insert
of a column.

**Returns:** whether or not this is an insert column

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

- getRow

```java
public int getRow()
```

Returns the row index where a dropped item should be placed in the
table. Interpretation of the value depends on the return of

isInsertRow()

. If that method returns

true

this value indicates the index where a new
row should be inserted. Otherwise, it represents the value
of an existing row on which the data was dropped. This index is
in terms of the view.

-1

indicates that the drop occurred over empty space,
and no row could be calculated.

**Returns:** the drop row

- getColumn

```java
public int getColumn()
```

Returns the column index where a dropped item should be placed in the
table. Interpretation of the value depends on the return of

isInsertColumn()

. If that method returns

true

this value indicates the index where a new
column should be inserted. Otherwise, it represents the value
of an existing column on which the data was dropped. This index is
in terms of the view.

-1

indicates that the drop occurred over empty space,
and no column could be calculated.

**Returns:** the drop row

- isInsertRow

```java
public boolean isInsertRow()
```

Returns whether or not this location represents an insert
of a row.

**Returns:** whether or not this is an insert row

- isInsertColumn

```java
public boolean isInsertColumn()
```

Returns whether or not this location represents an insert
of a column.

**Returns:** whether or not this is an insert column

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

getRow

```java
public int getRow()
```

Returns the row index where a dropped item should be placed in the
table. Interpretation of the value depends on the return of

isInsertRow()

. If that method returns

true

this value indicates the index where a new
row should be inserted. Otherwise, it represents the value
of an existing row on which the data was dropped. This index is
in terms of the view.

-1

indicates that the drop occurred over empty space,
and no row could be calculated.

**Returns:** the drop row

---

#### getRow

public int getRow()

Returns the row index where a dropped item should be placed in the
table. Interpretation of the value depends on the return of

isInsertRow()

. If that method returns

true

this value indicates the index where a new
row should be inserted. Otherwise, it represents the value
of an existing row on which the data was dropped. This index is
in terms of the view.

-1

indicates that the drop occurred over empty space,
and no row could be calculated.

-1

indicates that the drop occurred over empty space,
and no row could be calculated.

getColumn

```java
public int getColumn()
```

Returns the column index where a dropped item should be placed in the
table. Interpretation of the value depends on the return of

isInsertColumn()

. If that method returns

true

this value indicates the index where a new
column should be inserted. Otherwise, it represents the value
of an existing column on which the data was dropped. This index is
in terms of the view.

-1

indicates that the drop occurred over empty space,
and no column could be calculated.

**Returns:** the drop row

---

#### getColumn

public int getColumn()

Returns the column index where a dropped item should be placed in the
table. Interpretation of the value depends on the return of

isInsertColumn()

. If that method returns

true

this value indicates the index where a new
column should be inserted. Otherwise, it represents the value
of an existing column on which the data was dropped. This index is
in terms of the view.

-1

indicates that the drop occurred over empty space,
and no column could be calculated.

-1

indicates that the drop occurred over empty space,
and no column could be calculated.

isInsertRow

```java
public boolean isInsertRow()
```

Returns whether or not this location represents an insert
of a row.

**Returns:** whether or not this is an insert row

---

#### isInsertRow

public boolean isInsertRow()

Returns whether or not this location represents an insert
of a row.

isInsertColumn

```java
public boolean isInsertColumn()
```

Returns whether or not this location represents an insert
of a column.

**Returns:** whether or not this is an insert column

---

#### isInsertColumn

public boolean isInsertColumn()

Returns whether or not this location represents an insert
of a column.

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

