# Interface Predicate

**Source:** `java.sql.rowset\javax\sql\rowset\Predicate.html`

### Class Description

```java
public interface
Predicate
```

The standard interface that provides the framework for all

FilteredRowSet

objects to describe their filters.

1.0 Background

The

Predicate

interface is a standard interface that
applications can implement to define the filter they wish to apply to a
a

FilteredRowSet

object. A

FilteredRowSet

object consumes implementations of this interface and enforces the
constraints defined in the implementation of the method

evaluate

.
A

FilteredRowSet

object enforces the filter constraints in a
bi-directional manner: It outputs only rows that are within
the constraints of the filter; and conversely, it inserts, modifies, or updates
only rows that are within the constraints of the filter.

2.0 Implementation Guidelines

In order to supply a predicate for the

FilteredRowSet

.
this interface must be implemented. At this time, the JDBC RowSet
Implementations (JSR-114) does not specify any standard filters definitions.
By specifying a standard means and mechanism for a range of filters to be
defined and deployed with both the reference and vendor implementations
of the

FilteredRowSet

interface, this allows for a flexible
and application motivated implementations of

Predicate

to emerge.

A sample implementation would look something like this:

```java
public class Range implements Predicate {

private int[] lo;
private int[] hi;
private int[] idx;

public Range(int[] lo, int[] hi, int[] idx) {
this.lo = lo;
this.hi = hi;
this.idx = idx;
}

public boolean evaluate(RowSet rs) {

// Check the present row determine if it lies
// within the filtering criteria.

for (int i = 0; i < idx.length; i++) {
int value;
try {
value = (Integer) rs.getObject(idx[i]);
} catch (SQLException ex) {
Logger.getLogger(Range.class.getName()).log(Level.SEVERE, null, ex);
return false;
}

if (value < lo[i] && value > hi[i]) {
// outside of filter constraints
return false;
}
}
// Within filter constraints
return true;
}
}
```

The example above implements a simple range predicate. Note, that
implementations should but are not required to provide

String

and integer index based constructors to provide for JDBC RowSet Implementation
applications that use both column identification conventions.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean evaluate​(
RowSet
rs)

This method is typically called a

FilteredRowSet

object
internal methods (not public) that control the

RowSet

object's
cursor moving from row to the next. In addition, if this internal method
moves the cursor onto a row that has been deleted, the internal method will
continue to ove the cursor until a valid row is found.

**Parameters:**
- rs

- The

RowSet

to be evaluated

**Returns:**
- true

if there are more rows in the filter;

false

otherwise

---

#### boolean evaluate​(
Object
value,
int column)
throws
SQLException

This method is called by a

FilteredRowSet

object
to check whether the value lies between the filtering criterion (or criteria
if multiple constraints exist) set using the

setFilter()

method.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

**Parameters:**
- value

- An

Object

value which needs to be checked,
whether it can be part of this

FilterRowSet

object.
- column

- a

int

object that must match the
SQL index of a column in this

RowSet

object. This must
have been passed to

Predicate

as one of the columns
for filtering while initializing a

Predicate

**Returns:**
- true

if row value lies within the filter;

false

otherwise

**Throws:**
- SQLException

- if the column is not part of filtering criteria

---

#### boolean evaluate​(
Object
value,

String
columnName)
throws
SQLException

This method is called by the

FilteredRowSet

object
to check whether the value lies between the filtering criteria set
using the setFilter method.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

**Parameters:**
- value

- An

Object

value which needs to be checked,
whether it can be part of this

FilterRowSet

.
- columnName

- a

String

object that must match the
SQL name of a column in this

RowSet

, ignoring case. This must
have been passed to

Predicate

as one of the columns for filtering
while initializing a

Predicate

**Returns:**
- true

if value lies within the filter;

false

otherwise

**Throws:**
- SQLException

- if the column is not part of filtering criteria

---

### Additional Sections

#### Interface Predicate

```java
public interface
Predicate
```

The standard interface that provides the framework for all

FilteredRowSet

objects to describe their filters.

1.0 Background

The

Predicate

interface is a standard interface that
applications can implement to define the filter they wish to apply to a
a

FilteredRowSet

object. A

FilteredRowSet

object consumes implementations of this interface and enforces the
constraints defined in the implementation of the method

evaluate

.
A

FilteredRowSet

object enforces the filter constraints in a
bi-directional manner: It outputs only rows that are within
the constraints of the filter; and conversely, it inserts, modifies, or updates
only rows that are within the constraints of the filter.

