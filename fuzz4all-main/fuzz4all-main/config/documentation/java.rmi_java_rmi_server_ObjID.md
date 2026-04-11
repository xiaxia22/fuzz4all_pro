# Class ObjID

**Source:** `java.rmi\java\rmi\server\ObjID.html`

### Class Description

```java
public final class
ObjID

extends
Object

implements
Serializable
```

An

ObjID

is used to identify a remote object exported
to an RMI runtime. When a remote object is exported, it is assigned
an object identifier either implicitly or explicitly, depending on
the API used to export.

The

ObjID()

constructor can be used to generate a unique
object identifier. Such an

ObjID

is unique over time
with respect to the host it is generated on.

The

ObjID(int)

constructor can be used to create a
"well-known" object identifier. The scope of a well-known

ObjID

depends on the RMI runtime it is exported to.

An

ObjID

instance contains an object number (of type

long

) and an address space identifier (of type

UID

). In a unique

ObjID

, the address space
identifier is unique with respect to a given host over time. In a
well-known

ObjID

, the address space identifier is
equivalent to one returned by invoking the

UID(short)

constructor with the value zero.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then the

ObjID()

constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int REGISTRY_ID

Object number for well-known

ObjID

of the registry.

**See Also:**
- Constant Field Values

---

#### public static final int ACTIVATOR_ID

Object number for well-known

ObjID

of the activator.

**See Also:**
- Constant Field Values

---

#### public static final int DGC_ID

Object number for well-known

ObjID

of
the distributed garbage collector.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ObjID()

Generates a unique object identifier.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then this constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

---

#### public ObjID​(int objNum)

Creates a "well-known" object identifier.

An

ObjID

created via this constructor will not
clash with any

ObjID

s generated via the no-arg
constructor.

**Parameters:**
- objNum

- object number for well-known object identifier

---

### Method Details

#### public void write​(
ObjectOutput
out)
throws
IOException

Marshals a binary representation of this

ObjID

to
an

ObjectOutput

instance.

Specifically, this method first invokes the given stream's

DataOutput.writeLong(long)

method with this object
identifier's object number, and then it writes its address
space identifier by invoking its

UID.write(DataOutput)

method with the stream.

**Parameters:**
- out

- the

ObjectOutput

instance to write
this

ObjID

to

**Throws:**
- IOException

- if an I/O error occurs while performing
this operation

---

#### public static
ObjID
read​(
ObjectInput
in)
throws
IOException

Constructs and returns a new

ObjID

instance by
unmarshalling a binary representation from an

ObjectInput

instance.

Specifically, this method first invokes the given stream's

DataInput.readLong()

method to read an object number,
then it invokes

UID.read(DataInput)

with the
stream to read an address space identifier, and then it
creates and returns a new

ObjID

instance that
contains the object number and address space identifier that
were read from the stream.

**Parameters:**
- in

- the

ObjectInput

instance to read

ObjID

from

**Returns:**
- unmarshalled

ObjID

instance

**Throws:**
- IOException

- if an I/O error occurs while performing
this operation

---

#### public int hashCode()

Returns the hash code value for this object identifier, the
object number.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this object identifier

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
obj)

Compares the specified object with this

ObjID

for
equality.

This method returns

true

if and only if the
specified object is an

ObjID

instance with the same
object number and address space identifier as this one.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to compare this

ObjID

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

Returns a string representation of this object identifier.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this object identifier

---

### Additional Sections

#### Class ObjID

java.lang.Object

- java.rmi.server.ObjID

java.rmi.server.ObjID

**All Implemented Interfaces:** Serializable

```java
public final class
ObjID

extends
Object

implements
Serializable
```

An

ObjID

is used to identify a remote object exported
to an RMI runtime. When a remote object is exported, it is assigned
an object identifier either implicitly or explicitly, depending on
the API used to export.

The

ObjID()

constructor can be used to generate a unique
object identifier. Such an

ObjID

is unique over time
with respect to the host it is generated on.

The

ObjID(int)

constructor can be used to create a
"well-known" object identifier. The scope of a well-known

ObjID

depends on the RMI runtime it is exported to.

An

ObjID

instance contains an object number (of type

long

) and an address space identifier (of type

UID

). In a unique

ObjID

, the address space
identifier is unique with respect to a given host over time. In a
well-known

ObjID

, the address space identifier is
equivalent to one returned by invoking the

UID(short)

constructor with the value zero.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then the

ObjID()

constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

**Since:** 1.1
**See Also:** Serialized Form

public final class

ObjID

extends

Object

