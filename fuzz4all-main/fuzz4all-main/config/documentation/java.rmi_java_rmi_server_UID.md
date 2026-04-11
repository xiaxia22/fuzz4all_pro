# Class UID

**Source:** `java.rmi\java\rmi\server\UID.html`

### Class Description

```java
public final class
UID

extends
Object

implements
Serializable
```

A

UID

represents an identifier that is unique over time
with respect to the host it is generated on, or one of 2

16

"well-known" identifiers.

The

UID()

constructor can be used to generate an
identifier that is unique over time with respect to the host it is
generated on. The

UID(short)

constructor can be used to
create one of 2

16

well-known identifiers.

A

UID

instance contains three primitive values:

- unique

, an

int

that uniquely identifies
the VM that this

UID

was generated in, with respect to its
host and at the time represented by the

time

value (an
example implementation of the

unique

value would be a
process identifier),
or zero for a well-known

UID

time

, a

long

equal to a time (as returned
by

System.currentTimeMillis()

) at which the VM that this

UID

was generated in was alive,
or zero for a well-known

UID

count

, a

short

to distinguish

UID

s generated in the same VM with the same

time

value

An independently generated

UID

instance is unique
over time with respect to the host it is generated on as long as
the host requires more than one millisecond to reboot and its system
clock is never set backward. A globally unique identifier can be
constructed by pairing a

UID

instance with a unique host
identifier, such as an IP address.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UID()

Generates a

UID

that is unique over time with
respect to the host that it was generated on.

---

#### public UID​(short num)

Creates a "well-known"

UID

.

There are 2

16

possible such well-known ids.

A

UID

created via this constructor will not
clash with any

UID

s generated via the no-arg
constructor.

**Parameters:**
- num

- number for well-known

UID

---

### Method Details

#### public int hashCode()

Returns the hash code value for this

UID

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

UID

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
obj)

Compares the specified object with this

UID

for
equality.

This method returns

true

if and only if the
specified object is a

UID

instance with the same

unique

,

time

, and

count

values as this one.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to compare this

UID

to

**Returns:**
- true

if the given object is equivalent to
this one, and

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns a string representation of this

UID

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

UID

---

#### public void write​(
DataOutput
out)
throws
IOException

Marshals a binary representation of this

UID

to
a

DataOutput

instance.

Specifically, this method first invokes the given stream's

DataOutput.writeInt(int)

method with this

UID

's

unique

value, then it invokes the stream's

DataOutput.writeLong(long)

method with this

UID

's

time

value, and then it invokes the stream's

DataOutput.writeShort(int)

method with this

UID

's

count

value.

**Parameters:**
- out

- the

DataOutput

instance to write
this

UID

to

**Throws:**
- IOException

- if an I/O error occurs while performing
this operation

---

#### public static
UID
read​(
DataInput
in)
throws
IOException

Constructs and returns a new

UID

instance by
unmarshalling a binary representation from an

DataInput

instance.

Specifically, this method first invokes the given stream's

DataInput.readInt()

method to read a

unique

value,
then it invoke's the stream's

DataInput.readLong()

method to read a

time

value,
then it invoke's the stream's

DataInput.readShort()

method to read a

count

value,
and then it creates and returns a new

UID

instance
that contains the

unique

,

time

, and

count

values that were read from the stream.

**Parameters:**
- in

- the

DataInput

instance to read

UID

from

**Returns:**
- unmarshalled

UID

instance

**Throws:**
- IOException

- if an I/O error occurs while performing
this operation

---

### Additional Sections

#### Class UID

java.lang.Object

- java.rmi.server.UID

java.rmi.server.UID

**All Implemented Interfaces:** Serializable

```java
public final class
UID

extends
Object

implements
Serializable
```

A

UID

represents an identifier that is unique over time
with respect to the host it is generated on, or one of 2

16

"well-known" identifiers.

The

UID()

constructor can be used to generate an
identifier that is unique over time with respect to the host it is
generated on. The

UID(short)

constructor can be used to
create one of 2

16

well-known identifiers.

A

UID

instance contains three primitive values:

- unique

, an

int

that uniquely identifies
the VM that this

UID

was generated in, with respect to its
host and at the time represented by the

time

value (an
example implementation of the

unique

value would be a
process identifier),
or zero for a well-known

UID

time

, a

long

equal to a time (as returned
by

System.currentTimeMillis()

) at which the VM that this

UID

was generated in was alive,
or zero for a well-known

UID

count

, a

short

to distinguish

UID

s generated in the same VM with the same

time

value

An independently generated

UID

instance is unique
over time with respect to the host it is generated on as long as
the host requires more than one millisecond to reboot and its system
clock is never set backward. A globally unique identifier can be
constructed by pairing a