2.0 Implementation Guidelines

In order to supply a predicate for the

FilteredRowSet

.
this interface must be implemented. At this time, the JDBC RowSet
Implementations (JSR-114) does not specify any standard filters definitions.
By specifying a standard means and mechanism for a range of filters to be
defined and deployed with both the reference and vendor implementations
of the

FilteredRowSet

interface, this allows for a flexible
and application motivated implementations of

Predicate

to emerge.

A sample implementation would look something like this:

```java
public class Range implements Predicate {

private int[] lo;
private int[] hi;
private int[] idx;

public Range(int[] lo, int[] hi, int[] idx) {
this.lo = lo;
this.hi = hi;
this.idx = idx;
}

public boolean evaluate(RowSet rs) {

// Check the present row determine if it lies
// within the filtering criteria.

for (int i = 0; i < idx.length; i++) {
int value;
try {
value = (Integer) rs.getObject(idx[i]);
} catch (SQLException ex) {
Logger.getLogger(Range.class.getName()).log(Level.SEVERE, null, ex);
return false;
}

if (value < lo[i] && value > hi[i]) {
// outside of filter constraints
return false;
}
}
// Within filter constraints
return true;
}
}
```

The example above implements a simple range predicate. Note, that
implementations should but are not required to provide

String

and integer index based constructors to provide for JDBC RowSet Implementation
applications that use both column identification conventions.

**Since:** 1.5

public interface

Predicate

The standard interface that provides the framework for all

FilteredRowSet

objects to describe their filters.

1.0 Background

The

Predicate

interface is a standard interface that
applications can implement to define the filter they wish to apply to a
a

FilteredRowSet

object. A

FilteredRowSet

object consumes implementations of this interface and enforces the
constraints defined in the implementation of the method

evaluate

.
A

FilteredRowSet

object enforces the filter constraints in a
bi-directional manner: It outputs only rows that are within
the constraints of the filter; and conversely, it inserts, modifies, or updates
only rows that are within the constraints of the filter.

2.0 Implementation Guidelines

In order to supply a predicate for the

FilteredRowSet

.
this interface must be implemented. At this time, the JDBC RowSet
Implementations (JSR-114) does not specify any standard filters definitions.
By specifying a standard means and mechanism for a range of filters to be
defined and deployed with both the reference and vendor implementations
of the

FilteredRowSet

interface, this allows for a flexible
and application motivated implementations of

Predicate

to emerge.

A sample implementation would look something like this:

```java
public class Range implements Predicate {

private int[] lo;
private int[] hi;
private int[] idx;

public Range(int[] lo, int[] hi, int[] idx) {
this.lo = lo;
this.hi = hi;
this.idx = idx;
}

public boolean evaluate(RowSet rs) {

// Check the present row determine if it lies
// within the filtering criteria.

for (int i = 0; i < idx.length; i++) {
int value;
try {
value = (Integer) rs.getObject(idx[i]);
} catch (SQLException ex) {
Logger.getLogger(Range.class.getName()).log(Level.SEVERE, null, ex);
return false;
}

if (value < lo[i] && value > hi[i]) {
// outside of filter constraints
return false;
}
}
// Within filter constraints
return true;
}
}
```

The example above implements a simple range predicate. Note, that
implementations should but are not required to provide

String

and integer index based constructors to provide for JDBC RowSet Implementation
applications that use both column identification conventions.

---

#### 2.0 Implementation Guidelines

A sample implementation would look something like this:

```java
public class Range implements Predicate {

private int[] lo;
private int[] hi;
private int[] idx;

public Range(int[] lo, int[] hi, int[] idx) {
this.lo = lo;
this.hi = hi;
this.idx = idx;
}

public boolean evaluate(RowSet rs) {

// Check the present row determine if it lies
// within the filtering criteria.

for (int i = 0; i < idx.length; i++) {
int value;
try {
value = (Integer) rs.getObject(idx[i]);
} catch (SQLException ex) {
Logger.getLogger(Range.class.getName()).log(Level.SEVERE, null, ex);
return false;
}

if (value < lo[i] && value > hi[i]) {
// outside of filter constraints
return false;
}
}
// Within filter constraints
return true;
}
}
```

The example above implements a simple range predicate. Note, that
implementations should but are not required to provide

String

and integer index based constructors to provide for JDBC RowSet Implementation
applications that use both column identification conventions.

