# Class FieldPosition

**Source:** `java.base\java\text\FieldPosition.html`

### Class Description

```java
public class
FieldPosition

extends
Object
```

FieldPosition

is a simple class used by

Format

and its subclasses to identify fields in formatted output. Fields can
be identified in two ways:

- By an integer constant, whose names typically end with

_FIELD

. The constants are defined in the various
subclasses of

Format

.

By a

Format.Field

constant, see

ERA_FIELD

and its friends in

DateFormat

for an example.

FieldPosition

keeps track of the position of the
field within the formatted output with two indices: the index
of the first character of the field and the index of the last
character of the field.

One version of the

format

method in the various

Format

classes requires a

FieldPosition

object as an argument. You use this

format

method
to perform partial formatting or to get information about the
formatted output (such as the position of a field).

If you are interested in the positions of all attributes in the
formatted string use the

Format

method

formatToCharacterIterator

.

**Since:** 1.1
**See Also:** Format

---

### Field Details

*No entries found.*

### Constructor Details

#### public FieldPosition​(int field)

Creates a FieldPosition object for the given field. Fields are
identified by constants, whose names typically end with _FIELD,
in the various subclasses of Format.

**Parameters:**
- field

- the field identifier

**See Also:**
- NumberFormat.INTEGER_FIELD

,

NumberFormat.FRACTION_FIELD

,

DateFormat.YEAR_FIELD

,

DateFormat.MONTH_FIELD

---

#### public FieldPosition​(
Format.Field
attribute)

Creates a FieldPosition object for the given field constant. Fields are
identified by constants defined in the various

Format

subclasses. This is equivalent to calling

new FieldPosition(attribute, -1)

.

**Parameters:**
- attribute

- Format.Field constant identifying a field

**Since:**
- 1.4

---

#### public FieldPosition​(
Format.Field
attribute,
int fieldID)

Creates a

FieldPosition

object for the given field.
The field is identified by an attribute constant from one of the

Field

subclasses as well as an integer field ID
defined by the

Format

subclasses.

Format

subclasses that are aware of

Field

should give precedence
to

attribute

and ignore

fieldID

if

attribute

is not null. However, older

Format

subclasses may not be aware of

Field

and rely on

fieldID

. If the field has no corresponding integer
constant,

fieldID

should be -1.

**Parameters:**
- attribute

- Format.Field constant identifying a field
- fieldID

- integer constant identifying a field

**Since:**
- 1.4

---

### Method Details

#### public
Format.Field
getFieldAttribute()

Returns the field identifier as an attribute constant
from one of the

Field

subclasses. May return null if
the field is specified only by an integer field ID.

**Returns:**
- Identifier for the field

**Since:**
- 1.4

---

#### public int getField()

Retrieves the field identifier.

**Returns:**
- the field identifier

---

#### public int getBeginIndex()

Retrieves the index of the first character in the requested field.

**Returns:**
- the begin index

---

#### public int getEndIndex()

Retrieves the index of the character following the last character in the
requested field.

**Returns:**
- the end index

---

#### public void setBeginIndex​(int bi)

Sets the begin index. For use by subclasses of Format.

**Parameters:**
- bi

- the begin index

**Since:**
- 1.2

---

#### public void setEndIndex​(int ei)

Sets the end index. For use by subclasses of Format.

**Parameters:**
- ei

- the end index

**Since:**
- 1.2

---

#### public boolean equals​(
Object
obj)

Overrides equals

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code for this FieldPosition.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Return a string representation of this FieldPosition.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this object

---

### Additional Sections

#### Class FieldPosition

java.lang.Object

- java.text.FieldPosition

java.text.FieldPosition

```java
public class
FieldPosition

extends
Object
```

FieldPosition

is a simple class used by

Format

and its subclasses to identify fields in formatted output. Fields can
be identified in two ways:

- By an integer constant, whose names typically end with

_FIELD

. The constants are defined in the various
subclasses of

Format

.

By a

Format.Field

constant, see

ERA_FIELD

and its friends in

DateFormat

for an example.

FieldPosition

keeps track of the position of the
field within the formatted output with two indices: the index
of the first character of the field and the index of the last
character of the field.

One version of the

format

method in the various

Format

classes requires a

FieldPosition

object as an argument. You use this

format

method
to perform partial formatting or to get information about the
formatted output (such as the position of a field).

If you are interested in the positions of all attributes in the
formatted string use the

Format

method

formatToCharacterIterator

.

**Since:** 1.1
**See Also:** Format

public class

FieldPosition

extends

Object

FieldPosition

is a simple class used by

Format

and its subclasses to identify fields in formatted output. Fields can
be identified in two ways:

- By an integer constant, whose names typically end with

_FIELD

. The constants are defined in the various
subclasses of

Format

.

By a

Format.Field

constant, see

ERA_FIELD

and its friends in

DateFormat

for an example.

FieldPosition

keeps track of the position of the
field within the formatted output with two indices: the index
of the first character of the field and the index of the last
character of the field.

One version of the

format

method in the various

Format

classes requires a

FieldPosition

object as an argument. You use this

format

method
to perform partial formatting or to get information about the
formatted output (such as the position of a field).

If you are interested in the positions of all attributes in the
formatted string use the

Format

method

formatToCharacterIterator

.

By an integer constant, whose names typically end with

_FIELD

. The constants are defined in the various
subclasses of

Format

.

By a

Format.Field

constant, see

ERA_FIELD

and its friends in

DateFormat

for an example.

FieldPosition

keeps track of the position of the
field within the formatted output with two indices: the index
of the first character of the field and the index of the last
character of the field.

One version of the

format

method in the various

Format

classes requires a

FieldPosition

object as an argument. You use this

format

method
to perform partial formatting or to get information about the
formatted output (such as the position of a field).

If you are interested in the positions of all attributes in the
formatted string use the

Format

method

formatToCharacterIterator

.

One version of the

format

method in the various

Format

classes requires a

FieldPosition

object as an argument. You use this

format

method
to perform partial formatting or to get information about the
formatted output (such as the position of a field).

If you are interested in the positions of all attributes in the
formatted string use the

Format

method

formatToCharacterIterator

.

If you are interested in the positions of all attributes in the
formatted string use the

Format

method

formatToCharacterIterator

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FieldPosition

​(int field)

Creates a FieldPosition object for the given field.

FieldPosition

​(

Format.Field

attribute)

Creates a FieldPosition object for the given field constant.

FieldPosition

​(

Format.Field

attribute,
int fieldID)

Creates a

FieldPosition

object for the given field.

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

obj)

Overrides equals

int

getBeginIndex

()

Retrieves the index of the first character in the requested field.

int

getEndIndex

()

Retrieves the index of the character following the last character in the
requested field.

int

getField

()

Retrieves the field identifier.

Format.Field

getFieldAttribute

()

Returns the field identifier as an attribute constant
from one of the

Field

subclasses.

int

hashCode

()

Returns a hash code for this FieldPosition.

void

setBeginIndex

​(int bi)

Sets the begin index.

void

setEndIndex

​(int ei)

Sets the end index.

String

toString

()

Return a string representation of this FieldPosition.

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

FieldPosition

​(int field)

Creates a FieldPosition object for the given field.

FieldPosition

​(

Format.Field

attribute)

Creates a FieldPosition object for the given field constant.

FieldPosition

​(

Format.Field

attribute,
int fieldID)

Creates a

FieldPosition

object for the given field.

---

#### Constructor Summary

Creates a FieldPosition object for the given field.

Creates a FieldPosition object for the given field constant.

Creates a

FieldPosition

object for the given field.

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

obj)

Overrides equals

int

getBeginIndex

()

Retrieves the index of the first character in the requested field.

int

getEndIndex

()

Retrieves the index of the character following the last character in the
requested field.

int

getField

()

Retrieves the field identifier.

Format.Field

getFieldAttribute

()

Returns the field identifier as an attribute constant
from one of the

Field

subclasses.

int

hashCode

()

Returns a hash code for this FieldPosition.

void

setBeginIndex

​(int bi)

Sets the begin index.

void

setEndIndex

​(int ei)

Sets the end index.

String

toString

()

Return a string representation of this FieldPosition.

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

Overrides equals

Retrieves the index of the first character in the requested field.

Retrieves the index of the character following the last character in the
requested field.

Retrieves the field identifier.

Returns the field identifier as an attribute constant
from one of the

Field

subclasses.

Returns a hash code for this FieldPosition.

Sets the begin index.

Sets the end index.

Return a string representation of this FieldPosition.

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

- FieldPosition

```java
public FieldPosition​(int field)
```

Creates a FieldPosition object for the given field. Fields are
identified by constants, whose names typically end with _FIELD,
in the various subclasses of Format.

**Parameters:** field

- the field identifier
**See Also:** NumberFormat.INTEGER_FIELD

,

NumberFormat.FRACTION_FIELD

,

DateFormat.YEAR_FIELD

,

DateFormat.MONTH_FIELD

- FieldPosition

```java
public FieldPosition​(
Format.Field
attribute)
```

Creates a FieldPosition object for the given field constant. Fields are
identified by constants defined in the various

Format

subclasses. This is equivalent to calling