UID

instance with a unique host
identifier, such as an IP address.

**Since:** 1.1
**See Also:** Serialized Form

public final class

UID

extends

Object

implements

Serializable

A

UID

represents an identifier that is unique over time
with respect to the host it is generated on, or one of 2

16

"well-known" identifiers.

The

UID()

constructor can be used to generate an
identifier that is unique over time with respect to the host it is
generated on. The

UID(short)

constructor can be used to
create one of 2

16

well-known identifiers.

A

UID

instance contains three primitive values:

- unique

, an

int

that uniquely identifies
the VM that this

UID

was generated in, with respect to its
host and at the time represented by the

time

value (an
example implementation of the

unique

value would be a
process identifier),
or zero for a well-known

UID

time

, a

long

equal to a time (as returned
by

System.currentTimeMillis()

) at which the VM that this

UID

was generated in was alive,
or zero for a well-known

UID

count

, a

short

to distinguish

UID

s generated in the same VM with the same

time

value

An independently generated

UID

instance is unique
over time with respect to the host it is generated on as long as
the host requires more than one millisecond to reboot and its system
clock is never set backward. A globally unique identifier can be
constructed by pairing a

UID

instance with a unique host
identifier, such as an IP address.

The

UID()

constructor can be used to generate an
identifier that is unique over time with respect to the host it is
generated on. The

UID(short)

constructor can be used to
create one of 2

16

well-known identifiers.

A

UID

instance contains three primitive values:

- unique

, an

int

that uniquely identifies
the VM that this

UID

was generated in, with respect to its
host and at the time represented by the

time

value (an
example implementation of the

unique

value would be a
process identifier),
or zero for a well-known

UID

time

, a

long

equal to a time (as returned
by

System.currentTimeMillis()

) at which the VM that this

UID

was generated in was alive,
or zero for a well-known

UID

count

, a

short

to distinguish

UID

s generated in the same VM with the same

time

value

An independently generated

UID

instance is unique
over time with respect to the host it is generated on as long as
the host requires more than one millisecond to reboot and its system
clock is never set backward. A globally unique identifier can be
constructed by pairing a

UID

instance with a unique host
identifier, such as an IP address.

A

UID

instance contains three primitive values:

- unique

, an

int

that uniquely identifies
the VM that this

UID

was generated in, with respect to its
host and at the time represented by the

time

value (an
example implementation of the

unique

value would be a
process identifier),
or zero for a well-known

UID

time

, a

long

equal to a time (as returned
by

System.currentTimeMillis()

) at which the VM that this

UID

was generated in was alive,
or zero for a well-known

UID

count

, a

short

to distinguish

UID

s generated in the same VM with the same

time

value

An independently generated

UID

instance is unique
over time with respect to the host it is generated on as long as
the host requires more than one millisecond to reboot and its system
clock is never set backward. A globally unique identifier can be
constructed by pairing a

UID

instance with a unique host
identifier, such as an IP address.

unique

, an

int

that uniquely identifies
the VM that this

UID

was generated in, with respect to its
host and at the time represented by the

time

value (an
example implementation of the

unique

value would be a
process identifier),
or zero for a well-known

UID

time

, a

long

equal to a time (as returned
by

System.currentTimeMillis()

) at which the VM that this

UID

was generated in was alive,
or zero for a well-known

UID

count

, a

short

to distinguish

UID

s generated in the same VM with the same

time

value

An independently generated

UID

instance is unique
over time with respect to the host it is generated on as long as
the host requires more than one millisecond to reboot and its system
clock is never set backward. A globally unique identifier can be
constructed by pairing a

UID

instance with a unique host
identifier, such as an IP address.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UID

()

Generates a

UID

that is unique over time with
respect to the host that it was generated on.

UID

​(short num)

Creates a "well-known"

UID

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

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

Compares the specified object with this

UID

for
equality.

int

hashCode

()

Returns the hash code value for this

UID

.

static

UID

read

​(

DataInput

in)

Constructs and returns a new

UID

instance by
unmarshalling a binary representation from an

DataInput

instance.

String

toString

()

Returns a string representation of this

UID

.

void

write

​(

DataOutput

out)

Marshals a binary representation of this

UID

to
a

DataOutput

instance.

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

UID

()

Generates a

UID

that is unique over time with
respect to the host that it was generated on.

UID

​(short num)

Creates a "well-known"

UID

.

---

#### Constructor Summary

Generates a

UID

that is unique over time with
respect to the host that it was generated on.

Creates a "well-known"

UID

.

Method Summary

All Methods

Static Methods

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