public class Range implements Predicate {

private int[] lo;
private int[] hi;
private int[] idx;

public Range(int[] lo, int[] hi, int[] idx) {
this.lo = lo;
this.hi = hi;
this.idx = idx;
}

public boolean evaluate(RowSet rs) {

// Check the present row determine if it lies
// within the filtering criteria.

for (int i = 0; i < idx.length; i++) {
int value;
try {
value = (Integer) rs.getObject(idx[i]);
} catch (SQLException ex) {
Logger.getLogger(Range.class.getName()).log(Level.SEVERE, null, ex);
return false;
}

if (value < lo[i] && value > hi[i]) {
// outside of filter constraints
return false;
}
}
// Within filter constraints
return true;
}
}

The example above implements a simple range predicate. Note, that
implementations should but are not required to provide

String

and integer index based constructors to provide for JDBC RowSet Implementation
applications that use both column identification conventions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

evaluate

​(

Object

value,
int column)

This method is called by a

FilteredRowSet

object
to check whether the value lies between the filtering criterion (or criteria
if multiple constraints exist) set using the

setFilter()

method.

boolean

evaluate

​(

Object

value,

String

columnName)

This method is called by the

FilteredRowSet

object
to check whether the value lies between the filtering criteria set
using the setFilter method.

boolean

evaluate

​(

RowSet

rs)

This method is typically called a

FilteredRowSet

object
internal methods (not public) that control the

RowSet

object's
cursor moving from row to the next.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

evaluate

​(

Object

value,
int column)

This method is called by a

FilteredRowSet

object
to check whether the value lies between the filtering criterion (or criteria
if multiple constraints exist) set using the

setFilter()

method.

boolean

evaluate

​(

Object

value,

String

columnName)

This method is called by the

FilteredRowSet

object
to check whether the value lies between the filtering criteria set
using the setFilter method.

boolean

evaluate

​(

RowSet

rs)

This method is typically called a

FilteredRowSet

object
internal methods (not public) that control the

RowSet

object's
cursor moving from row to the next.

---

#### Method Summary

This method is called by a

FilteredRowSet

object
to check whether the value lies between the filtering criterion (or criteria
if multiple constraints exist) set using the

setFilter()

method.

This method is called by the

FilteredRowSet

object
to check whether the value lies between the filtering criteria set
using the setFilter method.

This method is typically called a

FilteredRowSet

object
internal methods (not public) that control the

RowSet

object's
cursor moving from row to the next.

============ METHOD DETAIL ==========

- Method Detail

- evaluate

```java
boolean evaluate​(
RowSet
rs)
```

This method is typically called a

FilteredRowSet

object
internal methods (not public) that control the

RowSet

object's
cursor moving from row to the next. In addition, if this internal method
moves the cursor onto a row that has been deleted, the internal method will
continue to ove the cursor until a valid row is found.

**Parameters:** rs

- The

RowSet

to be evaluated
**Returns:** true

if there are more rows in the filter;

false

otherwise

- evaluate

```java
boolean evaluate​(
Object
value,
int column)
throws
SQLException
```

This method is called by a

FilteredRowSet

object
to check whether the value lies between the filtering criterion (or criteria
if multiple constraints exist) set using the

setFilter()

method.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

**Parameters:** value

- An

Object

value which needs to be checked,
whether it can be part of this

FilterRowSet

object.
**Parameters:** column

- a

int

object that must match the
SQL index of a column in this

RowSet

object. This must
have been passed to

Predicate

as one of the columns
for filtering while initializing a

Predicate
**Returns:** true

if row value lies within the filter;

false

otherwise
**Throws:** SQLException

- if the column is not part of filtering criteria

- evaluate

```java
boolean evaluate​(
Object
value,

String
columnName)
throws
SQLException
```

This method is called by the

FilteredRowSet

object
to check whether the value lies between the filtering criteria set
using the setFilter method.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

**Parameters:** value

- An

Object

value which needs to be checked,
whether it can be part of this

FilterRowSet

.
**Parameters:** columnName

- a

String

object that must match the
SQL name of a column in this

RowSet

, ignoring case. This must
have been passed to

Predicate

as one of the columns for filtering
while initializing a

Predicate
**Returns:** true

if value lies within the filter;

false

otherwise
**Throws:** SQLException

- if the column is not part of filtering criteria

Method Detail

- evaluate

```java
boolean evaluate​(
RowSet
rs)
```

This method is typically called a

FilteredRowSet