new FieldPosition(attribute, -1)

.

**Parameters:** attribute

- Format.Field constant identifying a field
**Since:** 1.4

- FieldPosition

```java
public FieldPosition​(
Format.Field
attribute,
int fieldID)
```

Creates a

FieldPosition

object for the given field.
The field is identified by an attribute constant from one of the

Field

subclasses as well as an integer field ID
defined by the

Format

subclasses.

Format

subclasses that are aware of

Field

should give precedence
to

attribute

and ignore

fieldID

if

attribute

is not null. However, older

Format

subclasses may not be aware of

Field

and rely on

fieldID

. If the field has no corresponding integer
constant,

fieldID

should be -1.

**Parameters:** attribute

- Format.Field constant identifying a field
**Parameters:** fieldID

- integer constant identifying a field
**Since:** 1.4

============ METHOD DETAIL ==========

- Method Detail

- getFieldAttribute

```java
public
Format.Field
getFieldAttribute()
```

Returns the field identifier as an attribute constant
from one of the

Field

subclasses. May return null if
the field is specified only by an integer field ID.

**Returns:** Identifier for the field
**Since:** 1.4

- getField

```java
public int getField()
```

Retrieves the field identifier.

**Returns:** the field identifier

- getBeginIndex

```java
public int getBeginIndex()
```

Retrieves the index of the first character in the requested field.

**Returns:** the begin index

- getEndIndex

```java
public int getEndIndex()
```

Retrieves the index of the character following the last character in the
requested field.

**Returns:** the end index

- setBeginIndex

```java
public void setBeginIndex​(int bi)
```

Sets the begin index. For use by subclasses of Format.

**Parameters:** bi

- the begin index
**Since:** 1.2

- setEndIndex

```java
public void setEndIndex​(int ei)
```

Sets the end index. For use by subclasses of Format.

**Parameters:** ei

- the end index
**Since:** 1.2

- equals

```java
public boolean equals​(
Object
obj)
```

Overrides equals

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this FieldPosition.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Return a string representation of this FieldPosition.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object

Constructor Detail

- FieldPosition

```java
public FieldPosition​(int field)
```

Creates a FieldPosition object for the given field. Fields are
identified by constants, whose names typically end with _FIELD,
in the various subclasses of Format.

**Parameters:** field

- the field identifier
**See Also:** NumberFormat.INTEGER_FIELD

,

NumberFormat.FRACTION_FIELD

,

DateFormat.YEAR_FIELD

,

DateFormat.MONTH_FIELD

- FieldPosition

```java
public FieldPosition​(
Format.Field
attribute)
```

Creates a FieldPosition object for the given field constant. Fields are
identified by constants defined in the various

Format

subclasses. This is equivalent to calling

new FieldPosition(attribute, -1)

.

**Parameters:** attribute

- Format.Field constant identifying a field
**Since:** 1.4

- FieldPosition

```java
public FieldPosition​(
Format.Field
attribute,
int fieldID)
```

Creates a

FieldPosition

object for the given field.
The field is identified by an attribute constant from one of the

Field

subclasses as well as an integer field ID
defined by the

Format

subclasses.

Format

subclasses that are aware of

Field

should give precedence
to

attribute

and ignore

fieldID

if

attribute

is not null. However, older

Format

subclasses may not be aware of

Field

and rely on

fieldID

. If the field has no corresponding integer
constant,

fieldID

should be -1.

**Parameters:** attribute

- Format.Field constant identifying a field
**Parameters:** fieldID

- integer constant identifying a field
**Since:** 1.4

---

#### Constructor Detail

FieldPosition

```java
public FieldPosition​(int field)
```

Creates a FieldPosition object for the given field. Fields are
identified by constants, whose names typically end with _FIELD,
in the various subclasses of Format.

**Parameters:** field

- the field identifier
**See Also:** NumberFormat.INTEGER_FIELD

,

NumberFormat.FRACTION_FIELD

,

DateFormat.YEAR_FIELD

,

DateFormat.MONTH_FIELD

---

#### FieldPosition

public FieldPosition​(int field)

Creates a FieldPosition object for the given field. Fields are
identified by constants, whose names typically end with _FIELD,
in the various subclasses of Format.

FieldPosition

```java
public FieldPosition​(
Format.Field
attribute)
```

Creates a FieldPosition object for the given field constant. Fields are
identified by constants defined in the various

Format

subclasses. This is equivalent to calling

new FieldPosition(attribute, -1)

.

**Parameters:** attribute

- Format.Field constant identifying a field
**Since:** 1.4

---

#### FieldPosition

public FieldPosition​(

Format.Field

attribute)