Compares the specified object with this

UID

for
equality.

int

hashCode

()

Returns the hash code value for this

UID

.

static

UID

read

​(

DataInput

in)

Constructs and returns a new

UID

instance by
unmarshalling a binary representation from an

DataInput

instance.

String

toString

()

Returns a string representation of this

UID

.

void

write

​(

DataOutput

out)

Marshals a binary representation of this

UID

to
a

DataOutput

instance.

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

Compares the specified object with this

UID

for
equality.

Returns the hash code value for this

UID

.

Constructs and returns a new

UID

instance by
unmarshalling a binary representation from an

DataInput

instance.

Returns a string representation of this

UID

.

Marshals a binary representation of this

UID

to
a

DataOutput

instance.

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

- UID

```java
public UID()
```

Generates a

UID

that is unique over time with
respect to the host that it was generated on.

- UID

```java
public UID​(short num)
```

Creates a "well-known"

UID

.

There are 2

16

possible such well-known ids.

A

UID

created via this constructor will not
clash with any

UID

s generated via the no-arg
constructor.

**Parameters:** num

- number for well-known

UID

============ METHOD DETAIL ==========

- Method Detail

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

UID

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

UID
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this

UID

for
equality.

This method returns

true

if and only if the
specified object is a

UID

instance with the same

unique

,

time

, and

count

values as this one.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this

UID

to
**Returns:** true

if the given object is equivalent to
this one, and

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string representation of this

UID

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UID

- write

```java
public void write​(
DataOutput
out)
throws
IOException
```

Marshals a binary representation of this

UID

to
a

DataOutput

instance.

Specifically, this method first invokes the given stream's

DataOutput.writeInt(int)

method with this

UID

's

unique

value, then it invokes the stream's

DataOutput.writeLong(long)

method with this

UID

's

time

value, and then it invokes the stream's

DataOutput.writeShort(int)

method with this

UID

's

count

value.

**Parameters:** out

- the

DataOutput

instance to write
this

UID

to
**Throws:** IOException

- if an I/O error occurs while performing
this operation

- read

```java
public static
UID
read​(
DataInput
in)
throws
IOException
```

Constructs and returns a new

UID

instance by
unmarshalling a binary representation from an

DataInput

instance.

Specifically, this method first invokes the given stream's

DataInput.readInt()

method to read a

unique

value,
then it invoke's the stream's

DataInput.readLong()

method to read a

time

value,
then it invoke's the stream's

DataInput.readShort()

method to read a

count

value,
and then it creates and returns a new

UID

instance
that contains the

unique

,

time

, and

count

values that were read from the stream.

**Parameters:** in

- the

DataInput

instance to read

UID

from
**Returns:** unmarshalled

UID

instance
**Throws:** IOException

- if an I/O error occurs while performing
this operation

Constructor Detail

- UID

```java
public UID()
```

Generates a

UID

that is unique over time with
respect to the host that it was generated on.

- UID

```java
public UID​(short num)
```

Creates a "well-known"

UID

.

There are 2

16

possible such well-known ids.

A

UID

created via this constructor will not
clash with any

UID

s generated via the no-arg
constructor.

**Parameters:** num

- number for well-known

UID

---

#### Constructor Detail

UID

```java
public UID()
```

Generates a

UID

that is unique over time with
respect to the host that it was generated on.

---

#### UID

public UID()

Generates a

UID

that is unique over time with
respect to the host that it was generated on.

UID

```java
public UID​(short num)
```

Creates a "well-known"

UID

.

There are 2

16

possible such well-known ids.

A

UID

created via this constructor will not
clash with any

UID

s generated via the no-arg
constructor.

**Parameters:** num

- number for well-known

UID

---

#### UID

public UID​(short num)

Creates a "well-known"

UID

.

There are 2

16

possible such well-known ids.

A

UID

created via this constructor will not
clash with any

UID

s generated via the no-arg
constructor.

A

UID

created via this constructor will not
clash with any

UID

s generated via the no-arg
constructor.

Method Detail

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

UID

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

UID
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this

UID

for
equality.

This method returns

true

if and only if the
specified object is a

UID

instance with the same

unique

,

time

, and

count

values as this one.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this

UID

to
**Returns:** true

if the given object is equivalent to
this one, and

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string representation of this

UID

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UID

- write

```java
public void write​(
DataOutput
out)
throws
IOException
```

Marshals a binary representation of this

UID

to
a

DataOutput

instance.

Specifically, this method first invokes the given stream's

DataOutput.writeInt(int)

method with this

UID

's

unique

value, then it invokes the stream's

DataOutput.writeLong(long)

method with this

UID

's

time

