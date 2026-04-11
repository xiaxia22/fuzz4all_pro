# Class ParsePosition

**Source:** `java.base\java\text\ParsePosition.html`

### Class Description

```java
public class
ParsePosition

extends
Object
```

ParsePosition

is a simple class used by

Format

and its subclasses to keep track of the current position during parsing.
The

parseObject

method in the various

Format

classes requires a

ParsePosition

object as an argument.

By design, as you parse through a string with different formats,
you can use the same

ParsePosition

, since the index parameter
records the current position.

**Since:** 1.1
**See Also:** Format

---

### Field Details

*No entries found.*

### Constructor Details

#### public ParsePosition​(int index)

Create a new ParsePosition with the given initial index.

**Parameters:**
- index

- initial index

---

### Method Details

#### public int getIndex()

Retrieve the current parse position. On input to a parse method, this
is the index of the character at which parsing will begin; on output, it
is the index of the character following the last character parsed.

**Returns:**
- the current parse position

---

#### public void setIndex​(int index)

Set the current parse position.

**Parameters:**
- index

- the current parse position

---

#### public void setErrorIndex​(int ei)

Set the index at which a parse error occurred. Formatters
should set this before returning an error code from their
parseObject method. The default value is -1 if this is not set.

**Parameters:**
- ei

- the index at which an error occurred

**Since:**
- 1.2

---

#### public int getErrorIndex()

Retrieve the index at which an error occurred, or -1 if the
error index has not been set.

**Returns:**
- the index at which an error occurred

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

Returns a hash code for this ParsePosition.

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

Return a string representation of this ParsePosition.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this object

---

### Additional Sections

#### Class ParsePosition

java.lang.Object

- java.text.ParsePosition

java.text.ParsePosition

```java
public class
ParsePosition

extends
Object
```

ParsePosition

is a simple class used by

Format

and its subclasses to keep track of the current position during parsing.
The

parseObject

method in the various

Format

classes requires a

ParsePosition

object as an argument.

By design, as you parse through a string with different formats,
you can use the same

ParsePosition

, since the index parameter
records the current position.

**Since:** 1.1
**See Also:** Format

public class

ParsePosition

extends

Object

ParsePosition

is a simple class used by

Format

and its subclasses to keep track of the current position during parsing.
The

parseObject

method in the various

Format

classes requires a

ParsePosition

object as an argument.

By design, as you parse through a string with different formats,
you can use the same

ParsePosition

, since the index parameter
records the current position.

By design, as you parse through a string with different formats,
you can use the same

ParsePosition

, since the index parameter
records the current position.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ParsePosition

​(int index)

Create a new ParsePosition with the given initial index.

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

getErrorIndex

()

Retrieve the index at which an error occurred, or -1 if the
error index has not been set.

int

getIndex

()

Retrieve the current parse position.

int

hashCode

()

Returns a hash code for this ParsePosition.

void

setErrorIndex

​(int ei)

Set the index at which a parse error occurred.

void

setIndex

​(int index)

Set the current parse position.

String

toString

()

Return a string representation of this ParsePosition.

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

ParsePosition

​(int index)

Create a new ParsePosition with the given initial index.

---

#### Constructor Summary

Create a new ParsePosition with the given initial index.

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

getErrorIndex

()

Retrieve the index at which an error occurred, or -1 if the
error index has not been set.

int

getIndex

()

Retrieve the current parse position.

int

hashCode

()

Returns a hash code for this ParsePosition.

void

setErrorIndex

​(int ei)

Set the index at which a parse error occurred.

void

setIndex

​(int index)

Set the current parse position.

String

toString

()

Return a string representation of this ParsePosition.

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

Retrieve the index at which an error occurred, or -1 if the
error index has not been set.

Retrieve the current parse position.

Returns a hash code for this ParsePosition.

Set the index at which a parse error occurred.

Set the current parse position.

Return a string representation of this ParsePosition.

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

- ParsePosition

```java
public ParsePosition​(int index)
```

Create a new ParsePosition with the given initial index.

**Parameters:** index