Creates a FieldPosition object for the given field constant. Fields are
identified by constants defined in the various

Format

subclasses. This is equivalent to calling

new FieldPosition(attribute, -1)

.

FieldPosition

```java
public FieldPosition​(
Format.Field
attribute,
int fieldID)
```

Creates a

FieldPosition

object for the given field.
The field is identified by an attribute constant from one of the

Field

subclasses as well as an integer field ID
defined by the

Format

subclasses.

Format

subclasses that are aware of

Field

should give precedence
to

attribute

and ignore

fieldID

if

attribute

is not null. However, older

Format

subclasses may not be aware of

Field

and rely on

fieldID

. If the field has no corresponding integer
constant,

fieldID

should be -1.

**Parameters:** attribute

- Format.Field constant identifying a field
**Parameters:** fieldID

- integer constant identifying a field
**Since:** 1.4

---

#### FieldPosition

public FieldPosition​(

Format.Field

attribute,
int fieldID)

Creates a

FieldPosition

object for the given field.
The field is identified by an attribute constant from one of the

Field

subclasses as well as an integer field ID
defined by the

Format

subclasses.

Format

subclasses that are aware of

Field

should give precedence
to

attribute

and ignore

fieldID

if

attribute

is not null. However, older

Format

subclasses may not be aware of

Field

and rely on

fieldID

. If the field has no corresponding integer
constant,

fieldID

should be -1.

Method Detail

- getFieldAttribute

```java
public
Format.Field
getFieldAttribute()
```

Returns the field identifier as an attribute constant
from one of the

Field

subclasses. May return null if
the field is specified only by an integer field ID.

**Returns:** Identifier for the field
**Since:** 1.4

- getField

```java
public int getField()
```

Retrieves the field identifier.

**Returns:** the field identifier

- getBeginIndex

```java
public int getBeginIndex()
```

Retrieves the index of the first character in the requested field.

**Returns:** the begin index

- getEndIndex

```java
public int getEndIndex()
```

Retrieves the index of the character following the last character in the
requested field.

**Returns:** the end index

- setBeginIndex

```java
public void setBeginIndex​(int bi)
```

Sets the begin index. For use by subclasses of Format.

**Parameters:** bi

- the begin index
**Since:** 1.2

- setEndIndex

```java
public void setEndIndex​(int ei)
```

Sets the end index. For use by subclasses of Format.

**Parameters:** ei

- the end index
**Since:** 1.2

- equals

```java
public boolean equals​(
Object
obj)
```

Overrides equals

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this FieldPosition.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Return a string representation of this FieldPosition.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object

---

#### Method Detail

getFieldAttribute

```java
public
Format.Field
getFieldAttribute()
```

Returns the field identifier as an attribute constant
from one of the

Field

subclasses. May return null if
the field is specified only by an integer field ID.

**Returns:** Identifier for the field
**Since:** 1.4

---

#### getFieldAttribute

public

Format.Field

getFieldAttribute()

Returns the field identifier as an attribute constant
from one of the

Field

subclasses. May return null if
the field is specified only by an integer field ID.

getField

```java
public int getField()
```

Retrieves the field identifier.

**Returns:** the field identifier

---

#### getField

public int getField()

Retrieves the field identifier.

getBeginIndex

```java
public int getBeginIndex()
```

Retrieves the index of the first character in the requested field.

**Returns:** the begin index

---

#### getBeginIndex

public int getBeginIndex()

Retrieves the index of the first character in the requested field.

getEndIndex

```java
public int getEndIndex()
```

Retrieves the index of the character following the last character in the
requested field.

**Returns:** the end index

---

#### getEndIndex

public int getEndIndex()

Retrieves the index of the character following the last character in the
requested field.

setBeginIndex

```java
public void setBeginIndex​(int bi)
```

Sets the begin index. For use by subclasses of Format.

**Parameters:** bi

- the begin index
**Since:** 1.2

---

#### setBeginIndex

public void setBeginIndex​(int bi)

Sets the begin index. For use by subclasses of Format.

setEndIndex

```java
public void setEndIndex​(int ei)
```

Sets the end index. For use by subclasses of Format.

**Parameters:** ei

- the end index
**Since:** 1.2

---

#### setEndIndex

public void setEndIndex​(int ei)

Sets the end index. For use by subclasses of Format.

equals

```java
public boolean equals​(
Object
obj)
```

Overrides equals

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Overrides equals

hashCode

```java
public int hashCode()
```

Returns a hash code for this FieldPosition.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code for this FieldPosition.

toString

```java
public
String
toString()
```

Return a string representation of this FieldPosition.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object

---

#### toString

public

String

toString()

Return a string representation of this FieldPosition.

---