value, and then it invokes the stream's

DataOutput.writeShort(int)

method with this

UID

's

count

value.

**Parameters:** out

- the

DataOutput

instance to write
this

UID

to
**Throws:** IOException

- if an I/O error occurs while performing
this operation

- read

```java
public static
UID
read​(
DataInput
in)
throws
IOException
```

Constructs and returns a new

UID

instance by
unmarshalling a binary representation from an

DataInput

instance.

Specifically, this method first invokes the given stream's

DataInput.readInt()

method to read a

unique

value,
then it invoke's the stream's

DataInput.readLong()

method to read a

time

value,
then it invoke's the stream's

DataInput.readShort()

method to read a

count

value,
and then it creates and returns a new

UID

instance
that contains the

unique

,

time

, and

count

values that were read from the stream.

**Parameters:** in

- the

DataInput

instance to read

UID

from
**Returns:** unmarshalled

UID

instance
**Throws:** IOException

- if an I/O error occurs while performing
this operation

---

#### Method Detail

hashCode

```java
public int hashCode()
```

Returns the hash code value for this

UID

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

UID
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this

UID

.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this

UID

for
equality.

This method returns

true

if and only if the
specified object is a

UID

instance with the same

unique

,

time

, and

count

values as this one.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this

UID

to
**Returns:** true

if the given object is equivalent to
this one, and

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares the specified object with this

UID

for
equality.

This method returns

true

if and only if the
specified object is a

UID

instance with the same

unique

,

time

, and

count

values as this one.

toString

```java
public
String
toString()
```

Returns a string representation of this

UID

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UID

---

#### toString

public

String

toString()

Returns a string representation of this

UID

.

write

```java
public void write​(
DataOutput
out)
throws
IOException
```

Marshals a binary representation of this

UID

to
a

DataOutput

instance.

Specifically, this method first invokes the given stream's

DataOutput.writeInt(int)

method with this

UID

's

unique

value, then it invokes the stream's

DataOutput.writeLong(long)

method with this

UID

's

time

value, and then it invokes the stream's

DataOutput.writeShort(int)

method with this

UID

's

count

value.

**Parameters:** out

- the

DataOutput

instance to write
this

UID

to
**Throws:** IOException

- if an I/O error occurs while performing
this operation

---

#### write

public void write​(

DataOutput

out)
throws

IOException

Marshals a binary representation of this

UID

to
a

DataOutput

instance.

Specifically, this method first invokes the given stream's

DataOutput.writeInt(int)

method with this

UID

's

unique

value, then it invokes the stream's

DataOutput.writeLong(long)

method with this

UID

's

time

value, and then it invokes the stream's

DataOutput.writeShort(int)

method with this

UID

's

count

value.

Specifically, this method first invokes the given stream's

DataOutput.writeInt(int)

method with this

UID

's

unique

value, then it invokes the stream's

DataOutput.writeLong(long)

method with this

UID

's

time

value, and then it invokes the stream's

DataOutput.writeShort(int)

method with this

UID

's

count

value.

read

```java
public static
UID
read​(
DataInput
in)
throws
IOException
```

Constructs and returns a new

UID

instance by
unmarshalling a binary representation from an

DataInput

instance.

Specifically, this method first invokes the given stream's

DataInput.readInt()

method to read a

unique

value,
then it invoke's the stream's

DataInput.readLong()

method to read a

time

value,
then it invoke's the stream's

DataInput.readShort()

method to read a

count

value,
and then it creates and returns a new

UID

instance
that contains the

unique

,

time

, and

count

values that were read from the stream.

**Parameters:** in

- the

DataInput

instance to read

UID

from
**Returns:** unmarshalled

UID

instance
**Throws:** IOException

- if an I/O error occurs while performing
this operation

---

#### read

public static

UID

read​(

DataInput

in)
throws

IOException

Constructs and returns a new

UID

instance by
unmarshalling a binary representation from an

DataInput

instance.

Specifically, this method first invokes the given stream's

DataInput.readInt()

method to read a

unique

value,
then it invoke's the stream's

DataInput.readLong()

method to read a

time

value,
then it invoke's the stream's

DataInput.readShort()

method to read a

count

value,
and then it creates and returns a new

UID

instance
that contains the

unique

,

time

, and

count

values that were read from the stream.

Specifically, this method first invokes the given stream's

DataInput.readInt()

method to read a

unique

value,
then it invoke's the stream's

DataInput.readLong()

method to read a

time

value,
then it invoke's the stream's

DataInput.readShort()

method to read a

count

value,
and then it creates and returns a new

UID

instance
that contains the

unique

,

time

, and

count

values that were read from the stream.

---