- initial index

============ METHOD DETAIL ==========

- Method Detail

- getIndex

```java
public int getIndex()
```

Retrieve the current parse position. On input to a parse method, this
is the index of the character at which parsing will begin; on output, it
is the index of the character following the last character parsed.

**Returns:** the current parse position

- setIndex

```java
public void setIndex​(int index)
```

Set the current parse position.

**Parameters:** index

- the current parse position

- setErrorIndex

```java
public void setErrorIndex​(int ei)
```

Set the index at which a parse error occurred. Formatters
should set this before returning an error code from their
parseObject method. The default value is -1 if this is not set.

**Parameters:** ei

- the index at which an error occurred
**Since:** 1.2

- getErrorIndex

```java
public int getErrorIndex()
```

Retrieve the index at which an error occurred, or -1 if the
error index has not been set.

**Returns:** the index at which an error occurred
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

Returns a hash code for this ParsePosition.

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

Return a string representation of this ParsePosition.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object

Constructor Detail

- ParsePosition

```java
public ParsePosition​(int index)
```

Create a new ParsePosition with the given initial index.

**Parameters:** index

- initial index

---

#### Constructor Detail

ParsePosition

```java
public ParsePosition​(int index)
```

Create a new ParsePosition with the given initial index.

**Parameters:** index

- initial index

---

#### ParsePosition

public ParsePosition​(int index)

Create a new ParsePosition with the given initial index.

Method Detail

- getIndex

```java
public int getIndex()
```

Retrieve the current parse position. On input to a parse method, this
is the index of the character at which parsing will begin; on output, it
is the index of the character following the last character parsed.

**Returns:** the current parse position

- setIndex

```java
public void setIndex​(int index)
```

Set the current parse position.

**Parameters:** index

- the current parse position

- setErrorIndex

```java
public void setErrorIndex​(int ei)
```

Set the index at which a parse error occurred. Formatters
should set this before returning an error code from their
parseObject method. The default value is -1 if this is not set.

**Parameters:** ei

- the index at which an error occurred
**Since:** 1.2

- getErrorIndex

```java
public int getErrorIndex()
```

Retrieve the index at which an error occurred, or -1 if the
error index has not been set.

**Returns:** the index at which an error occurred
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

Returns a hash code for this ParsePosition.

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

Return a string representation of this ParsePosition.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object

---

#### Method Detail

getIndex

```java
public int getIndex()
```

Retrieve the current parse position. On input to a parse method, this
is the index of the character at which parsing will begin; on output, it
is the index of the character following the last character parsed.

**Returns:** the current parse position

---

#### getIndex

public int getIndex()

Retrieve the current parse position. On input to a parse method, this
is the index of the character at which parsing will begin; on output, it
is the index of the character following the last character parsed.

setIndex

```java
public void setIndex​(int index)
```

Set the current parse position.

**Parameters:** index

- the current parse position

---

#### setIndex

public void setIndex​(int index)

Set the current parse position.

setErrorIndex

```java
public void setErrorIndex​(int ei)
```

Set the index at which a parse error occurred. Formatters
should set this before returning an error code from their
parseObject method. The default value is -1 if this is not set.

**Parameters:** ei

- the index at which an error occurred
**Since:** 1.2

---

#### setErrorIndex

public void setErrorIndex​(int ei)

Set the index at which a parse error occurred. Formatters
should set this before returning an error code from their
parseObject method. The default value is -1 if this is not set.

getErrorIndex

```java
public int getErrorIndex()
```

Retrieve the index at which an error occurred, or -1 if the
error index has not been set.

**Returns:** the index at which an error occurred
**Since:** 1.2

---

#### getErrorIndex

public int getErrorIndex()

Retrieve the index at which an error occurred, or -1 if the
error index has not been set.

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

Returns a hash code for this ParsePosition.

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

Returns a hash code for this ParsePosition.

toString

```java
public
String
toString()
```

Return a string representation of this ParsePosition.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object

---

#### toString

public

String

toString()

Return a string representation of this ParsePosition.

---