implements

Serializable

An

ObjID

is used to identify a remote object exported
to an RMI runtime. When a remote object is exported, it is assigned
an object identifier either implicitly or explicitly, depending on
the API used to export.

The

ObjID()

constructor can be used to generate a unique
object identifier. Such an

ObjID

is unique over time
with respect to the host it is generated on.

The

ObjID(int)

constructor can be used to create a
"well-known" object identifier. The scope of a well-known

ObjID

depends on the RMI runtime it is exported to.

An

ObjID

instance contains an object number (of type

long

) and an address space identifier (of type

UID

). In a unique

ObjID

, the address space
identifier is unique with respect to a given host over time. In a
well-known

ObjID

, the address space identifier is
equivalent to one returned by invoking the

UID(short)

constructor with the value zero.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then the

ObjID()

constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

The

ObjID()

constructor can be used to generate a unique
object identifier. Such an

ObjID

is unique over time
with respect to the host it is generated on.

The

ObjID(int)

constructor can be used to create a
"well-known" object identifier. The scope of a well-known

ObjID

depends on the RMI runtime it is exported to.

An

ObjID

instance contains an object number (of type

long

) and an address space identifier (of type

UID

). In a unique

ObjID

, the address space
identifier is unique with respect to a given host over time. In a
well-known

ObjID

, the address space identifier is
equivalent to one returned by invoking the

UID(short)

constructor with the value zero.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then the

ObjID()

constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

An

ObjID

instance contains an object number (of type

long

) and an address space identifier (of type

UID

). In a unique

ObjID

, the address space
identifier is unique with respect to a given host over time. In a
well-known

ObjID

, the address space identifier is
equivalent to one returned by invoking the

UID(short)

constructor with the value zero.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then the

ObjID()

constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then the

ObjID()

constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ACTIVATOR_ID

Object number for well-known

ObjID

of the activator.

static int

DGC_ID

Object number for well-known

ObjID

of
the distributed garbage collector.

static int

REGISTRY_ID

Object number for well-known

ObjID

of the registry.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ObjID

()

Generates a unique object identifier.

ObjID

​(int objNum)

Creates a "well-known" object identifier.

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

ObjID

for
equality.

int

hashCode

()

Returns the hash code value for this object identifier, the
object number.

static

ObjID

read

​(

ObjectInput

in)

Constructs and returns a new

ObjID

instance by
unmarshalling a binary representation from an

ObjectInput

instance.

String

toString

()

Returns a string representation of this object identifier.

void

write

​(

ObjectOutput

out)

Marshals a binary representation of this

ObjID

to
an

ObjectOutput

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

ACTIVATOR_ID

Object number for well-known

ObjID

of the activator.

static int

DGC_ID

Object number for well-known

ObjID

of
the distributed garbage collector.

static int

REGISTRY_ID

Object number for well-known

ObjID

of the registry.

---

#### Field Summary

Object number for well-known

ObjID

of the activator.

Object number for well-known

ObjID

of
the distributed garbage collector.

Object number for well-known

ObjID

of the registry.

Constructor Summary

Constructors

Constructor

Description

ObjID

()

Generates a unique object identifier.

ObjID

​(int objNum)

Creates a "well-known" object identifier.

---

#### Constructor Summary

Generates a unique object identifier.

Creates a "well-known" object identifier.

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

ObjID

for
equality.

int

hashCode

()

Returns the hash code value for this object identifier, the
object number.

static

ObjID

read

​(

ObjectInput

in)

Constructs and returns a new

ObjID

instance by
unmarshalling a binary representation from an

ObjectInput

instance.

String

toString

()

Returns a string representation of this object identifier.

void

write

​(

ObjectOutput

out)

Marshals a binary representation of this

ObjID

to
an

ObjectOutput

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

ObjID

for
equality.

Returns the hash code value for this object identifier, the
object number.

Constructs and returns a new

ObjID

instance by
unmarshalling a binary representation from an

ObjectInput

instance.

Returns a string representation of this object identifier.

Marshals a binary representation of this

ObjID

to
an

ObjectOutput

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

============ FIELD DETAIL ===========

- Field Detail

- REGISTRY_ID

```java
public static final int REGISTRY_ID
```

Object number for well-known

ObjID

of the registry.

**See Also:** Constant Field Values

- ACTIVATOR_ID

```java
public static final int ACTIVATOR_ID
```

Object number for well-known

ObjID

of the activator.

**See Also:** Constant Field Values

- DGC_ID

```java
public static final int DGC_ID
```

Object number for well-known