object
internal methods (not public) that control the

RowSet

object's
cursor moving from row to the next. In addition, if this internal method
moves the cursor onto a row that has been deleted, the internal method will
continue to ove the cursor until a valid row is found.

**Parameters:** rs

- The

RowSet

to be evaluated
**Returns:** true

if there are more rows in the filter;

false

otherwise

- evaluate

```java
boolean evaluate​(
Object
value,
int column)
throws
SQLException
```

This method is called by a

FilteredRowSet

object
to check whether the value lies between the filtering criterion (or criteria
if multiple constraints exist) set using the

setFilter()

method.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

**Parameters:** value

- An

Object

value which needs to be checked,
whether it can be part of this

FilterRowSet

object.
**Parameters:** column

- a

int

object that must match the
SQL index of a column in this

RowSet

object. This must
have been passed to

Predicate

as one of the columns
for filtering while initializing a

Predicate
**Returns:** true

if row value lies within the filter;

false

otherwise
**Throws:** SQLException

- if the column is not part of filtering criteria

- evaluate

```java
boolean evaluate​(
Object
value,

String
columnName)
throws
SQLException
```

This method is called by the

FilteredRowSet

object
to check whether the value lies between the filtering criteria set
using the setFilter method.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

**Parameters:** value

- An

Object

value which needs to be checked,
whether it can be part of this

FilterRowSet

.
**Parameters:** columnName

- a

String

object that must match the
SQL name of a column in this

RowSet

, ignoring case. This must
have been passed to

Predicate

as one of the columns for filtering
while initializing a

Predicate
**Returns:** true

if value lies within the filter;

false

otherwise
**Throws:** SQLException

- if the column is not part of filtering criteria

---

#### Method Detail

evaluate

```java
boolean evaluate​(
RowSet
rs)
```

This method is typically called a

FilteredRowSet

object
internal methods (not public) that control the

RowSet

object's
cursor moving from row to the next. In addition, if this internal method
moves the cursor onto a row that has been deleted, the internal method will
continue to ove the cursor until a valid row is found.

**Parameters:** rs

- The

RowSet

to be evaluated
**Returns:** true

if there are more rows in the filter;

false

otherwise

---

#### evaluate

boolean evaluate​(

RowSet

rs)

This method is typically called a

FilteredRowSet

object
internal methods (not public) that control the

RowSet

object's
cursor moving from row to the next. In addition, if this internal method
moves the cursor onto a row that has been deleted, the internal method will
continue to ove the cursor until a valid row is found.

evaluate

```java
boolean evaluate​(
Object
value,
int column)
throws
SQLException
```

This method is called by a

FilteredRowSet

object
to check whether the value lies between the filtering criterion (or criteria
if multiple constraints exist) set using the

setFilter()

method.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

**Parameters:** value

- An

Object

value which needs to be checked,
whether it can be part of this

FilterRowSet

object.
**Parameters:** column

- a

int

object that must match the
SQL index of a column in this

RowSet

object. This must
have been passed to

Predicate

as one of the columns
for filtering while initializing a

Predicate
**Returns:** true

if row value lies within the filter;

false

otherwise
**Throws:** SQLException

- if the column is not part of filtering criteria

---

#### evaluate

boolean evaluate​(

Object

value,
int column)
throws

SQLException

This method is called by a

FilteredRowSet

object
to check whether the value lies between the filtering criterion (or criteria
if multiple constraints exist) set using the

setFilter()

method.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

evaluate

```java
boolean evaluate​(
Object
value,

String
columnName)
throws
SQLException
```

This method is called by the

FilteredRowSet

object
to check whether the value lies between the filtering criteria set
using the setFilter method.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

**Parameters:** value

- An

Object

value which needs to be checked,
whether it can be part of this

FilterRowSet

.
**Parameters:** columnName

- a

String

object that must match the
SQL name of a column in this

RowSet

, ignoring case. This must
have been passed to

Predicate

as one of the columns for filtering
while initializing a

Predicate
**Returns:** true

if value lies within the filter;

false

otherwise
**Throws:** SQLException

- if the column is not part of filtering criteria

---

#### evaluate

boolean evaluate​(

Object

value,

String

columnName)
throws

SQLException

This method is called by the

FilteredRowSet

object
to check whether the value lies between the filtering criteria set
using the setFilter method.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

The

FilteredRowSet

object will use this method internally
while inserting new rows to a

FilteredRowSet

instance.

---