ObjID

of
the distributed garbage collector.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ObjID

```java
public ObjID()
```

Generates a unique object identifier.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then this constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

- ObjID

```java
public ObjID​(int objNum)
```

Creates a "well-known" object identifier.

An

ObjID

created via this constructor will not
clash with any

ObjID

s generated via the no-arg
constructor.

**Parameters:** objNum

- object number for well-known object identifier

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(
ObjectOutput
out)
throws
IOException
```

Marshals a binary representation of this

ObjID

to
an

ObjectOutput

instance.

Specifically, this method first invokes the given stream's

DataOutput.writeLong(long)

method with this object
identifier's object number, and then it writes its address
space identifier by invoking its

UID.write(DataOutput)

method with the stream.

**Parameters:** out

- the

ObjectOutput

instance to write
this

ObjID

to
**Throws:** IOException

- if an I/O error occurs while performing
this operation

- read

```java
public static
ObjID
read​(
ObjectInput
in)
throws
IOException
```

Constructs and returns a new

ObjID

instance by
unmarshalling a binary representation from an

ObjectInput

instance.

Specifically, this method first invokes the given stream's

DataInput.readLong()

method to read an object number,
then it invokes

UID.read(DataInput)

with the
stream to read an address space identifier, and then it
creates and returns a new

ObjID

instance that
contains the object number and address space identifier that
were read from the stream.

**Parameters:** in

- the

ObjectInput

instance to read

ObjID

from
**Returns:** unmarshalled

ObjID

instance
**Throws:** IOException

- if an I/O error occurs while performing
this operation

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object identifier, the
object number.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this object identifier
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

ObjID

for
equality.

This method returns

true

if and only if the
specified object is an

ObjID

instance with the same
object number and address space identifier as this one.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this

ObjID

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

Returns a string representation of this object identifier.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object identifier

Field Detail

- REGISTRY_ID

```java
public static final int REGISTRY_ID
```

Object number for well-known

ObjID

of the registry.

**See Also:** Constant Field Values

- ACTIVATOR_ID

```java
public static final int ACTIVATOR_ID
```

Object number for well-known

ObjID

of the activator.

**See Also:** Constant Field Values

- DGC_ID

```java
public static final int DGC_ID
```

Object number for well-known

ObjID

of
the distributed garbage collector.

**See Also:** Constant Field Values

---

#### Field Detail

REGISTRY_ID

```java
public static final int REGISTRY_ID
```

Object number for well-known

ObjID

of the registry.

**See Also:** Constant Field Values

---

#### REGISTRY_ID

public static final int REGISTRY_ID

Object number for well-known

ObjID

of the registry.

ACTIVATOR_ID

```java
public static final int ACTIVATOR_ID
```

Object number for well-known

ObjID

of the activator.

**See Also:** Constant Field Values

---

#### ACTIVATOR_ID

public static final int ACTIVATOR_ID

Object number for well-known

ObjID

of the activator.

DGC_ID

```java
public static final int DGC_ID
```

Object number for well-known

ObjID

of
the distributed garbage collector.

**See Also:** Constant Field Values

---

#### DGC_ID

public static final int DGC_ID

Object number for well-known

ObjID

of
the distributed garbage collector.

Constructor Detail

- ObjID

```java
public ObjID()
```

Generates a unique object identifier.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then this constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

- ObjID

```java
public ObjID​(int objNum)
```

Creates a "well-known" object identifier.

An

ObjID

created via this constructor will not
clash with any

ObjID

s generated via the no-arg
constructor.

**Parameters:** objNum

- object number for well-known object identifier

---

#### Constructor Detail

ObjID

```java
public ObjID()
```

Generates a unique object identifier.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then this constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

---

#### ObjID

public ObjID()

Generates a unique object identifier.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then this constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

If the system property

java.rmi.server.randomIDs

is defined to equal the string

"true"

(case insensitive),
then this constructor will use a cryptographically
strong random number generator to choose the object number of the
returned

ObjID

.

ObjID

```java
public ObjID​(int objNum)
```

Creates a "well-known" object identifier.

An

ObjID

created via this constructor will not
clash with any

ObjID

s generated via the no-arg
constructor.

**Parameters:** objNum

- object number for well-known object identifier

---

#### ObjID

public ObjID​(int objNum)

Creates a "well-known" object identifier.

An

ObjID

created via this constructor will not
clash with any

ObjID

s generated via the no-arg
constructor.

An

ObjID

created via this constructor will not
clash with any

ObjID

s generated via the no-arg
constructor.

Method Detail

- write

```java
public void write​(
ObjectOutput
out)
throws
IOException
```

Marshals a binary representation of this

ObjID

to
an

ObjectOutput

instance.

Specifically, this method first invokes the given stream's

DataOutput.writeLong(long)

method with this object
identifier's object number, and then it writes its address
space identifier by invoking its

UID.write(DataOutput)

method with the stream.

**Parameters:** out

- the

ObjectOutput

instance to write
this

ObjID

to
**Throws:** IOException

- if an I/O error occurs while performing
this operation

- read

```java
public static
ObjID
read​(
ObjectInput
in)
throws
IOException
```

Constructs and returns a new

ObjID

instance by
unmarshalling a binary representation from an

ObjectInput

instance.

Specifically, this method first invokes the given stream's

DataInput.readLong()

method to read an object number,
then it invokes

UID.read(DataInput)

with the
stream to read an address space identifier, and then it
creates and returns a new

ObjID

instance that
contains the object number and address space identifier that
were read from the stream.

**Parameters:** in

- the

ObjectInput

instance to read

ObjID

from
**Returns:** unmarshalled

ObjID

instance
**Throws:** IOException

- if an I/O error occurs while performing
this operation

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object identifier, the
object number.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this object identifier
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

ObjID

for
equality.

This method returns

true

if and only if the
specified object is an

ObjID

instance with the same
object number and address space identifier as this one.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this

ObjID

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

Returns a string representation of this object identifier.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object identifier

---

#### Method Detail

write

```java
public void write​(
ObjectOutput
out)
throws
IOException
```

Marshals a binary representation of this

ObjID

to
an

ObjectOutput

instance.

Specifically, this method first invokes the given stream's

DataOutput.writeLong(long)

method with this object
identifier's object number, and then it writes its address
space identifier by invoking its

UID.write(DataOutput)

method with the stream.

**Parameters:** out

- the

ObjectOutput

instance to write
this

ObjID

to
**Throws:** IOException

- if an I/O error occurs while performing
this operation

---

#### write

public void write​(

ObjectOutput

out)
throws

IOException

Marshals a binary representation of this

ObjID

to
an

ObjectOutput

instance.

Specifically, this method first invokes the given stream's

DataOutput.writeLong(long)

method with this object
identifier's object number, and then it writes its address
space identifier by invoking its

UID.write(DataOutput)

method with the stream.

Specifically, this method first invokes the given stream's

DataOutput.writeLong(long)

method with this object
identifier's object number, and then it writes its address
space identifier by invoking its

UID.write(DataOutput)

method with the stream.

read

```java
public static
ObjID
read​(
ObjectInput
in)
throws
IOException
```

Constructs and returns a new

ObjID

instance by
unmarshalling a binary representation from an

ObjectInput

instance.

Specifically, this method first invokes the given stream's

DataInput.readLong()

method to read an object number,
then it invokes

UID.read(DataInput)

with the
stream to read an address space identifier, and then it
creates and returns a new

ObjID

instance that
contains the object number and address space identifier that
were read from the stream.

**Parameters:** in

- the

ObjectInput

instance to read

ObjID

from
**Returns:** unmarshalled

ObjID

instance
**Throws:** IOException

- if an I/O error occurs while performing
this operation

---

#### read

public static

ObjID

read​(

ObjectInput

in)
throws

IOException

Constructs and returns a new

ObjID

instance by
unmarshalling a binary representation from an

ObjectInput

instance.

Specifically, this method first invokes the given stream's

DataInput.readLong()

method to read an object number,
then it invokes

UID.read(DataInput)

with the
stream to read an address space identifier, and then it
creates and returns a new

ObjID

instance that
contains the object number and address space identifier that
were read from the stream.

Specifically, this method first invokes the given stream's

DataInput.readLong()

method to read an object number,
then it invokes

UID.read(DataInput)

with the
stream to read an address space identifier, and then it
creates and returns a new

ObjID

instance that
contains the object number and address space identifier that
were read from the stream.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this object identifier, the
object number.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this object identifier
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this object identifier, the
object number.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this

ObjID

for
equality.

This method returns

true

if and only if the
specified object is an

ObjID

instance with the same
object number and address space identifier as this one.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this

ObjID

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

ObjID

for
equality.

This method returns

true

if and only if the
specified object is an

ObjID

instance with the same
object number and address space identifier as this one.

toString

```java
public
String
toString()
```

Returns a string representation of this object identifier.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object identifier

---

#### toString

public

String

toString()

Returns a string representation of this object identifier.

---

